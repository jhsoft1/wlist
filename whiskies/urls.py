from django.urls import path
from .views import WhiskyListView, WhiskyDetailView, WhiskyUpdateView, WhiskyDeleteView, WhiskyCreateView

urlpatterns = [
    path('', WhiskyListView.as_view(), name="whisky_list"),
    path('create/', WhiskyCreateView.as_view(), name="whisky_create"),
    path('<int:pk>/', WhiskyDetailView.as_view(), name="whisky_detail"),
    path('<int:pk>/update/', WhiskyUpdateView.as_view(), name="whisky_update"),
    path('<int:pk>/delete/', WhiskyDeleteView.as_view(), name="whisky_delete"),
]