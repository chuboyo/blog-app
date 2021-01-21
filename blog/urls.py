from django.urls import path

from .views import BListView, BDetailView

urlpatterns = [
    path('', BListView.as_view(), name='home'),
    path('post/<int:pk>/', BDetailView.as_view(), name='post_detail' ),
]

