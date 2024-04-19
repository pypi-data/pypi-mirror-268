# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from . import models


class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'request_method', 'request_url',
                    'response_code', 'datetime', 'ip_address')
    date_hierarchy = 'datetime'
    list_filter = ('request_method', 'response_code')
    search_fields = ('user', 'request_url')


class BlackListAdmin(admin.ModelAdmin):
    list_display = ('id' , 'ip_address', 'block_network_address','blocked')
    list_editable = ('ip_address', 'block_network_address','blocked')
    list_display_links = ('id',)
    list_filter = ('block_network_address','blocked')
    search_fields = list_display_links

admin.site.register(models.BlackListIPAdress,BlackListAdmin)

admin.site.register(models.ActivityLog, LogAdmin)
