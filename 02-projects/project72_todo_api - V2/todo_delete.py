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

    
def can_be_deleted_by(self, user_id):

    if self.user_id == user_id:
        return DomainResult(True, None)

    if self.user_id != user_id:
        return DomainResult(False, "NOT_OWNER")

    if self.user_id 
        return DomainResult(False, "TODO_COMPLETED")