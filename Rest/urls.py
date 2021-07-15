from django.urls import path, include
# from .views import article_list, article_detail
from .views import ArticleListAPIView, ArticleDetailAPIView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    # path('article/', article_list, name='article_list'),
    # path('detail/<int:pk>/', article_detail, name='article_detail'),
    path('article/', ArticleListAPIView.as_view(), name='article_list'),
    path('detail/<int:id>/', ArticleDetailAPIView.as_view(), name='article_detail'),
    path('generic-article/<int:id>/', GenericAPIView.as_view(), name='generic_article'),
]