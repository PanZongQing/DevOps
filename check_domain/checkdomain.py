#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:高效码农

import pprint
import time
import random
import xlsxwriter
from datetime import datetime
import urllib.request
from lxml import etree


# 批量读取文件中的域名
def read_file(filePath):
    with open(filePath, "r") as f:  # 打开文件
        data = f.readlines()  # 读取文件
        return data


# 通过某网站获取域名到期时间
def get_expiry_date(url_list):
    url_expiry_date_list = []
    for url in url_list:
        url_expiry_date_dict = {}
        time.sleep(random.randrange(3))
        req_whois = urllib.request.urlopen('https://whois.chinaz.com/' + url)
        result = req_whois.read().decode()
        # print(result)
        html = etree.HTML(result)
        print(html)

        endTimes = html.xpath('//*[@id="whois_info"]/li[5]/div[2]/span/text()')
        print(endTimes)
        if len(endTimes) > 0:
            endTime = endTimes[0].replace('年', '-').replace('月', '-').replace('日', '')
        else:
            errorInfo = html.xpath('//div[@class="IcpMain02"]')
            endTime = errorInfo[0].xpath('string(.)').strip()
        url_expiry_date_dict['url'] = url.replace('\n', '')
        url_expiry_date_dict['endTime'] = endTime
        pprint.pprint(url_expiry_date_dict)
        url_expiry_date_list.append(url_expiry_date_dict)
    pprint.pprint(url_expiry_date_list)
    return url_expiry_date_list


# 写入Excel文件
def write_excel(domain_list):
    # 创建一个新的文件
    with xlsxwriter.Workbook('host_ip.xlsx') as workbook:
        # 添加一个工作表
        worksheet = workbook.add_worksheet('域名信息')
        # 设置一个加粗的格式
        bold = workbook.add_format({"bold": True})
        # 分别设置一下 A 和 B 列的宽度
        worksheet.set_column('A:A', 50)
        worksheet.set_column('B:B', 15)
        # 先把表格的抬头写上，并设置字体加粗
        worksheet.write('A1', '域名', bold)
        worksheet.write('B1', '信息', bold)
        # 设置数据写入文件的初始行和列的索引位置
        row = 1
        col = 0
        for domain_ex_date in domain_list:
            url = domain_ex_date['url']
            endTime = domain_ex_date['endTime']
            currDate = datetime.today().date()
            try:
                endDate = datetime.strptime(endTime, "%Y-%m-%d").date()
                diffDate = endDate - currDate
                if diffDate.days <= 7:
                    style = workbook.add_format({'font_color': "red"})
                else:
                    style = workbook.add_format({'font_color': "black"})
            except:
                style = workbook.add_format({'font_color': "red"})
            pprint.pprint(url + ': ' + endTime)
            worksheet.write(row, col, url, style)
            worksheet.write(row, col + 1, endTime, style)
            row += 1


urls = read_file('domain.txt')
urls_list = get_expiry_date(urls)
write_excel(urls_list)