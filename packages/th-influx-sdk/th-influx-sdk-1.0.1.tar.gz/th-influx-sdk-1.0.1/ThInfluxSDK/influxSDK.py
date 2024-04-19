# -*- coding: utf-8 -*-
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
from typing import List
from dateutil import parser
from datetime import datetime, timedelta, timezone
from dateutil.tz import tzutc
from collections import OrderedDict
import json


def get_influx_db_connection(url, username, password, timeout):
    """
    获取InfluxDB连接，使用完必须使用close()关闭。

    :param url: 数据库连接地址
    :param username: 用户名
    :param password: 密码
    :param timeout: 设置HTTP客户端超时时间（单位：秒）
    :return: InfluxDBClient实例
    """
    # 创建InfluxDBClient实例，并设置超时
    client = InfluxDBClient(host=url, username=username, password=password, timeout=timeout)

    # 尝试连接到数据库
    try:
        client.ping()
        print("InfluxDB connection successful")
    except InfluxDBClientError as e:
        print(f"InfluxDB connection failed: {e}")
        return None

    return client


def get_time_list(start_time: int, end_time: int, interval: int) -> List[int]:
    """
    获取时间集合

    :param start_time: 开始时间（时间戳，单位：毫秒）
    :param end_time: 结束时间（时间戳，单位：毫秒）
    :param interval: 时间间隔（单位：秒）
    :return: 包含时间戳的列表
    """
    time_list = []
    while start_time <= end_time:
        time_list.append(start_time)
        start_time += interval * 1000  # 将秒转换为毫秒
    return time_list


def utc_get_time(utc_time: str) -> int:
    """
    获取UTC时间对应的时间戳

    :param utc_time: UTC时间字符串
    :return: 返回UTC时间的时间戳（毫秒）
    """
    # 使用 dateutil.parser 解析UTC时间字符串
    time = parser.parse(utc_time)
    # 转换为时间戳（毫秒）
    timestamp = int(time.timestamp() * 1000)
    return timestamp


def utc_time_add_one_day(utc_time: str) -> int:
    """
    UTC时间增加一天的时间戳

    :param utc_time: 传入的UTC时间, 时间格式：2024-03-13T16:00:00Z
    :return: UTC时间增加一天的时间戳（毫秒）
    """
    # 使用dateutil.parser解析UTC时间字符串
    time = parser.parse(utc_time)
    # 把日期往后增加一天
    new_time = time + timedelta(days=1)
    # 转换为时间戳（毫秒）
    timestamp = int(new_time.timestamp() * 1000)
    return timestamp


def utc_time_add_one_day(utc_time: str) -> str:
    """
    UTC时间增加一天

    :param utc_time: 传入的UTC时间, 时间格式：2024-03-13T16:00:00Z
    :return: 返回增加一天后的UTC时间，时间格式：2024-03-14T16:00:00Z
    """
    # 使用dateutil.parser解析UTC时间字符串
    time = parser.parse(utc_time)
    # 把日期往后增加一天
    new_time = time + timedelta(days=1)
    # 转换回UTC时间字符串
    utc_add_day = new_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    return utc_add_day


def utc_time_to_timestamp(utc: str) -> int:
    """
    UTC时间转换成毫秒时间戳

    :param utc: UTC时间字符串
    :return: 毫秒级时间戳
    """
    # 使用dateutil.parser解析UTC时间字符串
    utc_datetime = parser.parse(utc)
    # 转换为timestamp（毫秒）
    timestamp = int(utc_datetime.timestamp() * 1000)
    return timestamp


def convert_utc_to_beijing_time(utc_time: str) -> str:
    """
    UTC时间转换成北京时间，时间格式："yyyy-MM-dd HH:mm:ss"

    :param utc_time: UTC时间字符串
    :return: 北京时间字符串
    """
    # 将UTC时间字符串解析为datetime对象
    utc_datetime = datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%SZ')
    # 将UTC时间转换为UTC时区对应的datetime对象
    utc_aware = utc_datetime.replace(tzinfo=timezone.utc)
    # 将UTC时间转换为北京时间（东八区）
    beijing_aware = utc_aware + timedelta(hours=8)
    # 格式化时间为指定格式
    beijing_time_str = beijing_aware.strftime('%Y-%m-%d %H:%M:%S')
    return beijing_time_str


def get_new_set_data(database: str, tableName: str, queryTime: str, pointList: List[str],
                     influxDB: InfluxDBClient) -> str:
    # 1. 初始化 resultList
    resultList = []
    # 2. 使用join方法将pointList中的字符串用'|'连接起来
    pointStr = '|'.join(pointList)
    # 3. 构建SQL查询字符串
    SQLForMaxTime = f"SELECT LAST(VALUE), UUID FROM {tableName} WHERE UUID =~ /^{pointStr}$/"

    # 4. 如果queryTime不为空，则添加时间条件
    if queryTime is not None and queryTime != "":
        SQLForMaxTime += f" AND time <= '{queryTime}'"

    # 5. 执行查询
    queryResult = influxDB.query(SQLForMaxTime, database=database)

    # 6. 从查询结果中提取最大的时间戳
    maxTime = ""
    if queryResult and 'results' in queryResult and queryResult['results']:
        for result in queryResult['results']:
            if 'series' in result and result['series']:
                series = result['series'][0]
                if 'values' in series and series['values']:
                    maxTime = series['values'][0][0]
                    break

    # 添加 group by UUID 到查询字符串
    SQLForData = SQLForMaxTime + " GROUP BY UUID"

    # 执行查询
    query_result_for_data = influxDB.query(SQLForData, database=database)

    # 初始化结果列表
    resultList = []

    # 进行数据时间对齐处理
    if query_result_for_data and 'results' in query_result_for_data:
        for result in query_result_for_data['results']:
            if 'series' in result and result['series']:
                for series in result['series']:
                    # 遍历每个序列的值
                    for value in series['values']:
                        # 创建一个新的列表来存储对齐后的数据
                        obj_list = [maxTime, value[1], value[2]]  # 假设maxTime已经在之前的代码中定义
                        # 添加其他需要的值到列表中，注意Python中索引是从0开始的
                        # 将对齐后的数据添加到结果列表中
                        resultList.append(obj_list)

    map = OrderedDict()

    if len(resultList) > 0:
        # 假设resultList的每个子列表的第一个元素是时间，我们将其转换为北京时间
        map["time"] = convert_utc_to_beijing_time(resultList[0][0])

        # 遍历resultList的每个子列表
        for sublist in resultList:
            # 假设每个子列表的第三个元素是键，第二个元素是值
            map[sublist[2]] = sublist[1]

            # 将字典转换为JSON字符串
    toJSONString = json.dumps(map)

    # 返回JSON字符串
    return toJSONString
