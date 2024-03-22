from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

vs_choices = (
    ('public', 'public'),
    ('private', 'private'),
    ('limited', 'limited')
)

class Notes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    is_deleted = models.BooleanField(default=0)
    visibility = models.CharField(choices=vs_choices, default='private', max_length=255)

    def __str__(self):
        return self.title