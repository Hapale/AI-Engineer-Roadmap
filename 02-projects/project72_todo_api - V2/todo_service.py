from todo import Todo

class TodoService:

    def __init__(self, repository):
        self._repository = repository

    def add(self, title, description):
        todo = Todo(title, description)
        self._repository.save(todo)

    def get_all(self):
        return self._repository.get_all()

    def delete(self, todo):
        self._repository.delete(todo)

    def search(self, keyword):
        return self._repository.search(keyword)