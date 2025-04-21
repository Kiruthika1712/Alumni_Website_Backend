from django.shortcuts import render
from django.http import HttpRequest
from .models import OfficialAlumni, EventCategories, Events, NewsCategories, News, Blogs, Mentor, Mentee, Gallery
from .serializers import AlumniSerializer, EventCategoriesSerializer, EventsSerializer, NewsCategoriesSerializer, NewsSerializer, BlogsSerializer, MentorSerializer, MenteeSerializer, GallerySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def alumni_list(request: HttpRequest):

    if request.method =='GET':
        alumni_record = OfficialAlumni.objects.filter()
        serializer= AlumniSerializer(alumni_record, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        verify_data= request.data
        try:
            reg= verify_data['regno']
            print("------------test", reg)
            record = OfficialAlumni.objects.filter(regno=reg)
            serializer = AlumniSerializer(data=request.data)
            if serializer.is_valid():
                    # serializer.save()
                    return Response(serializer.data)
            else:
                print(serializer.data)
                return Response("oops")
        except Exception as e:
            print(e)
            return Response("ooo")
        
@api_view(['GET','POST'])
def event_categories_list(request: HttpRequest):

    if request.method =='GET':
        event_categories_list = EventCategories.objects.filter()
        serializer = EventCategoriesSerializer (event_categories_list, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def events_list(request: HttpRequest, id: int):

    if request.method =='GET':
        events_list = Events.objects.filter(event_category=id)
        serializer = EventsSerializer (events_list, many=True)
        return Response(serializer.data)
    
@api_view(['GET','POST'])
def events_list_home(request: HttpRequest):

    if request.method =='GET':
        events_list_home = Events.objects.filter()[:3]
        serializer = EventsSerializer (events_list_home, many=True)
        return Response(serializer.data) 

@api_view(['GET','POST'])
def news_categories_list(request: HttpRequest):

    if request.method =='GET':
        news_categories_list = NewsCategories.objects.filter()
        serializer = NewsCategoriesSerializer (news_categories_list, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def news_list(request: HttpRequest, id: int):

    if request.method =='GET':
        news_list = News.objects.filter(news_category=id)
        serializer = NewsSerializer (news_list, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def news_list_home(request: HttpRequest):

    if request.method =='GET':
        news_list_home = News.objects.filter()[:4]
        serializer = NewsSerializer (news_list_home, many=True)
        return Response(serializer.data) 

@api_view(['GET', 'POST'])
def blogs(request: HttpRequest):
    if request.method == 'GET':
        blogs_list = Blogs.objects.filter()
        serializer = BlogsSerializer(blogs_list, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def mentor(request: HttpRequest):
    if request.method == 'GET':
        mentor_list = Mentor.objects.filter()
        serializer = MentorSerializer(mentor_list, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    
@api_view(['GET', 'POST'])
def mentee(request: HttpRequest, id: int):
    if request.method == 'GET':
        mentee_list = Mentee.objects.filter(mentor_id = id)
        serializer = MenteeSerializer(mentee_list, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def gallery(request: HttpRequest):
    if request.method == 'GET':
        gallery_list = Gallery.objects.filter()
        serializer = GallerySerializer(gallery_list, many=True)
        return Response(serializer.data)