# -*- coding: utf-8 -*-
import requests
from lxml import html
import json
import urllib3
import time


def login():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    email = "satai1919@gmail.com"
    pas = "FintechMl"
    LOGIN_URL = "https://ycharts.com/login"
    
    session = requests.session()
    
    result = session.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')))[0]
    
    payload = {
        'username': email,
        'password': pas,
        'csrfmiddlewaretoken': authenticity_token
    }
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-CN;q=0.5,fr;q=0.4',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '142',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '__utmc=69688216; __utmz=69688216.1552357223.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); hblid=JQ0XqOZqwIXsXwT51y8Lx0HAoArzb6aB; _okdetect=%7B%22token%22%3A%2215523572229710%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22ycharts.com%22%7D; olfsk=olfsk12322538568271435; _ok=1228-592-10-8601; hubspotutk=7cf8506f03419977c4be0b998e16b46e; __hssrc=1; _cb_ls=1; _cb=B56Z-XDKRC_SC1U7V5; 33e807c05af9078f6b2ed01ced5fc28d5c8f52f4=1; wcsid=dhJeybtiypg1EtEV1y8Lx0Harz6ZJ0AA; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1552376476295%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _okac=f0b90d7b5b31a4a193bbea257a02ab8a; _okla=1; __utma=69688216.990749136.1552357223.1552376476.1552379039.4; __hstc=165832289.7cf8506f03419977c4be0b998e16b46e.1552357225006.1552376478295.1552379041795.4; _cb_svref=null; csrftoken='+authenticity_token+'; ycsessionid=uualzce6xlp27stjyfdee97evws5ollz; __utmt=1; page_view_ctr=51; __utmb=69688216.46.10.1552379039; mp_bd6455515e9730c7dc2f008755a4ddfe_mixpanel=%7B%22distinct_id%22%3A%20%221696fb366da666-05b45b73c1e575-36657105-fa000-1696fb366db7e2%22%2C%22%24device_id%22%3A%20%221696fb366da666-05b45b73c1e575-36657105-fa000-1696fb366db7e2%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%221696fb366da666-05b45b73c1e575-36657105-fa000-1696fb366db7e2%22%7D; __hssc=165832289.42.1552379041795; _chartbeat2=.1552357225125.1552382317031.1.B8gGKsDfweQGDsM3n-BBKPGqB8ZxQ4.40; _oklv=1552382376998%2CdhJeybtiypg1EtEV1y8Lx0Harz6ZJ0AA',
        'Host': 'ycharts.com',
        'Origin': 'https://ycharts.com',
        'Referer': 'https://ycharts.com/login',
        'Upgrade-Insecure-Requests': '1',
    }
    
    r = session.post("https://ycharts.com/login", data=payload, headers = headers, verify=False)
    
    r.status_code
    return session