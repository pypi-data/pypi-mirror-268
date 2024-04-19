import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)

import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)

import pandas as pd
from loguru import logger
import mns_common.component.common_service_fun_api as common_service_fun_api
import mns_common.component.trade_date.trade_date_common_service_api as trade_date_common_service_api
import mns_common.api.em.east_money_stock_api as east_money_stock_api
import mns_common.utils.date_handle_util as date_handle_util
import mns_common.component.company.company_common_service_api as company_common_service_api
import mns_common.component.data.data_init_api as data_init_api
from mns_common.db.MongodbUtil import MongodbUtil
import mns_common.utils.data_frame_util as data_frame_util
import mns_common.component.zt.zt_common_service_api as zt_common_service_api

mongodb_util = MongodbUtil('27017')
mongodb_util_27019 = MongodbUtil('27019')

save_zt_name = 'realtime_quotes_now_zt_new'
choose_field = ["_id",
                "symbol",
                "name",
                "industry",
                "now_price",
                "chg",
                "quantity_ratio",
                "amount_level",
                "disk_ratio",
                "real_disk_diff_amount_exchange",
                'max_real_main_inflow_multiple',
                'sum_main_inflow_disk',
                "real_main_inflow_multiple",
                "real_super_main_inflow_multiple",
                "super_main_inflow_multiple",
                "main_inflow_multiple",
                "disk_diff_amount_exchange",
                "large_inflow_multiple",
                "today_main_net_inflow",
                "today_main_net_inflow_ratio",
                "super_large_order_net_inflow",
                "super_large_order_net_inflow_ratio",
                "large_order_net_inflow",
                "large_order_net_inflow_ratio",
                "reference_main_inflow",
                "disk_diff_amount",
                "mv_circulation_ratio",
                "real_exchange",
                "exchange",
                'real_exchange',
                "total_mv",
                "flow_mv",
                "volume",
                "high",
                "low",
                "open",
                "yesterday_price",
                "amount",
                "total_mv_sp",
                "flow_mv_sp",
                "outer_disk",
                "inner_disk",
                "classification",
                "number",
                "str_day",
                "str_now_date"
                ]


def create_index():
    mongodb_util.create_index(save_zt_name,
                              [("symbol", 1), ("number", 1)])

    mongodb_util.create_index(save_zt_name,
                              [("symbol", 1)])

    mongodb_util.create_index(save_zt_name,
                              [("number", 1)])

    mongodb_util.create_index(save_zt_name,
                              [("str_day", 1)])

    mongodb_util.create_index(save_zt_name,
                              [("str_now_date", 1)])
    mongodb_util.create_index(save_zt_name,
                              [("symbol", 1), ("str_now_date", 1)])
    mongodb_util.create_index(save_zt_name,
                              [("str_day", 1), ("str_now_date", 1)])

    mongodb_util.create_index(save_zt_name,
                              [("symbol", 1), ("str_day", 1)])


def get_mongodb_util(str_day):
    tag = mongodb_util.exist_data_query('trade_date_list', query={'_id': str_day, "tag": True})
    if tag:
        return mongodb_util_27019
    else:
        return mongodb_util


