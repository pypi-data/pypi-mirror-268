import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager

# 上下文管理器
@contextmanager
def mysql_connection(db_config):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
    finally:
        connection.commit()
        cursor.close()
        connection.close()

# 查询数据(sql)
def fetch_data_from_mysql(db_config, query):
    try:
        with mysql_connection(db_config) as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    except Error:
        raise Error

# 插入的前置准备(sql)
def check_sentences_is_unique(db_config, query, params):
    try:
        with mysql_connection(db_config) as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result['count']
    except Error:
        raise Error
    
# 获取插入 id(sql)
def fetch_insert_id(cursor):
    try:
        # 获取插入 id
        last_insert_id_query = "SELECT LAST_INSERT_ID()"
        cursor.execute(last_insert_id_query)
        last_insert_id = cursor.fetchone()["LAST_INSERT_ID()"]
        return last_insert_id
    except Error:
        raise Error
    

# 将数据插入 MySQL 数据库并返回插入信息
def insert_data_into_mysql(db_config, params, insert_query, select_query):
    try:
        with mysql_connection(db_config) as cursor:
            # 执行插入语句
            cursor.execute(insert_query, params)

            # 获取插入 id
            last_insert_id = fetch_insert_id(cursor)
        
            # 执行查询语句
            cursor.execute(select_query, (last_insert_id,))
            record = cursor.fetchone()
            return record
    except Error:
        raise Error
    
# 将数据加入到 tsv 中
def append_data_to_file(annotations, file_path):
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            for text, label in annotations:
                f.write('\t'.join([text, label]) + '\n')
            f.write('\n')
        return True
    except IOError as e:
        return False
    
# 从数据库删除数据
def delete_data_from_mysql(db_config, delete_query, params):
    try:
        with mysql_connection(db_config) as cursor:
            # 执行删除语句
            cursor.execute(delete_query, params)
    except Error:
        raise Error
