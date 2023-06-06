from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FollowUserView,
                    IngredientViewSet,
                    RecipeViewSet,
                    SubscriptionsView,
                    TagViewSet)

router = DefaultRouter()
router.register('tags', TagViewSet, basename='tags')
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('ingredients', IngredientViewSet, basename='ingredients')


urlpatterns = [
    path('users/subscriptions/', SubscriptionsView.as_view()),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
    path('users/<int:id>/subscribe/', FollowUserView.as_view()),
]
