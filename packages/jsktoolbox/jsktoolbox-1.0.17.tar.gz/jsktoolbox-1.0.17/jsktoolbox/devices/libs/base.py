# -*- coding: UTF-8 -*-
"""
  Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
  Created: 04.12.2023

  Purpose: Base classes.
"""

from typing import Dict, List, Optional, Union, Tuple, Any, TypeVar
from inspect import currentframe

from jsktoolbox.attribtool import NoDynamicAttributes, ReadOnlyClass
from jsktoolbox.raisetool import Raise
from jsktoolbox.logstool.logs import LoggerClient, LoggerQueue
from jsktoolbox.libs.base_data import BData

from jsktoolbox.netaddresstool.ipv4 import (
    Address,
    Netmask,
    Network,
    SubNetwork,
)
from jsktoolbox.netaddresstool.ipv6 import (
    Address6,
    Network6,
    Prefix6,
    SubNetwork6,
)

from jsktoolbox.devices.network.connectors import IConnector

TDev = TypeVar("TDev", bound="BDev")


class _Keys(object, metaclass=ReadOnlyClass):
    """Keys definition class.

    For internal purpose only.
    """

    CH = "__connector_handler__"
    DEBUG = "__debug__"
    LC = "__logs_client__"
    PARENT = "__parent__"
    ROOT = "__root__"
    VERBOSE = "__verbose__"


class BDebug(BData):
    """Base class for debug flags."""

    @property
    def debug(self) -> bool:
        """Return debug flag."""
        if _Keys.DEBUG not in self._data:
            self._data[_Keys.DEBUG] = False
        return self._data[_Keys.DEBUG]

    @debug.setter
    def debug(self, debug: bool) -> None:
        """Set debug flag."""
        self._data[_Keys.DEBUG] = debug

    @property
    def verbose(self) -> bool:
        """Return verbose flag."""
        if _Keys.VERBOSE not in self._data:
            self._data[_Keys.VERBOSE] = False
        return self._data[_Keys.VERBOSE]

    @verbose.setter
    def verbose(self, verbose: bool) -> None:
        """Set verbose flag."""
        self._data[_Keys.VERBOSE] = verbose


class BDev(BDebug):
    """Base devices class."""

    @property
    def _ch(self) -> Optional[IConnector]:
        """Returns optional Connector object."""
        if _Keys.CH not in self._data:
            self._data[_Keys.CH] = None
        return self._data[_Keys.CH]

    @_ch.setter
    def _ch(self, value: IConnector) -> None:
        """Sets Connector object."""
        if not isinstance(value, IConnector):
            raise Raise.error(
                f"Expected IConnector derived type, received: '{type(value)}'.",
                TypeError,
                self._c_name,
                currentframe(),
            )
        self._data[_Keys.CH] = value

    @property
    def logs(self) -> Optional[LoggerClient]:
        """Returns optional LoggerClient object."""
        if _Keys.LC not in self._data:
            self._data[_Keys.LC] = None
        return self._data[_Keys.LC]

    @logs.setter
    def logs(self, value: LoggerClient) -> None:
        """Sets Connector object."""
        if not isinstance(value, LoggerClient):
            raise Raise.error(
                f"Expected LoggerClient type, received: '{type(value)}'.",
                TypeError,
                self._c_name,
                currentframe(),
            )
        self._data[_Keys.LC] = value

    @property
    def root(self) -> str:
        """Gets RouterOS command root."""
        if _Keys.ROOT not in self._data:
            self._data[_Keys.ROOT] = ""
        tmp: str = self._data[_Keys.ROOT]
        if self.parent is not None:
            item: BDev = self.parent
            tmp = f"{item.root}{tmp}"
        return tmp

    @root.setter
    def root(self, value: str) -> None:
        """Sets RouterOS command root."""
        if not isinstance(value, str):
            raise Raise.error(
                f"Expected string type, received: '{type(value)}'",
                TypeError,
                self._c_name,
                currentframe(),
            )
        self._data[_Keys.ROOT] = value

    @property
    def parent(self) -> Optional[TDev]:
        """Returns parent for current object."""
        if _Keys.PARENT not in self._data:
            self._data[_Keys.PARENT] = None
        return self._data[_Keys.PARENT]

    @parent.setter
    def parent(self, value: Optional[TDev]) -> None:
        """Sets parent for current object."""
        if value is not None and not isinstance(value, BDev):
            raise Raise.error(
                f"Expected BDev type, received: '{type(value)}'",
                TypeError,
                self._c_name,
                currentframe(),
            )
        self._data[_Keys.PARENT] = value


# #[EOF]#######################################################################
