from django.db import models
from random import random

QLEVEL = (
    ('L1', 'LEVEL1'),
    ('L2', 'LEVEL2'),
    ('L3', 'LEVEL3'),
)


def url(self, filename):
    print self.question
    return "%s/%s" % (self.question, filename)


class Year(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)


class Company(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    ceo = models.CharField(max_length=50, blank=True, null=True)
    founded = models.ForeignKey(Year, blank=True)
    founders = models.CharField(max_length=50, blank=True, null=True)
    headquarters = models.CharField(max_length=50, blank=True, null=True)
    about = models.CharField(max_length=1000, null=True)
    history = models.CharField(max_length=1000, null=True)
    why_join = models.CharField(max_length=1000, null=True)
    def __str__(self):
        return self.name

    # def founded(self):
    #     return self.founded

class Topic(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, related_name='subtopics')
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    data = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to=url, blank=True, null=True)
    company = models.ManyToManyField(Company, blank=True)
    sub_topic = models.ForeignKey(SubTopic,related_name='questions')
    level = models.CharField(choices=QLEVEL, max_length=10)
    reference = models.ForeignKey('self', null=True, blank=True, related_name='linked_questions')
    date = models.ManyToManyField(Year)

    def __str__(self):
        return str(self.sub_topic.topic)


class Choice(models.Model):
    description = models.CharField(max_length=100)
    question = models.ForeignKey(Question, related_name='choices')
    image = models.ImageField(upload_to=url, blank=True, null=True)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)


class Answer(models.Model):
    explination = models.CharField(max_length=2000)
    image = models.ImageField(upload_to=url, blank=True, null=True)
    question = models.ForeignKey(Question, related_name='answers')

    def __str__(self):
        return str(self.question)
