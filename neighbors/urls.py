from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LedgerUpdateViewSet, LedgerUpdateFilteredViewSet

router = DefaultRouter()
router.register(r'ledgers', LedgerUpdateViewSet, basename='ledger')
router.register(r'ledgers-filtered', LedgerUpdateFilteredViewSet, basename='ledger-filtered')

urlpatterns = [
    path('', include(router.urls)),
]
