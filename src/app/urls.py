from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'app.views.login'),
    url(r'^logout$', 'app.views.logout'),
    url(r'^doLogin', 'app.views.doLogin'),
    url(r'^$', 'app.views.index'),
    
    url(r'^parts/$', 'parts.views.index'),
    url(r'^parts/search', 'parts.views.search'),
    url(r'^parts/loadAll', 'parts.views.loadAll'),
)
