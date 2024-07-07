from rest_framework import routers
from .api import RecipeViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = []

urlpatterns += router.urls