# 同步一天高涨幅列表
def save_stock_high_chg_pool(str_day):
    real_time_quotes_now_init = east_money_stock_api.get_real_time_quotes_all_stocks()

    sync_date = date_handle_util.add_date_day(date_handle_util.no_slash_date(str_day), 0)
    str_now_day = sync_date.strftime('%Y-%m-%d')

    realtime_quotes_db_name = 'realtime_quotes_now_' + str_now_day
    number = get_today_realtime_quotes_max_number(realtime_quotes_db_name, str_day)

    query = {"number": number, "chg": {'$gte': 9.7}}

    real_time_quotes_now = mongodb_util.find_query_data(realtime_quotes_db_name, query)
    if real_time_quotes_now.shape[0] == 0:
        return
    real_time_quotes_now = common_service_fun_api.total_mv_classification(
        real_time_quotes_now.copy())
    real_time_quotes_now = real_time_quotes_now.sort_values(by=['chg'], ascending=False)
    real_time_quotes_now = common_service_fun_api.exclude_new_stock(real_time_quotes_now)

    # todo fix industry
    industry_group_df = company_common_service_api.get_company_info_industry()
    industry_group_df = industry_group_df.set_index(['_id'], drop=True)
    real_time_quotes_now.drop(columns=['industry'], inplace=True)
    real_time_quotes_now = real_time_quotes_now.set_index(['symbol'], drop=False)
    real_time_quotes_now = pd.merge(real_time_quotes_now, industry_group_df, how='outer',
                                    left_index=True, right_index=True)
    real_time_quotes_now = real_time_quotes_now.dropna(inplace=False)

    zt_symbol_info = zt_common_service_api.get_last_trade_day_zt(str_day)

    zt_symbol_connected_boards_numbers_list = zt_symbol_info.loc[
        zt_symbol_info['symbol'].isin(real_time_quotes_now['symbol'])]

    real_time_quotes_now['connected_boards_numbers'] = 1
    if zt_symbol_connected_boards_numbers_list is not None and zt_symbol_connected_boards_numbers_list.shape[0] != 0:
        for yesterday_zt in zt_symbol_connected_boards_numbers_list.itertuples():
            real_time_quotes_now.loc[
                real_time_quotes_now["symbol"] == yesterday_zt.symbol, ['connected_boards_numbers']] \
                = 1 + yesterday_zt.connected_boards_numbers

    for stock_one in real_time_quotes_now.itertuples():
        try:

            symbol = stock_one.symbol

            classification = common_service_fun_api.classify_symbol_one(symbol)

            chg = float(stock_one.chg)
            if classification == 'X' and chg > 30:
                continue
            elif classification != 'X' and chg > 21:
                continue
            real_time_quotes_now_one = real_time_quotes_now_init.loc[
                real_time_quotes_now_init['symbol'] == symbol]
            list_date = list(real_time_quotes_now_one['list_date'])[0]
            list_date = str(list_date)
            list_date = list_date.replace(".0", "")
            list_date = date_handle_util.lash_date(list_date)

            list_date_time = date_handle_util.str_to_date(list_date, "%Y-%m-%d")
            str_now_day_time = date_handle_util.str_to_date(str_now_day, "%Y-%m-%d")

            list_to_now_days = date_handle_util.days_diff(str_now_day_time, list_date_time)

            last_trade_day = trade_date_common_service_api.get_last_trade_day(str_day)

            last_day_high_chg = mongodb_util.exist_data_query('stock_hfq_daily',
                                                              query={"symbol": symbol, "date": last_trade_day,
                                                                     "chg": {'$gte': 9}})

            open = stock_one.open
            high = stock_one.high
            close = stock_one.now_price
            yi_zhi_ban = False
            if open == high and open == close:
                yi_zhi_ban = True

            stock_high_chg_pool = {
                '_id': symbol + '_' + str_now_day,
                'symbol': symbol,
                'name': stock_one.name,
                'industry': stock_one.industry,
                'str_day': str_now_day,
                'classification': classification,
                'chg': stock_one.chg,
                "connected_boards_numbers": stock_one.connected_boards_numbers,
                "open": stock_one.open,
                "close": stock_one.now_price,
                "high": stock_one.high,
                "low": stock_one.low,
                "volume": stock_one.volume,
                "amount": stock_one.amount,
                "flow_mv_level": stock_one.flow_mv_level,
                "flow_mv_sp": stock_one.flow_mv_sp,
                "total_mv_sp": stock_one.total_mv_sp,
                "list_to_now_days": list_to_now_days,
                "list_date": list_date,
                "exchange": stock_one.exchange,
                "last_day_high_chg": last_day_high_chg,
                "yi_zhi_ban": yi_zhi_ban
            }
            mongodb_util.save_mongo(pd.DataFrame([stock_high_chg_pool], index=[0]),
                                    'stock_high_chg_pool')
            logger.info("更新高涨幅数据成功{},{}", stock_one.symbol, str_now_day)
        except Exception as e:
            logger.error("更新高涨幅数据异常:{},{},{}", stock_one.symbol, str_now_day, e)
            continue


