from django.urls import path
from rest_framework.routers import DefaultRouter
from activity import views


router = DefaultRouter()
router.register('update', views.UpdateViewSet)



urlpatterns = []

urlpatterns += router.urls
