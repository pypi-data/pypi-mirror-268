# -*- coding: UTF-8 -*-
"""
  Author:  Jacek Kotlarski --<szumak@virthost.pl>
  Created: 01.09.2023

  Purpose: BData container base class.
"""

from inspect import currentframe
from typing import Dict, List, Any, Optional
from types import FrameType

from jsktoolbox.attribtool import NoDynamicAttributes
from jsktoolbox.raisetool import Raise


class BClasses(NoDynamicAttributes):
    """Base class for projects."""

    @property
    def _c_name(self) -> str:
        """Return class name."""
        return self.__class__.__name__

    @property
    def _f_name(self) -> str:
        """Return current method name."""
        tmp: Optional[FrameType] = currentframe()
        if tmp is not None:
            frame: Optional[FrameType] = tmp.f_back
            if frame is not None:
                method_name: str = frame.f_code.co_name
                return method_name
        return ""


class BData(BClasses):
    """BData container class."""

    __data: Optional[Dict] = None
    __types: Optional[Dict[str, Any]] = None

    def __check_keys(self, key: str) -> bool:
        """Checks if key is present in __data list."""
        if self.__data and key in self.__data:
            return True
        return False

    def __has_type(self, key: str) -> bool:
        """Checks if key is present in __types list."""
        if self.__types and key in self.__types:
            return True
        return False

    def __check_type(self, key: str, received_type: Optional[Any]) -> bool:
        """Check that the stored type matches the received type."""
        if self.__types and self.__has_type(key):
            if isinstance(received_type, self.__types[key]):
                return True
            return False
        raise Raise.error(
            f'The key: "{key}" is missing in the directory.',
            KeyError,
            self._c_name,
            currentframe(),
        )

    def _get_data(
        self,
        key: str,
        set_default_type: Optional[Any] = None,
        default_value: Any = None,
    ) -> Optional[Any]:
        """Gets data from internal dict.

        ## ARGUMENTS:
        - key [str] - variable name,
        - set_default_type [Optional[Any]] - sets and restrict default type of variable if not None,
        - default_value [Any] - returns it if variable not found
        """
        if self.__check_keys(key):
            return self._data[key]
        elif set_default_type:
            if self.__types is None:
                self.__types = {}
            self.__types[key] = set_default_type
        if default_value is not None:
            if (
                self.__types
                and self.__has_type(key)
                and not isinstance(default_value, self.__types[key])
            ):
                raise Raise.error(
                    f"Expected '{self.__types[key]}' type, received default_value type is: {type(default_value)}",
                    TypeError,
                    self._c_name,
                    currentframe(),
                )
            return default_value
        return None

    def _set_data(
        self, key: str, value: Any, set_default_type: Optional[Any] = None
    ) -> None:
        """Sets data to internal dict.

        ## ARGUMENTS:
        - key [str] - variable name,
        - value [Any] - value of variable
        - set_default_type [Optional[Any]] - sets and restrict default type of variable if not None,
        """
        if self.__types is None:
            self.__types = {}
        if self.__has_type(key):
            if isinstance(value, self.__types[key]):
                self._data[key] = value
            else:
                raise Raise.error(
                    f"Expected '{self.__types[key]}' type, received: '{type(value)}'",
                    TypeError,
                    self._c_name,
                    currentframe(),
                )
        else:
            if set_default_type:
                self.__types[key] = set_default_type
                if isinstance(value, set_default_type):
                    self._data[key] = value
                else:
                    raise Raise.error(f"", TypeError, self._c_name, currentframe())
            else:
                self._data[key] = value

    @property
    def _data(self) -> Dict:
        """Return data dict."""
        if self.__data is None:
            self.__data = {}
        if self.__types is None:
            self.__types = {}
        return self.__data

    @_data.setter
    def _data(self, value: Optional[Dict]) -> None:
        """Set data dict."""
        if value is None:
            self.__data = {}
            return None
        if isinstance(value, Dict) and self.__data is not None:
            for key in value.keys():
                if self.__types and self.__has_type(key):
                    if not self.__check_type(key, type(value[key])):
                        raise Raise.error(
                            f"Expected '{self.__types[key]}' type, received: '{type(value[key])}'",
                            TypeError,
                            self._c_name,
                            currentframe(),
                        )
                self.__data[key] = value[key]
        else:
            raise Raise.error(
                f"Expected Dict type, received: '{type(value)}'.",
                AttributeError,
                self._c_name,
                currentframe(),
            )


# #[EOF]#######################################################################
