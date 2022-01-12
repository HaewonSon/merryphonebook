from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from merryphonebook.users import models as user_model


class NumberModel():
    memberNumber = models.AutoField(primary_key=True)


class Category(models.Model):
    # CategoryChoices = [
    #     ('01', '가족'),
    #     ('02', '친구'),
    #     ('03', '회사'),
    #     ('04', '기타')
    # ]
    # categoryId = models.CharField(primary_key=True, blank=False, max_length=255)
    categoryName = models.CharField(primary_key=True, blank=False, max_length=255)


class Phonebook(models.Model,NumberModel):
    author = models.ForeignKey(
        user_model.User,
        null=False,
        on_delete=models.CASCADE,  # 외래키를 갖는 유저가 삭제되면 어떻게 처리될것인지 명시
        related_name='phonebook_author'
    )
    memberName = models.CharField(blank=True, max_length=255)
    phoneNum = models.CharField(blank=False, max_length=11)
    address = models.CharField(blank=True, max_length=255)
    category = models.ForeignKey(
        Category,
        null=False,
        on_delete=models.CASCADE,
        related_name='phonebook_category'
    )
    # userNumber = models.ForeignKey(user_model.User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} : {self.memberName}, {self.phoneNum}, {self.address}"
