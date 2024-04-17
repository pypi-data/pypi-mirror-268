#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Dict

import aiomysql
import pymysql
import pandas as pd
import pymysql.cursors

from collections import deque

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.types import NVARCHAR, Float, Integer
from dbutils.pooled_db import PooledDB

from openfinance.config import Config
from openfinance.utils.singleton import Singleton
from openfinance.datacenter.database import EMPTY_DATA, EMPTY_NUM
from openfinance.utils.string_tools.util import is_chinese

_bound_num = 10000

class Database:
    """ Python连接到 MySQL 数据库及相关操作 """

    connected = False
    engine = None
    pool = None
    # 构造函数，初始化时直接连接数据库

    def __init__(self, conf):
        if type(conf) is not dict:
            print('错误: 参数不是字典类型！')
        else:
            for key in ['host', 'port', 'user', 'pw', 'db']:
                if key not in conf.keys():
                    print('错误: 参数字典缺少 %s' % key)
            if 'charset' not in conf.keys():
                conf['charset'] = 'utf8'
        try:
            self.pool = PooledDB(
                creator=pymysql,
                maxconnections=6,
                mincached=2,
                maxcached=5,
                maxshared=3,
                blocking=True,
                maxusage=None,
                setsession=['SET AUTOCOMMIT = 1'],
                ping=0,
                host=conf['host'],
                port=conf['port'],
                user=conf['user'],
                passwd=conf['pw'],
                db=conf['db'],
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.connected = True
            self.engine = create_engine(
                "mysql+pymysql://%(user)s:%(pw)s@%(host)s:%(port)d/%(db)s?charset=utf8" % conf
            )
        except pymysql.Error as e:
            print('数据库连接失败:', end='')

    def create_table(self, table, contents):
        with self.pool.connection() as conn:
            try:
                # 使用execute()方法执行sql，如果表存在则删除
                with conn.cursor() as cursor:
                    cursor.execute('drop table if EXISTS ' + table)
                # 创建表的sql
                    if isinstance(contents, dict):
                        new_contents = ""
                        for k, v in contents.items():
                            new_contents += "\n" + k + " " + v + ","
                        contents = new_contents[:-1]  # delete last ","
                    sql = '''create table ''' + table + '''\n(''' + contents + '''\n)'''
                    print(sql)
                    cursor.execute(sql)
            except pymysql.Error as e:
                print(e)
                conn.rollback()
                return False

    def add_column_to_table(self, table, contents):
        with self.pool.connection() as conn:
            try:
                with conn.cursor() as cursor:
                    if isinstance(contents, dict):
                        new_contents = ""
                        for k, v in contents.items():
                            new_contents += k + " " + v + ","
                        contents = new_contents[:-1]  # delete last ","
                    sql = '''ALTER TABLE ''' + table + ''' ADD ''' + contents
                    print(sql)
                    cursor.execute(sql)
            except pymysql.Error as e:
                conn.rollback()
                return False

    # 插入数据到数据表
    def insert(self, table, val_obj, dup_key=None):
        sql_top = 'INSERT INTO ' + table + ' ('
        sql_tail = ') VALUES ('
        with self.pool.connection() as conn:
            try:
                for key, val in val_obj.items():
                    sql_top += key + ','
                    if isinstance(val, str):
                        val = "\"" + val + "\""
                    else:
                        val = str(val)
                    sql_tail += val + ','
                sql = sql_top[:-1] + sql_tail[:-1] + ')'
                #print(sql)
                if dup_key:
                    sql += " ON DUPLICATE KEY UPDATE "
                    for key in dup_key:
                        val = val_obj[key]
                        if isinstance(val, str):
                            val = "\"" + val + "\""
                        else:
                            val = str(val)                      
                        sql += key + "=" + val + ","
                    sql = sql[:-1]
                print(sql)
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                #return conn.insert_id()
                return True
            except pymysql.Error as e:
                conn.rollback()
                return False

    # 插入数据到数据表
    def execute(self, sql):
        with self.pool.connection() as conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return True
            except pymysql.Error as e:
                conn.rollback()
                return False

    # 更新数据到数据表
    def update(self, table, val_obj, range_str):
        with self.pool.connection() as conn:
            sql = 'UPDATE ' + table + ' SET '
            try:
                for key, val in val_obj.items():
                    if isinstance(val, str):
                        val = "\"" + val + "\""
                    sql += key + '=' + val + ','
                sql = sql[:-1] + ' WHERE ' + range_str
                #print(sql)
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return cursor.rowcount
            except pymysql.Error as e:
                conn.rollback()
                return False

    # 删除数据在数据表中
    def delete(self, table, range_str):
        with self.pool.connection() as conn:
            sql = 'DELETE FROM ' + table + ' WHERE ' + range_str
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return cursor.rowcount
            except pymysql.Error as e:
                conn.rollback()
                return False

    # 查询唯一数据在数据表中
    def select_one(self, table, factor_str, field='*'):
        with self.pool.connection() as conn:
            sql = 'SELECT ' + field + ' FROM ' + table + ' WHERE ' + factor_str
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return cursor.fetchall()[0]
            except pymysql.Error as e:
                return False

    # 查询多条数据在数据表中
    def select_more(self, table, range_str="", field='*'):
        with self.pool.connection() as conn:
            if range_str:
                sql = 'SELECT ' + field + ' FROM ' + table + ' WHERE ' + range_str
            else:
                sql = 'SELECT ' + field + ' FROM ' + table 
            # print(sql)
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return cursor.fetchall()
            except pymysql.Error as e:
                return False

    # 查询条件筛选查询
    def select_by_order(self, table, order_column, limit_num=4, field='*'):
        with self.pool.connection() as conn:
            inner_sql = 'SELECT ' + field + ' FROM ' + table + \
                        ' order by ' + order_column + \
                ' desc limit ' + str(limit_num)
            sql = "SELECT * from (" + inner_sql + ")t order by " + order_column
            # print(sql)
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return cursor.fetchall()
            except pymysql.Error as e:
                print(e)
                return False

    # 直接执行
    def exec(self, sql):
        with self.pool.connection() as conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return cursor.fetchall()
            except pymysql.Error as e:
                print(e)
                return False

    # 统计某表某条件下的总行数
    def count(self, table, range_str='1'):
        with self.pool.connection() as conn:
            sql = 'SELECT count(*) FROM ' + table + ' WHERE ' + range_str
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return cursor.fetchall()[0]['res']
            except pymysql.Error as e:
                return False

    # 统计某字段（或字段计算公式）的合计值
    def sum(self, table, field, range_str='1'):
        with self.pool.connection() as conn:
            sql = 'SELECT SUM(' + field + ') AS res FROM ' + \
                table + ' WHERE ' + range_str
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                conn.commit()
                return cursor.fetchall()[0]['res']
            except pymysql.Error as e:
                return False

    def insert_data_by_pandas(
        self,
        dataframe,
        table_name,
        dtypes={},
        if_exists='append',
        single=False
    ):
        '''
        通过dataframe 向 sql 中插入表，此方法缺点是若表已存在，不能替换表中部分重复数据，只能替换/追加整张表
        :param dataframe: pd.Dataframe类型
        :param table_name: 插入的表名
        :param if_exists: {'fail', 'replace', 'append'}, default 'fail'
            - fail: If table exists, do nothing.
            - replace: If table exists, drop it, recreate it, and insert data.
            - append: If table exists, insert data. Create if does not exist.
        :return:
        '''
        def create_upsert_method(primary_key_column):
            def method(table, conn, keys, data_iter):
                # Create the INSERT statement with named placeholders
                insert = f"INSERT INTO {table.name} ({','.join(keys)})"
                try:
                    for d in data_iter:
                        values = " VALUES("
                        update = " ON DUPLICATE KEY UPDATE "
                        for i, name in enumerate(keys):
                            new_val = "NULL,"
                            if d[i]:
                                new_val = "'" + str(d[i]) + "',"
                            values += new_val
                            if name not in primary_key_column:
                                update += name + "=" + new_val

                        values = values[:-1] + ")"
                        sql = insert + values + update[:-1]
                        conn.execute(text(sql))
                except Exception as e:
                    print("An error occurred:", str(e))
            return method

        if single:
            for i in range(len(dataframe)):
                try:
                    dataframe.iloc[i:i+1].to_sql(
                        table_name,
                        self.engine,
                        if_exists=if_exists,
                        index=False,
                        chunksize=100,
                        dtype=dtypes,
                        method=create_upsert_method(list(dtypes.keys()))
                    )
                except Exception as e:
                    print(e)
                    pass
        else:
            try:
                dataframe.to_sql(
                    table_name,
                    self.engine,
                    if_exists=if_exists,
                    index=False,
                    chunksize=100,
                    dtype=dtypes,
                    method=create_upsert_method(list(dtypes.keys()))
                )
            except Exception as e:
                print(e)
                pass

    # 查询多条数据在数据表中
    def get_data_and_manuel_summary(
        self,
        table,
        order_str,
        limit_num=5,
        summary_num=5,
        summary_mode='sample',
        columns_to_names=None,
        with_chart=False
    ):
        fields = ""
        if columns_to_names is None:
            fields = "*"
        else:
            fields = ", ".join(k for k, v in columns_to_names.items())
        # order name not in show
        if order_str not in fields:
            fields += ", " + order_str
        data = self.select_by_order(
            table=table,
            order_column=order_str,
            limit_num=limit_num,
            field=fields
        )
        if data:
        # print(data, columns_to_names)
            if summary_mode == "sample":
                summary_data = deque()
                shift = int(
                    (len(data))/summary_num) if len(data) >= summary_num else 1
                for i in range(len(data)-1, -1, -shift):
                    summary_data.appendleft(data[i])
            else:
                summary_data = data[-summary_num:]
            idx = 0
            for line in summary_data:
                for k, v in line.items():
                    if k in columns_to_names:
                        if k == order_str:
                            continue # remove Time Order in String
                        if 0 == idx:
                            columns_to_names[k] = columns_to_names[k] + \
                                " in sequencial order: "
                        try:
                            if abs(v) > _bound_num:
                                # to short it number
                                columns_to_names[k] += "{:.1e}".format(v) + ", "
                            else:
                                # to short it number
                                columns_to_names[k] += str(
                                    round(float(v), 1)) + ", "
                        except:
                            columns_to_names[k] += str(v) + ", "
                idx += 1
            result = ""
            if fields == "*":
                result = " \n".join("The " + k + " : " + v for k,
                                    v in columns_to_names.items())
                # error here, to improve later
            else:
                result = " \n".join(v[:-2] for k, v in columns_to_names.items())
            if with_chart:
                return {
                    "result": result,
                    "chart": data
                }
            else:
                return result
        else:
            return EMPTY_DATA

    # 直接执行sql查询多条数据在数据表中
    def exec_by_modelformat(
        self,
        sql,
        columns_to_names
    ):
        data = self.exec(sql)
        if not data:
            return EMPTY_DATA
        # print(data, columns_to_names)
        hit_columns = dict()
        idx = 0
        for line in data:
            for k, v in line.items():
                if k in columns_to_names:
                    if 0 == idx:
                        hit_columns[k] = "Progressive " + \
                            columns_to_names[k] + ":"
                    try:
                        if abs(v) > _bound_num:
                            # to short it number
                            hit_columns[k] += "{:.1e}".format(v) + ", "
                        else:
                            # to short it number
                            hit_columns[k] += str(round(float(v), 1)) + ", "
                    except:
                        hit_columns[k] += str(v) + ", "
                elif is_chinese(k):
                    if 0 == idx:
                        hit_columns[k] = "Progressive " + k + ":"
                    try:
                        if abs(v) > _bound_num:
                            # to short it number
                            hit_columns[k] += "{:.1e}".format(v) + ", "
                        else:
                            # to short it number
                            hit_columns[k] += str(round(float(v), 1)) + ", "
                    except:
                        hit_columns[k] += str(v) + ", "
            idx += 1
        if len(hit_columns) == 0:
            return EMPTY_DATA
        result = " \n".join(v[:-2] for k, v in hit_columns.items())
        return result

class AsyncDB:
    conn = None
    connected = False
    conf = None

    def __init__(
        self,
        conf
    ):
        self.conf = conf

    async def connect(
        self
    ):
        if not self.connected:
            self.conn = await aiomysql.connect(
                host = self.conf.get("host", "localhost"), 
                port = self.conf.get("port", "3306"), 
                user = self.conf.get("user", "root"), 
                password = self.conf.get("pw", ""),
                db = self.conf.get("db", "")
            )
            self.connected = True
     
    async def exec(
        self,
        sql
    ):
        try:
            async with self.conn.cursor() as cursor:
                await cursor.execute(sql)
                return await cursor.fetchall()
        except pymysql.Error as e:
            print(e)
            return False

    async def select_more(
        self,
        table, 
        range_str="", 
        field='*'        
    ):
        try:
            if range_str:
                sql = 'SELECT ' + field + ' FROM ' + table + ' WHERE ' + range_str
            else:
                sql = 'SELECT ' + field + ' FROM ' + table
            async with self.conn.cursor() as cursor:
                await cursor.execute(sql)
                return await cursor.fetchall()
        except pymysql.Error as e:
            print(e)
            return False

class DataBaseManager(metaclass=Singleton):
    name_to_databases: Dict[str, Database] = {}

    def _add(
        self,
        name: str, 
        db: Database 
    ) -> None:
        try:
            if name not in self.name_to_databases:
                self.name_to_databases.update({name: db})
        except Exception as e:
            raise e
    def get(
        self, 
        name: str
    ):
        return self.name_to_databases.get(name, None)

    def __init__(
        self,
        conf
    ):
        conf = conf.get("db")
        for k, v in conf.items():
            if v.get("async", False):
                self._add(k, AsyncDB(v))
            else:
                self._add(k, Database(v))