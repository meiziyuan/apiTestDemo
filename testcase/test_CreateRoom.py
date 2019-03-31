from testcase.CommonApi import api
import unittest
from common.excelOperation import excelAPI

class CreateRoomApi(api):
    '''测试CreateRoom接口'''

    def test_CreateRoom_1(self):
        '''正常添加房间'''

        caseid = '001'
        res = super(CreateRoomApi, self).sendRequest(caseid)
        self.assertEqual(0, res['errorCode'])
        self.assertEqual(0, res['allRows'])
        self.assertTrue(res['data']['rid'] > 0)

    def test_CreateRoom_2(self):
        '''添加的房间名称为空'''

        caseid = '002'
        res = super(CreateRoomApi, self).sendRequest(caseid)
        self.assertEqual(20020, res['errorCode'])
        self.assertEqual(0, res['allRows'])
        self.assertEqual('房间名称不能为空!', res['data'])
        pass

    def test_getroomlist_3(self):
        '''添加重复的房间'''

        caseid = '003'
        res = super(CreateRoomApi, self).sendRequest(caseid)
        self.assertEqual(20023, res['errorCode'])
        self.assertEqual(0, res['allRows'])
        self.assertEqual('房间名称不能重名，请重新输入', res['data'])

    def test_getroomlist_4(self):
        '''输入含特殊字符房间名'''

        caseid = '004'
        res = super(CreateRoomApi, self).sendRequest(caseid)
        self.assertEqual(20023, res['errorCode'])
        self.assertEqual(0, res['allRows'])
        self.assertEqual('房间名称不能重名，请重新输入', res['data'])

    def test_getroomlist_5(self):
        '''输入字符超出长度'''

        caseid = '005'
        res = super(CreateRoomApi, self).sendRequest(caseid)
        self.assertEqual(20023, res['errorCode'])
        self.assertEqual(0, res['allRows'])
        self.assertEqual('房间名称不能重名，请重新输入', res['data'])

    def test_getroomlist_6(self):
        '''创建房间数超过20个'''

        caseid = '006'
        res = super(CreateRoomApi, self).sendRequest(caseid)
        self.assertEqual(20023, res['errorCode'])
        self.assertEqual(0, res['allRows'])
        self.assertEqual('房间名称不能重名，请重新输入', res['data'])

if __name__ == "__main__":
    unittest.main()