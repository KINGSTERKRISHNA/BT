from django.shortcuts import render, redirect, get_object_or_404, reverse, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from .tables import RawdataTable
from django_tables2 import RequestConfig
from .filters import RawdataFilter
from django_tables2.export.export import TableExport


def rawdata_list(request):
    table = RawdataTable(Post.objects.all(), order_by="-id")
    RequestConfig(request).configure(table)
    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))

    return render(request, 'rawdata/rawdata_list.html', {'table': table})


def search(request):
    rawdata_list = Post.objects.all()
    rawdata_filter = RawdataFilter(request.GET, queryset=rawdata_list)
    return render(request, 'rawdata/search.html', {'filter': rawdata_filter})
