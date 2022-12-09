from django.urls import path
from . import views

app_name='blog'

#'' -> http://127.0.0.1:8000/blog/
# urlpatterns에 add/만 해주면 됨. '' -> blog까지를 뜻함

urlpatterns=[
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]