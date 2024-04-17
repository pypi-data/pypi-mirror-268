from random import randint

from database_infrastructure_local.number_generator import NumberGenerator
from database_mysql_local.generic_crud import GenericCRUD
from email_address_local.email_address import EmailAddressesLocal
from location_local.locations_local_crud import LocationsLocal
from logger_local.MetaLogger import MetaLogger

from .constans import user_local_python_code_logger_object


class UsersLocal(GenericCRUD, metaclass=MetaLogger, object=user_local_python_code_logger_object):
    def __init__(self, is_test_data: bool = False):
        super().__init__(default_schema_name="user", default_view_table_name="user_not_deleted_view",
                         default_table_name="user_table", default_id_column_name="user_id",
                         is_test_data=is_test_data)

    def insert(self, username: str, main_email: str,  # noqa
               first_name: str, last_name: str, location_id: int, is_test_data: bool = False) -> int:
        """Returns user_id (int) of the inserted user record"""
        number = NumberGenerator.get_random_number("user", "user_table", "user_id")
        data_json = {"number": number, "username": username, "main_email": main_email,
                     "first_name": first_name, "last_name": last_name, "active_location_id": location_id,
                     "is_test_data": is_test_data}
        user_id = super().insert(data_json=data_json)
        return user_id

    def update_by_user_id(self, user_id: int, username: str = None, main_email: str = None, first_name: str = None,
                          last_name: str = None, active_location_id: int = None):
        """Updates the user record with the given user_id with the given values"""
        data_json = {k: v for k, v in locals().items() if k != "self" and v is not None}
        assert len(data_json) > 1, "At least one of the fields must be updated"
        self.update_by_id(data_json=data_json,
                          id_column_name="user_id", id_column_value=user_id)

    def read_user_tuple_by_user_id(self, user_id: int) -> (int, int, str, str, str, str, int):
        """
        Returns a tuple of (number, username, main_email, first_name, last_name, active_location_id)
        """
        return self.select_one_tuple_by_id(
            select_clause_value="number, username, main_email, first_name, last_name, active_location_id",
            id_column_value=user_id)

    def read_user_dict_by_user_id(self, user_id: int) -> dict:
        """
        Returns a tuple of (number, username, main_email, first_name, last_name, active_location_id)
        """
        return self.select_one_dict_by_id(
            select_clause_value="number, username, main_email, first_name, last_name, active_location_id",
            id_column_value=user_id)

    def delete_by_user_id(self, user_id: int):
        """
        Updates the user end_timestamp with the given user_id
        """
        self.delete_by_id(id_column_value=user_id)

    def get_test_user_id(self):
        username = "test username " + str(randint(1, 100000))
        test_email_address = EmailAddressesLocal.get_test_email_address()
        first_name = "test first name " + str(randint(1, 100000))
        last_name = "test last name " + str(randint(1, 100000))
        test_location_id = LocationsLocal().get_test_location_id()
        insert_kwargs = {"username": username, "main_email": test_email_address,
                         "first_name": first_name, "last_name": last_name, "location_id": test_location_id}

        return self.get_test_entity_id(entity_name="user",
                                       insert_function=self.insert,
                                       insert_kwargs=insert_kwargs)
