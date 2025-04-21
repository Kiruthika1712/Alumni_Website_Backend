from rest_framework import serializers
from .models import OfficialAlumni, EventCategories, Events, NewsCategories, News, Blogs, Mentor, Mentee, Gallery


class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialAlumni
        fields = ["regno", "studentname", "mobile", "batchid"]


# 22352001


class EventCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategories
        # fields =['regno','studentname','mobile','batchid']
        fields = "__all__"  # to get all fields from the model


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
    class Meta:
        model = Blogs
        fields = "__all__"

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "__all__"

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
        