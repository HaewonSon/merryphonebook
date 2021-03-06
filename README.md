# merryphonebook
Django를 활용한 웹 연락처 프로그램입니다.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy merryphonebook

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

## Deployment


###### 시작 페이지 
![main.png](capture/1_main.png)
<br>
<br>
###### 로그인 후 메인 페이지 
![1.5_phonebook.png](capture/2_phonebook.png)
<br>
<br>
###### 연락처 추가 
![3_addmember.png](capture/3_addmember.png)
<br>
<br>
###### '야옹이' 연락처 추가 완료 
![4_addOk.png](capture/4_addOk.png)
<br>
<br>
###### '야옹이'의 연락처 수정 
![5_update.png](capture/5_update.png)
<br>
<br>
###### '야옹이' 연락처 수정 완료 
![6_updateOk.png](capture/6_updateOk.png)
<br>
<br>
###### '꼬꼬'와 '소금이' 연락처 삭제 
![7_deleteOk.png](capture/7_deleteOk.png)
<br>
<br>
###### 로그아웃 
![8_logout.png](capture/8_logout.png)
<br>
<br>
###### 회원가입 
![9_signup.png](capture/9_signup.png)
<br>
<br>

###### 회원가입 후 자동 로그인 
![10_signupOk.png](capture/10_signupOk.png)
<br>
