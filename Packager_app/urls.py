from django.conf.urls import patterns, url

from Packager_app import views

urlpatterns = patterns('',
	url(r'^$', views.login_user, name='login_user'),
	url(r'^customers$', views.customers, name='customers'),
	url(r'^customer/(?P<customer_id>\d+)/$', views.customer, name='customer'),
	url(r'^items$', views.items, name='items'),
	url(r'^item/(?P<item_id>\d+)/$', views.item, name='item'),
	url(r'^packages$', views.packages, name='packages'),
	url(r'^package/(?P<package_id>\d+)/$', views.package, name='package'),
	url(r'^package_group/(?P<package_group_id>\d+)/$', views.package_group, name='package_group'),
	url(r'^package_group/new/$', views.new_package_group, name='new_package_group'),
	url(r'^delivery/$', views.bulk_delivery, name='bulk_delivery'),
        url(r'^delivery/(?P<item_group_id>\d+)/$', views.delivery, name='delivery'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^logs/$', views.logs, name='logs'),
	url(r'^daemons/$', views.daemons, name='daemons'),
	url(r'^image_rendition/(?P<image_rendition_id>\d+)/$', views.image_rendition, name='image_rendition'),
	url(r'^image_renditions/upload/(?P<item_id>\d+)/$', views.image_renditions_upload, name='image_renditions_upload'),
	url(r'^search$', views.search, name='search'),
)
