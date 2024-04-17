# -*- coding: utf-8 -*-

from kafka import KafkaConsumer


##################################################
# kafka function
##################################################

def kafka_consumer(topic, group, servers, offset):
    return KafkaConsumer(topic, group_id=group, bootstrap_servers=servers, auto_offset_reset=offset)
