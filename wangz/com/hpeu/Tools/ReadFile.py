import os
import configparser

class ReadFile():
    def getURL(self,section,option):
        curpath = os.path.dirname(os.path.abspath("."))
        file_path = curpath + "\\..\\..\\resources\\Configuration.properties"
        config = configparser.ConfigParser()
        config.read(file_path)
        URL = config.get(section, option)
        return URL
    
    def getElement(self,section,option):
        curpath = os.path.dirname(os.path.abspath("."))
        file_path = curpath + "\\..\\..\\resources\\PageElement.properties"
        config = configparser.ConfigParser()
        config.read(file_path)
        Element = config.get(section, option)
        return Element
        
    def getInputValue(self,section,option): 
        curpath = os.path.dirname(os.path.abspath("."))
        file_path = curpath + "\\..\\..\\resources\\InputDate.properties"
        config = configparser.ConfigParser()
        config.read(file_path)
        InputElement = config.get(section, option)
        return InputElement
    
    def getExistElement(self,section,option):
        curpath = os.path.dirname(os.path.abspath("."))
        file_path = curpath + "\\..\\..\\resources\\ExistElement.properties"
        config = configparser.ConfigParser()
        config.read(file_path)
        ExistElement = config.get(section, option)
        return ExistElement
    
    
    
