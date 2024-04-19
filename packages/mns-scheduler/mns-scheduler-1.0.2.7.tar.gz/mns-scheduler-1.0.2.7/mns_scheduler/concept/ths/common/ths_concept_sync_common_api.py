import sys
import os

import pandas as pd
import time
import mns_common.api.ths.ths_stock_api as ths_stock_api
import datetime
from mns_common.db.MongodbUtil import MongodbUtil
import mns_common.component.company.company_common_service_api as company_common_service_api

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)
mongodb_util = MongodbUtil('27017')
import mns_common.api.msg.push_msg_api as push_msg_api
import mns_scheduler.company_info.company_info_sync_api as company_info_sync_api
import mns_common.utils.data_frame_util as data_frame_util
max_concept_code = 886110

order_fields = [
    "index",
    "symbol",
    "name",
    "now_price",
    "chg",
    "change",
    "exchange",
    "amount",
    "concept_code",
]


def push_msg_to_we_chat_web(concept_code, concept_name, url):
    msg = "概念代码:" + str(concept_code) + "," + "概念名称:" + concept_name + "," + "url:   " + url
    title = "新增同花顺概念:" + str(concept_code) + "-" + concept_name
    push_msg_api.push_msg_to_wechat(title, msg)


# 保存新概念信息到数据库
def save_ths_concept_list(concept_code, concept_name, str_day, str_now_time):
    url = 'http://q.10jqka.com.cn/thshy/detail/code/' + str(concept_code)
    ths_concept_list = pd.DataFrame([
        [concept_code, concept_code, concept_name, str_day, url, str_now_time, True, True],
    ], columns=['_id', 'symbol', 'name', 'str_day', 'url', 'str_now_time', 'success', 'valid'])
    mongodb_util.save_mongo(ths_concept_list, 'ths_concept_list')


# 获取最大概念代码
def get_max_concept_code():
    query = {"symbol": {'$ne': 'null'}, "success": True}
    ths_concept_max = mongodb_util.descend_query(query, 'ths_concept_list', 'symbol', 1)
    if ths_concept_max.shape[0] == 0:
        concept_code = 885284
    else:
        concept_code = list(ths_concept_max['symbol'])[0]

    return concept_code


# 保存新概念详细信息到数据库
def save_ths_concept_detail(new_concept_symbol_df,
                            concept_name, str_day,
                            str_now_time, concept_code):
    concept_code = int(concept_code)
    new_concept_symbol_df['symbol'] = new_concept_symbol_df['symbol'].astype(str)
    new_concept_symbol_df['_id'] = str(concept_code) + '_' + new_concept_symbol_df['symbol']
    new_concept_symbol_df['concept_code'] = concept_code
    new_concept_symbol_df['concept_name'] = concept_name

    new_concept_symbol_df['concept_name'] = new_concept_symbol_df['concept_name'].replace(" ", "")

    query_ths_concept = {'symbol': concept_code}
    ths_concept_list = mongodb_util.find_query_data('ths_concept_list', query_ths_concept)
    if ths_concept_list.shape[0] == 0:
        concept_create_day = str_day
    else:
        concept_create_day = list(ths_concept_list['str_day'])[0]

    new_concept_symbol_df['str_day'] = str_day
    new_concept_symbol_df['str_now_time'] = str_now_time
    new_concept_symbol_df['concept_create_day'] = concept_create_day

    new_concept_symbol_list = list(new_concept_symbol_df['symbol'])

    query_company_info = {'symbol': {'$in': new_concept_symbol_list}}
    query_field = {"first_industry": 1, "first_industry": 1, "industry": 1,
                   "company_type": 1, "flow_mv_sp": 1,
                   "total_mv_sp": 1}
    company_info = mongodb_util.find_query_data_choose_field('company_info',
                                                             query_company_info, query_field)

    company_info = company_info.set_index(['_id'], drop=True)
    new_concept_symbol_df = new_concept_symbol_df.set_index(['symbol'], drop=False)

    new_concept_symbol_df = pd.merge(new_concept_symbol_df, company_info, how='outer',
                                     left_index=True, right_index=True)
    new_concept_symbol_df['concept_name'] = new_concept_symbol_df['concept_name'].replace(" ", "")
    query = {'concept_code': concept_code}

    if bool(1 - ('way' in new_concept_symbol_df.columns)):
        new_concept_symbol_df['way'] = 'symbol_sync'

    new_concept_symbol_df = new_concept_symbol_df[[
        "_id",
        "index",
        "symbol",
        "name",
        "now_price",
        "chg",
        "change",
        "exchange",
        "amount",
        "concept_code",
        "concept_name",
        "str_day",
        "str_now_time",
        "industry",
        "flow_mv_sp",
        "total_mv_sp",
        "company_type",
        "concept_create_day",
        "way"
    ]]

    exist_concept_detail = mongodb_util.find_query_data('ths_stock_concept_detail', query)
    if exist_concept_detail is None or exist_concept_detail.shape[0] == 0:
        mongodb_util.save_mongo(new_concept_symbol_df, 'ths_stock_concept_detail')
    else:
        exist_concept_detail_symbol_list = list(exist_concept_detail['symbol'])
        new_concept_symbol_df = new_concept_symbol_df.loc[~(
            new_concept_symbol_df['symbol'].isin(exist_concept_detail_symbol_list))]
        if new_concept_symbol_df.shape[0] > 0:
            mongodb_util.save_mongo(new_concept_symbol_df, 'ths_stock_concept_detail')
            # 保存到当日新增概念列表
            new_concept_symbol_df['concept_type'] = 'ths'
            mongodb_util.save_mongo(new_concept_symbol_df, 'today_new_concept_list')
    update_company_info(new_concept_symbol_df)
    # 公司缓存信息清除
    company_common_service_api.company_info_industry_cache_clear()


