import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)

import mns_common.component.concept.ths_concept_common_service_api as ths_concept_common_service_api
from mns_common.db.MongodbUtil import MongodbUtil
from loguru import logger
import mns_common.utils.data_frame_util as data_frame_util
import mns_common.constant.db_name_constant as db_name_constant

mongodb_util = MongodbUtil('27017')


def update_ths_concept_detail(ths_symbol_all_concepts, symbol):
    all_ths_concept = ths_concept_common_service_api.get_all_ths_concept()
    for concept_one in ths_symbol_all_concepts.itertuples():
        try:
            ths_concept_one_db_list = all_ths_concept.loc[all_ths_concept['web_concept_code'] == int(concept_one.cid)]
            if data_frame_util.is_not_empty(ths_concept_one_db_list):

                for ths_one_concept in ths_concept_one_db_list.itertuples():
                    concept_code = ths_one_concept.symbol
                    query = {"$or": [{'symbol': symbol, "concept_code": int(concept_code)},
                                     {'symbol': symbol, "concept_code": int(concept_one.cid)}]}
                    short = concept_one.short
                    long = concept_one.long
                    new_values = {"$set": {"short": short, "long": long}}
                    mongodb_util.update_many(query, new_values, db_name_constant.THS_STOCK_CONCEPT_DETAIL)
        except BaseException as e:
            logger.error("更新ths概念入选理由异常{},{},{}", symbol, concept_one.title, e)
