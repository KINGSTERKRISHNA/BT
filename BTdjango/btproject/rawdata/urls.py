from . import views
from django.conf.urls import url
from urllib.parse import unquote
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name = 'rawdata'

urlpatterns = [
    url(r'^rawdata_list/', views.rawdata_list, name='rawdata_list'),
    url(r'^search/$', views.search, name='search'),
]
