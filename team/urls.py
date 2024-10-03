from rest_framework.routers import DefaultRouter
from team.views import TeamViewSet

router = DefaultRouter()
router.register("teams", TeamViewSet)

urlpatterns = router.urls

app_name = "team"
