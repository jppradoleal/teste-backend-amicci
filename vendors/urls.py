from rest_framework.routers import DefaultRouter

from vendors.views import VendorViewSet


router = DefaultRouter()
router.register("", VendorViewSet)

urlpatterns = router.urls
