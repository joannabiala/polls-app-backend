from django.contrib import admin
from django.urls import include, path
from poll.pollApp import views, urls
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('auth/', views.obtain_auth_token)]
