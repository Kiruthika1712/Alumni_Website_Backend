from rest_framework import serializers
from .models import OfficialAlumni, EventCategories, Events, NewsCategories, News, Blogs, Mentor, Mentee, Gallery, NonMonetaryContribution, LetterOfRecommendation, ClassNote


class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialAlumni
        fields = ["regno", "studentname", "mobile", "batchid"]


# 22352001


class EventCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategories
        fields = "__all__" 


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class NewsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategories
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class BlogsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Blogs
        fields = ['id', 'title', 'description', 'content', 'image_url', 'created_at', 'author', 'username']


    class Meta:
        model = Blogs
        fields = ['id', 'title', 'description', 'content', 'image_url', 'created_at', 'author', 'username']
class MentorSerializer(serializers.ModelSerializer):
    mentor_user_name = serializers.CharField(source='user_id.username', read_only=True)
    approver_name = serializers.CharField(source='approved_by.username', read_only=True)

    class Meta:
        model = Mentor
        fields = [
            'id', 
            'industry', 
            'role', 
            'company', 
            'guidance_areas', 
            'contact_method', 
            'availability', 
            'linkedin', 
            'is_verified', 
            'created_at', 
            'mentor_user_name', 
            'approver_name'
        ]


class MentorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "__all__"

class MenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentee
        fields = "__all__"

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"
        
class NonMonetaryContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonMonetaryContribution
        fields = '__all__'

class LetterOfRecommendationSerializer(serializers.ModelSerializer):
    date_submitted = serializers.ReadOnlyField()

    class Meta:
        model = LetterOfRecommendation
        fields = ['id', 'role', 'template', 'name', 'recommender_name', 'recommender_title', 
                  'academic_performance', 'work_experience', 'skills', 'projects', 
                  'areas_of_contribution', 'achievements', 'purpose', 'date_submitted', 'user_id']
class ClassNoteSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)  # Show username of the related user
    alumni_id = serializers.CharField(source='user.alumni_id', read_only=True)  # Show alumni_id of the related user
    email = serializers.EmailField(source='user.email', read_only=True)  # Show email of the related user

    class Meta:
        model = ClassNote
        fields = ['id', 'title', 'category', 'description', 'attachment', 'user_name', 'alumni_id', 'email', 'status']