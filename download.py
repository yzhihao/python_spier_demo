__author__ = 'yzh'
#coding=utf-8
import urllib2
import socket
import socks
class htmldowmloader(object):
    def download(self,url):
        if url is None:
            return None
        try:
            # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "110.73.33.207", 6673)
            # socket.socket = socks.socksocket
            proxy = urllib2.ProxyHandler({'HTTP': '1.175.79.25:8080'})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)
            response=urllib2.urlopen(url,timeout=8)
            if response.getcode()!= 200:
                return None
            print('response.urlopen is ok')
        except Exception, e:
            print('Exception='+str(e))
        try:
            html=response.read()
        except Exception, e:
            print('Exception='+str(e))
        return html