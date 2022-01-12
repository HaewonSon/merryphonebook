from django.urls import path
from . import views

app_name = "phonebook"
urlpatterns = [
    path('', views.phonebook, name='phonebook'),
    path('create/', views.member_create, name='member_create'), # 연락처 추가 페이지
    path('<int:phonebook_id>/update/', views.member_update, name='member_update'), # 연락처 수정
    path('<int:phonebook_id>/delete/', views.member_delete, name='member_delete'), # 연락처 삭제
]
