from atexit import register
from django.urls import path
from .views import about, category_detail, category_list, contact, post_list, post_detail, post_create, post_edit, post_delete

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:post_id>/edit/', post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', post_delete, name='post_delete'),
]


urlpatterns += [
    path('register/', register, name='register'),
]


urlpatterns += [
    path('categories/', category_list, name='category_list'),
]
# blog/urls.py

urlpatterns += [
    path('category/<int:category_id>/', category_detail, name='category_detail'),
]
urlpatterns += [
    path('about/', about, name='about'),
]
# blog/urls.py

urlpatterns += [
    path('contact/', contact, name='contact'),
]
