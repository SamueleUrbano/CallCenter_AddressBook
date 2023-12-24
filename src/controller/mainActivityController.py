from src.model.mainActivityModel import MainActivityModel

class MainActivityController:

    def __init__(self):
        print('@Debug: MainActivityController init...')
        
        self.model = MainActivityModel()


    def handleSearchButtonAction(self, department, departmentSpecified):
        if department != '' and departmentSpecified != '':
            print('@Debug: value = ' + department + ' ' + departmentSpecified)
            return self.model.retrieveResultByDepartmentAndDepartmentSpecified(department=department, departmentSpecified=departmentSpecified)
        elif department != '':
            print('@Debug: value = ' + department)
            return self.model.retrieveResultByDepartment(department=department)
        elif departmentSpecified != '':
            print('@Debug: value = ' + departmentSpecified)
            return self.model.retrieveResultByDepartmentSpecified(departmentSpecified=departmentSpecified)
        
    def getResultCount(self, rows):
        return 'Risultati trovati: ' + str(rows)