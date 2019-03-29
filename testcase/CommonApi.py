import requests
from common.excelOperation import excelAPI
from common.ConfOperation import getConfData
import unittest
class api(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.xslData = excelAPI(cls.__name__)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.xslData.closeXsl()
        pass

    def setElements(self, apisheetname, caseid):
        info = self.xslData.getCaseData(caseid)
        params = dict(eval(getConfData("httpParams", "dataCommon")))
        params.update(info['params'])
        self.apisheetName = apisheetname
        self.apiname = info["apiName"]
        self.caseid =caseid
        self.casename = info["caseName"]
        self.url = info["url"]
        self.method = info["method"]
        self.param = params

    def sendRequest(self, caseid):
        self.setElements(self.__class__.__name__, caseid)
        if self.method in ('get', 'GET'):
            self.result = requests.get(self.url, params=self.param).json()
        elif self.method in ('post', 'POST'):
            self.result = requests.post(url=self.url, data=self.param).json()
        else:
            self.result = ""
            print("方法名错误")
        print("响应结果：", self.result)
        return self.result
