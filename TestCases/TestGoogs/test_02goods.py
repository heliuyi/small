# #!/usr/bin/python
# # --*-- coding: utf-8 --*--
# # @Author  : dwf
# # @Time    : 2022/7/7 15:03
# # @File    : test_02goods.py
#
#
# import unittest, json,random
# from Common.handle_request import send_requests
# from Common.handle_excel import HandleExcel
# from Common.handle_log import logger
# from Common.handle_path import datas_dir
#
# from Common.handle_data import replace_mark_with_data,replace_mark_with_data_int
# from unittestreport import ddt, list_data
# from TestCases.fixture import BaseTest
# from faker import Faker
# fk=Faker(locale="zh-cn")
#
# exc = HandleExcel(datas_dir + "\\Goods.xlsx", "商品管理")
# caseDatas = exc.read_all_datas()
# exc.close_file()
#
# @ddt
# class Testgoods(unittest.TestCase,BaseTest):
#     @classmethod
#     def setUpClass(cls) -> None:
#         logger.info("***************测试用例（商品管理）开始执行***************")
#
#     @classmethod
#     def setUp(self) -> None:
#         self.Goods()
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         logger.info("***************测试用例（商品管理）执行结束***************")
#
#     @list_data(caseDatas)
#     def test_goods(self,case):
#         expected_data = json.loads(case["expected"])  # 字符串转换成字典
#         print("{0}===期望结果：{1}".format(case["title"],case["expected"]))
#
#         if case["request_data"].find("#name#") != -1:
#             case = replace_mark_with_data(case, '#name#', str(random.randint(10000, 99999)))
#
#         if case["request_data"].find("#categoryCode#") != -1:
#             case = replace_mark_with_data(case, '#categoryCode#', str(self.categoryCode))
#
#         if case["request_data"].find("#parentId#") != -1:
#             case = replace_mark_with_data(case, '#parentId#', str(self.parentId))
#
#         res = send_requests(case["method"], case["url"], case["request_data"])
#         print("{0}===接口执行后的响应结果：{1}".format(case["title"],res.json()))
#
#         try:
#             self.assertEqual(res.json()["code"], expected_data["code"])
#             self.assertEqual(res.json()["msg"], expected_data["msg"])
#             #self.assertEqual(res.json()["success"],bool(expected_data["success"]))
#         except AssertionError as e:
#             logger.error("用例--【{}】--执行失败".format(case["title"]))
#             logger.exception(e)
#             raise e
#         else:
#             logger.info("用例--【{}】--执行成功".format(case["title"]))