from django.urls import path
from . import views
# from django.conf.urls import patterns, url
# from mysite.views import MyView

urlpatterns = [
    # path('', views.index, name='index'),
    # path('register', views.register, name='register'),
    # path('login', views.login, name='login'),
    path('main', views.main, name='main')
    # path('', views.get_request, name='get_request'),
    # url(r'^mine/$', MyView.as_view(), name='my-view'),
]
