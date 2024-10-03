from rest_framework.routers import DefaultRouter

from user.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = router.urls

app_name = "user"
