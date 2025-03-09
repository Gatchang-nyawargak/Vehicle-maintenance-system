from django.urls import path
from .views import (
    VehicleListCreateView, VehicleDetailView,
    MaintenanceTaskListCreateView, MaintenanceTaskDetailView
)

urlpatterns = [

    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    
  
    path('tasks/', MaintenanceTaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', MaintenanceTaskDetailView.as_view(), name='task-detail'),
]