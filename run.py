
import unittest
import os, sys, time
from BeautifulReport import BeautifulReport
from common.smtpOperation import  Email


case_path = sys.path[0]+"\\testcase"
current_path = os.getcwd()
report_path = os.path.join(current_path, "testreport")
now = time.strftime("%Y-%m-%d_%H%M%S", time.localtime(time.time()))
# 报告地址&名称
report_title = now +"_智能家居接口自动化测试报告.html"     # 如果不能打开这个文件，可能是now的格式，不支持：和空格
# 报告描述
desc = '智能家居接口自动化测试'


if __name__ == '__main__':
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    suite.addTest(discover)
#    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=test_GetRoomList.GetRoomListApi))
#    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=test_CreateRoom.CreateRoomApi))
    run = BeautifulReport(suite)
    run.report(description=desc, filename=report_title, log_path=report_path)
    em = Email()
    em.send(report_path+os.sep+report_title)
