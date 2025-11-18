class AppError(Exception):
    pass

class DatabaseConnectionError(AppError):
    pass

class InvalidDataError(AppError):
    pass

class PostNotFoundError(AppError):
    pass