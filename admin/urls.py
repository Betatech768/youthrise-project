from django.urls import path
from . import views

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
    

]
    
