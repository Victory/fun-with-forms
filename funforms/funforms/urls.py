from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import bythebook.views
import hideyshowy.views
import extraball.views

from extraball.models import ExtraBallForm1, ExtraBallForm2

urlpatterns = patterns(
    '',
    url(r'^books', bythebook.views.BookView.as_view(), name='add_book'),
    url(r'^manual',
        bythebook.views.BookManualView.as_view(),
        name='add_book_manual'),
    url(r'^hideyshowy',
        hideyshowy.views.ManualView.as_view(),
        name='add_hideyshowy_manual'),
    url(r'^book-added',
        bythebook.views.BookAddedView.as_view(),
        name='add_book'),
    url(r'^extraball',
        extraball.views.ExtraBallView.as_view([ExtraBallForm1, ExtraBallForm2]),
        name='extraball'),

    url(r'^extraball/done',
        extraball.views.DoneView.as_view(),
        name='extraball_done'),

    url(r'^admin/', include(admin.site.urls)),
)
