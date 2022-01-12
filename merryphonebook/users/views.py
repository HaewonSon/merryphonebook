from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def main(request):

    # 페이지 요청
    if request.method == 'GET':
        return render(request, 'users/main.html')

    # 로그인
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # 로그인 성공
        if user is not None:
            login(request, user)
            # 연락처 메인 페이지 리턴
            return HttpResponseRedirect(reverse('phonebook:phonebook'))

        # 로그인 실패
        else:
            # 홈 메인 페이지 리턴
            return render(request, 'users/main.html')


def signup(request):

    if request.method == 'GET':
        form = SignUpForm
        return render(request, 'users/signup.html', {'form':form})

    elif request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            # 회원가입 후 자동 로그인

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            # 로그인 성공
            if user is not None:
                login(request, user)
                # 연락처 메인 페이지 리턴
                return HttpResponseRedirect(reverse('phonebook:phonebook'))

        # 회원가입 실패 : 홈 메인 페이지 리턴
        return render(request, 'users/main.html')


