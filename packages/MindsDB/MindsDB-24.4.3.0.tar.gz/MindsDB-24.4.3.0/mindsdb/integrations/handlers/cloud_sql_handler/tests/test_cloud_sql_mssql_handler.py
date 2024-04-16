import unittest
from mindsdb.integrations.handlers.cloud_sql_handler.cloud_sql_handler import CloudSQLHandler
from mindsdb.api.executor.data_types.response_type import RESPONSE_TYPE


class CloudSQLMSSQLHandlerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kwargs = {
            "host": "",
            "port": 1433,
            "user": "root",
            "password": "",
            "database": "public",
            "db_engine": "mssql"
        }
        cls.handler = CloudSQLHandler('test_cloud_sql_mssql_handler', cls.kwargs)

    def test_0_check_connection(self):
        assert self.handler.check_connection()

    def test_1_native_query_select(self):
        query = "SELECT * FROM person"
        result = self.handler.native_query(query)
        assert result.type is RESPONSE_TYPE.TABLE

    def test_2_get_tables(self):
        tables = self.handler.get_tables()
        assert tables.type is not RESPONSE_TYPE.ERROR

    def test_3_get_columns(self):
        columns = self.handler.get_columns('person')
        assert columns.type is not RESPONSE_TYPE.ERROR


if __name__ == '__main__':
    unittest.main()
