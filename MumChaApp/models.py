from django.db import models

#アカウントテーブル
class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    img = models.ImageField(null=True)
    birth = models.DateField(null=True)
    comment = models.TextField(max_length=200, null=True)

#投稿テーブル
class Posting(models.Model):
    contents_id = models.IntegerField(primary_key=True)
    content = models.TextField(max_length=200)
    posting_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

#フォローテーブル
class Follow(models.Model):
    follow_id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(User, on_delete=models.CASCADE)

#いいねテーブル
class Favorite(models.Model):
    fav_id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.ForeignKey(Posting, on_delete=models.CASCADE)