# -*- coding: utf-8 -*-
# (C) Run, Inc. 2022
# All rights reserved (Author BinZHU)
# Licensed under Simplified BSD License (see LICENSE)

import os
import sys
import logging
from logging.handlers import RotatingFileHandler

def get_logger (filename, 
                rotating=True, 
                verbosity=1, 
                name=None):
    r'''Define C type logging method`.
    
    :param filename: filename where logs are stored.
    :param verbosity: whether verbosity infos are required.
    :param name: name of logger
    :return: logger instance with usage logger.info(msg)
    '''
    level_dcit = {
        0: logging.DEBUG,
        1: logging.INFO,
        2: logging.WARNING
    }
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s][line:%(lineno)d][%(levelname)s] %(message)s"
    )
    logger = logging.getLogger(name)
    logger.setLevel(level_dcit[verbosity])
    
    if not filename.startswith("/"):
        save_path = os.path.join(os.getcwd(), '/logs/')
        filename = save_path + filename
    file_handle = logging.FileHandler(filename, "w")
    if rotating:
        file_handle = RotatingFileHandler (filename=filename, 
                                           maxBytes=1024*1024*100, 
                                           backupCount=10)  
    file_handle.setFormatter(formatter)
    logger.addHandler(file_handle)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger