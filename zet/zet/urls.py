from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'inicio.views.inicio', name='inicio'),
    url(r'^', include('inicio.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
