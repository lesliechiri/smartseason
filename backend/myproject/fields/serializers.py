from rest_framework import serializers
from .models import Field, CropLog

class CropLogSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CropLog
        fields = ['id', 'date', 'growth_stage', 'notes', 'created_by']



class FieldSerializer(serializers.ModelSerializer):
    agent = serializers.StringRelatedField()
    agent_id = serializers.IntegerField(write_only=True, required=False)
    current_stage = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    logs = CropLogSerializer(many=True, read_only=True)

    class Meta:
        model = Field
        fields = ['id', 'name', 'crop_type', 'planting_date', 'agent', 'agent_id','current_stage', 'status', 'logs']
                   