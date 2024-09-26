from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
import re
class Article(models.Model):
    CATEGORY_CHOICES = [
        ("PERSONAL", "personal"),
        ("BUSINESS", "business"),
        ("ENTERTAINMENT","entertainment")
    ]
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    category = models.CharField(max_length=150, choices=CATEGORY_CHOICES, default="personal")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            if Article.objects.filter(slug=slug).exists():
                slug = f"{self.slug} + {get_random_string(4)}"
                slug = re.sub(r'[^\w\s-]', '', self.title)
                slug = slug.strip().lower().replace(' ', '-')
            self.slug = slug
        super(Article, self).save(*args, **kwargs)




# Create your models here.
