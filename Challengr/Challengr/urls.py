from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from apps.player.views import PlayerViewSet
from apps.account.views import AccountViewSet, ThisAccount
admin.autodiscover()


router = routers.SimpleRouter()
router.register(r'player', PlayerViewSet)
router.register(r'account', AccountViewSet)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Challengr.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^api-token-auth/$', obtain_auth_token),

                       url(r'^api/account/this/$', ThisAccount.as_view()),
                       url(r'^api/', include(router.urls)),
                       )

if settings.DEBUG:
    urlpatterns += (
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            url(r'^docs/', include('rest_framework_swagger.urls')),
                            )


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
