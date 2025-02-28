from django.db import models

class Result(models.Model):  # models.Model を継承

    # タイトル用フィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=30
    )

    # 本文用フィールド
    content = models.TextField(
        verbose_name='本文',
        max_length=300
    )

    # 写真用フィールド
    # image1 = models.ImageField(
    #     verbose_name='イメージ１',
    #     upload_to='photos'
    # )

    def __str__(self):
        return self.title
