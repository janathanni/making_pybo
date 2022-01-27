from django.shortcuts import render, get_object_or_404
from.models import Question


# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date') #-가 붙으면 내림차순이당.
    context = {'question_list' : question_list,
                'name' : '홍길동'
    }

    return render(request, 'pybo/question_list.html', context)
#HttpResponse를 반환하는 게 render


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk = question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

