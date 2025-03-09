from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
import logging

from vehicles.models import Vehicle
from maintenance.models import MaintenanceTask
from .serializers import VehicleSerializer, MaintenanceTaskSerializer

logger = logging.getLogger(__name__)

# Define filter classes
class VehicleFilter(filters.FilterSet):
    registration_number = filters.CharFilter(lookup_expr='icontains')
    make = filters.CharFilter(lookup_expr='icontains')
    model = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Vehicle
        fields = ['registration_number', 'make', 'model', 'year']

class MaintenanceTaskFilter(filters.FilterSet):
    registration_number = filters.CharFilter(
        field_name='vehicle__registration_number', lookup_expr='icontains'
    )
    task_type = filters.CharFilter(field_name='task_type', lookup_expr='icontains')
    status = filters.CharFilter(field_name='status', lookup_expr='icontains')

    class Meta:
        model = MaintenanceTask
        fields = ['vehicle__registration_number', 'task_type', 'status']


class VehicleListCreateView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = VehicleFilter
    
    def get(self, request):
        """Retrieve all vehicles with optional filtering"""
        logger.info("Fetching all vehicles")
        vehicles = Vehicle.objects.all()
        
        # Apply filters if any
        filtered_vehicles = self.filterset_class(request.GET, queryset=vehicles)
        serializer = VehicleSerializer(filtered_vehicles.qs, many=True)
        
        logger.info(f"{len(filtered_vehicles.qs)} vehicles retrieved")
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create a new vehicle"""
        logger.info("Creating a new vehicle")
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Vehicle created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Vehicle creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleDetailView(APIView):
    def get(self, request, pk):
        """Retrieve a single vehicle"""
        logger.info(f"Fetching vehicle with ID: {pk}")
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        """Update a vehicle"""
        logger.info(f"Updating vehicle with ID: {pk}")
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Vehicle with ID {pk} updated successfully")
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f"Vehicle update failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a vehicle"""
        logger.info(f"Deleting vehicle with ID: {pk}")
        vehicle = get_object_or_404(Vehicle, pk=pk)
        vehicle.delete()
        logger.info(f"Vehicle with ID {pk} deleted successfully")
        return Response({"message": "Vehicle deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class MaintenanceTaskListCreateView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = MaintenanceTaskFilter
    
    def get(self, request):
        """Retrieve all maintenance tasks with optional filtering"""
        logger.info("Fetching all maintenance tasks")
        tasks = MaintenanceTask.objects.all()
        
        # Apply filters if any
        filtered_tasks = self.filterset_class(request.GET, queryset=tasks)
        serializer = MaintenanceTaskSerializer(filtered_tasks.qs, many=True)
        
        logger.info(f"{len(filtered_tasks.qs)} maintenance tasks retrieved")
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create a new maintenance task"""
        logger.info("Creating a new maintenance task")
        serializer = MaintenanceTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Maintenance task created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Maintenance task creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaintenanceTaskDetailView(APIView):
    def get(self, request, pk):
        """Retrieve a specific maintenance task"""
        logger.info(f"Fetching maintenance task with ID: {pk}")
        task = get_object_or_404(MaintenanceTask, pk=pk)
        serializer = MaintenanceTaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        """Update a maintenance task"""
        logger.info(f"Updating maintenance task with ID: {pk}")
        task = get_object_or_404(MaintenanceTask, pk=pk)
        serializer = MaintenanceTaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Maintenance task with ID {pk} updated successfully")
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f"Maintenance task update failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a maintenance task"""
        logger.info(f"Deleting maintenance task with ID: {pk}")
        task = get_object_or_404(MaintenanceTask, pk=pk)
        task.delete()
        logger.info(f"Maintenance task with ID {pk} deleted successfully")
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)