def get_today_realtime_quotes_max_number(realtime_quotes_db_name, str_day):
    mongo = get_mongodb_util(str_day)
    query = {"symbol": "000001"}
    realtime_quotes = mongo.descend_query(query, realtime_quotes_db_name, 'number', 1)
    if realtime_quotes is None or realtime_quotes.shape[0] == 0:
        return 1
    else:
        return list(realtime_quotes['number'])[0]


def get_high_chg_symbol(str_day):
    realtime_quotes_db_name = 'stock_qfq_daily'

    query = {"date": date_handle_util.no_slash_date(str_day), "chg": {'$gte': 9.7}}
    # 今日高涨幅的list
    real_time_quotes_now_high_chg = mongodb_util.find_query_data(realtime_quotes_db_name, query)
    if real_time_quotes_now_high_chg.shape[0] == 0:
        return None
    high_chg_list = list(real_time_quotes_now_high_chg['symbol'])
    # 今日涨停股

    query_zt = {'str_day': str_day}
    zt_pool = mongodb_util.find_query_data('stock_zt_pool', query_zt)
    if zt_pool.shape[0] > 0:
        zt_pool_list = list(zt_pool['symbol'])
        high_chg_list.extend(zt_pool_list)
    high_chg_list = list(set(high_chg_list))
    return high_chg_list


# 保存一天详细涨停数据
def sync_his_high_one_day(str_day):
    mongo = get_mongodb_util(str_day)

    realtime_quotes_db_name = 'realtime_quotes_now_' + str_day
    high_chg_list = get_high_chg_symbol(str_day)
    if high_chg_list is None or len(high_chg_list) == 0:
        return

    for symbol in high_chg_list:
        try:
            query_all = {"symbol": symbol}
            real_time_quotes_now_high_chg_all = mongo.find_query_data(realtime_quotes_db_name, query_all)
            if real_time_quotes_now_high_chg_all.shape[0] == 0:
                return
            real_time_quotes_now_high_chg_all = company_common_service_api.amendment_industry_exist_na(
                real_time_quotes_now_high_chg_all,
                high_chg_list)
            real_time_quotes_now_high_chg_all.dropna(subset=['symbol'], axis=0,
                                                     inplace=True)
            real_time_quotes_now_high_chg_all = data_init_api.calculate_parameter_factor(
                real_time_quotes_now_high_chg_all)

            real_time_quotes_now_high_chg_all['amount_level'] = round(
                (real_time_quotes_now_high_chg_all['amount'] / common_service_fun_api.HUNDRED_MILLION), 2) * 10
            real_time_quotes_now_high_chg_all['flow_mv_sp'] = round(
                (real_time_quotes_now_high_chg_all['flow_mv'] / common_service_fun_api.HUNDRED_MILLION), 2)
            real_time_quotes_now_high_chg_all['total_mv_sp'] = round(
                (real_time_quotes_now_high_chg_all['total_mv'] / common_service_fun_api.HUNDRED_MILLION), 2)

            save_realtime_quotes_now_zt_data(real_time_quotes_now_high_chg_all, str_day, symbol)
            logger.info("同步涨停信息:{},{}", str_day, symbol)
        except BaseException as e:
            logger.error("发生异常:{}:{},{}", str_day, e, symbol)


def save_one_symbol_day(symbol, str_day):
    mongo = get_mongodb_util(str_day)
    realtime_quotes_db_name = 'realtime_quotes_now_' + str_day
    high_chg_list = [symbol]
    query_all = {"symbol": symbol}
    real_time_quotes_now_high_chg_all = mongo.find_query_data(realtime_quotes_db_name, query_all)
    if real_time_quotes_now_high_chg_all.shape[0] == 0:
        return
    real_time_quotes_now_high_chg_all = company_common_service_api.amendment_industry_exist_na(
        real_time_quotes_now_high_chg_all,
        high_chg_list)
    real_time_quotes_now_high_chg_all = real_time_quotes_now_high_chg_all.dropna(inplace=False)
    real_time_quotes_now_high_chg_all = data_init_api.calculate_parameter_factor(
        real_time_quotes_now_high_chg_all)

    real_time_quotes_now_high_chg_all.loc[:, 'amount_level'] = round(
        (real_time_quotes_now_high_chg_all.loc[:, 'amount'] / common_service_fun_api.HUNDRED_MILLION), 2) * 10
    real_time_quotes_now_high_chg_all.loc[:, 'flow_mv_sp'] = round(
        (real_time_quotes_now_high_chg_all.loc[:, 'flow_mv'] / common_service_fun_api.HUNDRED_MILLION), 2)
    real_time_quotes_now_high_chg_all.loc[:, 'total_mv_sp'] = round(
        (real_time_quotes_now_high_chg_all['total_mv'] / common_service_fun_api.HUNDRED_MILLION), 2)

    save_realtime_quotes_now_zt_data(real_time_quotes_now_high_chg_all, str_day, symbol)


