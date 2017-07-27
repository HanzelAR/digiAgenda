from django.conf.urls import url, include
from . import views


app_name = 'users'

urlpatterns = [
    url(r'^login/$', views.login, name='login')
]
