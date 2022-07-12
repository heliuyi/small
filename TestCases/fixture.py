# *_* coding : UTF-8 *_*

# 开发时间  ：  2022/05/19  15:19
# 文件名称  :  fixture.PY
# 开发工具  :  PyCharm

import requests
from jsonpath import jsonpath
from Common.handle_phone import get_old_phone, get_admin_phone
from Common.handle_request import send_requests
from Common.handle_db import HandleDB
import hashlib, time, requests, random, json
import random

class BaseTest:

    @classmethod
    def get_now_datetime(cls):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    # ====================================================================================================
    '''营销活动'''
    @classmethod
    def Activity(cls, ActivityType):
        Activity_Id = random.randint(100, 1000)

        #限时秒杀
        if ActivityType == "secKill":
            killtime_params = {
                "name": "自动化全天场次{}".format(random.randint(100, 1000)),
                "startTime": "01:{0}9:{1}9".format(random.randint(1, 5), random.randint(1, 5)),
                "endTime": "23:{0}9:{1}9".format(random.randint(1, 5), random.randint(1, 5))
            }
            '''添加活动场次'''
            send_requests("POST", "/promote/promoteseckilltime", killtime_params)
            sql = 'SELECT id FROM promote_sec_kill_time WHERE tenant_code="10000001" ORDER BY create_time DESC'
            promoteTimeId = HandleDB("test_fanxing_promote").select_one_data(sql)
            promoteTimeId = json.dumps(promoteTimeId)
            print("===========秒杀的场次Id:{}=================".format(promoteTimeId))

            '''新增秒杀活动单表头'''
            params = {
                "promoteName": "自动化秒杀{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "promoteTimeIdList": [
                    promoteTimeId[-4:-1]
                ],
                "commonStockType": 0,
                "superpositionCoupon": 1
            }
        #限时促销
        elif ActivityType == "specialPrice":
            params = {
                "promoteName": "自动化限时促销{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "childType": 1,
                "startTime": "08:49:06",
                "endTime": "18:49:06",
                "commonStockType": 0
            }
        #部分满减
        elif ActivityType == "partFullReduce":
            params = {
                "promoteName": "自动化部分满减{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "activityRuleList": [
                    {
                        "buyValue": 2,
                        "giftValue": 1
                    },
                    {
                        "buyValue": 3,
                        "giftValue": 2
                    },
                    {
                        "buyValue": 4,
                        "giftValue": 3
                    },
                    {
                        "buyValue": 5,
                        "giftValue": 4
                    },
                    {
                        "buyValue": 16,
                        "giftValue": 15
                    }
                ],
                "startTime": "00:00:00",
                "endTime": "23:59:59"
            }
        #配送费满减
        elif ActivityType == "deliveryFullReduce":
            # ************配送费满减活动，同一活动日期中不能有重复的活动******************
            # 查询进行中的配送费满减活动，进行活动关闭
            sql = "SELECT id FROM `promote_activity` WHERE promote_type=3 and `status`=1"
            result = HandleDB("test_fanxing_promote").select_all_data(sql)
            params_id = []
            for i in result:
                params_id.append(str(i['id']))

            result = send_requests("POST", "promote/deliveryFullReduce/close", params_id)
            print(result.json())

            '''配送费满减'''
            params = {
                "promoteName": "自动化配送费满减{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "activityRuleList": [
                    {
                        "buyValue": 2,
                        "giftValue": 1
                    },
                    {
                        "buyValue": 3,
                        "giftValue": 2
                    },
                    {
                        "buyValue": 4,
                        "giftValue": 3
                    },
                    {
                        "buyValue": 5,
                        "giftValue": 4
                    },
                    {
                        "buyValue": 16,
                        "giftValue": 15
                    }
                ],
                "startTime": "00:00:00",
                "endTime": "23:59:59"
            }
        #买赠活动
        elif ActivityType == "buyGift":
            params = {
                "promoteName": "自动化买赠活动{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "activityRuleList": [
                    {
                        "buyValue": 2,
                        "giftValue": 1
                    },
                    {
                        "buyValue": 3,
                        "giftValue": 2
                    },
                    {
                        "buyValue": 4,
                        "giftValue": 3
                    },
                    {
                        "buyValue": 5,
                        "giftValue": 4
                    },
                    {
                        "buyValue": 6,
                        "giftValue": 5
                    }
                ],
                "commonStockType": 0,
                "superpositionCoupon": 1,
                "startTime": "00:00:00",
                "endTime": "23:59:59"
            }
        #预售活动
        elif ActivityType == "preSale":
            params = {
                "promoteName": "自动化预售活动{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "pickUpStartTime": "{}".format(BaseTest.get_now_datetime()),
                "pickUpEndTime": "2022-08-09 23:59:59",
                "commonStockType": 0,
                "superpositionCoupon": 1,
                "startTime": "17:40:33",
                "endTime": "17:40:35"
            }
        #拼团活动
        elif ActivityType == "groupBooking":
            params = {
                "promoteName": "自动化预售活动{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "commonStockType": 0,
                "superpositionCoupon": 1,
                "promoteType": 8,
                "startTime": "00:00:00",
                "endTime": "23:59:59",
                "groupExpireTime": 259200
            }
        #砍价助力
        elif ActivityType == "bargain":
            params = {
                "promoteName": "自动化砍价助力{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "startTime": "02:00:30",
                "endTime": "20:00:30",
                "firstBargain": 0,
                "childType": 1,
                "bargainUserLimit": 2,
                "expireTime": 1,
                "canBuyWay": 1,
                "showProgress": 1,
                "commonStockType": 0,
                "superpositionCoupon": 1,
                "promoteDescribe": "<p>自动化测试砍价活动</p>",
                "promoteType": 9,
                "activityExtra": {
                    "firstBargain": 0,
                    "bargainUserLimit": 2,
                    "expireTime": 1,
                    "canBuyWay": 1,
                    "showProgress": 1,
                    "promoteDescribe": "<p>自动化测试砍价活动</p>"
                }
            }
        #社区团购  groupCommunity
        else:
            params = {
                "promoteName": "自动化社区团购{}".format(Activity_Id),
                "startDate": "{}".format(BaseTest.get_now_datetime()),
                "endDate": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "pickUpStartTime": "{}".format(BaseTest.get_now_datetime()),
                "pickUpEndTime": "2022-08-2{} 00:00:00".format(random.randint(1, 9)),
                "commonStockType": 0,
                "superpositionCoupon": 1,
                "startTime": "08:42:59",
                "endTime": "23:43:01"
            }

        response = send_requests("POST", "/promote/{0}/save".format(ActivityType), params)  # 创建活动单头
        cls.promoteId = response.json()['data']  # 获取活动Id   data: "8798"

        #配送费满减活动，不需要创建商品信息
        if ActivityType != "deliveryFullReduce":
            '''总店创建活动需要创建选择门店'''
            shopsave_params = {
                "promoteId": "{0}".format(cls.promoteId),
                "shopIds": ["2", "57", "58"]
            }
            send_requests("POST", "/promote/{0}/shop/save".format(ActivityType), shopsave_params)  # 添加活动门店
    # ====================================================================================================
    '''商品管理'''
    @classmethod
    def categoryCode_randint(cls):
        return random.randint(88800, 999999)

    @classmethod
    def Goods(cls):
        categoryCode=BaseTest.categoryCode_randint()
        url = '/goods/category/duplicateCheck?categoryCode={0}&shopId=0'.format(categoryCode)
        result = send_requests("GET", url)
        # 判断分类是否重复，data等于0没有重复的，1有重复
        if result.json()['data'] == 0:
            cls.categoryCode=categoryCode
        else:
            cls.categoryCode=BaseTest.categoryCode_randint()

        sql = 'SELECT id FROM s_category WHERE tenant_code="10000001" and shop_id="2" ORDER BY create_time DESC;'
        parentId = HandleDB("test_fanxing_goods").select_one_data(sql)
        print("===========分类的父级Id:{}=================".format(parentId))
        cls.parentId = parentId['id']#json.dumps(parentId)

    '''
    SELECT * FROM `s_category` WHERE tenant_code='10000001' ORDER BY create_time DESC;  
    

    
    
    '''