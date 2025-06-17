from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Team, TeamCategory, CustomUser

User = get_user_model()

class TeamCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCategory
        fields = ['id', 'name']


class TeamSerializer(serializers.ModelSerializer):
    category = TeamCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=TeamCategory.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Team
        fields = ['id', 'name', 'category', 'category_id']


class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(), source='team', write_only=True, allow_null=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'team', 'team_id']

class CustomUserSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)
    team_category = serializers.CharField(source='team.category.name', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'team', 'team_name', 'team_category']
        read_only_fields = ['id', 'team_name', 'team_category']