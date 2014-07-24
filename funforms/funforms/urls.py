from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import bythebook.views

urlpatterns = patterns(
    '',
    url(r'^books', bythebook.views.BookView.as_view(), name='add_book'),
    url(r'^admin/', include(admin.site.urls)),
)
