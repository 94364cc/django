from django.conf.urls import patterns, include, url
from django.contrib import admin
from depotapp.views import product_list

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^depotapp/', include('depotapp.urls')),

)
# urlpatterns+=patterns('djangoTest.views',
#     url(r'^hello/', 'hello'),
#
# )
