import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)

import mns_common.utils.date_handle_util as date_handle_util
from loguru import logger

import mns_common.component.trade_date.trade_date_common_service_api as trade_date_common_service_api
import mns_common.component.company.company_common_service_api as company_common_service_api
import mns_common.component.common_service_fun_api as common_service_fun_api
import mns_common.component.data.data_init_api as data_init_api
import pandas as pd
from datetime import time
from mns_common.db.MongodbUtil import MongodbUtil
import mns_common.utils.data_frame_util as data_frame_util

mongodb_util = MongodbUtil('27017')
mongodb_util_21019 = MongodbUtil('27019')

realtime_quotes_now_zt_new_kc_open_field = ['_id',
                                            'symbol',
                                            'name',
                                            'chg',
                                            'quantity_ratio',
                                            'amount_level',
                                            'real_exchange',
                                            'sum_main_inflow_disk',
                                            'disk_diff_amount',
                                            'flow_mv_level',
                                            'total_mv_level',
                                            'today_chg',
                                            'industry',
                                            'first_sw_industry',
                                            'second_sw_industry',
                                            'third_sw_industry',
                                            'ths_concept_name',
                                            'ths_concept_code',
                                            'em_industry',
                                            'disk_ratio',
                                            'company_type',
                                            'reference_main_inflow',
                                            'main_inflow_multiple', 'super_main_inflow_multiple',
                                            'disk_diff_amount_exchange', 'exchange', 'amount', 'today_main_net_inflow',
                                            'today_main_net_inflow_ratio', 'super_large_order_net_inflow',
                                            'super_large_order_net_inflow_ratio', 'large_order_net_inflow',
                                            'large_order_net_inflow_ratio', 'now_price',
                                            'high', 'low', 'open', 'yesterday_price',
                                            'volume', 'total_mv', 'flow_mv',
                                            'outer_disk', 'inner_disk',
                                            'classification', 'str_now_date', 'number', 'str_day',
                                            'yesterday_high_chg',
                                            'ths_concept_sync_day', 'mv_circulation_ratio',
                                            'large_inflow_multiple', 'real_main_inflow_multiple',
                                            'max_real_main_inflow_multiple', 'list_date',
                                            'real_super_main_inflow_multiple', 'real_flow_mv',
                                            'real_disk_diff_amount_exchange', 'no_open_data']


# fix 错杀数据 有成交量的数据
def fix_industry_data(real_time_quotes_now):
    #  fix industry
    real_time_quotes_now_r = company_common_service_api.amendment_industry(real_time_quotes_now.copy())

    symbol_list = list(real_time_quotes_now_r['symbol'])

    na_real_now = real_time_quotes_now.loc[
        ~(real_time_quotes_now['symbol'].isin(symbol_list))]

    na_real_now = na_real_now.loc[na_real_now['amount'] != 0]

    real_time_quotes_now_result = pd.concat([real_time_quotes_now_r, na_real_now], axis=0)
    return real_time_quotes_now_result


def get_db(str_day):
    trade_date_list = mongodb_util.find_query_data('trade_date_list', query={"_id": str_day, 'tag': False})
    tag = trade_date_list.shape[0] > 0
    if tag:
        return mongodb_util
    else:
        return mongodb_util_21019


def create_db_index(db):
    db.create_index('realtime_quotes_now_zt_new_kc', [("str_day", 1)])
    db.create_index('realtime_quotes_now_zt_new_kc', [("symbol", 1)])
    db.create_index('realtime_quotes_now_zt_new_kc', [("number", 1)])
    db.create_index('realtime_quotes_now_zt_new_kc', [("symbol", 1), ("number", 1)])
    db.create_index('realtime_quotes_now_zt_new_kc', [("str_now_date", 1)])


