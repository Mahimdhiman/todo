from django.db import models # type: ignore
class Task(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.TextField(blank=True)  # Store tags as a comma-separated string
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='OPEN')

    def save(self, *args, **kwargs):
        # Ensure tags are unique and clean
        if self.tags:
            self.tags = ','.join(sorted(set(tag.strip() for tag in self.tags.split(','))))
        super().save(*args, **kwargs)

    def _str_(self):
        return self.title
# Create your models here.
