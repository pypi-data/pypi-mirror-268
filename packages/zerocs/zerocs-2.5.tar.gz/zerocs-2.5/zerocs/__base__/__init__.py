# -*- encoding: utf-8 -*-
import os


class Init:
    """
    init observer
    """

    _os = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for dir in os.listdir(_os):
        if '__' not in dir and dir.startswith('.') is False:
            module = __import__(f"zerocs.{dir}.{dir}", globals=globals(), locals=locals())
