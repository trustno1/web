from django.conf.urls import patterns, include, url
from views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^list/$',addressbook),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^test/$',test),
    #(r'^static/(?P<path>.*)','django.views.static.serve',{'document_root':STATICFILES_DIRS}),
) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
