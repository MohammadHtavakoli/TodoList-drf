from django.test import TestCase
from tasks.models import Task


class TaskModelTest(TestCase):

    def test_create_task(self):
        task = Task.objects.create(title="Test Task", description="Test description", is_completed=False)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.is_completed)

    def test_read_task(self):
        task = Task.objects.create(title="Test Task", description="Test description", is_completed=False)
        fetched_task = Task.objects.get(id=task.id)
        self.assertEqual(fetched_task.title, "Test Task")
        self.assertEqual(fetched_task.description, "Test description")
        self.assertFalse(fetched_task.is_completed)

    def test_update_task(self):
        task = Task.objects.create(title="Old Title", description="Old description", is_completed=False)
        task.title = "Updated Title"
        task.description = "Updated description"
        task.is_completed = True
        task.save()
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.title, "Updated Title")
        self.assertEqual(updated_task.description, "Updated description")
        self.assertTrue(updated_task.is_completed)

    def test_delete_task(self):
        task = Task.objects.create(title="Test Task", description="Test description", is_completed=False)
        self.assertEqual(Task.objects.count(), 1)
        task.delete()
        self.assertEqual(Task.objects.count(), 0)
