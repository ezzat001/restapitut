from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset',ArticleViewSet)
urlpatterns = [
    #path('article' ,article_list),
    #path('detail/<int:pk>/',article_detail),
    path('article', ArticleAPIView.as_view()),
    path('generic/<int:id>/',GenericAPIView.as_view()),
    path('detail/<int:id>/',ArticleDetails.as_view()),
    path('',include(router.urls)),
    path('<int:id>',include(router.urls)),

]
