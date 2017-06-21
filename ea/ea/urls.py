from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ea.views.home'),
    
    # auth
    url(r'^accounts/login/$',  'ea.views.login'),
    url(r'^accounts/auth/$',  'ea.views.auth_view'),    
    url(r'^accounts/logout/$', 'ea.views.logout'),
    url(r'^accounts/loggedin/$', 'ea.views.loggedin'),
    url(r'^accounts/invalid/$', 'ea.views.invalid_login'),    
    url(r'^accounts/register/$', 'ea.views.register_user'),
    url(r'^accounts/register_success/$', 'ea.views.register_success'),
    # Examples:
    # url(r'^$', 'ea.views.home', name='home'),
    # url(r'^ea/', include('ea.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
