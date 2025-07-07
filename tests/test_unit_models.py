import pytest
from todos.models import Todo

@pytest.mark.django_db
def test_todo_default_completed_false():
    todo = Todo.objects.create()
    assert todo.isCompleted is False        # OK

@pytest.mark.django_db
def test_todo_str_returns_string():
    todo = Todo.objects.create()
    assert isinstance(str(todo), str)       # solo verificamos que es str
