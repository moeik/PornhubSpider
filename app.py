#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re,requests,time,os
from lxml import etree

url_sta = "https://cn.pornhub.com"
url_list = []
title_list = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}

def Mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        pass

def FileDel():
    os.remove('url.txt')

def Read_file(filepath):
    with open(filepath) as fp:
        content=fp.read()
    return content

def Get_Page(x):
    Page = requests.get(x,headers=headers)
    Page.encoding = "utf-8"
    Page = Page.text
    Page = etree.HTML(Page)
    return Page

def Get_Url(x):
    if 'search?search=' in x:
        VideoUrl = Get_Page(x).xpath('//*[@id="videoSearchResult"]/li/div/div/a/@href')
        VideoTitle = Get_Page(x).xpath('//*[@id="videoSearchResult"]/li/div/div/span/a/text()')
    else:
        VideoUrl = Get_Page(x).xpath('//*[@id="videoCategory"]/li/div/div/a/@href')
        VideoTitle = Get_Page(x).xpath('//*[@id="videoCategory"]/li/div/div/span/a/text()')
    for i in range(1, len(VideoUrl)):
        url_list.append(url_sta + VideoUrl[i])
    for i in range(len(VideoTitle)):
        title = re.sub("[\n\t\\\/:*?,，!！？。()（ ）.\"<=->|\]\[]","",VideoTitle[i])
        title_list.append(title)

def Get_Video_Link(x):
    while True:
        JS_File = Get_Page(x).xpath('//*[@id="player"]/script[1]/text()')
        JS = re.sub('[\n\t]','',JS_File[0])
        voll = re.findall('var player_mp4_seek = "ms";(.*?)flashvars',JS)  #ms/start
        try:
            if voll[0]:
                break
        except:
            continue
    var_start =  re.sub('var ','',voll[0])
    var_end =  re.sub('/\*(.*?)\*/','',var_start)
    sta = re.findall('(.*?)quality_',var_end)
    end = re.findall('quality_\d{3,4}p=(.*?);',var_end)
    WriteUrl = sta[0]+'\n'+'url = '+end[0]+'\nfile_handle=open("url.txt",mode="w")'+\
               '\nfile_handle.write(url)'+'\nfile_handle.close()'
    exec(WriteUrl)

def Get_Img(x):
    ImgUrl = Get_Page(x).xpath('/html/head/meta[19]/@content')
    save_img = requests.get(ImgUrl[0], headers=headers)
    with open(r"Pornhub/" + Title + "/" + 'cover' + ".jpg", "wb") as fh:
        fh.write(save_img.content)
        fh.flush()

def Download():
    DVLink = Read_file('url.txt')
    FileDel()
    NowTime = time.strftime("%Y%m%d", time.localtime())
    r = requests.get(DVLink, stream=True)
    f = open(r"Pornhub/" + Title + "/" + NowTime + ".mp4", "wb")
    for chunk in r.iter_content(chunk_size=1024):
       if chunk:
           f.write(chunk)

def cs1():
    global Title
    url = input("Video Url:")
    url = re.sub(" ","",url)
    Get_Video_Link(url)
    Title = Get_Page(url).xpath('//*[@class="inlineFree"]/text()')
    Title = re.sub("[\n\t\\\/:*?,，!！？。()（ ）.\"<=->|\]\[]", "", Title[0])
    Path = "Pornhub/" + Title + "/"
    print('标题：'+Title + '\n' + Read_file('url.txt') + '\n')
    Download_Chioce = input("是否下载当前视频？(y/n)")
    if Download_Chioce == 'y' or Download_Chioce == 'Y':
        Mkdir(Path)
        Get_Img(url)
        Download()
    else:
        pass

def cs2():
    global Title
    url = input("Page Url:")
    url = re.sub(" ","",url)
    Get_Url(url)
    Download_Chioce = input("当前页面共有%d个视频，是否全部下载？(y/n)"%len(url_list))
    if Download_Chioce == 'y' or Download_Chioce == 'Y':
        for i in range(len(url_list)):
            try:
                url = url_list[i]
                Get_Video_Link(url)
                Title = re.sub("[\n\t\\\/:*?,，!！？。()（ ）.\"<=->|\]\[]", "", title_list[i])
                Path = "Pornhub/" + Title + "/"
                print('标题：'+Title+'\n'+Read_file('url.txt')+'\n')
                Mkdir(Path)
                Get_Img(url)
                Download()
            except:
                continue
    else:
        pass


def start():
    cs = int(input("\033[32m解析选项：\n1.解析单个视频\n2.解析页面视频\n请选择："))
    if cs == 1:
        cs1()
    elif cs == 2:
        cs2()
    else:
        print("输入有误")
start()