def save_realtime_quotes_now_zt_data(realtime_quotes_now_zt, str_day, symbol):
    realtime_quotes_now_zt = common_service_fun_api.classify_symbol(realtime_quotes_now_zt.copy())
    # create_index()
    if 'wei_bi' in realtime_quotes_now_zt.columns and bool(1 - ("wei_bi" in choose_field)):
        choose_field.append("wei_bi")
    if 'up_speed' in realtime_quotes_now_zt.columns and bool(1 - ("up_speed" in choose_field)):
        choose_field.append("up_speed")
    if 'list_date' in realtime_quotes_now_zt.columns and bool(1 - ("list_date" in choose_field)):
        choose_field.append("list_date")
    realtime_quotes_now_zt.loc[:, 'str_day'] = str_day
    realtime_quotes_now_zt = realtime_quotes_now_zt[choose_field]
    remove_query = {"symbol": symbol, "str_day": str_day}
    result = mongodb_util.remove_data(remove_query, save_zt_name).acknowledged
    if result:
        mongodb_util.insert_mongo(realtime_quotes_now_zt, save_zt_name)


def sync_one_day_zt_info(str_day):
    sync_his_high_one_day(str_day)
    save_stock_high_chg_pool(str_day)


def sync_all_data():
    create_index()
    end_date = date_handle_util.add_date_day('20231029', 0)

    sync_date = date_handle_util.add_date_day('20231030', 0)

    str_now_day = sync_date.strftime('%Y-%m-%d')
    while sync_date > end_date:
        try:
            sync_one_day_zt_info(str_now_day)
            sync_date = date_handle_util.add_date_day(date_handle_util.no_slash_date(str_now_day), -1)
            str_now_day = sync_date.strftime('%Y-%m-%d')
            logger.info(str_now_day)
        except BaseException as e:
            logger.error("发生异常:{}:{}", str_now_day, e)


