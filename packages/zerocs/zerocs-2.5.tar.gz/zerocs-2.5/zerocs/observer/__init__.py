# -*- encoding: utf-8 -*-
from zerocs.common import BaseSetattr


class ObserverBase(BaseSetattr):
    """
    Observer base class, adding, deleting, and publishing messages
    """

    @staticmethod
    def attach(obs: object, subject: object) -> None:
        """
        Add client to subscription center
        :param obs:
        :param subject:
        :return:
        """

    @staticmethod
    def detach(obs: object, subject: object) -> None:
        """
        Remove client from subscription center
        :param obs:
        :param subject:
        :return:
        """

    @staticmethod
    def notify(obs: object) -> None:
        """
        Publish Message
        :return:
        """
