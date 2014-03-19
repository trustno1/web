#-*- coding:utf-8 -*-
import urllib, urllib2, cookielib
from  django.shortcuts  import  render_to_response
from django.http import HttpResponse




def index(request):
    return render_to_response('index.html')

address=[
    {'name':'zhou','address':'南宁'},
    {'name':'huang','address':'深圳'}
    ]

def addressbook(request):
    return render_to_response('list.html',{'address':address})

def test(request):
    response = urllib2.urlopen('http://mp3.baidu.com/dev/api/?tn=getinfo&ct=0&word=%E6%B5%81%E6%B5%AA%E8%AE%B0&ie=utf-8&format=json')
    context = response.read()
    #context = "hello"

    return render_to_response('test.html',{'context':context})

