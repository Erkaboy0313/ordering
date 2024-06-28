from rest_framework.routers import DefaultRouter
from .views import MenuViewSet



router = DefaultRouter()

router.register(r"menu",MenuViewSet,basename='menu')








