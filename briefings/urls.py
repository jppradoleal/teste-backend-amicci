from rest_framework.routers import DefaultRouter

from briefings.views import BriefingViewSet, CategoryViewSet

router = DefaultRouter()
router.register("briefings", BriefingViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = router.urls
