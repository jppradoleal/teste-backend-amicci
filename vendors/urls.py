from rest_framework.routers import DefaultRouter

from vendors.views import ListVendorsViewSet, VendorViewSet

router = DefaultRouter()
router.register("vendor", VendorViewSet, basename="vendor")
router.register("vendors", ListVendorsViewSet, basename="vendors")

urlpatterns = router.urls
