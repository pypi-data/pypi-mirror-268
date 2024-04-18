# -*- encoding: utf-8 -*-
import logging

from zerocs.observer import ObserverBase


@ObserverBase
class _ObserverBase:

    @staticmethod
    def attach(obs: object, subject: object) -> None:
        if subject not in obs.ObserverList:
            obs.ObserverList.append(subject)
            logging.debug(f"{obs.__name__} added {subject.__name__} Join observation queue...")

    @staticmethod
    def detach(obs: object, subject: object) -> None:
        obs.ObserverList.remove(subject)
        logging.debug(f"{obs.__name__} No longer observing {subject.__name__}")

    @staticmethod
    def notify(obs: object):
        for Observer in obs.ObserverList:
            Observer.update(obs)
