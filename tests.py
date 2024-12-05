# Create your tests here.
from django.test import TestCase # type: ignore
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            due_date="2024-12-31",
            tags="work,personal",
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertIn("work",self.task.tags)