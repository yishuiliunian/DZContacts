from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from contacts.views import contact_list
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DZContacts.views.home', name='home'),
    # url(r'^DZContacts/', include('DZContacts.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'contacts/$', contact_list),
)
