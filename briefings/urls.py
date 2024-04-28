from rest_framework.routers import DefaultRouter

from briefings.views import BriefingViewSet, CategoryViewSet

router = DefaultRouter()
router.register("briefing", BriefingViewSet)
router.register("category", CategoryViewSet)

urlpatterns = router.urls
