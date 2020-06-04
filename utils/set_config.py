import os
import errno
import configparser

class SetConfiguration(object):
    def __init__(self):
        self.set_config()
        self.set_path()
        self.set_test()
        self.set_result()
        
    def set_config(self):
        config_ini = configparser.ConfigParser()
        config_ini_path = './utils/config.ini'
        if not os.path.exists(config_ini_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)
        else:
            config_ini.read(config_ini_path)

        self.config_ini = config_ini
        return config_ini


    ##PATH SETTINGS
    def set_path(self):
        PATH = self.config_ini['PATH']
        self.PATH = PATH

    def get_path_data(self):
        PATH_DATA = self.PATH.get('DATA')
        self.PATH_DATA = PATH_DATA
        return PATH_DATA
        
    def get_path_save(self):
        PATH_SAVE = self.PATH.get('SAVE')
        self.PATH_SAVE = PATH_SAVE
        return PATH_SAVE

    def get_path_json(self):
        PATH_JSON = self.PATH.get('JSON')
        self.PATH_JSON = PATH_JSON
        return PATH_JSON


    ##TEST SETTINGS
    def set_test(self):
        TEST = self.config_ini['TEST']
        self.TEST = TEST

    def get_test_name(self, test_name):
        if test_name == 'angular_profile':
            TEST_NAME = eval(self.TEST.get('NAME'))[0]
            self.TEST_NAME = TEST_NAME
            return TEST_NAME
        else:
            raise ValueError("Invalid test name!")

    def get_test_type(self, test_type):
        if test_type == 'verification':
            TEST_TYPE = eval(self.TEST.get('TYPE'))[0]
            self.TEST_TYPE = TEST_TYPE
            return TEST_TYPE
        else:
            raise ValueError("Invalid test type!")

    def get_test_site(self, test_site):
        if test_site == 'chiba':
            TEST_SITE = eval(self.TEST.get('SITE'))[0]
            self.TEST_SITE = TEST_SITE
            return TEST_SITE
        else:
            raise ValueError("Invalid test site!")


    ##RESULT SETTINGS
    def set_result(self):
        RESULT = self.config_ini['RESULT']
        self.RESULT = RESULT

    def get_result_type(self, result_type):
        if result_type == 'graph':
            RESULT_TYPE = eval(self.RESULT.get('TYPE'))[0]
            self.RESULT_TYPE = RESULT_TYPE
            return RESULT_TYPE
        else:
            raise ValueError("Invalid result type!")

    def get_result_xlabel(self, result_xlabel):
        if result_xlabel == 'angle':
            RESULT_XLABEL = eval(self.RESULT.get('XLABEL'))[0]
            self.RESULT_XLABEL = RESULT_XLABEL
            return RESULT_XLABEL
        else:
            raise ValueError("Invalid result xlabel!")

    def get_result_ylabel(self, result_ylabel):
        if result_ylabel == 'intensity':
            RESULT_YLABEL = eval(self.RESULT.get('YLABEL'))[0]
            self.RESULT_YLABEL = RESULT_YLABEL
            return RESULT_YLABEL
        else:
            raise ValueError("Invalid result ylabel!")
