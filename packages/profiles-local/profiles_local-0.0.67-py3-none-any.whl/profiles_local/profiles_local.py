from typing import Dict

from database_mysql_local.generic_crud import GenericCRUD
from language_remote.lang_code import LangCode
from logger_local.MetaLogger import MetaLogger
from person_local.src.persons_local import PersonsLocal

from .constants_profiles_local import PROFILE_LOCAL_PYTHON_LOGGER_CODE, DEFAULT_LANG_CODE


class ProfilesLocal(GenericCRUD, metaclass=MetaLogger, object=PROFILE_LOCAL_PYTHON_LOGGER_CODE):
    def __init__(self):
        super().__init__(default_schema_name="profile", default_table_name="profile_table",
                         default_view_table_name="profile_view", default_id_column_name="profile_id")

    # TODO Shall we give insert() the person_id or shell insert() UPSERT person?
    def insert(self, profile_json: Dict[str, any], person_id: int, is_test_data: bool = False) -> int:  # noqa
        """Returns the new profile_id"""
        if "person_id" not in profile_json:
            profile_json["person_id"] = person_id
        if not isinstance(profile_json.get('preferred_lang_code'), str):
            profile_json["preferred_lang_code"] = profile_json.get('preferred_lang_code', DEFAULT_LANG_CODE).value

        profile_json["is_test_data"] = is_test_data
        valid_columns = ['profile_id', 'number', 'identifier', 'name', 'user_id', 'person_id', 'is_main',
                         'visibility_id', 'is_approved', 'profile_type_id', 'preferred_lang_code',
                         'experience_years_min', 'main_phone_id', 'profile_main_email', 'is_rip', 'gender_id', 'stars',
                         'last_dialog_workflow_state_id', 'is_system', 'internal_description', 'is_test_data',
                         'is_business_profile']
        profile_json = {k: v for k, v in profile_json.items() if k in valid_columns}
        super().insert(data_json=profile_json)

        profile_id = self.cursor.lastrowid()
        profile_ml_table_json = {
            "profile_id": profile_id,
            "lang_code": profile_json.get('lang_code', DEFAULT_LANG_CODE).value,
            "name": profile_json['name'],  # Cannot be None
            "name_approved": profile_json.get('name_approved'),
            "about": profile_json.get('about')
        }
        super().insert(table_name="profile_ml_table", data_json=profile_ml_table_json)

        return profile_id

    def update(self, profile_dict: Dict[str, any]) -> None:
        profile_id = profile_dict['profile_id']
        profile_json = {
            "person_id": profile_dict.get('person_id'),
            "name": profile_dict.get('name'),
            "user_id": profile_dict.get('user_id'),
            "is_main": profile_dict.get('is_main'),
            "visibility_id": profile_dict.get('visibility_id'),
            "is_approved": profile_dict.get('is_approved'),
            "profile_type_id": profile_dict.get('profile_type_id'),
            "preferred_lang_code": profile_dict.get('preferred_lang_code', DEFAULT_LANG_CODE).value,
            "experience_years_min": profile_dict.get('experience_years_min'),
            "main_phone_id": profile_dict.get('main_phone_id'),
            "is_rip": profile_dict.get('is_rip'),
            "gender_id": profile_dict.get('gender_id'),
            "stars": profile_dict.get('stars'),
            "last_dialog_workflow_state_id": profile_dict.get('last_dialog_workflow_state_id')
        }
        self.update_by_id(id_column_value=profile_id, data_json=profile_json)

        profile_ml_table_json = {
            "profile_id": profile_id,
            "lang_code": profile_dict.get('lang_code', DEFAULT_LANG_CODE).value,
            # TODO Should change in the database and code from name, name_approved to title, title_approved
            "name": profile_dict['name'],
            "name_approved": profile_dict['name_approved'],
            "about": profile_dict.get('about')
        }
        self.update_by_id(table_name="profile_ml_table",
                          id_column_value=profile_id, data_json=profile_ml_table_json)

    # TODO develop get_profile_object_by_profile_id( self, profile_id: int ) -> Profile[]:
    def get_profile_json_by_profile_id(self, profile_id: int) -> Dict[str, any]:
        profile_ml_dict = self.select_one_dict_by_id(
            view_table_name="profile_ml_view", id_column_value=profile_id)
        profile_dict = self.select_one_dict_by_id(id_column_value=profile_id)

        if not profile_ml_dict or not profile_dict:
            return {}
        return {**profile_ml_dict, **profile_dict}

    def get_profile_id_by_email_address(self, email_address: str) -> int:
        return self.select_one_dict_by_id(id_column_name="main_email_address",
                                          id_column_value=email_address,
                                          select_clause_value="profile_id").get('profile_id')

    def delete_by_profile_id(self, profile_id: int):
        self.delete_by_id(id_column_value=profile_id)

    def get_preferred_lang_code_by_profile_id(self, profile_id: int) -> LangCode:
        preferred_lang_code = self.select_one_dict_by_id(id_column_value=profile_id).get('preferred_lang_code')

        return LangCode(preferred_lang_code)

    def get_test_profile_id(self) -> int:
        person_id = PersonsLocal().get_test_person_id()
        return self.get_test_entity_id(entity_name="profile",
                                       insert_function=self.insert,
                                       insert_kwargs={"profile_json": {}, "person_id": person_id})

    def insert_profile_type(self, is_test_data: bool = False) -> int:
        profile_type_table_json = {"is_test_data": is_test_data}
        profile_type_id = super().insert(table_name="profile_type_table", data_json=profile_type_table_json)

        return profile_type_id

    def get_test_profile_type_id(self) -> int:
        return self.get_test_entity_id(entity_name="profile_type",
                                       insert_function=self.insert_profile_type)
