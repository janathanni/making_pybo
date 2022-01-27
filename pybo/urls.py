from django.urls import path
from . import views #현재 패키지의 views 모듈

urlpatterns = [
    path('', views.index), #views 모듈의 index 함수
    path('<int:question_id>', views.detail)
]