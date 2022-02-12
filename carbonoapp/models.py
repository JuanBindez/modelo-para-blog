from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=200,null=True)
    date_do_post = models.DateField()
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

