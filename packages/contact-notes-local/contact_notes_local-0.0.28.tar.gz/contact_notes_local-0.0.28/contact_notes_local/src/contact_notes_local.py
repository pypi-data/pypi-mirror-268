import re
from datetime import datetime

from action_items_local.action_items_local import ActionItemsLocal
from contact_group_local.contact_group import ContactGroup
from database_infrastructure_local.number_generator import NumberGenerator
from database_mysql_local.generic_crud import GenericCRUD
from database_mysql_local.generic_crud_ml import GenericCRUDML
from database_mysql_local.generic_mapping import GenericMapping
from language_remote.lang_code import LangCode
from logger_local.LoggerLocal import Logger
from text_block_local.text_block import TextBlocks
from user_context_remote.user_context import UserContext

from .contact_notes_local_constants import CONTACT_NOTES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT

DEFAULT_SCHEMA_NAME = "contact_note"
DEFAULT_TABLE_NAME = "contact_note_text_block_table"
DEFAULT_VIEW_NAME = "contact_note_text_block_view"
DEFAULT_ID_COLUMN_NAME = "conact_note_text_block_id"
DEFAULT_ENTITY_NAME1 = "contact_note"
DEFAULT_ENTITY_NAME2 = "text_block"

PROFILE_MILESTONE_SCHEMA_NAME = "profile_milestone"
PROFILE_MILESTONE_TABLE_NAME = "profile_milestone_table"
PROFILE_MILESTONE_VIEW_NAME = "profile_milestone_table_view"
PROFILE_MILESTONE_ID_COLUMN_NAME = "profile_milestone_id"

logger = Logger.create_logger(object=CONTACT_NOTES_PYTHON_PACKAGE_CODE_LOGGER_OBJECT)

user_context = UserContext()


# TODO We should add the action-items tables


