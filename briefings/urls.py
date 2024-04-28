from rest_framework.routers import DefaultRouter

from briefings.views import (
    BriefingViewSet,
    CategoryViewSet,
    ListBriefingsViewSet,
    ListCategoriesViewSet,
)

router = DefaultRouter()
router.register("briefing", BriefingViewSet, basename='briefing')
router.register("category", CategoryViewSet, basename='category')
router.register("briefings", ListBriefingsViewSet, basename='briefings')
router.register("categories", ListCategoriesViewSet, basename='categories')

urlpatterns = router.urls
