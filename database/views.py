from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response
from .models import *

# Create your views here.

def home(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies':companies})

def company(request, slug):
    company = Company.objects.get(slug=slug)
    years = Year.objects.all()
    paper_years = []
    for year in years:
        if Question.objects.filter(company=company,date=year):
            paper_years.append(year)
    return render(request, 'company.html',{'company': company, 'paper_years':paper_years, 'slug':slug})

def topic(request, slug):
    topic = Topic.objects.get(slug=slug)
    return render(request, 'topic.html',{'topic':topic})

def sub_topic(request, topic, sub_topic):
    topic = Topic.objects.get(slug=topic)
    subtopic = topic.subtopics.get(slug=sub_topic)
    questions = subtopic.questions.filter(reference=None)
    no_of_items = 10
    if 'passage-correction' == sub_topic:
        no_of_items = 3
    paginator = Paginator(questions, no_of_items) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
        request.GET = request.GET.copy()
        request.GET['page']=1
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    test=[(subtopic,questions)]
    dictctionary =  {'test':test,'slug':topic,'paginator':paginator}
    return render(request, 'subtopic.html', dictctionary)

def interview(request):
    topic = Topic.objects.get(slug='interview')
    subtopic = topic.subtopics.get(slug='interview')
    questions = subtopic.questions.all()
    paginator = Paginator(questions, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
        request.GET = request.GET.copy()
        request.GET['page']=1
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    test=[(subtopic,questions)]
    dictctionary =  {'test':test,'slug':topic,'paginator':paginator}
    return render(request, 'interview.html', dictctionary)

def company_test_start(request,slug,date_slug):
    questions = Question.objects.filter(company__slug=slug, date=Year.objects.get(date=date_slug))
    test=[]
    for topic in Topic.objects.all().exclude(slug='interview'):
        test.append((topic, questions.filter(sub_topic__in=topic.subtopics.all())))
    dictctionary =  {'test':test,'slug':slug, 'date_slug':date_slug}
    return render(request, 'add_question.html', dictctionary)

def company_test_view(request,slug,date_slug):
    questions = Question.objects.filter(company__slug=slug, date=Year.objects.get(date=date_slug))
    test=[]
    for topic in Topic.objects.all().exclude(slug='interview'):
        test.append((topic, questions.filter(sub_topic__in=topic.subtopics.all())))
    return render(request, 'add_question.html', {'test':test,'slug':slug,'view_test':True,'date_slug':date_slug})

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def handler404(request):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def robot(request):
    return render_to_response("robots.txt",content_type="text")

def sitemap(request):
    return render_to_response("sitemap.xml",content_type="text/xml")

def google_verification(request):
    return render_to_response("googlea95613a6b3c4ff8a.html", content_type="text/html")
