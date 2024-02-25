from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path("", views.index, name='index'),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),  # Changed name to "post_detail"
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('contactus', views.contact, name = 'contactus')
]
