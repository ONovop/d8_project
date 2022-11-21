from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    rate = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @classmethod
    def update_rating(cls, person:User.username):
        if cls.objects.filter(user__username = person).exists():
            art_rate = Post.objects.filter(author__user__username = person, type = Post.article).aggregate(Sum('rate'))
            com_rate = Comment.objects.filter(user__username = person).aggregate(Sum('rate'))
            art_com_rate = Comment.objects.filter(post__type = Post.article, post__author__user__username
                                                  = person).aggregate(Sum('rate'))
            extra = Comment.objects.filter(post__type = Post.article, post__author__user__username = person,
                                           user__username = person).aggregate(Sum('rate'))
            if extra['rate__sum'] is None:
                extra['rate__sum'] = 0
            #print(art_rate)
            #print(com_rate)
            #print(art_com_rate)
            #print(extra)
            obj = Author.objects.get(user__username = person)
            obj.rate = (art_rate['rate__sum'] * 3 + com_rate['rate__sum']
                        + art_com_rate['rate__sum'] - extra['rate__sum'])
            obj.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    article = 'A'
    news = 'N'
    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    type = models.CharField(max_length=1, choices=POSITIONS, default=news)
    time_creating = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(default=0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        str = self.text[:123] + '...'
        return str

    def __str__(self):
        return f'{self.title}: {self.text}'

    def get_absolute_url(self):
        return reverse('Detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    time_creating = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

