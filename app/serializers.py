from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers
from parler_rest.fields import TranslatedFieldsField
from .models import MenuItem,Category,Table



class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    pass

    def create(self, validated_data):
        return super().create(validated_data)

class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = Category)

    class Meta:
        model = Category
        fields = '__all__'

class MenuSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model = MenuItem)
    category = CategorySerializer(read_only = True)

    class Meta:
        model = MenuItem
        fields = "__all__"




