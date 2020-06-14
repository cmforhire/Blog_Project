from django.urls import path, include
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    #int:pk is the primary key being displayed in int form
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
