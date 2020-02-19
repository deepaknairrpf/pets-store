from rest_framework import routers
from .views import PetModelViewSet


router = routers.SimpleRouter()
router.register(r'pets', PetModelViewSet)
urlpatterns = router.urls
