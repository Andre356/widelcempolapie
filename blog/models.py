from django.db import models
from django.utils import timezone
from django.urls import reverse


class Dish(models.Model):
    name = models.CharField(max_length=128)
    portions = models.IntegerField(default=2, null=True, blank=True)
    ingredients = models.TextField(default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    added = models.DateField(null=False, blank=True, default=timezone.now)   # blank działa na rekordy w db
    photo0 = models.ImageField(upload_to='images/', null=False, blank=True, default='images/000empty.jpg')
    photo1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='images/', null=True, blank=True)
    rating = models.IntegerField(default=0)
    thermomix = models.BooleanField(default=False, blank=True)

    def dateformat(self):
        return self.added.strftime('%e.%m.%Y')

    # string representation
    def __str__(self):
        return self.name

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk': self.pk})


# class Comment(models.Model):
#     post = models.ForeignKey('blog.Dish', related_name='comments', on_delete=models.CASCADE)
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def __str__(self):
#         return self.text
#
#     # after posting a comment redirect to home page
#     def get_absolute_url(self):
#         return reverse('home')
