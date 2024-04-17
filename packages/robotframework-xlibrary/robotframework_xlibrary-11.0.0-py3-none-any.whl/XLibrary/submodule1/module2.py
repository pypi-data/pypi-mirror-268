#submodule1/module2.py
# -*- coding: utf-8 -*-
from robot.api.deco import keyword
import ast
import pymongo
import logging

class XDrint:
    def CDCDCD(self):
        print("Hello, world! เทสภาษาไทย222")

    @keyword("Connect Mongodb With URL")
    def connect_to_mongodb_with_uri(self, dbURI, timeout=10):
        """
        ***|    Description     |***
        | *`Connect Mongodb With URL`* | เป็น Keyword ไว้เชื่อมต่อกับ MongoDB โดยใช้ URI โดยเฉพาะ |

        
        ***|    Example     |***
        | *`Connect Mongodb With URL`* | *`mongodb+srv://username:password@host`* | *`timeout=10`* |
        

        ***|    Parameters     |***
            - **`dbURI`**  URL สำหรับการเชื่อมต่อไปยัง MongoDB.
            - **`timeout`**  ตั้งเวลา TimeOut ในการเชื่อมต่อไปยัง MongoDB.

            
       *`Create By Tassana Khrueawan`*
        """
        try:
            self._dbconnection = pymongo.MongoClient(dbURI, serverSelectionTimeoutMS=timeout*1000)
            self._dbconnection.server_info()
            logging.debug("| Succeed: เชื่อมต่อกับ MongoDB โดยใช้ URI | %s |" % dbURI)
        except pymongo.errors.ServerSelectionTimeoutError as e:
            logging.error("| Fail: การเชื่อมต่อ MongoDB ล้มเหลว เนื่องจาก TimeOut | %s |" % str(e))
            raise Exception("การเชื่อมต่อ MongoDB ล้มเหลว เนื่องจาก TimeOut")
        except Exception as e:
            logging.error("| Fail: การเชื่อมต่อ MongoDB ล้มเหลว | %s |" % str(e))
            raise Exception("การเชื่อมต่อ MongoDB ล้มเหลว: " + str(e))
    
    @keyword("Query MongoDB")
    def query_mongodb(self, database_name, collection_name, query):
        """
        ***|    Description     |***
        |   *`Query MongoDB`*   |   เป็น Keyword สำหรับ Query ข้อมูลใน Collection จะได้ทั้งก้อนออกมา |

        
        ***|    Example     |***
        | *`${result}`* | *`Query MongoDB`* | *`database_name`* | *`collection_name`* | *`Command Query`* | 
        | *`Log`* | *`${result}`* |


        ***|    Parameters     |***
            - **`database_name`**  Database NAME.
            - **`collection_name`**  Collection NAME.
	    - **`query`**  คำสั่ง Query.


        *`Create By Tassana Khrueawan`*
        """
        collection = self._dbconnection[database_name][collection_name]
        query_dict = ast.literal_eval(query)
        result = collection.find(query_dict)
        return list(result)
      
    
    @keyword("Query Dynamic Characteristic Value")
    def query_dynamic_characteristic_value(self, result_list, key='None', characteristic_name=None):
        """
        ***คำอธิบาย Description***
        |   Query Dynamic Characteristic Value   |   Keyword สำหรับ Query ข้อมูลใน key ที่กำหนดและได้ Value ของลักษณะที่ต้องการ |

        ***ตัวอย่างการใช้งาน Example***
        | ${value} =  Query Dynamic Characteristic Value  ${result}  key  characteristic_name |
        | key คือชื่อของ field ที่มีลักษณะสินค้า เช่น productCharacteristic |
        | characteristic_name เช่น number, ratingType, arpu หรือเป็น None ถ้าต้องการทั้ง object |
        | Log  ${value} |
        """
        for item in result_list:
            if key in item and isinstance(item[key], list):
                if characteristic_name:
                    for char in item[key]:
                        if char.get('name') == characteristic_name:
                            return char.get('value')
                else:
                    return item[key]
        return None  

    @keyword("Query Specific Field Value")
    def query_specific_field_value(self, document, field_name=None):
        """
        ***คำอธิบาย Description***
        |   Query Specific Field Value   |   Keyword สำหรับ Query ข้อมูลจาก field ที่กำหนดใน document |

        ***ตัวอย่างการใช้งาน Example***
        | ${value} = Query Specific Field Value ${document} field_name |
        | field_name เป็นชื่อของ field ที่ต้องการค่า เช่น name, status, productCharacteristic เป็นต้น |
        | หากไม่ระบุ field_name จะ return ทั้ง document |
        | Log ${value} |
        """
        # Return the whole document if no field_name is provided
        if not field_name:
            return document
        
        # If field_name is provided, navigate through the document to find the value
        value = document.get(field_name, None)

        # If field_name refers to a list of dictionaries, we may need to handle it differently
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            return [item.get('value', None) for item in value if 'value' in item]

        return value