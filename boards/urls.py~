from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', TopicListView.as_view(), name='board_topics'),
    url(r'^(?P<pk>\d+)/new/$', new_topic, name='new_topic'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', PostListView.as_view(), name='topic_posts'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', reply_topic, name='reply_topic'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',PostUpdateView.as_view(), name='edit_post'),
    ]

