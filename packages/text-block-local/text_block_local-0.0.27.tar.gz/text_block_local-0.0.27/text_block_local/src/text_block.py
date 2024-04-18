import json
import re
import time
from datetime import datetime

import mysql.connector
from database_mysql_local.generic_crud import GenericCRUD
from database_mysql_local.point import Point
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from user_context_remote.user_context import UserContext
from profiles_local.profiles_local import ProfilesLocal
from person_local.src.persons_local import PersonsLocal
from person_local.src.persons_local import Person

DEFAULT_GENDER_ID = 8 # = Prefer not to respond
MAX_ERRORS = 5
TEXT_BLOCK_COMPONENT_ID = 143
TEXT_BLOCK_COMPONENT_NAME = "text_block_local_python_package"
DEVELOPER_EMAIL = "akiva.s@circ.zone"
object1 = {
    'component_id': TEXT_BLOCK_COMPONENT_ID,
    'component_name': TEXT_BLOCK_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}
logger = Logger.create_logger(object=object1)
user_context = UserContext()

class TextBlocks(GenericCRUD):
    def __init__(self, text_block_id: int = None):
        GenericCRUD.__init__(self, default_schema_name="text_block")
        # TODO: add a seperate GenericCRUD object for field schema
        # TODO: add a seperate GenericCRUD object for table_definition_table schema
        self.text_block_id = text_block_id
        self.currect_profile_id = None
        self.errors_count = 0
        self.field_block_type_generic_crud = GenericCRUD(default_schema_name="field_text_block_type",
                                                         default_view_table_name="field_text_block_type_view",
                                                         default_select_clause_value="regex, field_id",
                                                         default_where="text_block_type_id = %s OR text_block_type_id IS NULL")
        self.profiles_local = ProfilesLocal()
        self.persons_local = PersonsLocal()

    def get_block_fields(self, text_block_type_id: int) -> dict:
        """Retrieves regular expressions and field IDs based on the provided `text_block_type_id`."""
        logger.start("Getting regex and field_id from block_id ...")
        self.set_schema(schema_name="field")
        # One field id can have multiple regexes
        block_fields = self.field_block_type_generic_crud.select_multi_dict_by_where(
            select_clause_value="regex, field_id, index_in_regex, comment",
            view_table_name="field_text_block_type_view",
            where="text_block_type_id = %s",
            params=(text_block_type_id,))

        logger.end("Regex and field ids retrieved", object={'block_fields': block_fields})
        return block_fields

    def get_fields(self) -> dict:
        """Retrieves field IDs and names from the database."""
        logger.start("Getting field ids and names ...")
        self.set_schema(schema_name="field")
        fields = dict(self.select_multi_tuple_by_where(view_table_name="field_view",
                                                       select_clause_value="field_id, name"))

        logger.end("Field names and ids retrieved", object={'fields': fields})
        return fields

    def get_block_type_ids_regex(self) -> dict:
        """Retrieves block type IDs and regular expressions from the database."""
        # TODO: we also have regexes in block_type_field_table, should we return those as well?
        logger.start("Getting block type ids and names ...")
        self.set_schema(schema_name="text_block_type")
        # One regex can have multiple block type ids
        block_types = dict(self.select_multi_tuple_by_where(view_table_name="text_block_type_regex_view",
                                                            select_clause_value="regex, text_block_type_id"))

        logger.end("Block types retrieved", object={'block_types': block_types})
        return block_types

    def get_block_types(self) -> dict:
        """Retrieves block type IDs and names from the database."""
        logger.start("Getting block type ids and names ...")
        self.set_schema(schema_name="text_block_type")
        block_types = dict(self.select_multi_tuple_by_where(view_table_name="text_block_type_ml_view",
                                                            select_clause_value="text_block_type_id, name"))

        logger.end("Block types retrieved", object={'block_types': block_types})
        return block_types

    def get_text_block_ids_types(self) -> dict:
        """Retrieves text block IDs and types from the database."""
        logger.start("Getting text blocks from text_block_table ...")
        self.set_schema(schema_name="text_block")
        result = self.select_multi_tuple_by_where(view_table_name="text_block_view",
                                                  select_clause_value="text_block_type_id, text_block_type_id, text_without_empty_lines, text")
        text_block_ids_types = {}
        for text_block_id, type_id, text_without_empty_lines, text in result:
            text_block_ids_types[text_block_id] = (type_id, text_without_empty_lines or text)

        logger.end("Text blocks retrieved", object={'text_blocks_ids_types': text_block_ids_types})
        return text_block_ids_types

    def process_text_blocks_updated_since_date(self, since_date: datetime) -> None:
        self.set_schema(schema_name="text_block")
        text_block_ids = self.select_multi_tuple_by_where(view_table_name="text_block_view",
                                                          select_clause_value="text_block_type_id",
                                                          where="updated_timestamp >= %s",
                                                          params=(since_date,))
        for text_block_id in text_block_ids:
            self.process_text_block_by_id(text_block_id[0])

    def process_text_block_by_id(self, text_block_id: int) -> None:
        """
        1. Retrieves the text and other details of the text block.
        2. Reformat the text if needed.
        3. Identifies and updates the text block type.
        4. Extract fields from the text based on the block type's regular expressions.
        5. Updates the text block with the extracted fields in JSON format.
        """

        try:
            self.text_block_id = text_block_id
            self.profile_id = None
            text, text_block_type_id, profile_id = self.get_text_block_details(text_block_id)

            # reformat text
            text = text.replace("\n", " ")

            if text_block_type_id is None:
                text_block_type_id = self.identify_and_update_text_block_type(text_block_id, text)

            fields_dict = self.extract_fields_from_text(text, text_block_type_id)
            self.update_text_block_fields(text_block_id, fields_dict)

        except mysql.connector.errors.DatabaseError as e:
            if "Lock wait timeout exceeded" in str(e) and self.errors_count < MAX_ERRORS:  # prevent infinite loop
                self.errors_count += 1
                logger.warn("Lock wait timeout exceeded. Retrying UPDATE after a short delay.")
                time.sleep(2)
                self.process_text_block_by_id(text_block_id)
            else:
                logger.error("Database Error", object=e)
                raise e

        except Exception as e:
            logger.exception("Error processing text block", object=e)
            raise e

        self.errors_count = 0

    def get_text_block_details(self, text_block_id: int) -> tuple:
        """Retrieves text and related details for a given text block ID."""
        logger.start("Getting text block details ...", object={'text_block_type_id': text_block_id})
        self.set_schema(schema_name="text_block")
        result = self.select_one_tuple_by_id(view_table_name="text_block_view",
                                             select_clause_value="text_without_empty_lines, text, text_block_type_id, profile_id",
                                             id_column_name="text_block_id",
                                             id_column_value=text_block_id)

        if result[0]:
            text, text_block_type_id, profile_id = (result[0], result[2], result[3])
        else:
            text, text_block_type_id, profile_id = (result[1], result[2], result[3])

        logger.end("Text block details retrieved", object={'text': text, 'text_block_type_id': text_block_type_id,
                                                           'profile_id': profile_id})
        return text, text_block_type_id, profile_id

    def extract_fields_from_text(self, text: str, text_block_type_id: int) -> dict:
        """
        Extracts fields from the text based on the block type's regular expressions.
        text_block_profile_id is the profile_id of the profile which referred to in the specific text_block (not user_context.profile_id)
        """

        logger.start("Extracting fields from text ...", object={'text': text, 'text_block_type_id': text_block_type_id})
        profile_id = None
        block_fields = self.get_block_fields(text_block_type_id)
        fields = self.get_fields()
        fields_dict = {}

        for item_index, item in enumerate(block_fields):
            regex = item.get("regex")
            field_id = item.get("field_id")
            if not regex:  # we have not defined those yet in the block_type_field_table
                continue
            try:
                re.compile(regex)
                matches = re.findall(regex, text)

                if not matches:
                    continue
                field = fields[field_id]
                fields_dict[field] = matches

                for index, match in enumerate(matches):
                    dict_to_organize = {field: matches}
                    organized_fields_dict = self.__organize_fields_dict(dict_to_organize, text_block_type_id, index)
                    self.process_and_update_field(
                        fields_dict=organized_fields_dict,
                        field_id=field_id,
                        match=match,
                        index=item_index)

            except re.error as e:
                logger.exception(f"Invalid regex: {regex}", object=e)

        logger.end("Fields extracted", object={'fields_dict': fields_dict})
        return fields_dict

    def process_and_update_field(self, fields_dict: dict, field_id: int, match: str, index: int) -> int:
        """Processes and updates the field."""
        # TODO: rewrite this method
        # https://github.com/circles-zone/text-block-local-python-package/blob/613e6cdbf5c5f54b40c37e4b479e0d48d820a03b/circles_text_block_local/text_block_microservice.py#L181
        logger.start("Processing and updating field ...", object={
            'field_id': field_id, 'match': match})
        field_info = self.select_one_tuple_by_id(
            schema_name="field",
            view_table_name='field_view',
            select_clause_value="table_id, database_field_name, database_sub_field_name, database_sub_field_value, processing_id, processing_database_field_name",
            id_column_name="field_id",
            id_column_value=field_id)
        table_id, database_field_name, database_sub_field_name, database_sub_field_value, processing_id, processing_database_field_name = field_info
        logger.info(object={"field_info": field_info})
        field_name = self.__get_field_name_by_field_id(field_id)
        field_column_value = fields_dict.get(field_name)
        if isinstance(field_column_value, tuple):
            field_column_value = field_column_value[index]
        profile_id = self.__get_profile_id(fields_dict)

        try:
            # TODO: process fields with _original
            # processed_value = self.process_field(processing_id, match)

            # get table definition
            self.cursor.execute("SELECT `schema`, table_name, view_name, profile_mapping_table_id FROM " \
                                "`database`.table_definition_table WHERE table_definition_id = %s", (table_id,))
            record = self.cursor.fetchone()
            if record is None:
                logger.error("No table definition found for database_field_name", object={"database_field_name": database_field_name})
                # raise Exception("No table definition found for field")
                return None
            schema, table_name, view_name, profile_mapping_table_id = record
            logger.info(object={"schema": schema, "table_name": table_name, "view_name": view_name, "profile_mapping_table_id": profile_mapping_table_id})

            # Get field information
            self.cursor.execute("SELECT `schema`, table_name, view_name FROM `database`.table_definition_table WHERE table_definition_id = %s",
                                (profile_mapping_table_id,))
            record = self.cursor.fetchone()
            if record is None:
                logger.error("No profile mapping table found for table_id", object={"table_id": table_id})
                # raise Exception("No profile mapping table found for profile_mapping_table_id")
                return None
            profile_mapping_table_schema, profile_mapping_table_name, profile_mapping_view_name = record
            logger.info(object={"profile_mapping_table_schema": profile_mapping_table_schema,
                                "profile_mapping_table_name": profile_mapping_table_name,
                                "profile_mapping_view_name": profile_mapping_view_name})

            if profile_id is not None and profile_mapping_table_id is not None:

                # Retrieve mapping ID for the profile
                select_clause_value = schema + "_id"
                if table_name == "person_table":
                    entity_id = self.select_one_value_by_id(schema_name="profile",
                                                            view_table_name="profile_view",
                                                            select_clause_value="person_id",
                                                            id_column_name="profile_id",
                                                            id_column_value=profile_id)
                else:
                    entity_id = self.select_one_value_by_id(schema_name=schema,
                                                            view_table_name=view_name,
                                                            select_clause_value=select_clause_value,
                                                            id_column_name=database_field_name,
                                                            id_column_value=field_column_value)
                if entity_id is None:
                    # insert information from extracted fields
                    if table_name == "person_table":
                        entity_id = self.__add_person_to_db(fields_dict=fields_dict, index=index)
                    else:
                        entity_id = self.insert_information_from_extracted_fields(
                            schema, table_name, database_field_name, field_column_value,
                            database_sub_field_name, database_sub_field_value)
                profile_mapping_id_name = profile_mapping_table_schema + "_id"
                mapping_id = self.select_one_value_by_where(schema_name=profile_mapping_table_schema,
                                                            view_table_name=profile_mapping_view_name,
                                                            select_clause_value=profile_mapping_id_name,
                                                            where="profile_id=%s AND " + select_clause_value + "=%s",
                                                            params=(profile_id, entity_id))
                if mapping_id is None:
                    # update the profile_mapping table
                    mapping_id = self.insert_profile_mapping(profile_id, entity_id, profile_mapping_table_schema, select_clause_value,
                                                             profile_mapping_table_name)
                if table_name != "person_table":
                    sql = "SELECT %s FROM %s.%s WHERE %s = %s" % (database_field_name, schema, view_name, select_clause_value, entity_id)
                    self.cursor.execute(sql)
                    field_old = self.cursor.fetchone()
                    if field_old is not None:
                        sql = "UPDATE %s.%s SET %s = '%s' WHERE %s = %s" % (
                            schema, table_name, database_field_name, field_column_value, select_clause_value, entity_id)
                        if database_sub_field_name and database_sub_field_value:
                            sql = "UPDATE %s.%s SET %s = '%s', %s = '%s' WHERE %s = %s" % (
                                schema, table_name, database_field_name, field_column_value, database_sub_field_name,
                                database_sub_field_value, select_clause_value, entity_id)
                        self.cursor.execute(sql)
                        self.connection.commit()
                        if field_old[0] != field_column_value:
                            self.update_logger_with_old_and_new_field_value(field_id, field_old[0], field_column_value)

            else:   # no  profile_id and profile_mapping_table_id
                # TODO: use GenericCRUD and delete the line below
                # Populate the person/profile class for each profile processed
                person_id = self.__add_person_to_db(fields_dict=fields_dict, index=index)
                if person_id is not None:
                    profile_id = self.__add_profile_to_db(person_id=person_id, fields_dict=fields_dict, index=index)
                else:
                    logger.error("No person_id found for profile_id", object={"profile_id": profile_id})
                    raise Exception("No person was not inserted into the database.")

                # insert information from extracted fieldss
                if table_name == "person_table":
                    entity_id = person_id
                else:
                    entity_id = self.insert_information_from_extracted_fields(
                        schema, table_name, database_field_name, field_column_value,
                        database_sub_field_name, database_sub_field_value)

                # update the profile_mapping table
                select_clause_value = schema + "_id"
                if profile_mapping_table_schema and profile_mapping_table_name and schema and profile_id and entity_id:
                    self.insert_profile_mapping(profile_id, entity_id, profile_mapping_table_schema, select_clause_value,
                                                profile_mapping_table_name)

        except Exception as e:
            logger.exception("Error processing field", object=e)

    def update_text_block_fields(self, text_block_id: int, fields_dict: dict) -> None:
        """Updates the text block with the extracted fields in JSON format."""
        logger.start("Updating text block fields ...", object={'text_block_id': text_block_id})
        fields_json = json.dumps(fields_dict)
        self.set_schema(schema_name="text_block")
        self.update_by_id(table_name="text_block_table", id_column_name="text_block_id", id_column_value=text_block_id,
                          data_json={"fields_extracted_json": fields_json})
        logger.end("Text block fields updated")

    def identify_and_update_text_block_type(self, text_block_id: int, text: str) -> int:
        """Identifies and updates the text block type."""
        logger.start("Identifying and updating block type for text block", object={
            'text_block_id': text_block_id, 'text': text})
        text_block_type_id = self.identify_text_block_type(text, text_block_id)
        if text_block_type_id is not None:
            self.set_schema(schema_name="text_block")
            self.update_by_id(table_name="text_block_table", id_column_name="text_block_id",
                              id_column_value=text_block_id,
                              data_json={"text_block_type_id": text_block_type_id})
        logger.end("Block type identified and updated", object={'text_block_type_id': text_block_type_id})
        return text_block_type_id

    def identify_text_block_type(self, text: str, text_block_id: int = None) -> int:
        """Identifies the text block type.
        If a text block ID is provided, it will first try to identify the block type based on its system ID and entity ID."""
        logger.start("Identifying block type for text block", object={'text_block_id': text_block_id, 'text': text})
        self.set_schema(schema_name="text_block_type")
        results = None
        if text_block_id:
            system = self.select_one_dict_by_id(view_table_name="text_block_type_view",
                                                select_clause_value="system_id, system_entity_id",
                                                id_column_name="text_block_type_id",
                                                id_column_value=text_block_id)
            # filter results with system_id and system_entity if possible
            if "system_entity_id" in system:
                results = self.select_multi_tuple_by_where(view_table_name="text_block_type_view",
                                                           select_clause_value="regex",
                                                           where="system_id = %s AND system_entity_id = %s",
                                                           params=(system["system_id"], system["system_entity_id"]))

            elif "system_id" in system:
                results = self.select_multi_tuple_by_id(view_table_name="text_block_type_view",
                                                        select_clause_value="regex",
                                                        id_column_name="system_id",
                                                        id_column_value=system["system_id"])
        if results and any(x[0] for x in results):
            regex_list = "(" + ",".join(str(regex[0]) for regex in results if regex[0]) + ")"
            potential_block_type_ids = dict(self.select_multi_tuple_by_where(
                view_table_name="text_block_type_regex_view",
                select_clause_value="text_block_type_id, regex",
                where="regex IN %s",
                params=(regex_list,)))
        else:
            logger.info("No system id for text block")
            potential_block_type_ids = self.get_block_type_ids_regex()

        # classify block_type using regex
        for regex, text_block_type_id in potential_block_type_ids.items():
            try:
                re.compile(regex)
                match = re.search(regex, text)
                if match:
                    return text_block_type_id
            except (re.error, TypeError) as e:
                logger.exception(f"Invalid regex: {regex}", object=e)

        # if no block type id has been found by this point
        logger.end("Unable to identify text_block_type_id for text block", object={'text_block_id': text_block_id})

    def check_all_text_blocks(self) -> None:
        """Checks all text blocks and updates their block type if needed."""
        # For all text_blocks
        logger.start("Checking all text blocks ...")
        text_block_ids_types = self.get_text_block_ids_types()
        block_types = self.get_block_types()
        for text_block_type_id in text_block_ids_types:
            existing_block_type = text_block_ids_types[text_block_type_id][0]
            if existing_block_type:
                logger.info("\nOld block type: " + str(existing_block_type) + ", '" + block_types[
                    existing_block_type] + "' for text block " + str(text_block_type_id))
            else:
                logger.info("Old block type: None")
            text = (text_block_ids_types[text_block_type_id][1]).replace("\n", " ")
            new_block_type = self.identify_and_update_text_block_type(text_block_type_id, text)
            if new_block_type is not None:
                logger.info("Identified block type: " + str(new_block_type) + " " + block_types[new_block_type])
        logger.end("All text blocks checked")

    def update_logger_with_old_and_new_field_value(self, field_id: int, field_value_old: str,
                                                   field_value_new: str) -> int:
        """Updates the logger with the old and new field value."""
        logger.start("Updating logger with old and new field value", object={
            'field_id': field_id, 'field_value_old': field_value_old, 'field_value_new': field_value_new})
        self.set_schema(schema_name="logger")
        data_json = {"field_id": field_id, "field_value_old": field_value_old, "field_value_new": field_value_new}
        logger_id = self.insert(table_name="logger_table", data_json=data_json)
        logger.end("Logger updated", object={'logger_id': logger_id})
        return logger_id

    def __add_person_to_db(self, fields_dict: dict, index: int) -> int:
        ADD_PERSON_TO_DB_METHOD_NAME = "__add_person_to_db"
        """Adds a person to the database."""
        person_id = None
        first_name = None
        last_name = None
        birthday_original = None
        email_address = None
        logger.start(log_message=ADD_PERSON_TO_DB_METHOD_NAME + ": Adding person to the database ...")
        if "Name" in fields_dict:
            full_name = fields_dict.get("Name")
            if isinstance(full_name, tuple):
                full_name = full_name[index]
            if full_name:
                full_name = full_name.split(" ")
                if len(full_name) > 1:
                    first_name = full_name[0]
                    last_name = full_name[-1]
                else:
                    first_name = full_name[0]
        if "Email" in fields_dict:
            email_address = fields_dict.get("Email")
            if isinstance(email_address, tuple):
                email_address = email_address[index]
        if "Birthday" in fields_dict:
            birthday_original = fields_dict.get("Birthday")  # , [None])[0]
        if "First Name" in fields_dict:
            first_name = fields_dict.get("First Name")  # , [None])[0]
        else:
            logger.warning(log_message=ADD_PERSON_TO_DB_METHOD_NAME + ": No first name found in fields_dict",
                           object={'fields_dict': fields_dict})
        if "Last Name" in fields_dict:
            last_name = fields_dict.get("Last Name")  # , [None])[0]
        else:
            logger.warning(log_message=ADD_PERSON_TO_DB_METHOD_NAME + ": No last name found in fields_dict",
                           object={'fields_dict': fields_dict})
        # TODO: can we get more information from the fields_dict and add it to the person object?
        if (first_name and last_name) or (first_name and email_address):
            person_object = Person(first_name=first_name, last_name=last_name, birthday_original=birthday_original,
                                   main_email_address=email_address,
                                   last_coordinate=Point(0.0, 0.0))
            insert_result = self.persons_local.insert_if_not_exists(
                person=person_object)
            if insert_result:
                person_id = insert_result[0]
        logger.end(log_message=ADD_PERSON_TO_DB_METHOD_NAME + ": Person added", object={'person_id': person_id})
        return person_id

    def __add_profile_to_db(self, person_id: int, index: int, fields_dict: dict = None) -> int:
        ADD_PROFILE_TO_DB_METHOD_NAME = "__add_profile_to_db"
        """Adds a profile to the database."""
        if not person_id:
            logger.warning(log_message=ADD_PROFILE_TO_DB_METHOD_NAME + ": No person_id provided")
            return None
        logger.start(log_message=ADD_PROFILE_TO_DB_METHOD_NAME + ": Adding profile to the database ...")
        # TODO: can we get more information from the fields_dict and add it to the profile object?
        name = fields_dict.get("Name")
        if isinstance(name, tuple):
            name = name[index]
        profile_json = {
            'visibility_id': 0,  # TODO: replace this magic number.
            'is_approved': 0,
            'stars': 0,
            'last_dialog_workflow_state_id': 1,
            'lang_code': user_context.get_effective_profile_preferred_lang_code_string(),
            'is_main': 0,
            'name': name,
            'name_approved': 0,
        }
        profile_id = self.profiles_local.insert(
            profile_json=profile_json,
            person_id=person_id)
        logger.end(log_message=ADD_PROFILE_TO_DB_METHOD_NAME + ": Profile added", object={'profile_id': profile_id})
        return profile_id

    # old version
    '''
    def create_person_profile(self, fields_dict: dict) -> int:
        """Creates a person and profile based on the provided fields."""
        logger.start("Creating person and profile ...")
        created_user_id = UserContext().get_effective_user_id()
        person_id = self.create_person(fields_dict)
        visibility_id = 0  # TODO: replace this magic number.
        self.set_schema(schema_name="profile")
        number = NumberGenerator.get_random_number("profile", "profile_view")
        data_json = {}
        data_json["number"] = number
        data_json["person_id"] = person_id
        data_json["visibility_id"] = visibility_id
        data_json["created_user_id"] = created_user_id
        self.insert(table_name="profile_table", data_json=data_json)

        profile_id = self.cursor.lastrowid()
        logger.end("Person and profile created", object={'person_id': person_id, 'profile_id': profile_id})

        return profile_id


    def create_person(self, fields_dict: dict) -> int:
        """Creates a person based on the provided fields."""
        logger.start("Creating person and profile ...")
        self.set_schema(schema_name="person")
        created_user_id = UserContext().get_effective_user_id()
        data_json = {}
        number = NumberGenerator.get_random_number("person", "person_view")
        if "First Name" in fields_dict and "Last Name" in fields_dict:
            first_name = fields_dict["First Name"][0]
            last_name = fields_dict["Last Name"][0]
            data_json["number"] = number
            data_json["first_name"] = first_name
            data_json["last_name"] = last_name
            data_json["created_user_id"] = created_user_id
        elif "Birthday" in fields_dict:
            birthday = fields_dict["Birthday"][0]
            data_json["number"] = number
            data_json["birthday_original"] = birthday
            data_json["created_user_id"] = created_user_id
        else:
            data_json["number"] = number
            data_json["created_user_id"] = created_user_id
        columns = ", ".join(data_json.keys())
        values = ", ".join(["%s"] * len(data_json.values()))
        self.cursor.execute(f"INSERT INTO person.person_table (last_coordinate, {columns}) "
                            # TODO Please DEFAULT_POINT constant from location-local-python repo
                            f"VALUES (POINT(0.0000, 0.0000), {values})", tuple(data_json.values()))
        # POINT can't be parameterized

        person_id = self.cursor.lastrowid()
        logger.end("Person created", object={'person_id': person_id})
        return person_id
    '''
    def insert_information_from_extracted_fields(self, schema: str, table_name: str, database_field_name: str,
                                                 match: str, database_sub_field_name: str,
                                                 database_sub_field_value: str) -> int:
        """Inserts information from extracted fields."""
        logger.start("Inserting information from extracted fields ...", object={
            'schema': schema, 'table_name': table_name, 'database_field_name': database_field_name,
            'match': match, 'database_sub_field_name': database_sub_field_name,
            'database_sub_field_value': database_sub_field_value})
        created_user_id = updated_user_id = user_context.get_effective_user_id()
        sql = "INSERT IGNORE INTO %s.%s (%s, created_user_id, updated_user_id) VALUES ('%s', %s, %s)" % (
            schema, table_name, database_field_name, match, created_user_id, updated_user_id)
        if database_sub_field_name is not None and database_sub_field_value is not None:
            sql = "INSERT IGNORE INTO %s.%s (%s, %s, created_user_id, updated_user_id) VALUES ('%s', '%s', %s, %s)" % (
                schema, table_name, database_field_name, database_sub_field_name, match,
                database_sub_field_value,
                created_user_id, updated_user_id)
        logger.info(object={"SQL command executed": sql})
        self.cursor.execute(sql)
        entity_id = self.cursor.lastrowid()
        self.connection.commit()
        logger.end("Information inserted", object={'entity_id': entity_id})
        return entity_id

    def insert_profile_mapping(self, profile_id: int, entity_id: int, profile_mapping_table_schema: str, select_clause_value: str,
                               profile_mapping_table_name: str) -> int:
        """Inserts a profile mapping."""
        logger.start("Inserting profile mapping ...", object={
            'profile_id': profile_id, 'entity_id': entity_id, 'profile_mapping_table_schema': profile_mapping_table_schema,
            'select_clause_value': select_clause_value, 'profile_mapping_table_name': profile_mapping_table_name})
        created_user_id = updated_user_id = user_context.get_effective_user_id()
        sql = "INSERT IGNORE INTO %s.%s (profile_id, %s, created_user_id, updated_user_id) VALUES (%s, %s, %s, %s)" % (
            profile_mapping_table_schema, profile_mapping_table_name, select_clause_value, profile_id, entity_id,
            created_user_id, updated_user_id)
        if profile_mapping_table_schema == "group_profile":
            sql = "INSERT IGNORE INTO %s.%s (profile_id, %s, relationship_type_id, created_user_id, updated_user_id) VALUES (%s, %s, %s, %s, %s)" % (
                profile_mapping_table_schema, profile_mapping_table_name, select_clause_value, profile_id, 5, entity_id,
                created_user_id, updated_user_id)
        self.cursor.execute(sql)
        self.connection.commit()
        inserted_id = self.cursor.lastrowid()
        logger.end("Profile mapping inserted", object={'inserted_id': inserted_id})
        return inserted_id

    def __get_profile_id(self, fields_dict: dict) -> int:
        """Gets the profile ID."""
        profile_id = None
        if "Email" in fields_dict:
            email_address = fields_dict["Email"]
            if isinstance(email_address, tuple):
                email_address = self.__get_email_from_tuple(email_address)
            # Try to get profile_id from person_id
            person_id = self.persons_local.get_person_id_by_email_address(email_address)
            if person_id:
                profile_id = self.profiles_local.select_one_value_by_id(
                    view_table_name="profile_view",
                    select_clause_value="profile_id",
                    id_column_name="person_id",
                    id_column_value=person_id
                )
            # Try to get profile_id from contact_id
            if not profile_id:
                # get email_address_id
                email_address_id = self.select_one_value_by_id(
                    schema_name="email_address",
                    view_table_name="email_address_view",
                    select_clause_value="email_address_id",
                    id_column_name="email_address",
                    id_column_value=email_address
                )
                if email_address_id:
                    # get contact_id
                    contact_id = self.select_one_value_by_id(
                        schema_name="contact_email_address",
                        view_table_name="contact_email_address_view",
                        select_clause_value="contact_id",
                        id_column_name="email_address_id",
                        id_column_value=email_address_id
                    )
                    if contact_id:
                        # get profile_id
                        profile_id = self.select_one_value_by_id(
                            schema_name="contact_profile",
                            view_table_name="contact_profile_view",
                            select_clause_value="profile_id",
                            id_column_name="contact_id",
                            id_column_value=contact_id
                        )
        elif "Phone Number" in fields_dict:
            phone_number = fields_dict["Phone Number"]
            # Try to get profile_id from contact_id
            phone_id = self.select_one_value_by_id(
                schema_name="phone",
                view_table_name="phone_view",
                select_clause_value="phone_id",
                id_column_name="number_original",
                id_column_value=phone_number
            )
            if not phone_id:
                phone_id = self.select_one_value_by_id(
                    schema_name="phone",
                    view_table_name="phone_view",
                    select_clause_value="phone_id",
                    id_column_name="full_number_normalized",
                    id_column_value=phone_number
                )
            if phone_id:
                # get contact_id
                contact_id = self.select_one_value_by_id(
                    schema_name="contact_phone",
                    view_table_name="contact_phone_view",
                    select_clause_value="contact_id",
                    id_column_name="phone_id",
                    id_column_value=phone_id
                )
                if contact_id:
                    # get profile_id
                    profile_id = self.select_one_value_by_id(
                        schema_name="contact_profile",
                        view_table_name="contact_profile_view",
                        select_clause_value="profile_id",
                        id_column_name="contact_id",
                        id_column_value=contact_id
                    )
        elif "Person Id" in fields_dict:
            person_id = fields_dict["Person Id"]
            profile_id = self.profiles_local.select_one_value_by_id(
                view_table_name="profile_view",
                select_clause_value="profile_id",
                id_column_name="person_id",
                id_column_value=person_id
            )
        if profile_id is not None:
            self.profile_id = profile_id
        elif self.profile_id is not None:
            profile_id = self.profile_id
        else:
            profile_id = self.select_one_value_by_id(
                schema_name="text_block",
                view_table_name="text_block_view",
                select_clause_value="profile_id",
                id_column_name="text_block_id",
                id_column_value=self.text_block_id
            )
        return profile_id

    def __get_index_in_regex_to_field_id_mapping(self, text_block_type_id: int) -> dict:
        """Gets the index_in_regex to field_id mapping."""
        field_text_block_types_dicts = self.field_block_type_generic_crud.select_multi_dict_by_where(
            select_clause_value="index_in_regex, field_id",
            view_table_name="field_text_block_type_view",
            where="text_block_type_id = %s",
            params=(text_block_type_id,))
        if not field_text_block_types_dicts:
            return None
        index_in_regex_to_field_id_mapping = {}
        for field_text_block_types_dict in field_text_block_types_dicts:
            if field_text_block_types_dict["index_in_regex"] is None:
                return None
            index_in_regex_to_field_id_mapping[field_text_block_types_dict["index_in_regex"]] = field_text_block_types_dict["field_id"]
        return index_in_regex_to_field_id_mapping

    def __get_field_name_by_field_id(self, field_id: int) -> str:
        """Gets the field name by field ID."""
        field_name = self.select_one_value_by_id(
            schema_name="field",
            view_table_name="field_view",
            select_clause_value="name",
            id_column_name="field_id",
            id_column_value=field_id
        )
        return field_name

    def __organize_fields_dict(self, fields_dict: dict, text_block_type_id: int, current_match_index: int) -> dict:
        """Organizes the fields dictionary."""
        organized_fields_dict = {}
        index_in_regex_to_field_id_mapping = self.__get_index_in_regex_to_field_id_mapping(text_block_type_id)
        if not index_in_regex_to_field_id_mapping:
            for key, matches in fields_dict.items():
                organized_fields_dict[key] = matches[current_match_index] if isinstance(matches, list) else matches
        else:
            for key, matches in fields_dict.items():
                for matches_index, match in enumerate(matches):
                    if matches_index != current_match_index:
                        continue
                    for match_index, item in enumerate(match):
                        field_id = index_in_regex_to_field_id_mapping.get(match_index)
                        if field_id:
                            field_name = self.__get_field_name_by_field_id(field_id)
                            organized_fields_dict[field_name] = match[match_index] if isinstance(match, list) else match
        return organized_fields_dict

    def __get_email_from_tuple(self, tuple_example):
        for element in tuple_example:
            if '@' in element:
                return element
        return None

    def process_field(self, processing_id, match):
        pass
        # if processing_id == 1: #birthday YYYY-MM-DD

        # else if processing_id ==2: #phone

        # return processed_value