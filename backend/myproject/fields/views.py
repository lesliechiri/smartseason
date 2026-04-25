from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Field, CropLog
from .serializers import FieldSerializer, CropLogSerializer
from .permissions import IsAdminOrReadOnly, IsAgentOfFieldOrAdmin, CanCreateLogForAssignedField


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated, IsAgentOfFieldOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Field.objects.all().prefetch_related('logs')

        return Field.objects.filter(agent=user).prefetch_related('logs')


    def perform_create(self, serializer):
        serializer.save()


    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, CanCreateLogForAssignedField])
    def logs(self, request, pk=None):
        field = self.get_object() 
        serializer = CropLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(field=field, created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DashboardStatsView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly] 

    def list(self, request):
        fields = Field.objects.all()
        breakdown = {'ACTIVE': 0, 'AT_RISK': 0, 'COMPLETED': 0}
        for f in fields:
            breakdown[f.status] += 1

        return Response({
            'total_fields': fields.count(),
            'status_breakdown': breakdown,
            'insights': {
                'overdue_fields': Field.objects.filter().count() 
            }
        })    





