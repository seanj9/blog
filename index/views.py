#coding:utf-8
from django.shortcuts import *
# Create your views here.
 
def index(request):
    return render_to_response('index.html')