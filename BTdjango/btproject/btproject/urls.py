from django.contrib import admin
from django.conf.urls import url, include
import rawdata.views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rawdata/', include('rawdata.urls')),
]
