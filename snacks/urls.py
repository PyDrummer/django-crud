from django.urls import path
from .views import HomePageView, SnackDetailView, SnackCreateView, SnackDeleteView, SnackUpdateView
 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_details'),
    path('new/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/edit', SnackUpdateView.as_view(), name='snack_update'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='snack_delete'),
]
