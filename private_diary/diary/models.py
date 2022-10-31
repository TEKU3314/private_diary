from accounts.models import CustomUser
from django.db import models

class Diary(models.Model):
    """日記モデル"""

    user = models.ForeignKey(CustomUser,verbose_name='ユーザー',
    on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    title_photo = models.ImageField(verbose_name='タイトル写真',blank=True,null=True)
    subtitle = models.CharField(verbose_name='サブタイトル',max_length=100)
    item1 = models.TextField(verbose_name='項目１',blank=True)
    content1 =  models.TextField(verbose_name='本文1',blank=True,null=True)
    photo1 = models.ImageField(verbose_name='写真１',blank=True,null=True)
    item2 = models.TextField(verbose_name='項目２',blank=True)
    content2 =  models.TextField(verbose_name='本文２',blank=True,null=True)
    photo2 = models.ImageField(verbose_name='写真２',blank=True,null=True)
    item3 = models.TextField(verbose_name='項目３',blank=True)
    content3 =  models.TextField(verbose_name='本文３',blank=True,null=True) 
    photo3 = models.ImageField(verbose_name='写真３',blank=True,null=True)
    item4 = models.TextField(verbose_name='項目４',blank=True)
    content4 =  models.TextField(verbose_name='本文４',blank=True,null=True) 
    photo4 = models.ImageField(verbose_name='写真４',blank=True,null=True)
    item5 = models.TextField(verbose_name='項目５',blank=True)
    content5 =  models.TextField(verbose_name='本文５',blank=True,null=True) 
    photo5 = models.ImageField(verbose_name='写真５',blank=True,null=True)
    conclude_title = models.TextField(verbose_name='まとめタイトル',blank=True)
    conclude_text = models.TextField(verbose_name='まとめテキスト',blank=True)
    user_photo  = models.ImageField(verbose_name='ユーザアイコン',blank=True,null=True)
    user_message = models.TextField(verbose_name='ユーザメッセージ',blank=True,null=True)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural = 'Diary'
    
    def __str__(self):
        return self.title
