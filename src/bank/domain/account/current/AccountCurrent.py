class AccountCurrent:
    def __init__(self, limitExtra: int) -> None:
        self._limitExtra = limitExtra

    @property
    def limitExtra(self) -> int:
        return self._limitExtra

    @limitExtra.setter
    def limitExtra(self, limitExtra: int) -> None:
        if isinstance(limitExtra, int):
            self._limitExtra = limitExtra
        raise TypeError('Argument limitExtra not type int')
