from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # 一覧画面
    path('', views.scraping, name='index'),
] +static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)