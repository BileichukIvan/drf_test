from rest_framework.routers import DefaultRouter
from team.views import TeamViewSet

router = DefaultRouter()
router.register(r"teams", TeamViewSet, basename="team")

urlpatterns = router.urls
