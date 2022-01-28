from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from.models import Question, Answer
from django.utils import timezone

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date') #-가 붙으면 내림차순이당.
    total_count = Question.objects.count
    context = {'question_list' : question_list,
                'total_count' : total_count,
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

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    content = request.POST.get('content')

    #방법1
    # answer = Answer(question = question, 
    #                 content = content,
    #                 create_date = timezone.now())
    
    # answer.save()

    #방법2 Foreignkey 관계인 경우

    question.answer_set.create(content = content, create_date = timezone.now())

    return redirect('pybo:detail', question_id = question.id)