def sync_all_kc_zt_data(str_day, symbols):
    create_db_index(mongodb_util)
    if symbols is None:
        query_daily = {'date': date_handle_util.no_slash_date(str_day),
                       "chg": {"$gte": 9.0}}
    else:
        query_daily = {'date': date_handle_util.no_slash_date(str_day),
                       'symbol': {"$in": symbols},
                       "chg": {"$gte": 9.0}}

    kc_stock_qfq_daily = mongodb_util.find_query_data('stock_qfq_daily', query_daily)
    if data_frame_util.is_empty(kc_stock_qfq_daily):
        logger.error("无k线数据:{}", symbols)
        return

    company_info = company_common_service_api.get_company_info_industry_list_date()
    company_info['symbol'] = company_info['_id']
    company_info = company_info.loc[company_info['_id'].isin(list(kc_stock_qfq_daily['symbol']))]

    for stock_one in company_info.itertuples():
        try:

            kc_stock_qfq_daily.loc[
                kc_stock_qfq_daily['symbol'] == stock_one.symbol, 'industry'] = stock_one.industry
            kc_stock_qfq_daily.loc[
                kc_stock_qfq_daily['symbol'] == stock_one.symbol, 'first_sw_industry'] = stock_one.first_sw_industry
            kc_stock_qfq_daily.loc[
                kc_stock_qfq_daily[
                    'symbol'] == stock_one.symbol, 'second_sw_industry'] = stock_one.second_sw_industry
            kc_stock_qfq_daily.loc[
                kc_stock_qfq_daily['symbol'] == stock_one.symbol, 'third_sw_industry'] = stock_one.third_sw_industry

            kc_stock_qfq_daily.loc[
                kc_stock_qfq_daily['symbol'] == stock_one.symbol, 'list_date'] = stock_one.list_date

            str_day_date = date_handle_util.str_to_date(str_day, '%Y-%m-%d')

            list_date = date_handle_util.str_to_date(str(stock_one.list_date).replace(".0", ""), '%Y%m%d')

            # 计算日期差值 距离现在上市时间
            kc_stock_qfq_daily.loc[
                kc_stock_qfq_daily['symbol'] == stock_one.symbol, 'diff_days'] = (str_day_date - list_date).days

            last_trade_day = trade_date_common_service_api.get_last_trade_day(str_day)

            query_high_chg = {'chg': {"$gte": 11}, 'date': date_handle_util.no_slash_date(last_trade_day),
                              "symbol": stock_one.symbol}
            yesterday_high_chg = mongodb_util.exist_data_query('stock_qfq_daily', query_high_chg)
            if yesterday_high_chg:
                kc_stock_qfq_daily.loc[
                    kc_stock_qfq_daily['symbol'] == stock_one.symbol, 'yesterday_high_chg'] = True
            else:
                kc_stock_qfq_daily.loc[
                    kc_stock_qfq_daily['symbol'] == stock_one.symbol, 'yesterday_high_chg'] = False

        except BaseException as e:
            logger.error("出现异常:{},{},{}", e, str_day, stock_one.symbol)

    mongodb_util.save_mongo(kc_stock_qfq_daily, 'kc_stock_qfq_daily')
    kc_stock_qfq_daily = kc_stock_qfq_daily.loc[(kc_stock_qfq_daily['classification'].isin(['K', 'C', 'X']))
                                                | (kc_stock_qfq_daily['name'].str.startswith('C'))]
    kc_stock_qfq_daily = common_service_fun_api.exclude_new_stock(kc_stock_qfq_daily)

    kc_stock_qfq_daily = kc_stock_qfq_daily.sort_values(by=['chg'], ascending=False)

    for kc_one in kc_stock_qfq_daily.itertuples():
        try:
            db_name = 'realtime_quotes_now_' + str_day
            logger.info("同步高涨幅开盘日期和代码:{},{}", str_day, kc_one.symbol)

            query_real_time = {'symbol': kc_one.symbol}
            db = get_db(str_day)
            realtime_quotes_now_kc = db.find_query_data(db_name, query_real_time)
            realtime_quotes_now_kc = common_service_fun_api.exclude_new_stock(realtime_quotes_now_kc)
            if realtime_quotes_now_kc.shape[0] == 0:
                logger.error("当期日期代码无开盘数据:{},{}", str_day, kc_one.symbol)
                continue
            # 同步当天高涨幅集合竞价数据
            one_symbol_day_open_data(realtime_quotes_now_kc, kc_one, str_day)
            # # 同步高涨幅整天交易数据
            one_symbol_day_data(str_day, kc_one, realtime_quotes_now_kc)
        except BaseException as e:
            logger.error("出现异常:{},{},{}", e, str_day, kc_one.symbol)


