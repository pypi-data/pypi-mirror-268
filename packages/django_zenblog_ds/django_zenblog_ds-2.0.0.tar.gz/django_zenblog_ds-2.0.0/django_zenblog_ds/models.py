from django.db import models
from mdeditor.fields import MDTextField
from _data.zenblogds import CATEGORY
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', default='default_thumbnail.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = MDTextField()
    status = models.IntegerField(choices=STATUS, default=0)
    remarkable = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("zenblogds:post_detail", kwargs={"slug": str(self.slug)})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     # Delete profile when user is deleted
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # show how we want it to be displayed
