from rest_framework.routers import DefaultRouter

from retailers.views import RetailerViewSet

router = DefaultRouter()
router.register('', RetailerViewSet)

urlpatterns = router.urls
