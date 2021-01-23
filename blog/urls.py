from django.urls import path

from .views import BListView, BDetailView, BCreateView, BUpdateView, BDeleteView

urlpatterns = [
    path('', BListView.as_view(), name='home'),
    path('post/<int:pk>/', BDetailView.as_view(), name='post_detail' ),
    path('post/new/', BCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BDeleteView.as_view(), name='post_delete'),
]

