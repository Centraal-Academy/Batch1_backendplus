from django.conf.urls import include, url
from django.contrib import admin
from my_app import urls, api_urls
from real_time import urls
import django.contrib.auth.urls


urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'new_app/', include('my_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/v1/', include('my_app.api_urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^channels/', include('real_time.urls')),
]
