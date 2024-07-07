from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import extend_schema


class Fix1(OpenApiViewExtension):
    target_class = 'recipesapp.api.RecipeViewSet'

    def view_replacement(self):
        @extend_schema(tags=['Recipe'])
        class Fixed(self.target_class):
            @extend_schema(description='Get list of all recipes')
            def list(self, request, *args, **kwargs):
                return super().list(request, *args, **kwargs)

            @extend_schema(description='Get recipe instance by id')
            def retrieve(self, request, *args, **kwargs):
                return super().retrieve(request, *args,**kwargs)

        return Fixed


class Fix2(OpenApiViewExtension):
    target_class = 'recipesapp.api.CategoryViewSet'

    def view_replacement(self):
        @extend_schema(tags=['Category'])
        class Fixed(self.target_class):
            @extend_schema(description='Get list of all categories')
            def list(self, request, *args, **kwargs):
                return super().list(request, *args, **kwargs)

        return Fixed
