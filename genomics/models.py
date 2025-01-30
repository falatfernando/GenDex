from django.db import models

# Create your models here.
class DNASequence(models.Model):
    name = models.CharField(max_length=100, blank=True)
    sequence = models.TextField()
    gc_content = models.FloatField()
    length = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name