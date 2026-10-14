class DomainResult:
    def __init__(self, success, reason):
        self._success = success
        self._reason = reason

        if success and reason is not None:
            raise ValueError(
                "Reason must be None when success is True"
            )

        if not success and reason is None:
            raise ValueError(
                "Reason is required when success is False"
            )

    @property
    def success(self):
        return self._success
    
    @property
    def reason(self):
        return self._reason