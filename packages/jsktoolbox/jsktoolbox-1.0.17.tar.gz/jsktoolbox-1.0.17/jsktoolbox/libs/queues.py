# -*- coding: UTF-8 -*-
"""
  Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 03.12.2023

  Purpose: Sets of container classes with FIFO queue functionality.
"""

from typing import List, Dict, Any

from jsktoolbox.attribtool import NoDynamicAttributes


class Fifo(dict, NoDynamicAttributes):
    """Fifo class."""

    __in: int = None  # type: ignore
    __out: int = None  # type: ignore

    def __init__(self) -> None:
        """Constructor."""
        self.__in = 0
        self.__out = 0

    def put(self, data: Any) -> None:
        """Put data to queue."""
        self.__in += 1
        self[self.__in] = data

    def get(self) -> Any:
        """Get first item from queue."""
        self.__out += 1
        return dict.pop(self, self.__out)


# #[EOF]#######################################################################
