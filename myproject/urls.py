from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accounts_url
from boards import urls as boards_url

from boards import views as boards_views


urlpatterns = [
    url(r'^$', boards_views.BoardListView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accounts_url)),
    url(r'^boards/', include(boards_url)),

]
