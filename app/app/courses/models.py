from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            # name__icontains=query, description__icontains=query  # AND  -> models.Q(name__icontains=query) & models.Q(description__icontains=query)
            models.Q(name__icontains=query) | models.Q(description__icontains=query)  # OR
            )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição')
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)  # MEDIA_ROOT = em settings.py
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']
        # ordering = ['-name']  # descending