# -*- coding: utf-8 -*-
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from .module2 import XDrint
from AppiumFlutterLibrary.finder import ElementFinder

class XPrint:
    def __init__(self):
        super().__init__()
        self._ne = XDrint()
        self._bi = BuiltIn()
        self.finder = ElementFinder()


    @keyword("XPrint Log")
    def XPrint_log(self):
        print("Hello, world! ,สวัสดีชาวโลก เทสภาษาไทย")

    def TestModule2(self):
        instance = XDrint()  
        instance.CDCDCD()   
        self._ne.CDCDCD() 

    def XQuit_App(self):
        """ปิดแอพปัจจุบันและปิดเซสชัน"""
        driver = self._current_application()
        driver.quit()

    @keyword('XSwitch Mode')
    def XSwitch_Mode(self, mode):
        """Switch Mode to NATIVE_APP OR FLUTTER."""
        driver = self._current_application()
        if mode == 'NATIVE':
            driver.switch_to.context('NATIVE_APP')
        elif mode == 'FLUTTER':
            driver.switch_to.context('FLUTTER')

    def _current_application(self):
        """คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน"""
        return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()


