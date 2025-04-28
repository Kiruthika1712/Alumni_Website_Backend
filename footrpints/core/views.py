from django.shortcuts import render
from django.http import HttpRequest
from .models import OfficialAlumni, EventCategories, Events, NewsCategories, News, Blogs, Mentor, Mentee, Gallery, NonMonetaryContribution, LetterOfRecommendation, ClassNote
from .serializers import AlumniSerializer, EventCategoriesSerializer, EventsSerializer, NewsCategoriesSerializer, NewsSerializer, BlogsSerializer, MentorSerializer, MenteeSerializer, GallerySerializer, NonMonetaryContributionSerializer, LetterOfRecommendationSerializer, ClassNoteSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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
        # Fetch all mentors and include related user data
        mentor_list = Mentor.objects.all()
        serializer = MentorSerializer(mentor_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Ensure that user_id and approved_by fields are provided
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
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
    
@api_view(['GET', 'POST'])
def non_monetary_contribution(request):
    if request.method == 'GET':
        contributions = NonMonetaryContribution.objects.all()
        serializer = NonMonetaryContributionSerializer(contributions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NonMonetaryContributionSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():
            serializer.save()  # Save the valid data to the database
            return Response(serializer.data, status=201)  # Return the serialized object
        return Response(serializer.errors, status=400)  # Return validation errors

@api_view(['GET', 'POST'])
def letter_of_recommendation(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        try:
            lors = LetterOfRecommendation.objects.filter(user_id=request.user)
            if not lors:
                return Response({'message': 'No letters of recommendation found for this user.'}, status=status.HTTP_200_OK)
            serializer = LetterOfRecommendationSerializer(lors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            serializer = LetterOfRecommendationSerializer(data=request.data)
            if serializer.is_valid():
                # Save with the user_id from the authenticated user
                serializer.save(user_id=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def class_note(request):
    if request.method == 'GET':
        notes = ClassNote.objects.all()
        serializer = ClassNoteSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClassNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user_name=request.user.username,
                alumni_id=request.user.alumni_id,  # Assuming user model has alumni_id
                email=request.user.email
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)