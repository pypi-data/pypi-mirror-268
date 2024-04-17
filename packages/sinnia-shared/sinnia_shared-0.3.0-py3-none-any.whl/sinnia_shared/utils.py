### Version 0.1
import sys, os, logging, yaml, re
from datetime import time, timedelta, datetime, tzinfo, date

import pymysql

class Utils(object):
    
    DF      = "%Y-%m-%d"
    FULL_DF = "%Y-%m-%d %H:%M:%S"

    default_frmttr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    default_root_frmttr = '%(asctime)s - %(levelname)s - %(message)s'    
    #default_frmttr = '%(levelname)-5s - %(asctime)-15s %(message)s'    
    default_level = 'DEBUG'
    conf = dict()
    active_connections = dict()

    def init(self, conf_file_path, trace_enabled = False):
        self.trace_enabled = trace_enabled
        with open(conf_file_path) as conf_file:
            self.conf = yaml.load(conf_file, Loader=yaml.FullLoader)
        self.logger = logging.getLogger(__name__)
        print('Utils inited logger')
        print(self.logger)

    # def old_init(self, conf_file_path, trace_enabled = False):
    #     self.trace_enabled = trace_enabled
    #     with open(conf_file_path) as conf_file:
    #         self.conf = yaml.load(conf_file)
    #     self.log_file = self.conf.get("log_file", 'logs/default.log')
    #     d = os.path.dirname(self.log_file)
    #     if not os.path.exists(d):
    #         os.makedirs(d)
    #     frmt = self.conf.get("log_formatter", self.default_root_frmttr)
    #     self.frmttr = logging.Formatter(frmt)
    #     self.level = logging.getLevelName(
    #         self.conf.get('log_level', self.default_level)
    #     )
    #     logging.basicConfig(format=frmt,level=self.level,filename=self.log_file)
        
    # def old_init_logger(self, logger_name='root'):
    #     if logger_name != 'root':
    #         frmt = self.conf.get("log_formatter", self.default_frmttr)
    #         frmttr = logging.Formatter(frmt)
    #     else:
    #         frmttr = self.frmttr
    #     logger = logging.getLogger(logger_name)
    #     fh = logging.FileHandler(self.log_file, mode='a', encoding='utf8')
    #     fh.setFormatter(frmttr)
    #     fh.setLevel(self.level)
    #     logger.addHandler(fh)
    #     console_level = self.conf.get("log_to_console")
    #     if console_level:
    #         ch = logging.StreamHandler()
    #         ch.setFormatter(self.frmttr)
    #         ch.setLevel(logging.getLevelName(console_level))
    #         logger.addHandler(ch)
    #         logger.debug("console: {}".format(console_level))
    #     logger.debug("log_file: {}".format(self.log_file))            
    #     logger.debug("logger_name: {}".format(logger_name))
    #     logger.debug("Top Level Config: %s" % str(self.conf.keys()))        
    #     return logger
        
    def from_config(self, path):
        try:
            path_args = path.split('.')
            current = self.conf
            for arg in path_args:
                current = current.get(arg)
            return current
        except Exception as ex:
            self.logger.error("Error extracting from config for path '%s'", path)
            raise ex

    def get_conn(self, name, register_conn=True):
        if not register_conn:
            return self._open_conn(name)
        conn = self.active_connections.get(name)
        if not conn:
            #db_config = conf.get('db_config').get(name)
            conn = self._open_conn(name)
            if conn:
                self.active_connections[name] = conn
        return conn
    
    def _open_conn(self, name):
        db_config = self.from_config('db_config.' + name)
        if db_config:
            return pymysql.connect(
                host = db_config.get("host"),
                user = db_config.get("user"),
                password = db_config.get("passwd"),
                db = db_config.get("db"),
                charset = db_config.get("charset"),
                use_unicode = False)
        else:
            sys.exit("DB config not found for name '%s'" % name)
        return None
    
    def close_conn(self, name):
        conn = self.active_connections.get(name)
        if conn:
            conn.close()
            self.active_connections.pop(name)
        
    def get_active_connections(self):
        return self.active_connections.values()

    def close_active_connections(self):
        for conn in self.active_connections.values(): 
            conn.close()
        self.active_connections.clear()                                

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
                if isinstance(val, (int, long)):
                    return str(val)
                else:
                    if conn:
                        return "'%s'" % (conn.escape_string(str(val)))
                    else:
                        return "'%s'" % (str(val))
                                     #.replace('\\', "").replace("'", "\\'"))
            return default
        return map(mapper, row)

    # @staticmethod
    # def insert_mapper(row):
    #     for val in row:
    #         yield str(val) if isinstance(val, (int, long)) \
    #             else "'%s'" % str(val).replace("'", "\\'")

    def has_trace_enabled(self):
        return self.trace_enabled

    def response_as_json(self, r):
        if r.status_code == 400 or r.status_code != 200:
            self.logger.error('Error: %s' % str(r))
            return False
        if not r.encoding:
            r.encoding = 'utf-8'
        if self.has_trace_enabled():
            self.logger.debug('Json: %s...' % r.text[:500])
        return r.json()





    def get_date(self, s = None):
      d = self.get_date_from_string(s)
      if d == None:
        self.logger.info("Using yesterday as default")
        d = self.get_yesterday()
      return d

    def get_yesterday(self):
        return date.today() - timedelta(days = 1)

    def get_last_week(self):
        return date.today() - timedelta(days = 7)
        
    def get_start_end_delta_str(self, delta):
        date_from, date_to = self.get_start_end_delta_dates(delta)
        return (datetime.strftime(date_from, DF), datetime.strftime(date_to, DF))

    def get_start_end_str(self, str1, str2):
        date_from, date_to = self.get_start_end_dates(str1, str2)
        return (datetime.strftime(date_from, DF), datetime.strftime(date_to, DF))
            
    def get_start_end_delta_dates(self, delta):
      date_from = None
      date_to = None
      try:
        date_to = date.today()
        date_from = date_to - timedelta(days = delta)
        return (date_from, date_to)
      except Exception as e:
        self.logger.exception("Error obtaining start/end delta dates")  
        self.logger.exception(traceback.format_exc())  
        raise e

    def get_start_end_dates(self, str1, str2):
      date_from = None
      date_to = None
      try:
        date_from = datetime.strptime(str1, DF)
        date_to = datetime.strptime(str2, DF)
        if date_from > date_to:
            self.logger.exception("Error: date_from after date_to")
        return (date_from, date_to)
      except Exception as e:
        self.logger.exception("Error obtaining start/end dates") 
        self.logger.exception(traceback.format_exc())  
        raise e

    def remove_nonspacing_marks(self, s):
      "Normalizes the unicode string s and removes non-spacing marks."
      return ''.join(c for c in unicodedata.normalize('NFKD', s)
                       if unicodedata.category(c) != 'Mn')

    def boolean_str_to_int(self, x):
      as_int = 0
      if x:
        if x == True:
          as_int = 1 
      return as_int

    def get_number_from_string(self, s):
      "Validates that the input exactly matches a number (may be negative)"
      pattern = re.compile(r"-?\d+")
      matched = pattern.match(s)
      if matched: 
        g = matched.group(0)
        return int(g) 
      return None

    def get_twitter_ids_from_string(self, s):
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

    def get_youtube_ids_from_string(self, s):
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

    def get_date_from_string(self, s):
      "Validates that the input is a date and returns it"
      d = None
      if s:
        try:
          d = datetime.strptime(s, self.DF).date()
        except Exception as e1:
          try: 
            d = datetime.strptime(s, self.FULL_DF).date()
          except Exception as e2:
            self.logger.error("Error obtaining date from string: %s" % s)  
      return d

    def camel_case_to_snake_case(self, camel):
        return ''.join(['_' + c.lower() if c.isupper() else c.lower() for c in camel]).lstrip('_')
