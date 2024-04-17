#XLibrary/__init__.py
# -*- coding: utf-8 -*-
from robot.api.deco import keyword
from .main import MainClass
from .submodule1 import XPrint
from .submodule1 import XDrint
from .submodule2 import Module21
from .submodule2 import Module22


 
__all__ = [ 'XLibrary','MainClass', 'XPrint', 'XDrint','Module21', 'Module22']



class XLibrary(
    MainClass,
    XPrint, 
    XDrint,
    Module21,
    Module22
    ):
    """ 
    *` XLibrary เป็น Library Custom ขึ้้นมาใช้เองโดยเฉพาะ`*
    *`Create By Tassana Khrueawan`*
    """


    def TTTTTT(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบไม่ได้แอดคีย์ """
        print("Hello, world! เทสภาษาไทยfdsafadsfsadfdsafdsa")


    @keyword("Hello world12")
    def Hello12(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบแอดคีย์ """
        print("Hello, world! Test keyword='Hello, world!'")
