from .models import Skill
from rest_framework import serializers
# Serializer to create JSON data from Skill client
class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id','skill', 'description']