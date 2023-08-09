from django.db import models

class New(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content