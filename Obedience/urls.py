from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$','dashboard.views.main'),
                       url(r'^login/$','dashboard.views.login_view'),
                       url(r'^Auth/$','dashboard.views.User_Auth'),
    # Examples:
    # url(r'^$', 'Obedience.views.home', name='home'),
    # url(r'^Obedience/', include('Obedience.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
