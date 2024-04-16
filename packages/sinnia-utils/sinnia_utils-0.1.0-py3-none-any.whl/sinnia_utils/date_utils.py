### Version 0.1
from typing import Literal
import logging, re, unicodedata
from datetime import time, timedelta, datetime, date, timezone

class DateUtils(object):
    
    DF      = "%Y-%m-%d"
    FULL_DF = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def get_dates_in_range(start_date, end_date):
        "Yields a generator of the dates contained in the range"
        curr = start_date
        while curr < end_date:
            yield curr
            curr += timedelta(days=1)

        # # as defined in scripts/database/mig/lib/find_bugs.py
        # def _daterange(start_date, end_date):
        #      for n in range(int ((end_date - start_date).days)):
        #           yield start_date + timedelta(n)

    @staticmethod
    def get_date(s, DF="%Y-%m-%d") -> date:
        "Validates that the input is a date and returns it. If not provided, the default format is '%Y-%m-%d'"
        try:
            return datetime.strptime(s, DF).date()
        except ValueError as e:
            raise ValueError(f"Error: Could not parse input date with the formatting.")  

    # # # implementacion anterior (e instagram_utils); usaba defaults no evidentes, p.ej regresar yesterday por default, y usar DF default
    # def get_date(self, s = None):
    #   d = self.get_date_from_string(s)
    #   if d == None:
    #     self.logger.info("Using yesterday as default")
    #     d = self.get_yesterday()
    #   return d
    # def get_date_from_string(self, s):
    #   "Validates that the input is a date and returns it"
    #   d = None
    #   if s:
    #     try:
    #       d = datetime.strptime(s, self.DF).date()
    #     except Exception as e1:
    #       try: 
    #         d = datetime.strptime(s, self.FULL_DF).date()
    #       except Exception as e2:
    #         self.logger.error("Error obtaining date from string: %s" % s)  
    #   return d


    @staticmethod
    def get_yesterday() -> date:
        "Returns the date of yesterday"  
        return date.today() - timedelta(days = 1)
        
    @staticmethod
    def get_last_week():
        "Returns the date of 7 days ago"  
        return date.today() - timedelta(days = 7)
    
    @staticmethod
    def get_start_end_dates(date_from_str, date_to_str, DF="%Y-%m-%d") -> tuple[date, date]:
        "Validates that both strings are dates, where date_from_str is before date_to_str, and returns them as a tuple"
        try:
            date_from = datetime.strptime(date_from_str, DF).date()
            date_to = datetime.strptime(date_to_str, DF).date()
            if date_from > date_to:
                raise ValueError(f"Error: date_from cannot be after date_to")
            return (date_from, date_to)
        except ValueError as e:
            raise ValueError(f"Error: Could not parse input dates")
        
    # # as defined in scripts/instagram/ig/instagram_utils.py
    # def get_start_end_dates(self, str1, str2):
    # date_from = None
    # date_to = None
    # try:
    #   date_from = datetime.strptime(str1, DF)
    #   date_to = datetime.strptime(str2, DF)
    #   if date_from > date_to:
    #     self.logger.exception("Error: date_from after date_to")
    #   return (date_from, date_to)
    # except Exception as e:
    #   self.logger.exception("Error obtaining start/end dates")
    #   self.logger.exception(traceback.format_exc())
    #   raise e

    @staticmethod
    def timestamp_offset_to_utc(date_string) -> str:
        try:
            offset_format = "%Y-%m-%dT%H:%M:%S%z"
            utc_format = "%Y-%m-%d %H:%M:%S"
            tz_date = datetime.strptime(date_string, offset_format)
            utc_date = tz_date.astimezone(timezone.utc)
            return datetime.strftime(utc_date, utc_format)
        except Exception as e:
            raise ValueError(f"Error: Could not parse input dates")

    @staticmethod
    def utc_string_to_date(date_string) -> date:
        try:
            utc_format = "%Y-%m-%d %H:%M:%S"
            return datetime.strptime(date_string, utc_format).date()
        except Exception as e:
            raise ValueError(f"Error: Could not parse input dates")