def one_symbol_day_open_data(realtime_quotes_now_kc, kc_one, str_day):
    realtime_quotes_now_kc = realtime_quotes_now_kc.sort_values(by=['_id'], ascending=True)
    realtime_quotes_now_kc = realtime_quotes_now_kc.loc[realtime_quotes_now_kc['str_now_date'] >= str_day + " 09:26:00"]
    realtime_quotes_now_zt_new_kc_open = realtime_quotes_now_kc.iloc[0:1]
    _id = list(realtime_quotes_now_zt_new_kc_open['_id'])[0]
    str_now_date = _id[7:26]
    now_date = date_handle_util.str_to_date(str_now_date, "%Y-%m-%d %H:%M:%S")
    now_date_time = now_date.time()
    target_time_09_31 = time(9, 31)
    realtime_quotes_now_zt_new_kc_open_copy = realtime_quotes_now_zt_new_kc_open.copy()

    if now_date_time > target_time_09_31:
        logger.error("当期日期代码无开盘数据:{},{}", str_day, kc_one.symbol)
        realtime_quotes_now_zt_new_kc_open_copy.loc[:, 'no_open_data'] = True
    else:
        realtime_quotes_now_zt_new_kc_open_copy.loc[:, 'no_open_data'] = False
        #

    realtime_quotes_now_zt_new_kc_open_copy.loc[:, 'yesterday_high_chg'] = kc_one.yesterday_high_chg
    realtime_quotes_now_zt_new_kc_open_copy.loc[:, 'today_chg'] = kc_one.chg
    realtime_quotes_now_zt_new_kc_open_copy.loc[:, 'str_day'] = str_day

    realtime_quotes_now_zt_new_kc_open_copy = handle_init_real_time_quotes_data(
        realtime_quotes_now_zt_new_kc_open_copy.copy(),
        str_now_date,
        1)
    realtime_quotes_now_zt_new_kc_open_copy = realtime_quotes_now_zt_new_kc_open_copy[
        realtime_quotes_now_zt_new_kc_open_field]

    # 将日期数值转换为日期时间格式
    realtime_quotes_now_zt_new_kc_open_copy['list_date_01'] = pd.to_datetime(
        realtime_quotes_now_zt_new_kc_open_copy['list_date'],
        format='%Y%m%d')
    # 将日期字符串转换为日期时间格式
    realtime_quotes_now_zt_new_kc_open_copy['str_day_01'] = pd.to_datetime(
        realtime_quotes_now_zt_new_kc_open_copy['str_day'],
        format='%Y-%m-%d')

    # 计算日期差值 距离现在上市时间
    realtime_quotes_now_zt_new_kc_open_copy['diff_days'] = realtime_quotes_now_zt_new_kc_open_copy.apply(
        lambda row: (row['str_day_01'] - row['list_date_01']).days, axis=1)

    del realtime_quotes_now_zt_new_kc_open_copy['str_day_01']
    del realtime_quotes_now_zt_new_kc_open_copy['list_date_01']

    mongodb_util.save_mongo(realtime_quotes_now_zt_new_kc_open_copy, 'realtime_quotes_now_zt_new_kc_open')


# 同步当前day整天数据
def one_symbol_day_data(str_day, kc_one, realtime_quotes_now_kc):
    realtime_quotes_now_kc.loc[
        realtime_quotes_now_kc['symbol'] == kc_one.symbol, 'industry'] = kc_one.industry

    realtime_quotes_now_kc['str_day'] = str_day

    query_remove = {"str_day": str_day, "symbol": kc_one.symbol}

    success02 = mongodb_util.remove_data(query_remove, 'realtime_quotes_now_zt_new_kc').acknowledged
    if success02:
        mongodb_util.insert_mongo(realtime_quotes_now_kc, 'realtime_quotes_now_zt_new_kc')


def handle_init_real_time_quotes_data(real_time_quotes_now, str_now_date, number):
    #  exclude b symbol
    real_time_quotes_now = common_service_fun_api.exclude_b_symbol(real_time_quotes_now.copy())
    #  classification symbol
    real_time_quotes_now = common_service_fun_api.classify_symbol(real_time_quotes_now.copy())
    #  fix industry
    real_time_quotes_now = fix_industry_data(real_time_quotes_now.copy())
    #  calculate parameter
    real_time_quotes_now = data_init_api.calculate_parameter_factor(real_time_quotes_now.copy())

    real_time_quotes_now = real_time_quotes_now.loc[real_time_quotes_now['amount'] != 0]
    real_time_quotes_now['str_now_date'] = str_now_date
    real_time_quotes_now['number'] = number
    return real_time_quotes_now


