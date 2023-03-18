from django.urls import path
from rest_framework.routers import DefaultRouter
from neighbors import views


router = DefaultRouter()
router.register('volunteer_users', views.VolunteerUsersViewSet)
router.register('update', views.UpdateViewSet)
router.register('profile', views.ProfileViewSet)
router.register('transactions_hash', views.TrxsHashViewSet)
router.register('transactions', views.TransactionsViewSet)

urlpatterns = []

urlpatterns += router.urls
