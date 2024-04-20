from typing import Union
import datetime

# Import constants
from ._constants import MONTH_GROUPS, AR_NUMS


class ArabicDate:
    def __init__(self, date_object: Union[datetime.date, datetime.datetime] = None) -> None:
        self._date_object = None
        self.date_object = date_object

        self.__year = str(self.date_object.year)
        self.__month = int(self.date_object.month)
        # convert first to `int` to turn 01 into 1
        self.__day = str(int(self.date_object.day))

        # string keys in translate table must be of length 1
        self.num_trans_table = str.maketrans(AR_NUMS)

    @property
    def date_object(self):
        return self._date_object

    @date_object.setter
    def date_object(self, value: Union[datetime.date, datetime.datetime] = None) -> None:
        if value == None:
            raise TypeError(
                f"ArabicDate class error: No parameter was passed as date_object or the parameter passed is None. Only datetime.date or datetime.datetime objects are allowed.")
        elif not isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
            raise TypeError(
                f"ArabicDate class error: The parameter passed as date_object is of type {type(value)}. Only datetime.date or datetime.datetime objects are allowed.")
        self._date_object = value

    # Group Name Methods
    def syriac_names(self, east_nums: bool = False) -> str:
        if not isinstance(east_nums, bool):
            raise TypeError(
                f"ArabicDate class error: east_nums must be a boolean. '{east_nums}' is not a boolean and was passed to the class method '{self.syriac_names.__name__}'.")

        if east_nums:
            return self.__day.translate(self.num_trans_table) + " " + MONTH_GROUPS["syriac"]["months"][self.__month-1] + " " + self.__year.translate(self.num_trans_table)
        else:
            return self.__day + " " + MONTH_GROUPS["syriac"]["months"][self.__month-1] + " " + self.__year

    def roman1_names(self, east_nums: bool = False) -> str:
        if not isinstance(east_nums, bool):
            raise TypeError(
                f"ArabicDate class error: east_nums must be a boolean. '{east_nums}' is not a boolean and was passed to the class method '{self.roman1_names.__name__}'.")

        if east_nums:
            return self.__day.translate(self.num_trans_table) + " " + MONTH_GROUPS["roman1"]["months"][self.__month-1] + " " + self.__year.translate(self.num_trans_table)
        else:
            return self.__day + " " + MONTH_GROUPS["roman1"]["months"][self.__month-1] + " " + self.__year

    def roman2_names(self, east_nums: bool = False) -> str:
        if not isinstance(east_nums, bool):
            raise TypeError(
                f"ArabicDate class error: east_nums must be a boolean. '{east_nums}' is not a boolean and was passed to the class method '{self.roman2_names.__name__}'.")

        if east_nums:
            return self.__day.translate(self.num_trans_table) + " " + MONTH_GROUPS["roman2"]["months"][self.__month-1] + " " + self.__year.translate(self.num_trans_table)
        else:
            return self.__day + " " + MONTH_GROUPS["roman2"]["months"][self.__month-1] + " " + self.__year

    def french_names(self, east_nums: bool = False) -> str:
        if not isinstance(east_nums, bool):
            raise TypeError(
                f"ArabicDate class error: east_nums must be a boolean. '{east_nums}' is not a boolean and was passed to the class method '{self.french_names.__name__}'.")

        if east_nums:
            return self.__day.translate(self.num_trans_table) + " " + MONTH_GROUPS["french"]["months"][self.__month-1] + " " + self.__year.translate(self.num_trans_table)
        else:
            return self.__day + " " + MONTH_GROUPS["french"]["months"][self.__month-1] + " " + self.__year

    # Dual Name Method
    def dual_names(self, first: str, second: str, east_nums: bool = False) -> str:
        if not isinstance(first, str):
            raise TypeError(
                f"ArabicDate class error: Unknown month group name: '{first}' passed as a parameter to the method '{self.dual_names.__name__}'.")
        elif not isinstance(second, str):
            raise TypeError(
                f"ArabicDate class error: Unknown month group name: '{second}' passed as a parameter to the method '{self.dual_names.__name__}'.")
        elif not isinstance(east_nums, bool):
            raise TypeError(
                f"ArabicDate class error: east_nums must be a boolean. '{east_nums}' is not boolean and was passed to the method '{self.dual_names.__name__}'.")

        if first.strip().lower() == second.strip().lower():
            raise ValueError(
                f"ArabicDate class error: The first group name and the second group name sould not be identicial: '{first}' was passed as the first and the second parameter to the method {self.dual_names.__name__}. Note that these particular parameters are not case sensitive.")
        valid_first_group = False
        valid_second_group = False
        for group, _ in MONTH_GROUPS.items():
            if first.lower() in group:
                valid_first_group = True
        for group, _ in MONTH_GROUPS.items():
            if second.lower() in group:
                valid_second_group = True
        if not valid_first_group or not valid_second_group:
            error_submessage = ""
            if not valid_first_group:
                error_submessage += f"Unknown first groupe name  '{
                    first}'"
            if not valid_second_group:
                if error_submessage == "":
                    error_submessage += f"Unknown second groupe name '{
                        second}'"
                else:
                    error_submessage += f" and also unknown second groupe name '{
                        second}'"
            raise ValueError(
                f"ArabicDate class error: {error_submessage} in the parameters passed to the method '{self.dual_names.__name__}'.")

        if east_nums == True:
            return self.__day.translate(self.num_trans_table) + " " + MONTH_GROUPS[first]["months"][self.__month-1] + " (" + MONTH_GROUPS[second]["months"][self.__month-1] + ") " + self.__year.translate(self.num_trans_table)
        else:
            return self.__day + " " + MONTH_GROUPS[first]["months"][self.__month-1] + " (" + MONTH_GROUPS[second]["months"][self.__month-1] + ") " + self.__year

    # Date By Country Code Method
    def by_country_code(self, country_code: str, east_nums: bool = None) -> str:
        if not isinstance(country_code, str):
            raise TypeError(
                f"ArabicDate class error: The 'country_code' parameter passed to the class method '{self.by_country_code.__name__}' is not a string.")

        elif east_nums is not None and not isinstance(east_nums, bool):
            raise TypeError(
                f"ArabicDate class error: east_nums must be a boolean. '{east_nums}' is not boolean and was passed to the class method '{self.french_names.__name__}'.")

        for _, group in MONTH_GROUPS.items():
            if country_code.upper() in group["countries"]:
                if east_nums is not None and east_nums:
                    return self.__day.translate(self.num_trans_table) + " " + group["months"][self.__month-1] + " " + self.__year.translate(self.num_trans_table)
                elif east_nums is not None and not east_nums:
                    return self.__day + " " + group["months"][self.__month-1] + " " + self.__year
                else:
                    if group["east_nums"]:
                        return self.__day.translate(self.num_trans_table) + " " + group["months"][self.__month-1] + " " + self.__year.translate(self.num_trans_table)
                    else:
                        return self.__day + " " + group["months"][self.__month-1] + " " + self.__year

        else:
            raise ValueError(
                f"ArabicDate class error: Unknown country code '{country_code}' passed to the class method '{self.by_country_code.__name__}'.")

    # Eastern Numeric Date Method
    def eastern_numeric_date(self, separator: str = "/") -> str:
        if not isinstance(separator, str):
            raise TypeError(
                f"ArabicDate class error: The 'separator' parameter passed to the class method '{self.eastern_numeric_date.__name__}' is not a string.")
        return self.__day.translate(self.num_trans_table) + separator + str(self.__month).translate(self.num_trans_table) + separator + self.__year.translate(self.num_trans_table)
