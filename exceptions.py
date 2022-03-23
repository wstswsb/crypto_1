class BaseAppException(Exception):
    pass


class InvalidSBlockFileException(BaseAppException):
    pass


class InvalidPermutationPatternException(BaseAppException):
    pass


class InvalidBitPositionException(BaseAppException):
    pass
