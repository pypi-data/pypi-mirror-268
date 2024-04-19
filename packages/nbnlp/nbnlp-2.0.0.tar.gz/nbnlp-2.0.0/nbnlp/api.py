import os
from mysql.connector import Error
from .db import fetch_data_from_mysql, check_sentences_is_unique, insert_data_into_mysql, append_data_to_file, delete_data_from_mysql

# 查询数据
def fetch_data(DB_CONFIG, query):
    try:
        return fetch_data_from_mysql(DB_CONFIG, query)
    except Error:
        raise Error("数据库查询出错")

# 插入的前置准备
def check_sentence(DB_CONFIG, query, params):
    try:
        return check_sentences_is_unique(DB_CONFIG, query, params)
    except Error:
        raise Error("数据库查询出错")

# 插入数据到数据库，并获取插入信息
def insert_data(DB_CONFIG, params, insert_query, select_query):
    try:
        return insert_data_into_mysql(DB_CONFIG, params, insert_query, select_query)
    except Error:
        raise Error("数据库插入出错")
    
# 插入到文件那种
def append_file(bieos):
    try:
        # 获取当前文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 获取当前文件所在的目录，即nbnlp目录
        project_dir = os.path.dirname(current_file_path)
        # 构建到data目录的绝对路径
        data_dir = os.path.join(project_dir, 'data')
        # 使用绝对路径
        training_corpus = os.path.join(data_dir, 'train.tsv')
        test_corpus = os.path.join(data_dir, 'test.tsv')

        if not append_data_to_file(bieos, training_corpus) or not append_data_to_file( bieos, test_corpus):
            return False
        return True
    except Error:
        raise Error("数据库插入出错")
    
# 删除数据
def delete_data(DB_CONFIG, query, params):
    try:
        return delete_data_from_mysql(DB_CONFIG, query, params)
    except Error:
        raise Error("数据库删除出错")
    
# 训练模型
def train_model(server, params, finetune_path, transformer_path, fine_electra_small_zh_path):
    try:
        training_result = server.train_model(params, finetune_path, transformer_path, fine_electra_small_zh_path)
        if not training_result:
            return False
        return True
    except Error as e:
        raise Error("模型训练出错")
