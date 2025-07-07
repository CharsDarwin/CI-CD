import pytest
from django.test import Client
from todos.models import Todo

client = Client()

@pytest.mark.django_db
def test_todos_list_view_status():
    resp = client.get("/todos/")           # URL directa
    assert resp.status_code == 200

@pytest.mark.django_db
def test_todos_list_contains_item_text():
    Todo.objects.create()
    resp = client.get("/todos/")
    assert "Todo" in resp.content.decode() or "task" in resp.content.decode()
