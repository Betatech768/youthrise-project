from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # The line `# path('', views.admin, name='admin_page'),` is a commented-out line of code in a
    # Django urlpatterns list. This means that it is not currently active or being used by the Django
    # application.
    path('', views.admin, name='admin_page'),
    path('blog/', views.create_and_list_blog_posts, name='blog_post'),
    path('edit_post/<int:post_id>/', views.edit_blog_post, name='edit_post'),
    path('edit_speaker/<int:speaker_id>/', views.edit_speaker, name='edit_speaker'),
    path('create_speaker/', views.create_speaker, name='create_speaker'),
    path('delete_speaker/<int:speaker_id>/', views.delete_speaker, name='delete_speaker'),
    path('delete/<int:post_id>/', views.delete_blog_post, name='delete_post'),
    path('sponsors-list', views.sponsors_list_view, name='sponsors_list'),
    path('exhibition-list/', views.exhibition_list_view, name='exhibition_list'),
    path('registration-list/', views.registration_list_view, name='registration_list'),
    # path('gallery-success/', views.gallery_success, name='gallery_success'),
    path('speaker-success/', views.speaker_success, name='speaker_success'),
    path('blog-success/', views.blog_success, name='blog_success'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('documents/', views.upload_document, name='document_list'),
    path('programme/delete/<int:pk>/', views.delete_document, name='delete_document'),
    path("sponsors-image/", views.sponsors_manage, name="sponsorsimage_list"),
    path("sponsors-image/delete/<int:pk>/", views.delete_sponsor, name="delete_sponsor"),
    path("update-package-list/delete/<int:pk>/", views.delete_sponsor_package, name="delete_sponsor_package"),
    path('update-package-list/', views.update_package, name='package_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
