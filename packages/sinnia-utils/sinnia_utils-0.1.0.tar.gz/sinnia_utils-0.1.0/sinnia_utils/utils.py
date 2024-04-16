### Version 0.1
import sys, os, logging, yaml, re
from datetime import time, timedelta, datetime, tzinfo, date

import pymysql

class Utils(object):
    
    DF      = "%Y-%m-%d"
    FULL_DF = "%Y-%m-%d %H:%M:%S"

    default_frmttr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    default_root_frmttr = '%(asctime)s - %(levelname)s - %(message)s'    
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
                host = str(db_config.get("host")),
                user = str(db_config.get("user")),
                password = str(db_config.get("passwd")),
                database = str(db_config.get("db")),
                charset = str(db_config.get("charset")),
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

