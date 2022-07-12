#!/usr/bin/python
# --*-- coding: utf-8 --*--
# @Author  : dwf
# @Time    : 2022/7/5 14:55
# @File    : test_08barGain.py

import unittest, json
from Common.handle_request import send_requests
from Common.handle_excel import HandleExcel
from Common.handle_log import logger
from Common.handle_path import datas_dir

from Common.handle_data import replace_mark_with_data,replace_mark_with_data_int
from unittestreport import ddt, list_data
from TestCases.fixture import BaseTest
from faker import Faker
fk=Faker(locale="zh-cn")

exc = HandleExcel(datas_dir + "\\Activitys.xlsx", "砍价助力")
caseDatas = exc.read_all_datas()
exc.close_file()

@ddt
class TestbarGain(unittest.TestCase,BaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("***************测试用例（砍价活动）开始执行***************")
        cls.Activity("bargain")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("***************测试用例（砍价活动）执行结束***************")

    @list_data(caseDatas)
    def test_barGain(self,case):
        expected_data = json.loads(case["expected"])  # 字符串转换成字典
        print("{0}===期望结果：{1}".format(case["title"],expected_data))

        if case["url"].find("#promoteId#") != -1:
            case = replace_mark_with_data_int(case, '#promoteId#',str(self.promoteId))

        if case["request_data"] is None:
            res = send_requests(case["method"], case["url"])
        else:
            if case["request_data"].find("#promoteId#") != -1:
                case = replace_mark_with_data(case, '#promoteId#', str(self.promoteId))
                res = send_requests(case["method"], case["url"], case["request_data"])

        print("{0}===接口执行后的响应结果：{1}".format(case["title"],res.json()))

        try:
            self.assertEqual(res.json()["code"], expected_data["code"])
            self.assertEqual(res.json()["msg"], expected_data["msg"])
            #self.assertEqual(res.json()["success"],bool(expected_data["success"]))
        except AssertionError as e:
            logger.error("用例--【{}】--执行失败".format(case["title"]))
            logger.exception(e)
            raise e
        else:
            logger.info("用例--【{}】--执行成功".format(case["title"]))