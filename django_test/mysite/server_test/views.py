from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
# from home.forms import HomeForm
from .blog_scraper import get_posts
# from django.contrib import auth
# from django.contrib.auth.models import User
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import pandas as pd
from io import StringIO
from scrap import scrapper, make_csv

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

# def register(req):
#     posts = get_posts()
#     data = {'post_data': posts}
#     print('===============================')
#     # print(data['post_data'])
#     if req.method == 'POST':
#         posts = get_posts()
#         data = {'post_data': posts}
#         return render(req, 'home.html', data)
#     return render(req, 'home.html', data)

# @csrf_exempt
# def register(req): #post name
#     if req.method == 'POST':
#         # username = req.POST['username']
#         first_name = req.POST['first_name']
#         last_name = req.POST['last_name']
#         user = User(first_name=first_name, last_name=last_name)
#         user.save()
#         data = {'response':'done'}
#         return render(req, 'home.html', data)
#     else:
#         return render(req, 'home.html')
#
# @csrf_exempt
# def login(req):
#     if req.method == 'POST':
#         first = req.POST['first_name']
#         last = req.POST['last_name']
#         data = User.objects.filter(first_name=first, last_name=last)
#         res = {'result': data}
#         # res = {'result':(data.first_name == first) and (data.last_name == last)}
#         return render(req, 'login.html', res)
#     else:
#         return render(req, 'login.html')

def df_creation(fileString):
    temp = StringIO(fileString)
    df = pd.read_csv(temp)
    return (df['Company Name'], df['Company domain name'])

def main(req):
    data = {'response': 'error'}
    if req.method == 'POST':
        file = req.POST['csv_file']
        company_lst = df_creation(file)
        res_lst = scrapper(company_lst)
        make_csv(file, res_lst)
        data = {'response': 'done'}
        return render(req, 'home.html', data)
    return render(req, 'home.html', data)

