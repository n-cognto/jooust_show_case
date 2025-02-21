# models.py
from django.db import models
from django.utils.text import slugify
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class BaseContent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='content_images/')
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def description_preview(self):
        return self.description[:150] + '...' if len(self.description) > 150 else self.description

class News(BaseContent):
    read_more_link = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "News"
        ordering = ['-created_date']

class Event(BaseContent):
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200,null=True)
    registration_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['event_date']

class Notice(BaseContent):
    priority = models.IntegerField(default=0)
    expiry_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-priority', '-created_date']

def validate_youtube_url(url):
    if 'youtube.com' not in url and 'youtu.be' not in url:
        raise ValidationError('Please enter a valid YouTube URL')

class Media(BaseContent):
    MEDIA_TYPES = (
        ('youtube', 'YouTube Video'),
        ('image', 'Image'),
    )
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    youtube_url = models.URLField(
        blank=True, 
        null=True,
        validators=[URLValidator(), validate_youtube_url]
    )
    
    def get_youtube_embed_url(self):
        if self.youtube_url and 'youtube.com' in self.youtube_url:
            video_id = self.youtube_url.split('v=')[-1]
            return f'https://www.youtube.com/embed/{video_id}'
        return None

    class Meta:
        verbose_name_plural = "Media"
        ordering = ['-created_date']

class PartnerLogo(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partner_logos/')
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name

class SchoolActivity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='school_activities/')
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title


# models.py
from django.db import models
from django.utils.text import slugify

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    published_date = models.DateTimeField(auto_now_add=True)
    read_more_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def content_preview(self):
        return self.content[:150] + '...' if len(self.content) > 150 else self.content