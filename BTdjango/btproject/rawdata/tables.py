from __future__ import unicode_literals
import django_tables2 as tables
from .models import Post
from . import models
from django_tables2.utils import A
from . import views
from django.utils.safestring import mark_safe
from django_tables2.export.export import TableExport


class RawdataTable(tables.Table):
    export_formats = ['csv', 'xls', 'xlsx', 'json']

    class Meta:
        model = models.Post
        template_name = 'django_tables2/semantic.html'
        attrs = {'tbody': {'id': 'myTable'}}
