from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Batches(models.Model):
    batchid = models.PositiveIntegerField(
        db_column='batchId',
        validators=[MinValueValidator(4),MaxValueValidator(7)],
        primary_key=True
    ) 
    coursename = models.CharField(db_column='courseName', blank=True, null=True, max_length=15)  
    joinyear = models.IntegerField(
        db_column='joinYear',
        blank=True,
        null=True,
        validators=[MinValueValidator(4),MaxValueValidator(7)]
    ) 
    endyear = models.IntegerField(
        db_column='endYear',
        blank=True,
        null=True,
        validators=[MinValueValidator(4),MaxValueValidator(7)]
    )
    class Meta:
        db_table = 'batches'

    def __str__(self):
        return f'{self.batchid}'

class OfficialAlumni(models.Model):
    regno = models.PositiveIntegerField(
        db_column='regNo',
        primary_key=True,
        validators=[MinValueValidator(4),MaxValueValidator(4)]
    )  
    studentname = models.CharField(db_column='studentName', max_length=40)  
    mobile = models.CharField(max_length=15, blank=True, null=True)
    instmail = models.EmailField(db_column='instMail', max_length=23, blank=True, null=True) 
    personalmail = models.EmailField(db_column='personalMail', max_length=255, blank=True, null=True) 
    batchid = models.ForeignKey(Batches, models.PROTECT, db_column='batchId')  
    is_registered = models.BooleanField(default= False)
    
    class Meta:
        managed = True
        db_table = 'official_alumni'
# add column registerd boolean type in db 

class Users(models.Model):
    username = models.CharField(max_length=15, unique=True, db_index=True,null=False)
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(null=False, max_length=15) 
    profile_url = models.CharField(max_length=50)
    full_name = models.CharField(max_length=20) 
    start_year = models.IntegerField(validators=[MinValueValidator(4),MaxValueValidator(4)])
    end_year = models.IntegerField(validators=[MinValueValidator(4),MaxValueValidator(4)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'

class students(models.Model):
   registration_number = models.IntegerField(validators=[MinValueValidator(8),MaxValueValidator(15)])
   course_name = models.CharField(max_length=15)
   user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
   batch_id = models.ForeignKey(Batches, on_delete=models.SET_NULL, null=True)

   class Meta:
       db_table = 'students'

class faculties(models.Model):
    faculty_id = models.CharField(max_length=15)
    designation = models.CharField(max_length=25)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'faculties'

class alumni(models.Model):
    alumni_id = models.CharField(max_length=15)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'alumni'

class EventCategories(models.Model):
    title = models.CharField(null=False, max_length=25)
    description = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=50) 
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="created_by_eventcategories")
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="updated_by_eventcategories")

    class Meta:
        db_table = 'event_categories'

class Events(models.Model):
    title = models.CharField(null=False, max_length=25)
    description = models.CharField(max_length=255)
    content = models.TextField()
    event_category = models.ForeignKey(EventCategories, on_delete=models.SET_NULL, null=True)
    event_time = models.TimeField()
    event_date = models.DateField()
    location = models.CharField(max_length=50)
    contact_email = models.EmailField()
    event_slug = models.SlugField(unique = True, max_length=20)
    image_url = models.CharField(max_length=255)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="created_by_events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="updated_by_events")

    class Meta:
        db_table = 'events'
        ordering = ['-event_date'] 

class NewsCategories(models.Model):
    title = models.CharField(null=False, max_length=25)
    description = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=50) 
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="created_by_newscategories")
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="updated_by_newscategories")

    class Meta:
        db_table = 'news_categories'

class News(models.Model):
    title = models.CharField(null=False, max_length=25)
    description = models.CharField(max_length=255)
    content = models.TextField()
    news_category = models.ForeignKey(NewsCategories, on_delete=models.SET_NULL, null=True)
    news_date = models.DateField()
    news_slug = models.SlugField(unique = True, max_length=20)
    image_url = models.CharField(max_length=255)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="created_by_news")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="updated_by_news")

    class Meta:
        db_table = 'news'
        ordering = ['-news_date'] 

class Blogs(models.Model):
    title = models.CharField(null=False, max_length=25)
    description = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Users, on_delete=models.SET_NULL, related_name="author", null=True)
    image_url = models.CharField(max_length=255)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="created_by_blogs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="updated_by_blogs")

    class Meta:
        db_table = 'blogs'
        ordering = ['-created_at']

class Mentor (models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="user_id")
    industry = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    guidance_areas = models.CharField(max_length=250)
    contact_method = models.CharField(max_length=250)
    availability = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="approved_by")

    class Meta:
        db_table = 'mentor'

class Mentee (models.Model):
    mentee_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="mentee_id")
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name="mentor_id")
    short_note = models.CharField(max_length=250)
    status = models.BooleanField(null = True)
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mentee'

class Gallery (models.Model):
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="created_by")
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="event_id")

    class Meta:
        db_table = 'gallery'
