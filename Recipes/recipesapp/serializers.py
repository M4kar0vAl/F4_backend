from rest_framework import serializers

from .models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # needed for displaying human-readable value of difficulty choices
    difficulty = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        exclude = []

    def get_difficulty(self, obj):
        return obj.get_difficulty_display()
