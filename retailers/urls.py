from rest_framework.routers import DefaultRouter

from retailers.views import ListRetailersViewSet, RetailerViewSet

router = DefaultRouter()
router.register("retailer", RetailerViewSet, basename="retailer")
router.register("retailers", ListRetailersViewSet, basename="retailers")

urlpatterns = router.urls
