from rest_framework.viewsets import ModelViewSet
from .serializers import MenuSerializer,CategorySerializer,TableSerializer,OrderSerializer
from .models import MenuItem,Category,Table,Order,OrderItem
from rest_framework.permissions import IsAdminUser


class MenuViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminUser,)

    def get_permissions(self):
        if self.action == 'list':
            return []
        else:
            return [permission() for permission in self.permission_classes]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer




