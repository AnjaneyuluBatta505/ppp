from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .models import *
from django.conf import settings

# Create your views here.


def get_base_url(request):
    return "https://" + request.META["HTTP_HOST"]


def home(request):
    companies = Company.objects.all()
    context = {
        "companies": companies,
        "base_url": get_base_url(request)
    }
    return render(request, "home.html", context)


def company(request, slug):
    company = Company.objects.get(slug=slug)
    years = Year.objects.all()
    paper_years = []
    for year in years:
        if Question.objects.filter(company=company, date=year):
            paper_years.append(year)
    context = {
        "company": company,
        "paper_years": paper_years,
        "slug": slug,
        "base_url": get_base_url(request)
    }
    return render(request, "company.html", context)


def topic(request, slug):
    topic = Topic.objects.get(slug=slug)
    context = {
        "topic": topic,
        "base_url": get_base_url(request)
    }
    return render(request, "topic.html", context)


def reading_topic(request, slug):
    topic = Topic.objects.get(slug=slug)
    context = {
        "topic": topic,
        "base_url": get_base_url(request),
    }
    return render(request, "reading_topic.html", context)


def reading_sub_topic(request, topic, sub_topic):
    sub_topic = SubTopic.objects.get(slug=sub_topic)
    context = {
        "subtopic": sub_topic,
        "base_url": get_base_url(request),
        "slug": topic,
    }
    return render(request, "reading_subtopic.html", context)


def sub_topic(request, topic, sub_topic):
    topic = Topic.objects.get(slug=topic)
    subtopic = topic.subtopics.get(slug=sub_topic)
    questions = subtopic.questions.filter(reference=None)
    no_of_items = 10
    if "passage-correction" == sub_topic:
        no_of_items = 3
    elif "reading-comprehention" == sub_topic:
        no_of_items = 1
    elif "cubes-and-dices" == sub_topic:
        no_of_items = 5

    paginator = Paginator(questions, no_of_items)
    page = request.GET.get("page")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
        request.GET = request.GET.copy()
        request.GET["page"] = 1
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    start = int(request.GET["page"]) - 5
    end = int(request.GET["page"]) + 5
    if start < 0:
        start = 0
    elif end > paginator.num_pages:
        end = paginator.num_pages
    pages = list(paginator.page_range)[start: end]
    test = [(subtopic, questions)]
    context = {
        "test": test,
        "slug": topic,
        "paginator": pages,
        "sub_topic": sub_topic,
        "base_url": get_base_url(request)
    }
    return render(request, "subtopic.html", context)


def interview(request):
    topic = Topic.objects.get(slug="interview")
    subtopic = topic.subtopics.get(slug="interview")
    questions = subtopic.questions.all()
    paginator = Paginator(questions, 10)
    page = request.GET.get("page")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
        request.GET = request.GET.copy()
        request.GET["page"] = 1
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    start = int(request.GET["page"]) - 5
    end = int(request.GET["page"]) + 5
    if start < 0:
        start = 0
    elif end > paginator.num_pages:
        end = paginator.num_pages
    pages = list(paginator.page_range)[start: end]
    test = [(subtopic, questions)]
    context = {
        "test": test,
        "slug": topic,
        "paginator": pages,
        "sub_topic": sub_topic,
        "base_url": get_base_url(request)
    }
    return render(request, "interview.html", context)


def technical(request, topic, sub_topic):
    topic = Topic.objects.get(slug=topic)
    subtopic = topic.subtopics.get(slug=sub_topic)
    questions = subtopic.questions.all()
    paginator = Paginator(questions, 10)
    page = request.GET.get("page")
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
        request.GET = request.GET.copy()
        request.GET["page"] = 1
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    start = int(request.GET["page"]) - 5
    end = int(request.GET["page"]) + 5
    if start < 0:
        start = 0
    elif end > paginator.num_pages:
        end = paginator.num_pages
    pages = list(paginator.page_range)[start: end]
    test = [(subtopic, questions)]
    context = {
        "test": test,
        "slug": topic,
        "paginator": pages,
        "sub_topic": sub_topic,
        "base_url": get_base_url(request)
    }
    return render(request, "subtopic.html", context)


def company_test_start(request, slug, date_slug):
    questions = Question.objects.filter(
        company__slug=slug, date=Year.objects.get(date=date_slug), reference=None)
    test = []
    for topic in Topic.objects.all().exclude(slug="interview"):
        test.append(
            (topic, questions.filter(sub_topic__in=topic.subtopics.all())))
    context = {
        "test": test,
        "slug": slug,
        "date_slug": date_slug,
        "base_url": get_base_url(request)
    }
    return render(request, "company_test.html", context)


def company_test_view(request, slug, date_slug):
    questions = Question.objects.filter(
        company__slug=slug, date=Year.objects.get(date=date_slug), reference=None)
    test = []
    for topic in Topic.objects.all().exclude(slug="interview"):
        test.append(
            (topic, questions.filter(sub_topic__in=topic.subtopics.all()))
        )
    context = {
        "test": test,
        "slug": slug,
        "view_test": True,
        "date_slug": date_slug,
        "base_url": get_base_url(request)
    }
    return render(request, "company_test.html", context)


def privacy_policy(request):
    return render(request, "privacy-policy.html")


def handler404(request):
    response = render("404.html", context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response("500.html", context_instance=RequestContext(request))
    response.status_code = 500
    return response


def robot(request):
    return render_to_response("robots.txt", content_type="text")


def sitemap(request):
    import os.path
    import time
    import datetime
    filedb = settings.BASE_DIR + "/static/db.sqlite3"
    # modified = datetime.datetime.strptime(time.ctime(os.path.getmtime(filedb)), "%a %b %d %H:%M:%S %Y")
    modified = datetime.datetime.now() - datetime.timedelta(days=1)
    created = datetime.datetime.strptime(
        time.ctime(os.path.getctime(filedb)), "%a %b %d %H:%M:%S %Y")
    data = {
        "topics": Topic.objects.all(),
        "companies": Company.objects.all(),
        "paginate_len": range(2, 11),
        "created": created,
        "modified": modified,
        "base_url": get_base_url(request)
    }
    return render_to_response("sitemap.xml", data, content_type="text/xml")


def google_verification(request):
    return render_to_response("googlea95613a6b3c4ff8a.html", content_type="text/plain")


def bing_verification(request):
    return render_to_response("BingSiteAuth.xml", content_type="text/html")
