import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)
from mns_common.db.MongodbUtil import MongodbUtil
import pandas as pd
import mns_common.api.ths.ths_stock_api as ths_stock_api
import time

mongodb_util = MongodbUtil('27017')


# 统计概念数量
def update_concept_num():
    ths_concept_list = mongodb_util.find_all_data('ths_concept_list')
    for ths_concept_one in ths_concept_list.itertuples():
        query = {'concept_code': ths_concept_one.symbol}
        concept_count = (mongodb_util
                         .count(query, 'ths_stock_concept_detail'))
        ths_concept_list_one_df = ths_concept_list.loc[ths_concept_list['symbol'] == ths_concept_one.symbol]
        ths_concept_list_one_df['concept_count'] = concept_count
        mongodb_util.save_mongo(ths_concept_list_one_df, 'ths_concept_list')


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


if __name__ == '__main__':
    update_null_name()
    update_concept_num()
