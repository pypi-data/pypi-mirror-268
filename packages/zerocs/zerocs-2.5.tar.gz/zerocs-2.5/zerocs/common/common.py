# -*- encoding: utf-8 -*-


class _BaseSetattr:

    def __new__(cls, func):

        for _func in func.__dict__:
            if '__' not in _func:
                setattr(cls, _func, func.__dict__[_func])

        return cls, func
