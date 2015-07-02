from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'app.views.login'),
    url(r'^logout$', 'app.views.logout'),
    url(r'^doLogin', 'app.views.doLogin'),
    url(r'^$', 'app.views.index'),
    
    url(r'^parts/index$', 'parts.views.index'),
    url(r'^parts/loadAll', 'parts.views.loadAll'),
    url(r'^parts/search', 'parts.views.search'),
    url(r'^parts/consume$', 'parts.views.consume'),
    url(r'^parts/consume/search', 'parts.views.consumeSearch'),
    url(r'^parts/consume/loadAll', 'parts.views.consumeLoadAll'),
    url(r'^parts/incoming$', 'parts.views.incoming'),
    url(r'^parts/incoming/search', 'parts.views.incomingSearch'),
    url(r'^parts/incoming/loadAll', 'parts.views.incomingLoadAll'),
)
