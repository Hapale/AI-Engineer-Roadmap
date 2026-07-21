class TodoRepository:

    def __init__(self):

        self._todos = []

    def save(self, todo):

        if todo is None:
            raise ValueError("Todo cannot be None")
        
        self._todos.append(todo)

    def get_all(self):

        return self._todos.copy()

    def delete(self, todo):

        if todo is None:
            raise ValueError("Todo cannot be None")
        
        self._todos.remove(todo)

    
    def search(self, keyword):

        keyword = keyword.lower()

        return [
            todo
            for todo in self._todos
            if keyword in todo.title.lower()
        ] or [
            todo
            for todo in self._todos
            if keyword in todo.description.lower()
        ]