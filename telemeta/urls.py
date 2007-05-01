# Copyright (C) 2007 Samalyse SARL
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://svn.parisson.org/telemeta/TelemetaLicense.
#
# Author: Olivier Guilyardi <olivier@samalyse.com>

from django.conf.urls.defaults import *
from telemeta.models import MediaItem, MediaCollection
from telemeta.core import ComponentManager
from telemeta.views.web import WebView

# initialization
comp_mgr = ComponentManager()
web_view = WebView(comp_mgr)

# query sets for Django generic views
all_items = { 'queryset': MediaItem.objects.all(), }
all_collections = { 'queryset': MediaCollection.objects.all(), }

urlpatterns = patterns('',
    (r'^$', web_view.index),

    # items
    (r'^items/$', 'django.views.generic.list_detail.object_list', 
        dict(all_items, paginate_by=10, template_name="mediaitem_list.html")),
    (r'^items/(?P<item_id>[0-9]+)/$', web_view.item_detail),
    (r'^items/(?P<item_id>[0-9]+)/download/(?P<format>[0-9A-Z]+)/$', 
        web_view.item_export),

    # collections
    (r'^collections/$', 'django.views.generic.list_detail.object_list',
        dict(all_collections, paginate_by=10, template_name="collection_list.html")),
    (r'^collections/(?P<object_id>[0-9]+)/$', 
        'django.views.generic.list_detail.object_detail',
        dict(all_collections, template_name="collection_detail.html")),

    # search
    (r'^search/$', web_view.quick_search),

    # administration        
    (r'^admin/$', web_view.admin_index),        

    # dictionaries administrations
    (r'^admin/dictionaries/(?P<dictionary_id>[0-9a-z]+)/$', web_view.edit_dictionary),        
    (r'^admin/dictionaries/(?P<dictionary_id>[0-9a-z]+)/add/$', web_view.add_to_dictionary),        
    (r'^admin/dictionaries/(?P<dictionary_id>[0-9a-z]+)/update/$', web_view.update_dictionary),        
    (r'^admin/dictionaries/(?P<dictionary_id>[0-9a-z]+)/(?P<value_id>[0-9]+)/$',
        web_view.edit_dictionary_value),   

    (r'^admin/dictionaries/(?P<dictionary_id>[0-9a-z]+)/(?P<value_id>[0-9]+)/update/$',
        web_view.update_dictionary_value),   


    # CSS+Images (FIXME: for developement only)
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': './telemeta/htdocs/css'}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': './telemeta/htdocs/images'}),
)


