# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.module_loading import import_string as _load
from django.core.exceptions import DisallowedHost
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from .models import ActivityLog
from . import conf
from django.utils.encoding import  force_str
import json
import pprintpp
from .models import BlackListIPAdress
from django.db.models import Q
import re 

def get_ip_address(request):
    for header in conf.IP_ADDRESS_HEADERS:
        addr = request.META.get(header)
        if addr:
            return addr.split(',')[0].strip()

def get_META_headers(request):
    # Read the content from the LimitedStream
    content = request.META.read()

    # Decode the content using the appropriate encoding
    decoded_content = force_str(content, encoding='utf-8')

    # Convert the decoded content to a Python object (e.g., a dictionary)
    data = json.loads(decoded_content)

    # Return the data as JSON
    return json.dumps(data)

def get_extra_data(request, response, body):
    if not conf.GET_EXTRA_DATA:
        return
    return _load(conf.GET_EXTRA_DATA)(request, response, body)


class ActivityLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.saved_body = request.body
        if conf.LAST_ACTIVITY and request.user.is_authenticated:
            getattr(request.user, 'update_last_activity', lambda: 1)()

    def process_response(self, request, response):
        try:
            self._write_log(request, response, getattr(request, 'saved_body', ''))
        except DisallowedHost:
            return HttpResponseForbidden()
        return response

    def _write_log(self, request, response, body):
        miss_log = [
            not(conf.ANONYMOUS or request.user.is_authenticated),
            request.method not in conf.METHODS,
            any(url in request.path for url in conf.EXCLUDE_URLS)
        ]

        if conf.STATUSES:
            miss_log.append(response.status_code not in conf.STATUSES)

        if conf.EXCLUDE_STATUSES:
            miss_log.append(response.status_code in conf.EXCLUDE_STATUSES)

        if any(miss_log):
            return

        if getattr(request, 'user', None) and request.user.is_authenticated:
            user, user_id = request.user.get_username(), request.user.pk
        elif getattr(request, 'session', None):
            user, user_id = 'unknown_{}'.format(request.session.session_key), 0
        else:
            return

        ActivityLog.objects.create(
            user_id=user_id,
            user=user,
            request_url=request.build_absolute_uri()[:255],
            request_method=request.method,
            response_code=response.status_code,
            ip_address=get_ip_address(request),
            extra_data=get_extra_data(request, response, body),
            headers = pprintpp.pformat(dict(request.META.items()),indent=4),
            payload =  request.body
        )
    def __call__(self, request):
        ip_address = get_ip_address(request)
        network_address =re.findall(r"([\.\d]+)\.",ip_address)[0]
        query = Q(block_network_address=True , ip_address__startswith = network_address , blocked = True) | Q(ip_address=ip_address , blocked = True)
        if BlackListIPAdress.objects.filter(query).exists() :
            response = HttpResponseForbidden()
        else: 
            response = self.get_response(request)

        return response