# submodule2/module1.py
# -*- coding: utf-8 -*-
import logging
from robot.api.deco import keyword

class Module21:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    def PrintTEST21(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบไม่ได้แอดคีย์ """
        print("Hello, world! เทสภาษาไทย111")

    def log_tree_structure(self, data, level=0, prefix=''):
        indent = "│   " * level
        branch = "├── " if level > 0 else ""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    logging.info(f"{indent}{branch}{key}")
                    self.log_tree_structure(value, level + 1)
                else:
                    logging.info(f"{indent}{branch}{key}: {value}")
        elif isinstance(data, list):
            for i, item in enumerate(data):
                logging.info(f"{indent}├── [{i}]")
                self.log_tree_structure(item, level + 1)
        else:
            logging.info(f"{indent}{branch}{prefix}{data}")

    @keyword("Log Tree Data")
    def log_tree_data(self, data):
        """ 
        ***|    Description     |***
        |   *`Log Tree Data`*   |   เป็น Keyword สำหรับ Log Data ให้ออกมาเป็น Tree Data |


        ***|    Example     |***
        | *`Log Tree Data`* | *`${value}`* |
        

        ***|    Parameters     |***
            - **`data`**  ข้อมูล Json.


       *`Create By Tassana Khrueawan`*
        """
        self.log_tree_structure(data)
