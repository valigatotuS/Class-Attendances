# -*- coding: utf-8 -*-
import os

class Config(object):
    # cryptographic key, useful to generate signatures or tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'admin'
    DB_PATHS = {"database":"src/db.sqlite",
                "init": "files/init_db.txt",
                "tables":  "files/rows/"}
    
    