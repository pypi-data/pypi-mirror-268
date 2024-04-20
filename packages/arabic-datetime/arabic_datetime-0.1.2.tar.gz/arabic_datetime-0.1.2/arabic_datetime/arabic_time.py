from typing import Union
import datetime

# Import from constants
from ._constants import AR_NUMS


from typing import Union
import datetime


class ArabicTime:
    def __init__(self, time_object: Union[datetime.time, datetime.datetime] = None) -> None:
        self._time_object = None
        self.time_object = time_object

        # string keys in translate table must be of length 1
        self.num_trans_table = str.maketrans(AR_NUMS)

        # convert first to `int` to turn 01 into 1
        self.__hour = str(int(self._time_object.hour))
        self.__minute = str(int(self._time_object.minute))
        self.__second = str(int(self._time_object.second))
        self.__microsecond = str(int(self._time_object.microsecond))

    @property
    def time_object(self):
        return self._time_object

    @time_object.setter
    def time_object(self, value: Union[datetime.time, datetime.datetime] = None) -> None:
        if value == None:
            raise TypeError(
                f"ArabicTime class error: No parameter was passed as time_object or the parameter passed is None. Only datetime.time or datetime.datetime objects are allowed.")
        elif not isinstance(value, datetime.time) and not isinstance(value, datetime.datetime):
            raise TypeError(
                f"ArabicTime class error: The parameter passed as time_object is of type {type(value)}. Only datetime.time or datetime.datetime objects are allowed.")
        self._time_object = value

    def time(self, format: str = "HMS", separator: str = ":") -> str:
        if not isinstance(format, str):
            raise TypeError(
                f"ArabicTime class error: The 'format' parameter passed to the class method '{self.time.__name__}' is not a string.")
        elif not isinstance(separator, str):
            raise TypeError(
                f"ArabicTime class error: The 'separator' parameter passed to the class method '{self.time.__name__}' is not a string.")

        if format.upper() not in ["H", "HM", "HMS", "HMSF"]:
            raise ValueError(
                f"ArabicTime class error: Invalid format string passed to the class method '{self.time.__name__}'. Valid values are 'HMSF', 'HMS', 'HM' and 'H'.")

        time_elements = []
        if "H" in format.upper():
            time_elements.append(self.__hour.translate(self.num_trans_table))
        if "M" in format.upper():
            time_elements.append(self.__minute.translate(self.num_trans_table))
        if "S" in format.upper():
            time_elements.append(self.__second.translate(self.num_trans_table))
        if "F" in format.upper():
            time_elements.append(
                self.__microsecond.translate(self.num_trans_table))

        formated_time = separator.join(time_elements)

        return formated_time
