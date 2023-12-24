import os
import sqlite3

from src.util.configUtil import ConfigUtil

class Database:

    _config = None

    cursor = None
    connection = None

    def __init__(self):
        print('@Debug: Database init...')
        
        self._config = ConfigUtil(configType='DATABASE')

        if (os.path.exists(self._config.getDatabaseResourceFull())):
            self.connection = sqlite3.connect(database=self._config.getDatabaseResourceFull(), timeout=10000)
            self.cursor = self.connection.cursor()
            self.cursor.execute(self._config.getDatabaseDDLInitByName(ddlName='create_table_sql'))
        else:
            self.connection = sqlite3.connect(database=self._config.getDatabaseResourceFull(), timeout=10000)
            self.cursor = self.connection.cursor()

    
    def formatSQL(self, query, departmentEscape, departmentSpecifiedEscape):
        if '$d' in query:
            query = query.replace('$d', '"%' + departmentEscape + '%"')
        if '$s' in query:
            query = query.replace('$s', '"%' + departmentSpecifiedEscape + '%"')

        return query