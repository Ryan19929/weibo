# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
from lxml import etree
import re
import requests
import traceback

class weibo:
    cookie={"Cookie":"ALF=1555641304; SCF=ApRSzMac3kjcUBx4UF_Gp36PAEkPTvnieMUJwbsVf9Nb2eZImZUSBdH5V2OH-mMjQLll1lBwstFMmodSzcCwDOA.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W55RIB_wq7247bANwEPZMAy5JpX5KMhUgL.Fo-ESo.RSK-E1K22dJLoIEBLxKqL1-zL1-BLxKnLB--LBonLxKqL1h.L1K2LxKnL1K.L1-2t; _T_WM=80299f9c025f2bc6a3be1cb3928fe038; TMPTOKEN=ap0u38Dm2FUCea8XRddGugb0xIGfzalkCveRUNQAEJfP2B0dtCgwA9ERPvIsGY57; SUB=_2A25xldeoDeRhGeNM7VsZ9SvOwj2IHXVTefngrDV6PUJbkdAKLRXmkW1NThWn4pj_eYD6eSmqKdnxD9Xh-qIhvJAx; SUHB=0Yhhu-8dErQS7J; SSOLoginState=1553049592; MLOGIN=1; XSRF-TOKEN=be6922; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=uicode%3D20000174"}

    def __init__(self,content,start_time,end_time):
        self.content=content  #要搜索的内容
        self.username=[]
        self.weibo_content=[]
        self.weibo_time=[]
        self.up_num=[]
        self.comment_num=[]
        self.start_time=start_time
        self.end_time=end_time

    def get_username(self,info):
        try:
            str_name=info.xpath("")
            url="https://s.weibo.com/weibo?q="+self.content+"&typeall=1&suball=1&timescope=custom:"+self.start_time+":"+self.end_time
            html=requests.get(url, cookies=self.cookie).content
            print(url)
            selector=etree.HTML(html)
            username = selector.xpath("//a[@class='name']/text()")[0]
            return username
        except Exception as e:
            print("Error:",e)
            traceback.print_exc()

    def get_weibo_info(self):
        try:
            url="https://weibo.cn/search/?q=advancedfilter=1&keyword="+self.content+"nick=&starttime="+self.start_time+"&"+self.end_time+"&sort=time&smblog=搜索"
            html=requests.get(url,cookies=self.cookie).content
            selector=etree.HTML(html)
            if selector.xpath("//input[@name='mp']")==[]:
                page_num=1
            else:
                page_num=selector.xpath("//input[@name='mp']")[0].attrib["value"]
            for page in range(1,page_num+1):
                url2=url+"&page="+page
                html2=requests.get(url2,cookies=self.cookie).content
                selector2=etree.HTML(html2)
                info=selector2.xpath("//div[@class='c']")
                is_empty=info[0].xpath("//span[@class='ctt']")
                if is_empty:
                    for i in range(0,len(info)-2):
                        self.get_username(info[i])
        except:
            print()

def main():
    try:
        content="杭州电子科技大学"
        start_time="20190301"
        end_time="20190320"
        wb=weibo(content,start_time,end_time)
        abname=wb.get_username()
        print(abname)
    except Exception as e:
        print("error",e)
        traceback.print_exc()

if __name__=="__main__":
    main()