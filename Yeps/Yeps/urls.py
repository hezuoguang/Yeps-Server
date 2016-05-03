from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from Yep import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Yeps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^share/', views.share_view),
)

urlpatterns += patterns('Yep.api_router',
    # Examples:
    # url(r'^$', 'Yeps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^yeps/api/', "api_router"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
