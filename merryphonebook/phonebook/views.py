from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from merryphonebook.users.models import User as user_model
from merryphonebook.phonebook.models import Phonebook, Category
from django.urls import reverse
from . import models
from .forms import CreateMemberForm
from . import models, serializers

def phonebook(request):
    if request.method == 'GET':
        if request.user.is_authenticated:

            user = get_object_or_404(user_model, pk=request.user.id)
            phonebook = models.Phonebook.objects.filter(Q(author=user))

            phonebook_serializer = serializers.PhonebookSerializer(phonebook, many=True)

            return render(
                request,
                'phonebook/phonebook.html',
                {"phonebook":phonebook_serializer.data},
            )


def member_create(request):
    if request.method == 'GET': # 사용자의 페이지 요청
        form = CreateMemberForm()
        return render(request, 'phonebook/member_create.html', {"form":(form)}) # 연락처 생성 페이지 리턴

    elif request.method == 'POST':
        if request.user.is_authenticated:

            user = get_object_or_404(user_model, pk=request.user.id)
            phonebook = models.Phonebook.objects.filter(Q(author=user))
            phonebook_serializer = serializers.PhonebookSerializer(phonebook, many=True)

            # 연락처 생성 로직
            user = get_object_or_404(user_model, pk=request.user.id) # 로그인된 작성자
            member_name = request.POST['memberName'] # 연락처에 저장할 이름
            phone_number = request.POST['phoneNum']
            address = request.POST['address']
            category = request.POST['category']
            # category = Phonebook.objects.get(request.POST['category'],pk=request.user.id)


            new_post = models.Phonebook.objects.create(
                author = user,
                memberName = member_name,
                phoneNum = phone_number,
                address = address,
                category = Category.objects.get(categoryName=category) # django ORM 참고
            )
            # 연락처 저장
            new_post.save()
            # phonebook 메인 페이지로 리턴
            return render(request, 'phonebook/phonebook.html', {"phonebook":phonebook_serializer.data})

        else : # 로그인 되어있지 않은 경우
            return render(request, 'users/main.html')

def member_update(request, phonebook_id):

    if request.user.is_authenticated:
        # 작성자 체크
        phonebook = get_object_or_404(models.Phonebook, pk=phonebook_id)
        if request.user != phonebook.author:
            return redirect(reverse('phonebook:phonebook'))

        # GET 요청
        if request.method == 'GET':
            form = CreateMemberForm(instance=phonebook)
            return render(
                request,
                'phonebook/member_update.html',
                {"form":form, "phonebook":phonebook}
            )

        elif request.method == 'POST':
            # 업데이트 버튼 클릭 후 저장을 위한 POST api 요청 로직
            form = CreateMemberForm(request.POST)
            if form.is_valid():
                phonebook.memberName = form.cleaned_data['memberName']
                phonebook.phoneNum = form.cleaned_data['phoneNum']
                phonebook.address = form.cleaned_data['address']
                phonebook.category = form.cleaned_data['category']
                phonebook.save()

            return redirect(reverse('phonebook:phonebook'))
    else:
        return render(request, 'users/main.html')


def member_delete(request, phonebook_id):
    if request.user.is_authenticated:
        phonebook = get_object_or_404(models.Phonebook, pk=phonebook_id)
        if request.user == phonebook.author:
            phonebook.delete()
        return redirect(reverse('phonebook:phonebook'))

    else:
        return render(request, 'user/main.html')
