#!/usr/bin/python
#coding=utf-8
'''
Created on 2017年10月26日

@author: LIDA
'''
import urllib2,urllib
import sys
from bs4 import BeautifulSoup
import xlwt
import threading
import time
import re

#shenfeng = ['河北','山西','内蒙古','辽宁','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','四川','贵州','云南','西藏','甘肃','青海','宁夏','新疆','北京','上海','天津','重庆']

def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args,**kwargs)
        print('end time: %s'%(time.strftime('%x',time.localtime())) )
        print('run time: %s'%(time.time() - t0))
        return back
    return new_fun
@run_time
def ipSearch():
    if len(sys.argv) == 2:
        ipfile = sys.argv[1]
        f = open(ipfile,'r')
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('sheet 1',cell_overwrite_ok=True)
        i = 0
        f = open(ipfile,'r')
        for ip in f.readlines():
            url = 'http://ip.chinaz.com/%s' % ip
            req = urllib2.Request(url)
            res = urllib2.urlopen(req).read()
            soup = BeautifulSoup(res, 'html.parser')
            a = soup.find_all('span',class_="Whwtdhalf w50-0")
            b = a[1].string
            sheet.write(i, 0, ip)
            sheet.write(i, 1, b)
            i += 1
        wbk.save('ip-address.xls')
threads = []
t1 = threading.Thread(target=ipSearch())
threads.append(t1)

s = u'程序开始运行，请稍后...'
z = u'运行完成，已在当前目录自动生成报表'
if __name__=='__main__':
    print s
    for t in threads:
        t.setDaemon(True)
        t.start()
    #ipSearch()
    print z
