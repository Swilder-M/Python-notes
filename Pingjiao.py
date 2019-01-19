#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-19 22:40
# @Author  : Swilder_M
# @Site    : Poxiaobbs.com
# @File    : pingjiao
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    pj_url = 'http://172-20-139-153.webvpn.qqhru.edu.cn/jxpgXsAction.do?oper=listWj&wjbz=null'
    cookie = {
        'webvpn_username': '2016021011%7C1547906255%7Cb376309eb8ae40e0178e5fa7245ebc576c501e27',
        'JSESSIONID': 'ahgXUJhYa9Teh_Q7SzMHw',
        '_astraeus_session': 'cTczSHA2Q1QwSHlCcVcrTHVnNFRsVHhOSkhnaWx3cDZ2a2F3b1o2TkRkUU9TRVIrWEU5MXdaZjZKcU9YY0F6MlNBNnN1eUhJOTNMR3BGUHNlMEJZV3dya2xwUE84TCtDRGRUUnBYREZPeUtLQjNmSi9zYllOTEMrTUo3UmsraXhCOHozSzd3YkdOVWhvMFJIV1NjR2lsNTQ4cXBHdjlaTVBIcUFrc2VXazNiVTJlUWgvZ1Y0c1NpbG9iZGFHcTdDQTBEbEM5Smo5Tm9BTGo3TUhmSjNjSnBkTERLL1pTSlBiTVUrTXhpbUlrWGNMSkh0WHpjMExNdDFSTnFXMnI5MkNJRmNVTjY5VnhRVDZZZHpCODE2VEdSMzhycUJtNVR4V0xLR1ZmWmxvaWFKL1Z6TWg3VVhEZE91YkczTU03VXJaMjN6cC9HWitJRHF1UUtTNitVbGwweTBSVFRWRGhFcFNLY1NCaGNMZ2RZQ2E0enREKzlteWpmaGxxdFQybHJQLS10dm9iZGRFVVkraktBZ3RJYXpDclNRPT0%3D--8147d1ef7fc0f79e65dfe88ceb5347e4c9e2dc82'
    }
    res = requests.get(url=pj_url, cookies=cookie)

    # res.encoding = 'GBK'
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    teacher_tr = soup.findAll("img", {"align": "center"})

    for i in teacher_tr:
        info_list = i.get("name").split("#@")
        print(info_list)
        pj_post_url = 'http://172-20-139-153.webvpn.qqhru.edu.cn/jxpgXsAction.do?oper=wjpg'
        pj_data = {
            "wjbm": str(info_list[0]),
            "bpr": str(info_list[1]),
            "pgnr": str(info_list[-1]),
            "xumanyzg": "zg",
            "wjbz": "",
            "0000000027": "5_0.8",
            "0000000028": "5_0.8",
            "0000000029": "5_0.8",
            "0000000030": "5_0.8",
            "0000000031": "5_0.8",
            "0000000032": "5_0.8",
            "0000000033": "5_0.8",
            "0000000034": "5_0.8",
            "0000000035": "5_0.8",
            "0000000036": "5_0.8",
            "0000000037": "5_0.8",
            "0000000038": "5_0.8",
            "0000000039": "4_0.8",
            "0000000040": "4_0.8",
            "0000000041": "3_0.8",
            "0000000042": "4_0.8",
            "0000000043": "6_0.8",
            "0000000044": "6_0.8",
            "0000000045": "6_0.8",
            "0000000046": "7_0.8",
            "zgpj": ""
        }

        pj_res_data = requests.post(url=pj_post_url, cookies=cookie, data=pj_data)
        res_i_zz = re.compile(r'alert\("(.*?)"')
        res_success = res_i_zz.findall(pj_res_data.text)[0]
        print(res_success, end='')
        if (res_success.find('失败') > -1):
            print('可能是你已经评估完成，重复评估会显示失败')
        print('- ' * 50)
