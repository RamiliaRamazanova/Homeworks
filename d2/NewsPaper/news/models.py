from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('postRating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('commentRating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.authorRating = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return self.authorUser.username

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Category(models.Model):
    categoryName = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.categoryName
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    postTitle = models.CharField(max_length=64)
    postText = models.TextField()
    postRating = models.IntegerField(default=0)

    def like(self):
        self.postRating += 1
        self.save()

    def dislike(self):
        self.postRating -= 1
        self.save()

    def preview(self):
        return self.postText[0:123] + '...'

    def __str__(self):
        return f"{self.postTitle}"

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категория постов'
        verbose_name_plural = 'Категории постов'

    def __str__(self):
        return f"{self.post.postTitle}"

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    commentRating = models.IntegerField(default=0)

    def like(self):
        self.commentRating += 1
        self.save()

    def dislike(self):
        self.commentRating -= 1
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'