
from configparser import ConfigParser
import os, sys
cp = ConfigParser()
con = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])+"\\conf.ini"
cp.read(con)
def getConfData(sec, option):

    return cp.get(section=sec, option=option)


#print(getConfData('httpParams', 'dataCommon'))
print(con)