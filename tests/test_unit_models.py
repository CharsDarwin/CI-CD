import pytest
from todos.models import Todo

@pytest.mark.django_db
def test_todo_default_completed_false():
    todo = Todo.objects.create(text="Comprar leche")
    assert todo.completed is False

@pytest.mark.django_db
def test_todo_str_returns_text():
    todo = Todo.objects.create(text="Pagar luz")
    assert str(todo) == "Pagar luz"
