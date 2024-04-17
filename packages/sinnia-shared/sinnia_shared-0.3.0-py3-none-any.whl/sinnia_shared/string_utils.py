### Version 0.1
import logging, re
from datetime import time, timedelta, datetime, tzinfo, date

class StringUtils(object):
    
    DF      = "%Y-%m-%d"
    FULL_DF = "%Y-%m-%d %H:%M:%S"

    default_frmttr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    default_root_frmttr = '%(asctime)s - %(levelname)s - %(message)s'    
    #default_frmttr = '%(levelname)-5s - %(asctime)-15s %(message)s'    
    default_level = 'DEBUG'

    def init(conf_file_path, trace_enabled = False):
        self.trace_enabled = trace_enabled
        self.logger = logging.getLogger(__name__)
        print('Utils inited logger')
        print(self.logger)                      

    @staticmethod
    def daterange(start_date, end_date):
        n = -1
        for n in range(int ((end_date - start_date).days) - 1):
            ref_date = start_date + timedelta(n)
            yield (ref_date, ref_date + timedelta(1))
        if n == -1 :
            yield (start_date, end_date)
        else: 
            yield (start_date + timedelta(n + 1), end_date)

    @staticmethod
    def csv_mapper(row):
        return map(lambda val: val if val is not None else "NULL", row)

    @staticmethod
    def insert_mapper(row, default = "NULL", conn = None):
        def mapper(val):
            if val is not None:
                if isinstance(val, (int, float)):
                    return str(val)
                else:
                    if conn:
                        return f"'{conn.escape_string(str(val))}'"
                    else:
                        return f"'{str(val)}'"
            return default
        return map(mapper, row)

    @staticmethod
    def get_date(s, DF="%Y-%m-%d"):
      "Validates that the input is a date and returns it"
      try:
        return datetime.strptime(s, DF).date()
      except Exception as e1:
        raise Exception(f"Error obtaining date from string: {s}")  


    @staticmethod
    def get_yesterday():
      "Returns the date of yesterday"  
      return date.today() - timedelta(days = 1)
        
    @staticmethod
    def get_start_end_dates(str1, str2, DF="%Y-%m-%d"):
      "Validates that both strings are dates, where Str1 is before Str2, and returns them as a tuple"
      try:
        date_from = datetime.strptime(str1, DF).date()
        date_to = datetime.strptime(str2, DF).date()
        if date_from > date_to:
          raise Exception(f"Error: date_from cannot be after date_to")
        return (date_from.strftime(DF), date_to.strftime(DF))
      except ValueError as e:
        raise Exception(f"Error: Cannot parse input date")

    @staticmethod
    def remove_nonspacing_marks(s):
      "Normalizes the unicode string s and removes non-spacing marks."
      return ''.join(c for c in unicodedata.normalize('NFKD', s)
                       if unicodedata.category(c) != 'Mn')

    @staticmethod
    def boolean_str_to_int(x):
      as_int = 0
      if x:
        if x == True:
          as_int = 1 
      return as_int

    @staticmethod
    def get_number_from_string(s):
      "Validates that the input exactly matches a number (may be negative)"
      pattern = re.compile(r"-?\d+")
      matched = pattern.match(s)
      if matched: 
        g = matched.group(0)
        return int(g) 
      return None

    @staticmethod
    def get_twitter_ids_from_string(s):
      "Validates that the input is a series of comma-separated numbers (or a single number) and returns the matching part"
      s = re.sub(' ','', s)   # remove spaces
      s = re.sub(',$', '', s) # remove final comma, if any
      pattern = re.compile(r"[\d+,?\d+]+")
      searched = pattern.search(s)
      if searched:
        g = searched.group(0)
        s = re.sub(',$', '', g) # remove final comma, if any (may have been left behind after pattern matching)
        return s  
      return None

    @staticmethod
    def get_youtube_ids_from_string(s):
      "Validates that the input is a series of comma-separated youtube channel ids (or a single id) and returns the matching part"
      s = re.sub(' ','', s)   # remove spaces
      s = re.sub(',$', '', s) # remove final comma, if any
      pattern = re.compile(r"(UC[_0-9a-zA-Z]+[,]?)?")
      searched = pattern.search(s)
      if searched:
        g = searched.group()
        print(g)
        s = re.sub(',$', '', g) # remove final comma, if any (may have been left behind after pattern matching)
        return s
      return None

    @staticmethod
    def camel_case_to_snake_case(camel):
        return ''.join(['_' + c.lower() if c.isupper() else c.lower() for c in camel]).lstrip('_')
