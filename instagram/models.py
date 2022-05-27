from django.conf import settings
from django.core.validators import  MinValueValidator
from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(validators=[MinValueValidator(10)]
                               )
    photo = models.ImageField(blank=True, upload_to='instargram/post/%Y/%m/%d')
    is_public = models.BooleanField(default = False, verbose_name= '공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']