# 更新公司表信息 todo 清空cache 公司表中  common_service_fun_api.py  get_company_info_industry
def update_company_info(new_concept_symbol_df):
    if new_concept_symbol_df.shape[0] > 0:
        symbol_list = list(new_concept_symbol_df['symbol'])
        company_info_sync_api.sync_company_base_info(symbol_list)
        company_info_sync_api.fix_company_industry(None)
        # 公司缓存信息清除
        company_common_service_api.company_info_industry_cache_clear()


def update_null_name():
    query = {"_id": {'$gte': 886025}}
    ths_concept_list = mongodb_util.find_query_data('ths_concept_list', query)
    ths_concept_list = ths_concept_list.sort_values(by=['_id'], ascending=False)

    for concept_one in ths_concept_list.itertuples():
        concept_code = concept_one.symbol
        name = concept_one.name
        exist_url = concept_one.url

        if name == '':
            concept_name = ths_stock_api.get_concept_name(concept_code)
            query_concept = {"symbol": concept_code}
            new_values = {'$set': {"name": concept_name}}
            mongodb_util.update_one_query(query_concept, new_values, 'ths_concept_list')

            new_values_detail = {'$set': {"concept_name": concept_name}}

            query_concept_detail = {"concept_code": concept_code}

            mongodb_util.update_many(query_concept_detail, new_values_detail, 'ths_stock_concept_detail')
            time.sleep(10)

        if exist_url == '' or pd.isna(exist_url):
            url = 'http://q.10jqka.com.cn/thshy/detail/code/' + str(concept_code)
            str_now_time = concept_one.str_day + " " + "00:00:00"
            query_concept = {"symbol": concept_code}
            new_values = {'$set': {"url": url, "str_now_time": str_now_time}}
            mongodb_util.update_one_query(query_concept, new_values, 'ths_concept_list')


# 更新概念数量
def update_concept_number():
    query = {}
    ths_concept_list = mongodb_util.find_query_data('ths_concept_list', query)
    ths_concept_list = ths_concept_list.sort_values(by=['_id'], ascending=False)
    for concept_one in ths_concept_list.itertuples():
        try:
            query_detail = {'concept_code': concept_one.symbol}
            concept_number = mongodb_util.count(query_detail, 'ths_stock_concept_detail')
            query_update = {"symbol": concept_one.symbol}
            new_values = {'$set': {"concept_number": concept_number}}
            mongodb_util.update_one_query(query_update, new_values, 'ths_concept_list')
        except BaseException as e:
            print(e)


def get_concept_detail_info_web(concept_code):
    new_concept_symbol_list = ths_stock_api.ths_stock_concept(concept_code)
    if new_concept_symbol_list is None or new_concept_symbol_list.shape[0] == 0:
        return None
    new_concept_symbol_list['_id'] = str(concept_code) + '-' + new_concept_symbol_list['symbol']
    return new_concept_symbol_list


def update_nan_data():
    query = {"concept_code": float('NaN')}
    ths_stock_concept_detail = mongodb_util.find_query_data('ths_stock_concept_detail', query)

    ths_stock_concept_detail['concept_code'] = ths_stock_concept_detail['_id']
    for stock_one in ths_stock_concept_detail.itertuples():
        query = {"symbol": stock_one.symbol}
        company_info = mongodb_util.find_query_data('company_info', query)

        concept_code = stock_one.concept_code
        concept_code = int(concept_code[0:6])

        new_values = {'$set': {"concept_code": concept_code,
                               "flow_mv_sp": list(company_info['flow_mv_sp'])[0],
                               "total_mv_sp": list(company_info['total_mv_sp'])[0],
                               "company_type": list(company_info['company_type'])[0]

                               }}
        query_update = {"_id": stock_one.concept_code}
        mongodb_util.update_many(query_update, new_values, 'ths_stock_concept_detail')


def update_concept_create_day():
    query = {"symbol": {'$exists': True}}
    new_concept_list = mongodb_util.descend_query(query, "ths_concept_list", "_id", 500)

    if new_concept_list.shape[0] > 0:
        for one_concept in new_concept_list.itertuples():
            concept_create_day = one_concept.str_day
            query_update = {"concept_code": one_concept.symbol}

            new_values = {'$set': {"concept_create_day": concept_create_day}}

            mongodb_util.update_many(query_update, new_values, 'ths_stock_concept_detail')
