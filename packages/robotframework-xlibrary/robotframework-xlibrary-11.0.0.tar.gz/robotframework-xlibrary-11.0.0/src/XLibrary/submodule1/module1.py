# -*- coding: utf-8 -*-
from robot.api.deco import keyword
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from AppiumFlutterLibrary import AppiumFlutterLibrary
from .module2 import XDrint
from AppiumFlutterLibrary.finder import ElementFinder
import time


class XPrint(AppiumFlutterLibrary):
    def __init__(self):
        super().__init__()
        self._ne = XDrint()
        self._bi = BuiltIn()
        self.finder = ElementFinder()


    @keyword("XPrint Log")
    def XPrint_log(self):
        print("Hello, world! เทสภาษาไทย111")

    def TestModule2(self):
        instance = XDrint()  
        instance.CDCDCD()   
        self._ne.CDCDCD() 

    def XQuit_App(self):
        """ปิดแอพปัจจุบันและปิดเซสชัน"""
        driver = self._current_application()
        driver.quit()

    @keyword('Switch Mode')
    def Switch_Mode(self, mode):
        """Switch Mode to NATIVE_APP OR FLUTTER."""
        driver = self._current_application()
        if mode == 'NATIVE_APP':
            driver.switch_to.context('NATIVE_APP')
        elif mode == 'FLUTTER':  # Changed from 'if' to 'elif' for logical correctness
            driver.switch_to.context('FLUTTER')

    def _current_application(self):
        """คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน"""
        return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()

    @keyword('Is Button Active')
    def is_button_active(self, key):
        """ตรวจสอบว่าปุ่มที่มีคีย์ที่กำหนดให้นั้น active ในแอปพลิเคชัน Flutter หรือไม่"""
        try:
            driver = self._current_application() # มีการเพิ่มเข้ามา
            # button = self.finder.by_value_key(key)
            # element = driver.find_element(button)  # ลบ self
            element = self.finder.find(driver,key)
            is_visible = element.is_displayed()
            is_enabled = element.is_enabled()
            if is_visible and is_enabled:
                logger.info(f"ปุ่มที่มีคีย์ '{key}' นั้น active และมองเห็นได้.")
                return True
            else:
                if not is_visible:
                    logger.warn(f"ปุ่มที่มีคีย์ '{key}' นั้นมองไม่เห็น.")
                if not is_enabled:
                    logger.warn(f"ปุ่มที่มีคีย์ '{key}' นั้นไม่สามารถใช้งานได้.")
                return False
        except Exception as e:
            logger.error(f"มีข้อผิดพลาดในการตรวจสอบว่าปุ่ม active: {e}")
            return False

    @keyword('Wait Until Button Is Active')
    def wait_until_button_is_active(self, key, timeout=10):
        """รอจนกว่าปุ่มที่มีคีย์ที่กำหนดจะ active ในแอปพลิเคชัน Flutter"""
        end_time = time.time() + timeout
        while time.time() < end_time:
            if self.is_button_active(key):
                return True
            time.sleep(1)

        logger.warn(f"ปุ่มที่มีคีย์ '{key}' ไม่ได้กลายเป็น active ภายในเวลา {timeout} วินาที.")
        return False

    @keyword('Switch To Flutter Context')
    def switch_to_flutter_context(self):
        """เปลี่ยนไปยัง Context ของ Flutter ก่อนที่จะพยายามค้นหา elements."""
        driver = self._current_application()
        available_contexts = driver.contexts
        for context in available_contexts:
            if 'FLUTTER' in context:
                driver.switch_to.context(context)
                return
        logger.warn("ไม่พบ Context ของ Flutter.")