# fix miss symbol
def stock_qfq_daily_high_chg_pool(str_day):
    high_chg_list = get_high_chg_symbol(str_day)

    realtime_quotes_db_name = 'realtime_quotes_now_' + str_day
    number = get_today_realtime_quotes_max_number(realtime_quotes_db_name, str_day)

    query = {"number": number, "chg": {'$gte': 9.7}}
    mongodb = get_mongodb_util(str_day)
    real_time_quotes_now = mongodb.find_query_data(realtime_quotes_db_name, query)
    if real_time_quotes_now.shape[0] == 0:
        high_chg_list = high_chg_list
    else:
        real_time_quotes_now_symbol_list = real_time_quotes_now['symbol']
        high_chg_list.extend(real_time_quotes_now_symbol_list)
        high_chg_list = list(set(high_chg_list))

    if high_chg_list is None:
        return

    query = {'symbol': {"$in": high_chg_list}, 'date': date_handle_util.no_slash_date(str_day)}
    stock_qfq_daily_list = mongodb_util.find_query_data('stock_qfq_daily', query)

    real_time_quotes_now_init = east_money_stock_api.get_real_time_quotes_all_stocks()

    stock_qfq_daily_list = stock_qfq_daily_list.sort_values(by=['chg'], ascending=False)

    zt_symbol_info = zt_common_service_api.get_last_trade_day_zt(str_day)

    zt_symbol_connected_boards_numbers_list = zt_symbol_info.loc[
        zt_symbol_info['symbol'].isin(stock_qfq_daily_list['symbol'])]

    stock_qfq_daily_list['connected_boards_numbers'] = 1
    if zt_symbol_connected_boards_numbers_list is not None and zt_symbol_connected_boards_numbers_list.shape[0] != 0:
        for yesterday_zt in zt_symbol_connected_boards_numbers_list.itertuples():
            stock_qfq_daily_list.loc[
                stock_qfq_daily_list["symbol"] == yesterday_zt.symbol, ['connected_boards_numbers']] \
                = 1 + yesterday_zt.connected_boards_numbers

    for stock_one in stock_qfq_daily_list.itertuples():
        try:

            symbol = stock_one.symbol

            classification = common_service_fun_api.classify_symbol_one(symbol)

            real_time_quotes_now_one = real_time_quotes_now_init.loc[
                real_time_quotes_now_init['symbol'] == symbol]
            if data_frame_util.is_empty(real_time_quotes_now_one):
                list_date = '19890729'
            else:
                list_date = list(real_time_quotes_now_one['list_date'])[0]
                list_date = str(list_date)
                list_date = list_date.replace(".0", "")
            list_date = date_handle_util.lash_date(list_date)

            list_date_time = date_handle_util.str_to_date(list_date, "%Y-%m-%d")
            str_now_day_time = date_handle_util.str_to_date(str_day, "%Y-%m-%d")

            list_to_now_days = date_handle_util.days_diff(str_now_day_time, list_date_time)
            if list_to_now_days == 0:
                # 排除当天上市新股
                continue

            last_trade_day = trade_date_common_service_api.get_last_trade_day(str_day)

            last_day_high_chg = mongodb_util.exist_data_query('stock_hfq_daily',
                                                              query={"symbol": symbol, "date": last_trade_day,
                                                                     "chg": {'$gte': 9}})

            open = stock_one.open
            high = stock_one.high
            close = stock_one.close
            yi_zhi_ban = False
            if open == high and open == close:
                yi_zhi_ban = True

            stock_high_chg_pool = {
                '_id': symbol + '_' + str_day,
                'symbol': symbol,
                'name': stock_one.name,
                'industry': stock_one.industry,
                'str_day': str_day,
                'classification': classification,
                'chg': stock_one.chg,
                "connected_boards_numbers": stock_one.connected_boards_numbers,
                "open": stock_one.open,
                "close": stock_one.close,
                "high": stock_one.high,
                "low": stock_one.low,
                "volume": stock_one.volume,
                "amount": stock_one.amount,
                # "flow_mv_level": stock_one.flow_mv_level,
                "flow_mv_sp": stock_one.flow_mv_sp,
                # "total_mv_sp": stock_one.total_mv_sp,
                "list_to_now_days": list_to_now_days,
                "list_date": list_date,
                "exchange": stock_one.exchange,
                "last_day_high_chg": last_day_high_chg,
                "yi_zhi_ban": yi_zhi_ban,
                "miss_out": True
            }
            query_exists = {"symbol": symbol, "str_day": str_day}
            if mongodb_util.exist_data_query('stock_high_chg_pool', query_exists):
                continue
            else:
                mongodb_util.save_mongo(pd.DataFrame([stock_high_chg_pool], index=[0]),
                                        'stock_high_chg_pool')
            logger.info("更新高涨幅数据成功{},{}", stock_one.symbol, str_day)
        except Exception as e:
            logger.error("更新高涨幅数据异常:{},{},{}", stock_one.symbol, str_day, e)
            continue


if __name__ == '__main__':
    sync_one_day_zt_info('2022-06-28')

    # sync_date = date_handle_util.add_date_day('20221022', 0)
    # now_date = datetime.now()
    # str_now_day = sync_date.strftime('%Y-%m-%d')
    # while now_date > sync_date:
    #     try:
    #         save_one_symbol_day('000948', str_now_day)
    #         sync_date = date_handle_util.add_date_day(date_handle_util.no_slash_date(str_now_day), 1)
    #         str_now_day = sync_date.strftime('%Y-%m-%d')
    #         print(str_now_day)
    #     except BaseException as e:
    #         logger.error("发生异常:{}:{}", str_now_day, e)
