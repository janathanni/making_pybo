from django.urls import path
from .views import index, detail, answer_create #현재 패키지의 views 모듈

app_name = 'pybo' 

urlpatterns = [
    path('', index, name = 'index'), #views 모듈의 index 함수
    path('<int:question_id>/', detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_create, name='answer_create')
]