#submodule1/module2.py
# -*- coding: utf-8 -*-
from robot.api.deco import keyword
import ast
import pymongo
import logging

class XDrint:
    def CDCDCD(self):
        print("Hello, world! เทสภาษาไทย222")

    @keyword("XConnect Mongodb With URL")
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
    
    @keyword("XQuery MongoDB")
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
      
    
    @keyword("XQuery Dynamic Value")
    def query_dynamic_value(self, result, field='None', value='None', expect=None):
        """
        ***|    Description     |***
        |   *`XQuery Dynamic Value`*   |   เป็น Keyword สำหรับ Query ข้อมูลใน Collection แบบเจาะลงไป |

        
        ***|    Example     |***
        | *`${arpu_value}`* | *`XQuery Dynamic Value`* | *`result`* | *`productCharacteristic`* | *`name`* | *`arpu`* |
        | *`Log`* | *`${arpu_value}`* |

        
        ***|    Parameters     |***
            - **`result`**  ยังไม่ได้ใส่รายละเอียด
            - **`field`**   ยังไม่ได้ใส่รายละเอียด
            - **`value`**   ยังไม่ได้ใส่รายละเอียด
	        - **`expect`**  ยังไม่ได้ใส่รายละเอียด


        *`Create By Tassana Khrueawan`*
        """
        for item in result:
            if field in item and isinstance(item[field], list):
                if expect:
                    for char in item[field]:
                        if char.get(value) == expect:
                            return char.get('value')
                else:
                    return item[field]
        return None

    @keyword("XQuery Specific Value")
    def query_specific_value(self, result, field_name=None):
        """
        ***|    Description     |***
        |   XQuery Specific Value   |   Keyword สำหรับ Query ข้อมูลใน Collection แบบไม่เจาะลงไป |

        
        ***|    Example     |***
        | *`${name}`* | *`XQuery Specific Value`* | *`result`* | *`name`* |
        | *`Log`* | *`${name}`* |


        ***|    Parameters     |***
            - **`result`**  ยังไม่ได้ใส่รายละเอียด
            - **`field_name`**   ยังไม่ได้ใส่รายละเอียด


        *`Create By Tassana Khrueawan`*
        """
        if not field_name:
            return result

        results = []
        if isinstance(result, list):
            for doc in result:
                if isinstance(doc, dict) and field_name in doc:
                    results.append(doc[field_name])
        else:
            results = result.get(field_name, None)

        return results
