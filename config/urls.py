from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/', include('apiv1.urls')),
    re_path('', RedirectView.as_view(url='/')),
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]

# ファイルアップロードの設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)