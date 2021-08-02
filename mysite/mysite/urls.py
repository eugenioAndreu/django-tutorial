from django.contrib import admin
from django.urls import include, path
from polls import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]