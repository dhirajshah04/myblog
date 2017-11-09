from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import (login_view, logout_view, change_password)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^user/login/$', login_view, name='login'),
    url(r'^user/logout/$', logout_view, name='logout'),
    url(r'^user/password/$', change_password, name='change_password'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^blog/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^blog/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^user/password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^user/password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^user/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^user/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]