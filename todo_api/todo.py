class Todo:

    def _normalize_title(self, title: str) -> str:
        return title.strip()

    def _normalize_description(self, description: str) -> str:
        return description.strip()

    def _validate_title(self, title: str) -> None:

        if title is None:
            raise ValueError("Title cannot be None")

        if not title:
            raise ValueError("Title cannot be Empty")

    def _validate_description(self, description: str) -> None:
        pass

    def __init__(self, title: str, description: str = ""):

        title = self._normalize_title(title)
        description = self._normalize_description(description)

        self._validate_title(title)
        self._validate_description(description)

        self._title = title
        self._description = description

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    def set_title(self, new_title: str):

        new_title = self._normalize_title(new_title)
        self._validate_title(new_title)

        self._title = new_title

    def set_description(self, new_description: str):

        new_description = self._normalize_description(new_description)
        self._validate_description(new_description)

        self._description = new_description