# project_name/urls.py
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # The line `path('admin/', admin.site.urls)` in the `urls.py` file is creating a URL pattern that
    # maps requests with the path `/admin/` to the Django admin interface. When a user accesses the
    # `/admin/` URL in the browser, they will be directed to the Django admin site where they can
    # manage the project's data models, users, groups, permissions, and more through a web-based
    # interface. This line essentially includes the Django admin URLs and associates them with the
    # `/admin/` path in your project.
    # The line `path('admin/', admin.site.urls)` in the `urls.py` file is creating a URL pattern that
    # maps requests with the path `/admin/` to the Django admin interface. When a user accesses the
    # `/admin/` URL in the browser, they will be directed to the Django admin site where they can
    # manage the project's data models, users, groups, permissions, and more through a web-based
    # interface. This line essentially includes the Django admin URLs and associates them with the
    # `/admin/` path in your project.
    # path('admin/', admin.site.urls),
    path('blog/', include('blogpost.urls')),
    path('exhibition/', include('exhibition.urls')),  # <-- include blog URLs under /blog/
    path('sponsorship/', include('sponsorship.urls')),
    # path('speakers/', include('speakers.urls')),
    path('registration/', include('registration_app.urls')),
    path('gallery/', include('galleries.urls')),
    path('signin/',include('signin.urls')),
    path('',include('main.urls')),
    path('admin/', include('admin.urls')),
    path('', include('main.urls')),  
    path('images/', include('Images.urls')),  # optional: if you have a home app
]
# The line `'django.contrib.admin',` in the `INSTALLED_APPS` setting in Django is adding the
# Django admin application to the list of installed apps in your project. This application
# provides a web-based interface for managing the project's data models, users, groups,
# permissions, and more. It allows administrators to interact with the project's data and make
# changes through a user-friendly interface without needing to write custom views or forms.

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
