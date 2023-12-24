from src.util.database import Database
from src.util.configUtil import ConfigUtil

class MainActivityModel:

    def __init__(self):
        print('@Debug: MainActivityModel init...')
        
        self.config = ConfigUtil("DATABASE")
        self.database = Database()

    
    def retrieveResultByDepartment(self, department):
        return self.database.cursor.execute(self.database.formatSQL(self.config.getDatabaseDMLByName('select_by_department'), department.upper().strip(), ''))
    
    def retrieveResultByDepartmentSpecified(self, departmentSpecified):
        return self.database.cursor.execute(self.database.formatSQL(self.config.getDatabaseDMLByName('select_by_departmentSpecified'), '', departmentSpecified.upper().strip()))
    
    def retrieveResultByDepartmentAndDepartmentSpecified(self, department, departmentSpecified):
        return self.database.cursor.execute(self.database.formatSQL(self.config.getDatabaseDMLByName('select_by_misc'), department.upper(), departmentSpecified.upper().strip()))