# project_name/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogpost.urls')),
    path('exhibition/', include('exhibition.urls')),  # <-- include blog URLs under /blog/
    path('sponsorship/', include('sponsorship.urls')),
    path('speakers/', include('speakers.urls')),
    path('registration/', include('registration_app.urls')),
    path('gallery/', include('gallery.urls')),
    path('signin/',include('signin.urls'))
    # path('', include('main.urls')),       # optional: if you have a home app
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
