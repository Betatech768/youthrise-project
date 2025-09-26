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
    path("export-registrations/", views.export_registrations_excel, name="export_registrations"),
    path("contact-messages/", views.contact_messages, name="contact_messages"),
    path("newsletter-registrations/", views.newsletter_registrations, name="newsletter_registration"),
    path("export-newsletters/", views.export_newsletters_excel, name="export_newsletters"),
    path("export-exhibitions/", views.export_exhibitions_excel, name="export_exhibitions"),
    path("export-sponsors/", views.export_sponsors_excel, name="export_sponsors"),
    path("streaming/", views.streaming, name="streaming"),
    path("streaming/delete-streaming/<int:pk>/", views.delete_stream, name="delete-streaming"),
    path("stories-list/", views.story_list, name="stories-list"),
    path("export-stories/", views.export_stories_excel, name="export_stories_excel"),
    path("clear-sponsors/", views.clear_model, name="clear_sponsors"),
    path("clear-registrations/", views.clear_registration_model, name="clear_registrations"),
    path("clear-impactstories/", views.clear_impactstories_model, name="clear_impactstories"),
    path("clear-exhibitions/", views.clear_exhibition_model, name="clear_exhibitions"),
    path("conferencedate/", views.conferencedate, name="conferencedate"),
    path("conferencevenue/", views.conferencevenue, name="conferencevenue"),
    path("viewingday/", views.viewingday, name="viewingday"),
    path("viewingday/delete-viewingday/<int:pk>/", views.delete_viewingday, name="delete_viewingday"),
    path("conferencedate/delete-conferenceday/<int:pk>/", views.delete_conferenceday, name="delete_conferenceday"),
    path("conferencevenue/delete-conferencevenue/<int:pk>/", views.delete_conferencevenue, name="delete_conferencevenue"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
