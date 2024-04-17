from typing import Dict

from database_mysql_local.generic_crud import GenericCRUD
from language_local.lang_code import LangCode
from logger_local.MetaLogger import MetaLogger

from .constants import REACTION_LOCAL_PYTHON_LOGGER_CODE


# TODO Shall we use GenericCrudMl?
class ReactionsLocal(GenericCRUD, metaclass=MetaLogger, object=REACTION_LOCAL_PYTHON_LOGGER_CODE):
    def __init__(self, is_test_data: bool = False):
        super().__init__(default_schema_name="reaction", default_table_name="reaction_table",
                         default_view_table_name="reaction_ml_view", default_id_column_name="reaction_id",
                         is_test_data=is_test_data)

    def insert(self, reaction_dict: Dict[str, any], lang_code: LangCode) -> int:  # noqa
        reaction_type_id = self.select_one_value_by_id(select_clause_value="reaction_type_id",
                                                      view_table_name="reaction_type_ml_view",
                                                      id_column_name="title",
                                                      id_column_value=reaction_dict["title"])

        if not reaction_type_id:
            reaction_type_id = super().insert(data_json={})
            super().insert(table_name="reaction_type_ml_table", data_json={
                "reaction_type_id": reaction_type_id, "lang_code": lang_code.value, "title": reaction_dict["title"]})

        reaction_id = super().insert(data_json={"value": reaction_dict["value"], "image": reaction_dict["image"],
                                                "reaction_type_id": reaction_type_id})
        super().insert(table_name="reaction_ml_table", data_json={
            "reaction_id": reaction_id, "lang_code": lang_code.value, "title": reaction_dict["title"],
            "description": reaction_dict["description"], "name_approved": True})
        return reaction_id

    def update(self, reaction_id: int, reaction_json: Dict[str, any]) -> None:
        super().update_by_id(data_json={"value": reaction_json["value"], "image": reaction_json["image"]},
                             id_column_value=reaction_id)
        super().update_by_id(table_name="reaction_ml_table", id_column_value=reaction_id, data_json={
            "title": reaction_json["title"], "description": reaction_json["description"], "name_approved": True})

    def read_tuple_by_reaction_id(self, reaction_id: int) -> tuple:
        select_clause_value = "`value`, image, reaction_type_id, reaction_ml_id, lang_code, title, description"
        return self.select_one_tuple_by_id(select_clause_value=select_clause_value, view_table_name="reaction_ml_view",
                                           id_column_value=reaction_id)

    def read_dict_by_reaction_id(self, reaction_id: int) -> Dict[str, any]:
        select_clause_value = "`value`, image, reaction_type_id, reaction_ml_id, lang_code, title, description"
        return self.select_one_dict_by_id(select_clause_value=select_clause_value, view_table_name="reaction_ml_view",
                                          id_column_value=reaction_id)

    def delete_by_reaction_id(self, reaction_id: int):
        super().delete_by_id(id_column_value=reaction_id)

    @staticmethod
    def get_reaction_json_from_entry(entry: Dict[str, Dict[str, any]]) -> Dict[str, any]:
        return {
            "value": entry["reaction"].get("value", None),
            "image": entry["reaction"].get("image", None),
            "title": entry["reaction"].get("title", None)
        }