class ContactNotesLocal(GenericMapping):
    def __init__(self, contact_dict: dict, contact_id: int, profile_id: int,
                 default_schema_name: str = DEFAULT_SCHEMA_NAME,
                 default_table_name: str = DEFAULT_TABLE_NAME,
                 default_view_table_name: str = DEFAULT_VIEW_NAME,
                 default_id_column_name: str = DEFAULT_ID_COLUMN_NAME,
                 default_entity_name1: str = DEFAULT_ENTITY_NAME1,
                 default_entity_name2: str = DEFAULT_ENTITY_NAME2,
                 lang_code: LangCode = None, is_test_data: bool = False) -> None:
        GenericMapping.__init__(self, default_schema_name=default_schema_name,
                                default_table_name=default_table_name,
                                default_view_table_name=default_view_table_name,
                                default_id_column_name=default_id_column_name,
                                default_entity_name1=default_entity_name1,
                                default_entity_name2=default_entity_name2,
                                is_test_data=is_test_data)
        self.generic_crud_ml = GenericCRUDML(default_schema_name="name",
                                             default_table_name="first_name_table",
                                             default_id_column_name="first_name_id",
                                             is_test_data=is_test_data)
        self.lang_code = lang_code or user_context.get_effective_profile_preferred_lang_code()
        self.contact_id = contact_id
        self.profile_id = profile_id
        self.contact_dict = contact_dict
        self.text_blocks = TextBlocks()
        self.contact_group = ContactGroup()
        self.action_items_local = ActionItemsLocal()

    def insert_contact_notes_text_block(self) -> dict or None:
        logger.start()
        # check if the contact already has notes
        where_clause = "contact_id = %s"
        params = (self.contact_id,)
        contact_note_dict = self.select_one_dict_by_where(
            view_table_name="contact_note_view",
            where=where_clause,
            params=params
        )
        if contact_note_dict:
            logger.end(log_message="contact already has notes")
            # TODO: select contact_note_text_block_ids_list and add it to the return object
            insert_information = {
                "contact_note_id": contact_note_dict.get("contact_note_id"),
                "contact_note_text_block_ids_list": None
            }
            return insert_information
        # the contact does not have notes, insert the notes
        contact_note_id = self.insert_contact_notes()
        if not contact_note_id:
            logger.end(log_message="contact_note_id is None")
            return None
        contact_note_text_block_ids_list = self.insert_contact_note_text_block_table(contact_note_id=contact_note_id)
        logger.end(object={"contact_note_id": contact_note_id,
                           "contact_note_text_block_ids_list": contact_note_text_block_ids_list})
        insert_information = {
            "contact_note_id": contact_note_id,
            "contact_note_text_block_ids_list": contact_note_text_block_ids_list
        }
        return insert_information

    def insert_contact_notes(self, ignore_duplicate: bool = False) -> int or None:
        logger.start(object={"ignore_duplicate": ignore_duplicate})
        note = self.contact_dict.get('notes', None)
        random_number = NumberGenerator.get_random_number(schema_name=self.schema_name,
                                                          view_name="contact_note_table")
        identifier = NumberGenerator.get_random_identifier(schema_name=self.schema_name,
                                                           view_name="contact_note_table",
                                                           identifier_column_name="identifier")
        if not note:
            logger.end(f"no note for contact_id: {self.contact_id}")
            return None
        data_json = {
            'contact_id': self.contact_id,
            'note': note,
            'number': random_number,
            'identifier': identifier,
            # TODO: shall we add created_user_id?
            # TODO: shall we add created_real_user_id?
            # TODO: shall we add created_effective_profile_id? 
        }
        contact_note_id = self.insert(table_name="contact_note_table", data_json=data_json,
                                      ignore_duplicate=ignore_duplicate)
        logger.end(object={"contact_note_id": contact_note_id})
        return contact_note_id

    # TODO This is mapping table between contact_note_id, and text_block_id, with seq (order of the text_blocks) as attribute.
    #     I would expected to have those three as parameters.
    # TODO Update seq (order of text_blocks) in the database
    def insert_contact_note_text_block_table(self, contact_note_id: int) -> list or None:
        """
        This method will insert the note into the contact_note_text_block_table if it not exists there
        :param contact_note_id: the id of the contact_note_table
        :return: the id of the inserted row
        """
        logger.start(object={"contact_note_id": contact_note_id})
        note = self.contact_dict.get('notes', None)
        if not note:
            logger.end(log_message="no note for contact_note_id", object={"contact_note_id": contact_note_id})
            return None
        # Check if the contact_note is already linked to text_blocks
        mapping_tuple = self.select_multi_tuple_by_id(view_table_name=self.default_view_table_name,
                                                      id_column_name="contact_note_id",
                                                      id_column_value=contact_note_id)
        # TODO: shall we keep this check?
        if mapping_tuple:
            logger.end(log_message=f"contact_note_id: {contact_note_id} already linked to text_blocks",
                       object={"contact_note_id": contact_note_id})
            return None
        # TODO ..from_contact_note() or ..._by_contact_note_id()
        text_blocks_list = self.get_text_blocks_list_from_note()
        try:
            text_blocks_list = self.__process_text_blocks_list(text_blocks_list=text_blocks_list)
        except ValueError as value_error:
            logger.error(log_message=f"ValueError: {value_error}")
            logger.end(log_message="text_blocks were not inserted to the database because of ValueError")
            return None

        text_block_ids_list = []
        contact_note_text_block_ids_list = []
        for i, text_block in enumerate(text_blocks_list):
            is_text_block_none_type = False
            is_text_block_event = False
            if i == 0:
                data_json = {
                    'text': text_block,
                    'seq': i,  # This is the index of the current text_block in the list
                    'profile_id': self.profile_id,
                }
            else:
                is_text_block_none_type = not text_block.get('is_action_item') and text_block.get('text')
                if not text_block.get('is_action_item') and not text_block.get('text'):
                    # text block is event
                    is_text_block_event = True
                    start_timestamp = self.__extract_start_timestamp(text_block=text_block)
                    data_json = {
                        'text': text_block.get('event', None),
                        'start_timestamp': start_timestamp,
                        'seq': i,  # This is the index of the current text_block in the list
                        'profile_id': self.profile_id,
                    }
                elif is_text_block_none_type:
                    # text block is text
                    data_json = {
                        'text': text_block.get('text'),
                        'seq': i,  # This is the index of the current text_block in the list
                        'profile_id': self.profile_id,
                    }
                else:
                    # text block is action item
                    data_json = {
                        'text': text_block.get('text'),
                        'seq': i,  # This is the index of the current text_block in the list
                        'profile_id': self.profile_id,
                    }
            text_block_id = self.text_blocks.insert(schema_name="text_block", table_name="text_block_table",
                                                    data_json=data_json)
            text_block_ids_list.append(text_block_id)
            if is_text_block_none_type:
                self.text_blocks.process_text_block_by_id(text_block_id=text_block_id)

            # link the contact_note_id to the text_block_id
            data_json = {
                'seq': i,
            }
            # Insert the mapping between the contact_note_id and the text_block_id
            logger.info(log_message=f"Inserting mapping between contact_note_id: {contact_note_id} and"
                                    f" text_block_id: {text_block_id}")
            conact_note_text_block_id = self.insert_mapping(entity_name1=DEFAULT_ENTITY_NAME1,
                                                            entity_name2=DEFAULT_ENTITY_NAME2,
                                                            entity_id1=contact_note_id,
                                                            entity_id2=text_block_id,
                                                            data_json=data_json,
                                                            ignore_duplicate=True)
            contact_note_text_block_ids_list.append(conact_note_text_block_id)

            # add the text block to profile_milestone
            if is_text_block_event:
                # TODO: not used
                profile_milestone_id = self.__add_text_block_to_profile_milestone(text_block_id=text_block_id,
                                                                                  text_block=text_block)

        logger.end(object={"contact_note_id": contact_note_id, "text_block_ids_list": text_block_ids_list,
                           "conact_note_text_block_ids_list": contact_note_text_block_ids_list})
        return contact_note_text_block_ids_list

    def __add_text_block_to_profile_milestone(self, text_block_id: int, text_block: dict) -> int:
        logger.start(object={"text_block_id": text_block_id})
        number = NumberGenerator.get_random_number(
            schema_name=PROFILE_MILESTONE_SCHEMA_NAME, view_name=PROFILE_MILESTONE_TABLE_NAME
        )
        start_timestamp = self.__extract_start_timestamp(text_block=text_block)
        data_json = {
            'number': number,
            'text_block_id': text_block_id,
            'profile_id': self.profile_id,
            'is_sure': text_block.get('is_sure', True),
            'start_timestamp': start_timestamp,
            'is_test_data': self.is_test_data,
        }
        generic_crud = GenericCRUD(
            default_schema_name=PROFILE_MILESTONE_SCHEMA_NAME, default_table_name=PROFILE_MILESTONE_TABLE_NAME,
            default_view_table_name=PROFILE_MILESTONE_VIEW_NAME,
            default_id_column_name=PROFILE_MILESTONE_ID_COLUMN_NAME,
            is_test_data=self.is_test_data
        )
        profile_milestone_id = generic_crud.insert(data_json=data_json)
        logger.end(object={"profile_milestone_id": profile_milestone_id})
        return profile_milestone_id

    def get_text_blocks_list_from_note(self) -> list:
        note = self.contact_dict.get('notes')
        if not note:
            return []
        logger.start(object={"note": note})
        text_blocks_list = note.split("\n\n")
        logger.end(object={"text_blocks_list": text_blocks_list})
        return text_blocks_list

    def __process_text_blocks_list(self, text_blocks_list: list) -> list:
        logger.start(object={"text_blocks_list": text_blocks_list})
        processed_text_blocks_list = []
        for i, text_block in enumerate(text_blocks_list):
            if i == 0:
                # Process the first line (group names)
                self.__process_first_text_block(text_block=text_block)

                # Append the text_block to the processed_text_blocks_list
                processed_text_blocks_list.append(text_block)
            else:
                text_block_dict = self.__process_text_block(text_block=text_block)
                if text_block_dict:
                    processed_text_blocks_list.append(text_block_dict)
        logger.end()
        return processed_text_blocks_list

    # TODO If 1st line in the text_block includes -----, each line bellow is Action Item / Task
    def __process_text_block(self, text_block: str) -> dict:
        text_block_dict = {}
        # Split the text block into lines
        lines = text_block.splitlines()
        # Check if the first line contains '-----'
        if len(lines) > 0 and '-----' in lines[0]:
            # Process each line below as an Action Item / Task
            for line in lines[1:]:
                self.__process_insert_action_item(line)
            text_block_dict = {
                'is_action_item': True,
                'text': text_block,
            }
        elif len(lines) > 0:
            is_sure = True
            # Check if the first line contains '?'
            if '?' in lines[0]:
                is_sure = False

            # Split the text block into parts
            parts = text_block.split(' ')

            # The first part is always the date
            milestone_date = parts[0]

            # Specify the possible date formats
            date_formats = ["%y%m%d", "%y%m", "%Y", "%Y%m", "%d/%m/%y", "%d/%m/%Y"]

            is_event = False
            # Check if the date is in any of the formats
            for date_format in date_formats:
                formatted_date = self.__convert_date_format(date_str=milestone_date, date_format=date_format)
                if not formatted_date:
                    continue
                milestone_date = formatted_date
                is_event = True
                break
            # TODO: don't log error, add a "free" text block if it doesn't match any of the formats.
            # else:
            # logger.error(log_message=f"Date '{milestone_date}' is not in any of the formats: {date_formats}")
            # raise ValueError(f"Date '{milestone_date}' is not in any of the formats: {date_formats}")

            if is_event is False:
                text_block_dict = {
                    'is_action_item': False,
                    'text': text_block,
                }
                return text_block_dict
            # Check if the second part is a time
            time = None
            event_start_index = 1
            if len(parts) > 1 and parts[1]:
                if re.match(r'\d{2}:\d{2}:\d{2}', parts[1]):
                    time = parts[1]
                    event_start_index = 2

            # The rest of the parts form the event
            event = ' '.join(parts[event_start_index:])

            text_block_dict = {
                'is_action_item': False,
                'date': milestone_date,
                'time': time,
                'event': event,
                'is_sure': is_sure
            }

        return text_block_dict

    @staticmethod
    def __convert_date_format(date_str: str, date_format: str) -> str or None:
        # Parse the date from the input format
        date = None
        try:
            date = datetime.strptime(date_str, date_format)
        except ValueError:
            pass
        if date is None:
            return None

        # Format the date in the output format
        new_date_str = date.strftime("%Y-%m-%d")

        return new_date_str

    @staticmethod
    def __extract_start_timestamp(text_block: dict) -> str:
        date = text_block.get('date')
        time = text_block.get('time')
        if date and time:
            start_timestamp = date + " " + time
        elif date:
            start_timestamp = date + " 00:00:00"
        else:
            logger.exception(log_message=f"date and time are both None for text_block: {text_block}, "
                                         "please add date(and optionally time) to the start of the text_block")
            raise Exception(f"event text_block has invalid date : {text_block}")
        return start_timestamp

    def __process_insert_action_item(self, action_item: str) -> None:
        data_action_item = {
            'title': action_item,
            'is_title_approved': True,
        }
        self.action_items_local.insert_link_action_item_contact(data_action_item=data_action_item,
                                                                contact_id=self.contact_id,
                                                                contact_dict=self.contact_dict)

    @staticmethod
    def escape_string(string: str or None) -> str or None:
        if string is None:
            return None
        replacements = {
            "\\": "\\\\",
            "'": "\\'",
            '"': '\\"',
            "%": "\\%",
            "_": "\\_"
        }
        for search, replace in replacements.items():
            string = string.replace(search, replace)
        return string

    def __process_first_text_block(self, text_block: str) -> None:
        # is_sure gruops (not ending with 'X' or '?')
        text_block_fields = [
            name.strip()
            for name in text_block.split(',')
            if not (name.strip().endswith('X') or name.strip().endswith('?'))
        ]
        mapping_data_json = {
            'seq': 0,
            'is_sure': True,
        }
        groups = []
        if text_block_fields:  # Proceed only if there are valid group names
            for text_block_field in text_block_fields:
                if text_block_field[0] == "2":
                    self.__process_insert_action_item(action_item=text_block_field)
                else:
                    self.__update_name_schema(text_block_field=text_block_field)
                    groups.append(text_block_field)
            self.contact_group.insert_link_contact_group_with_groups_local(
                contact_id=self.contact_id,
                groups=groups,
                mapping_data_json=mapping_data_json
            )
        # not is_sure gruops (ending with '?')
        text_block_fields = [
            name.strip()
            for name in text_block.split(',')
            if name.strip().endswith('?')
        ]
        mapping_data_json = {
            'seq': 0,
            'is_sure': False,
        }
        if text_block_fields:  # Proceed only if there are valid group names
            self.contact_group.insert_link_contact_group_with_groups_local(
                contact_id=self.contact_id,
                groups=text_block_fields,
                mapping_data_json=mapping_data_json
            )

    # TODO: shall we move this to a new "name-local" package?
    def __update_name_schema(self, text_block_field: str):
        name_dict = self.__get_first_name_and_last_name()
        first_name = name_dict.get("first_name")
        last_name = name_dict.get("last_name")
        if not first_name or not last_name:
            return
        gender_dict = self.select_one_dict_by_id(
            schema_name="gender",
            view_table_name="gender_ml_view",
            id_column_name="title",
            id_column_value=text_block_field
        )
        gender_id = None
        if gender_dict:
            gender_id = gender_dict.get("gender_id")
        else:
            return
        if gender_id:
            # determine gender_list_id
            gender_list_id = 3
            if gender_id == 1:
                gender_list_id = 1
            elif gender_id == 2:
                gender_list_id = 2
            # add first name to db
            data_json = {
                "gender_id": gender_id,
                "gender_list_id": gender_list_id
            }
            data_ml_json = {
                "name": first_name,
                "is_name_approved": False,
                "is_description_approved": False
            }
            # We use upsert because it may update the gender_id
            self.generic_crud_ml.upsert_value(
                table_name="first_name_table",
                ml_table_name="first_name_ml_table",
                data_json=data_json,
                lang_code=self.lang_code,
                data_ml_json=data_ml_json
            )

            # add last name to db
            data_json = {
                "name": last_name
            }
            data_ml_json = {
                "name": last_name,
                "is_name_approved": False,
                "is_description_approved": False
            }
            # calling upsert can cause error: Duplicate entry for key 'last_name_table.name_UNIQUE'
            # when the upsert calls the update method
            self.generic_crud_ml.add_value_if_not_exist(
                table_name="last_name_table",
                ml_table_name="last_name_ml_table",
                data_json=data_json,
                lang_code=self.lang_code,
                data_ml_json=data_ml_json
            )

    def __get_first_name_and_last_name(self) -> dict:
        first_name = self.contact_dict.get('first_name', None)
        last_name = self.contact_dict.get('last_name', None)
        if not first_name or not last_name:
            profile_dict = self.select_one_dict_by_id(
                schema_name="profile",
                view_table_name="profile_view",
                id_column_name="profile_id",
                id_column_value=self.profile_id
            )
            if profile_dict:
                person_id = profile_dict.get("person_id")
                person_dict = self.select_one_dict_by_id(
                    schema_name="person",
                    view_table_name="person_view",
                    id_column_name="person_id",
                    id_column_value=person_id
                )
                if person_dict:
                    first_name = first_name or person_dict.get("first_name")
                    last_name = last_name or person_dict.get("last_name")
        result = {
            "first_name": first_name,
            "last_name": last_name
        }
        return result
