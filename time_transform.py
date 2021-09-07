#!/usr/bin/env python3

#_*_coding:utf-8_*_

# 本地时间 转换 为时间戳
import time
import sys


def unix_time(dt):
    #转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp
 
def local_time(timestamp):
    #转换成localtime
    time_local = time.localtime(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt
 
 
def unix2GPS_S(unix_time):
    stamp = float(unix_time)   
    Week = int((stamp + 18 - 315964800)/(7*24*3600))
    Sec = int((stamp + 18 - 315964800)-Week*7*24*3600)
    print ("GPS周内秒: ",Sec)
    

if __name__ == '__main__':
    #time_now = '2021-02-26 11:54:11'
    print("usage: python3 py_path '%Y-%m-%d %H:%M:%S'")
    time_now = sys.argv[1]
    print(time_now)
    unix_t = unix_time(time_now)
    print(unix_t)
    unix2GPS_S(unix_t)
    