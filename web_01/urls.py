from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
	path('control_panel/',include('control_panel.urls')),
	path('admin/',admin.site.urls),
	path('',include('main.urls')),
	path('',include('users.urls')),
]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
