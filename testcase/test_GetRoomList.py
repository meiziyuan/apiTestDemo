from testcase.CommonApi import api
import unittest


class GetRoomListApi(api):
    '''测试GetRoomList接口'''

    def test_getroomlist_1(self):
        '''正常获取房间列表'''

        caseid ='007'
        res = super(GetRoomListApi, self).sendRequest(caseid)
        self.assertEqual(0, res['errorCode'])
        self.assertEqual(3, res['allRows'])

    def test_getroomlist_2(self):
        '''token过期获取'''
        pass

    def test_getroomlist_3(self):
        '''uid为空获取'''
        pass

if __name__ == "__main__":
    unittest.main()