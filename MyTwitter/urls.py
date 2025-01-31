from django.contrib import admin
from django.urls import path, include
from feed_app import views as fd_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fd_views.index, name='index'),
    path('feed/', include('feed_app.urls')),
    path('mytweets/', fd_views.mytweets, name='mytweets'),
    path('account/', include('users_app.urls')),
]
