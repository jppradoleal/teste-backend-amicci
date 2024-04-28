from rest_framework.routers import DefaultRouter

from retailers.views import RetailerViewSet, ListRetailersViewSet

router = DefaultRouter()
router.register("retailer", RetailerViewSet, basename='retailer')
router.register("retailers", ListRetailersViewSet, basename='retailers')

urlpatterns = router.urls
