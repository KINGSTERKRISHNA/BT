from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from . import models
from django_tables2.utils import A
from . import views
from django.contrib.auth.models import User
import django_filters
from distutils.util import strtobool


class RawdataFilter(django_filters.FilterSet):
    class Meta:
        model = models.Post
        fields = '__all__'


def filter(request):
    filter = UserFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'rawdata/search.html', {'filter': filter})
