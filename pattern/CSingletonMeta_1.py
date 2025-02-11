#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 00:24:25 2023

@author: kukurihime
"""

from threading import Lock, Thread


class CSingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


if __name__ == "__main__":    
    class Singleton(metaclass=CSingletonMeta):
        value: str = None

        def __init__(self, value: str) -> None:
            self.value = value

    def test_singleton(value: str) -> None:
            singleton = Singleton(value)
            print(singleton.value)

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()