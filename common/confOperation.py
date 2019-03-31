
from configparser import ConfigParser
import os, sys
cp = ConfigParser()

##os.path.split(os.path.realpath(__file__)[0]  才能获取当前脚本所在路径
con = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])+"\\conf.ini"
cp.read(con, encoding='utf-8')


def getConfData(sec, option):
    return cp.get(section=sec, option=option)

def setOptionsValue(sec, option, value):
    cp.set(section=sec,option=option, value=value)
