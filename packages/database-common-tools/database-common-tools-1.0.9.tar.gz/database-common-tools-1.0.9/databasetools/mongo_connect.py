# -*- coding: utf-8 -*-

from pymongo import MongoClient, UpdateOne


##################################################
# mongo function
##################################################

def mongo_bulk(collection, docs):
    datas = list()
    for key, doc in docs.items():
        query = dict()
        query['_id'] = key
        bson = dict()
        bson['$set'] = doc
        datas.append(UpdateOne(query, bson, upsert=True))
    return collection.bulk_write(datas)


def mongo_collection(database, collection):
    return database[collection]


def mongo_collection_try(database, collection, indexes):
    if collection not in database.list_collection_names():
        for index in indexes:
            database[collection].create_index(index)
    return database[collection]


def mongo_connect(url):
    return MongoClient(url)


def mongo_database(connect, database):
    return connect[database]


def mongo_find_gt(collection, key, value):
    return collection.find({key: {'$gt': value}})


def mongo_find_gte(collection, key, value):
    return collection.find({key: {'$gte': value}})


def mongo_find_in(collection, key, values):
    return collection.find({key: {'$in': values}})


def mongo_find_all(collection):
    return collection.find()


def mongo_find_query(collection, query):
    return collection.find(query)


def mongo_find_page(collection, page, size):
    skip = (page - 1) * size
    return collection.find().skip(skip).limit(size)


def mongo_count_total(collection):
    return collection.count_documents({})


def mongo_find_start(collection, start, size):
    return collection.find().skip(start).limit(size)

##################################################
# mongo connect
##################################################
# url 连接mongo域名
# db  连接mongo 数据库
# tb  连接mongo 数据表
def mongo_conn(url, db, tb):
    return mongo_collection(mongo_database(mongo_connect(url), db), tb)


# url 连接mongo域名
# db  连接mongo 数据库
# tb  连接mongo 数据表
# ti  连接mongo 数据表索引
def mongo_conn_try(url, db, tb, ti):
    return mongo_collection_try(mongo_database(mongo_connect(url), db), tb, ti)