# 同步当天所有开盘数据
def sync_one_day_open_data(str_day):
    realtime_quotes_db_name = 'realtime_quotes_now_' + str_day

    number = realtime_quotes_now_min_number_sync(realtime_quotes_db_name, 'number', str_day, "000001")

    query = {"number": number}
    db = get_db(str_day)
    realtime_quotes_now_list = db.find_query_data(realtime_quotes_db_name, query)

    realtime_quotes_now_one = realtime_quotes_now_list.iloc[0]
    str_now_date = realtime_quotes_now_one['_id']
    str_now_date = str_now_date[7:26]

    now_date = date_handle_util.str_to_date(str_now_date, "%Y-%m-%d %H:%M:%S")
    now_date_time = now_date.time()

    target_time_09_31 = time(9, 31)
    if now_date_time >= target_time_09_31:
        return

    realtime_quotes_now_list['str_day'] = str_day

    realtime_quotes_now_list = handle_init_real_time_quotes_data(
        realtime_quotes_now_list.copy(),
        str_now_date, number)

    mongodb_util.insert_mongo(realtime_quotes_now_list, 'realtime_quotes_now_open')

    logger.info("同步str_day:{}开盘数据", str_day)


def realtime_quotes_now_min_number_sync(db_name, field, str_day, symbol):
    db = get_db(str_day)
    query = {'symbol': symbol}
    df = db.ascend_query(query, db_name, field, 1)
    if df is None or df.shape[0] == 0:
        return 1
    else:
        return list(df[field])[0]


def realtime_quotes_now_zt_new_kc_open_sync():
    realtime_quotes_now_zt_new_kc_open = mongodb_util.find_all_data('realtime_quotes_now_zt_new_kc_open')
    realtime_quotes_now_zt_new_kc_open = realtime_quotes_now_zt_new_kc_open[realtime_quotes_now_zt_new_kc_open_field]
    realtime_quotes_now_zt_new_kc_open = realtime_quotes_now_zt_new_kc_open.sort_values(by=['str_day'], ascending=False)

    mongodb_util.insert_mongo(realtime_quotes_now_zt_new_kc_open, 'realtime_quotes_now_zt_new_kc_open_copy')


#     query = {'$and': [{"_id": {'$lte': str_end}}, {"_id": {'$gte': '2022-04-25'}}]}
def sync_all_high_chg_data(str_end):
    query = {'$and': [{"_id": {'$lte': str_end}}, {"_id": {'$gte': '2024-03-01'}}]}
    trade_date_list = mongodb_util.find_query_data('trade_date_list', query)
    trade_date_list = trade_date_list.sort_values(by=['trade_date'], ascending=False)
    for date_one in trade_date_list.itertuples():
        try:
            str_day = date_one.trade_date
            sync_all_kc_zt_data(str_day, None)
        except BaseException as e:
            logger.error("发生异常:{},{}", str_day, e)


def fix_miss_data(str_end):
    query = {'$and': [{"_id": {'$lte': str_end}}, {"_id": {'$gte': '2023-12-05'}}]}
    trade_date_list = mongodb_util.find_query_data('trade_date_list', query)
    trade_date_list = trade_date_list.sort_values(by=['trade_date'], ascending=False)
    for date_one in trade_date_list.itertuples():
        try:
            str_day = date_one.trade_date
            query = {"str_day": str_day, "miss_out": True}
            stock_high_chg_pool_df = mongodb_util.find_query_data('stock_high_chg_pool', query)
            if data_frame_util.is_empty(stock_high_chg_pool_df):
                continue
            miss_symbol_list = list(stock_high_chg_pool_df['symbol'])
            sync_all_kc_zt_data(str_day, miss_symbol_list)
        except BaseException as e:
            logger.error("发生异常:{},{}", str_day, e)


if __name__ == '__main__':
    sync_all_high_chg_data('2024-03-08')
    # sync_all_kc_zt_data('2023-08-16')
    # sync_all_kc_zt_data('2023-07-07')
    # realtime_quotes_now_zt_new_kc_open_sync()
    # hui_ce_all('2023-06-16')
    # fix_diff_day()
    # sync_all_kc_zt_data('2023-06-30')

    # sync_all_kc_zt_data('2023-07-05')
    # sync_one_day_open_data('2023-07-05')
    # sync_all_kc_zt_data('2023-06-30')
    # sync_one_day_open_data('2023-05-31')
    # hui_ce_all('2023-03-16')
    # sync_all_kc_zt_data('2023-06-28')
    # sync_all_kc_zt_data('2023-05-12')
    # sync_all_kc_zt_data('2023-05-15')
    # sync_all_kc_zt_data('2023-05-16')
    # sync_all_kc_zt_data('2023-05-17')
    # sync_all_kc_zt_data('2023-05-10')
