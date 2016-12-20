# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import List


class ASTree(object, metaclass=ABCMeta):

    @abstractmethod
    def child(self, i: int) -> 'ASTree':
        pass

    @abstractmethod
    def num_children(self) -> int:
        pass

    @abstractmethod
    def children(self) -> List['ASTree']:
        pass

    @abstractmethod
    def location(self) -> str:
        pass

    def iterator(self) -> List['ASTree']:
        return self.children()

    @abstractmethod
    def to_string(self) -> str:
        pass
