from rest_framework import viewsets, mixins

from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer


class RecipeViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__id=category)
        return queryset


class CategoryViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
