import pytest
from django.urls import reverse
from todos.models import Todo

@pytest.mark.django_db
def test_todos_list_view_status(client):
    url = reverse("todo_list")           # /todos/
    resp = client.get(url)
    assert resp.status_code == 200

@pytest.mark.django_db
def test_todos_list_contains_item_text(client):
    Todo.objects.create(text="Cortar césped")
    url = reverse("todo_list")
    resp = client.get(url)
    assert "Cortar césped" in resp.content.decode()
