class VariableNotSetException(Exception):
    """Used when trying to retrieve a variable from an instance that has not set the target variable."""

    def __init__(self, target_variable: str):
        super().__init__(f"Target variable: '{target_variable}' was not set.")
