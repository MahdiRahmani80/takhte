from django.conf.urls import url
from  app.api import views


urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name="post-list api"),
    url(r'^(?P<id>\d)$', views.PostDitailAPIView.as_view(), name='Detail' ),
    url(r'^(?P<id>\d)/delete/$', views.PostDeleteAPIView.as_view(), name='Delete'),
        url(r'^(?P<id>\d)/update/$', views.PostUpdateAPIView.as_view(), name='Update'),

]