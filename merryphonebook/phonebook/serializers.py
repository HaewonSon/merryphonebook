# serializer : 데이터 명시
from rest_framework import serializers
from . import models
from merryphonebook.users.models import User as user_model
from merryphonebook.phonebook.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "categoryName"
        )

class PhonebookSerializer(serializers.ModelSerializer):
    # categoryName = CategorySerializer(many=True)
    class Meta:
        model = models.Phonebook
        fields = (
            "id",
            "memberName",
            "phoneNum",
            "address",
            "category_id",
            # "categoryName"
        )

