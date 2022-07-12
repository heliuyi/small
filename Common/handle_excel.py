# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_excel.py
# @Time      :2022-05-02 22:29
# @Author    :DongWenFei

'''
1.读取表头
2.读取数据-读取表头以外的所有数据
'''
import json
from Common.handle_path import datas_dir
from openpyxl import load_workbook

class HandleExcel:
    def __init__(self,file_path,sheet_name):
        self.wb=load_workbook(file_path)
        self.sh=self.wb[sheet_name]

    def read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:  # 遍历第1行每一列
            titles.append(item.value)
        return titles

    def read_all_datas(self):
        all_datas = []
        titles = self.read_titles()
        for item in list(self.sh.rows)[1:]:  # 遍历数据行
            values = []
            for val in item:
                values.append(val.value)
            res = dict(zip(titles, values))  # title和每一行数据，打包成字典
            # res["check"]=eval(res["check"])#将check的字符串，转换为字典对象# 字段不一定叫check

            all_datas.append(res)
        return all_datas

    def close_file(self):
        self.wb.close()





if __name__ == '__main__':
    pass

    exc=HandleExcel(datas_dir+"\\Activitys.xlsx","秒杀活动")
    excs=HandleExcel(datas_dir + "\\Goods.xlsx", "商品分类")
    #file_path = r'C:\Users\Administrator\Desktop\InterfaceAuto\TestDatas\Activitys.xlsx'
    #exc=HandleExcel(file_path,"Test")

    cases=excs.read_all_datas()
    # #print(cases)
    print(cases[0]['expected'])
    print(type(cases[0]['expected']))
    # expected_data = json.loads(cases["expected"])  # 字符串转换成字典
    # print(expected_data)

    # print("=============================================================")
    # case = excs.read_all_datas()
    # #print(case)
    # print(case[0]['expected'])

    #print(type(cases[5]['request_data']))

    # exc.close_file()
    # for case in cases:
    #     print(case)

