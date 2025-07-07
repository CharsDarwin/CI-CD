import pytest
from todos.models import Todo

@pytest.mark.django_db
def test_todo_default_completed_false():
    todo = Todo.objects.create()           # sin 'text'
    assert todo.isCompleted is False       # campo real

@pytest.mark.django_db
def test_todo_str_returns_pk():
    todo = Todo.objects.create()
    assert str(todo).isdigit()             # el __str__ devuelve pk
