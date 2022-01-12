from django import forms
from .models import Phonebook, Category

class CreateMemberForm(forms.ModelForm):
    class Meta:
        model = Phonebook
        fields = ["memberName","phoneNum","address","category"]

        labels = {
            "memberName":"이름",
            "phoneNum":"전화번호",
            "address":"주소(ex:제주도)",
            "category":"카테고리"
        }



