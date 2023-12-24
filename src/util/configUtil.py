import configparser

class ConfigUtil:

    config = configparser.ConfigParser()

    def __init__(self, configType):
        print('@Debug: ConfigUtil init...')
        print('@Debug: configType = ' + configType)
        
        if configType.upper() == 'DATABASE':
            self.config.read('config/database_config.ini')
        elif configType.upper() == 'APPLICATION':
            self.config.read('config/app_config.ini')


    def getApplicationResoucePath(self):
        return self.config.get('APPLICATION_CONFIG', 'ui_resource_path')
    
    def getApplicationResourceByName(self, resourceName):
        return self.config.get('APPLICATION_CONFIG', resourceName) if resourceName != None else None
    
    def getDatabaseResourcePath(self):
        return self.config.get('DATABASE_CONFIG', 'database_path')
    
    def getDatabaseResourceName(self):
        return self.config.get('DATABASE_CONFIG', 'database_name')
    
    def getDatabaseResourceFull(self):
        return self.getDatabaseResourcePath() + self.getDatabaseResourceName()
    
    def getDatabaseDDLInitByName(self, ddlName):
        return self.config.get('DATABASE_DDL', ddlName) if ddlName != None else None
    
    def getDatabaseDMLByName(self, dmlName):
        return self.config.get('DATABASE_DML', dmlName) if dmlName != None else None