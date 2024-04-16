"""
@Author: 馒头 (chocolate)
@Email: neihanshenshou@163.com
@File: selenium.py
@Time: 2023/12/9 18:00
"""

import platform
import warnings
from time import sleep, time

from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from SteamedBread import logger
from SteamedBread._Poium import config
from SteamedBread._Poium.config import Browser
from SteamedBread._Poium.universal.exceptions import PageElementError, FindElementTypesError, DriverNoneException
from SteamedBread._Poium.universal.selector import selection_checker

# Map PageElement constructor arguments to webdriver locator enums
LOCATOR_LIST = {
    # selenium
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,

}

BY_LIST = [
    # selenium
    By.CSS_SELECTOR,
    By.ID,
    By.NAME,
    By.XPATH,
    By.LINK_TEXT,
    By.PARTIAL_LINK_TEXT,
    By.TAG_NAME,
    By.CLASS_NAME
]


class BasePage:
    """
    Page Object pattern.
    """

    def __init__(self, driver=None, url: str = None, print_log: bool = False):
        """
        :param driver: `selenium.webdriver.WebDriver` Selenium webdriver instance
        :param url: `str`
        :param print_log: `bool` Need to be turned on when used with the seldom framework
        """
        self.driver = None
        if driver is not None:
            self.driver = driver
        else:
            ...

        if self.driver is None:
            raise DriverNoneException("driver is None, Please set selenium/appium driver.")
        self.root_uri = url if url else getattr(self.driver, 'url', None)
        config.printLog = print_log

    def get(self, uri: str) -> None:
        """
        go to uri
        :param uri: URI to GET, based off of the root_uri attribute.
        :return:
        """
        warnings.warn("use page.open() instead", DeprecationWarning, stacklevel=2)
        root_uri = self.root_uri or ''
        self.driver.get(root_uri + uri)
        self.driver.implicitly_wait(5)

    def open(self, uri: str) -> None:
        """
        open uri
        :param uri:  URI to GET, based off of the root_uri attribute.
        :return:
        """
        root_uri = self.root_uri or ''
        self.driver.get(root_uri + uri)
        logger.info(f'正在进入【{uri}】网站')
        self.driver.implicitly_wait(5)


class Element(object):
    """
    Returns an element object
    """

    def __init__(self,
                 selector: str = None,
                 id_: str = "",
                 name: str = "",
                 css: str = "",
                 xpath: str = "",
                 class_name: str = "",
                 timeout: int = 3,
                 describe: str = "",
                 index: int = 0,
                 **kwargs):
        self.selector = selector
        self.times = timeout
        self.index = index
        self.desc = describe
        self.exist = False

        if selector is not None:
            self.k, self.v = selection_checker(selector)
        else:
            if id_:
                kwargs['id_'] = id_
            elif name:
                kwargs['name'] = name
            elif css:
                kwargs['css'] = css
            elif xpath:
                kwargs['xpath'] = xpath
            elif class_name:
                kwargs['class_name'] = class_name
            if not kwargs:
                raise ValueError(f"Please specify a locator from {LOCATOR_LIST}")
            if len(kwargs) > 1:
                raise ValueError(f"Please specify only one locator from {LOCATOR_LIST}")
            self.kwargs = kwargs
            by, self.v = next(iter(kwargs.items()))

            self.k = LOCATOR_LIST.get(by, None)
            if self.k is None:
                raise FindElementTypesError("Element positioning of type '{}' is not supported.".format(self.k))

    def __get__(self, instance, owner):
        if instance is None:
            return None

        Browser.driver = instance.driver
        return self

    def __set__(self, instance, value):
        self.__get__(instance, instance.__class__)
        self.send_keys(value)

    @func_set_timeout(1)
    def find_elements_timeout(self, key: str, value: str):
        return Browser.driver.find_elements(key, value)

    def find(self, by: str, value: str) -> list:
        """
        Find if the element exists.
        """
        for i in range(self.times):
            try:
                elems = self.find_elements_timeout(by, value)
                break
            except FunctionTimedOut:
                sleep(1)
        else:
            elems = []

        if len(elems) == 1:
            logger.info(f"🔍 Find element: {by}={value}. {self.desc}")
        elif len(elems) > 1:
            logger.info(f"❓ Find {len(elems)} elements through: {by}={value}. {self.desc}")
        else:
            logger.warning(f"❌ Find 0 elements through: {by}={value}. {self.desc}")

        return elems

    def __get_element(self, by: str, value: str):
        """
        Judge element positioning way, and returns the element.
        """

        if by in BY_LIST:
            elem = self.find(by, value)
            if len(elem) == 0:
                self.exist = False
                return None
            else:
                self.exist = True
                elem = Browser.driver.find_elements(by, value)[self.index]
        else:
            raise FindElementTypesError("Please enter the correct targeting elements")

        if Browser.show is True:
            try:
                style_red = 'arguments[0].style.border="2px solid #FF0000"'
                style_blue = 'arguments[0].style.border="2px solid #00FF00"'
                style_null = 'arguments[0].style.border=""'

                for _ in range(2):
                    Browser.driver.execute_script(style_red, elem)
                    sleep(0.1)
                    Browser.driver.execute_script(style_blue, elem)
                    sleep(0.1)
                Browser.driver.execute_script(style_blue, elem)
                sleep(0.1)
                Browser.driver.execute_script(style_null, elem)
            except WebDriverException:
                pass

        return elem

    def is_exist(self) -> bool:
        """element is existed """
        self.__get_element(self.k, self.v)
        return self.exist

    def clear(self) -> None:
        """Clears the text if it's a text entry element."""
        logger.info("✅ clear.")
        elem = self.__get_element(self.k, self.v)
        elem.clear()

    def send_keys(self, value, clear=False, click=False) -> None:
        """
        Simulates typing into the element.
        If clear_before is True, it will clear the content before typing.
        """
        elem = self.__get_element(self.k, self.v)
        if click is True:
            elem.click()
            sleep(0.3)
            logger.info(f"✅ click().")
        if clear is True:
            elem.clear()
            sleep(0.3)
            logger.info(f"✅ clear().")
        elem.send_keys(value)
        logger.info(f"✅ send_keys('{value}').")

    def click(self) -> None:
        """
        Clicks the element.
        """
        elem = self.__get_element(self.k, self.v)
        elem.click()
        logger.info(f"✅ click().")

    def submit(self):
        """
        Submits a form.
        """
        elem = self.__get_element(self.k, self.v)
        elem.submit()
        logger.info(f"✅ submit().")

    @property
    def tag_name(self) -> str:
        """This element's ``tagName`` property."""
        elem = self.__get_element(self.k, self.v)
        tag_name = elem.tag_name
        logger.info(f"✅ tag_name: {tag_name}.")
        return tag_name

    @property
    def text(self) -> str:
        """The text of the element."""
        elem = self.__get_element(self.k, self.v)
        text = elem.text
        logger.info(f"✅ text: {text}.")
        return text

    @property
    def size(self) -> dict:
        """The size of the element."""
        elem = self.__get_element(self.k, self.v)
        size = elem.size
        logger.info(f"✅ size: {size}.")
        return size

    def value_of_css_property(self, property_name):
        """
        The value of a CSS property
        :param property_name:
        """
        elem = self.__get_element(self.k, self.v)
        property_value = elem.value_of_css_property(property_name)
        logger.info(f"✅ value_of_css_property('{property_name}') -> {property_value}.")
        return property_value

    def get_property(self, name) -> str:
        """
        Gets the given property of the element.
        """
        elem = self.__get_element(self.k, self.v)
        value = elem.get_property(name)
        logger.info(f"✅ get_property('{name}') -> {value}.")
        return value

    def get_attribute(self, name) -> str:
        """
        Gets the given attribute or property of the element.
        """
        elem = self.__get_element(self.k, self.v)
        value = elem.get_attribute(name)
        logger.info(f"✅ get_property('{name}') -> {value}.")
        return value

    def is_displayed(self) -> bool:
        """Whether the element is visible to a user."""
        elem = self.__get_element(self.k, self.v)
        display = elem.is_displayed()
        logger.info(f"✅ is_displayed() -> {display}.")
        return display

    def is_selected(self):
        """
        Returns whether the element is selected.

        Can be used to check if a checkbox or radio button is selected.
        """
        elem = self.__get_element(self.k, self.v)
        select = elem.is_selected()
        logger.info(f"✅ is_selected() -> {select}.")
        return select

    def is_enabled(self):
        """Returns whether the element is enabled."""
        elem = self.__get_element(self.k, self.v)
        enable = elem.is_enabled()
        logger.info(f"✅ is_enabled() -> {enable}.")
        return enable

    def switch_to_frame(self) -> None:
        """
        selenium API
        Switches focus to the specified frame
        """
        elem = self.__get_element(self.k, self.v)
        Browser.driver.switch_to.frame(elem)
        logger.info(f"✅ switch_to_frame().")

    def move_to_element(self) -> None:
        """
        selenium API
        Moving the mouse to the middle of an element
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).move_to_element(elem).perform()
        logger.info(f"✅ move_to_element().")

    def click_and_hold(self) -> None:
        """
        selenium API
        Holds down the left mouse button on an element.
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).click_and_hold(elem).perform()
        logger.info(f"✅ click_and_hold().")

    def double_click(self) -> None:
        """
        selenium API
        Holds down the left mouse button on an element.
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).double_click(elem).perform()
        logger.info(f"✅ double_click().")

    def context_click(self) -> None:
        """
        selenium API
        Performs a context-click (right click) on an element.
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).context_click(elem).perform()
        logger.info(f"✅ double_click().")

    def drag_and_drop_by_offset(self, x: int, y: int) -> None:
        """
        selenium API
        Holds down the left mouse button on the source element,
           then moves to the target offset and releases the mouse button.
        :param x: X offset to move to.
        :param y: Y offset to move to.
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).drag_and_drop_by_offset(elem, xoffset=x, yoffset=y).perform()
        logger.info(f"✅ drag_and_drop_by_offset('{x}', '{y}').")

    def refresh_element(self, timeout: int = 5) -> None:
        """
        selenium API
        Refreshes the current page, retrieve elements.
        """
        elem = self.__get_element(self.k, self.v)
        for i in range(timeout):
            if elem is not None:
                try:
                    elem
                except StaleElementReferenceException:
                    Browser.driver.refresh()
                else:
                    break
            else:
                sleep(1)
        else:
            raise TimeoutError("stale element reference: element is not attached to the page document.")

    def select_by_value(self, value: str) -> None:
        """
        selenium API
        Select all options that have a value matching the argument. That is, when given "foo" this
           would select an option like:

           <option value="foo">Bar</option>

           :Args:
            - value - The value to match against

           throws NoSuchElementException If there is no option with specisied value in SELECT
        """
        select_elem = self.__get_element(self.k, self.v)
        Select(select_elem).select_by_value(value)
        logger.info(f"✅ select_by_value('{value}').")

    def select_by_index(self, index: int) -> None:
        """
        selenium API
        Select the option at the given index. This is done by examing the "index" attribute of an
           element, and not merely by counting.

           :Args:
            - index - The option at this index will be selected

           throws NoSuchElementException If there is no option with specisied index in SELECT
        """
        select_elem = self.__get_element(self.k, self.v)
        Select(select_elem).select_by_index(index)
        logger.info(f"✅ select_by_index('{index}').")

    def select_by_visible_text(self, text: str) -> None:
        """
        selenium API
        Select all options that display text matching the argument. That is, when given "Bar" this
           would select an option like:

            <option value="foo">Bar</option>

           :Args:
            - text - The visible text to match against

            throws NoSuchElementException If there is no option with specisied text in SELECT
        """
        select_elem = self.__get_element(self.k, self.v)
        Select(select_elem).select_by_visible_text(text)
        logger.info(f"✅ select_by_visible_text('{text}').")

    def set_text(self, keys):
        """
        appium API
        Sends text to the element.
        """
        elem = self.__get_element(self.k, self.v)
        elem.set_text(keys)
        logger.info(f"✅ set_text('{keys}').")
        return self

    @property
    def location_in_view(self):
        """
        appium API
        Gets the location of an element relative to the view.
        Returns:
            dict: The location of an element relative to the view
        """
        elem = self.__get_element(self.k, self.v)
        location = elem.location_in_view
        logger.info(f"✅ location_in_view -> {location}.")
        return location

    def set_value(self, value: str):
        """
        appium API
        Set the value on this element in the application
        """
        elem = self.__get_element(self.k, self.v)
        elem.set_value(value)
        logger.info(f"✅ set_value('{value}').")
        return self

    def input(self, text="") -> None:
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(text)
        logger.info(f"🎹 input('{text}').")

    def enter(self) -> None:
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.ENTER)
        logger.info(f"🎹 enter.")

    def select_all(self) -> None:
        elem = self.__get_element(self.k, self.v)
        if platform.system().lower() == "darwin":
            elem.send_keys(Keys.COMMAND, "a")
        else:
            elem.send_keys(Keys.CONTROL, "a")
        logger.info(f"🎹 control + a.")

    def cut(self) -> None:
        elem = self.__get_element(self.k, self.v)
        if platform.system().lower() == "darwin":
            elem.send_keys(Keys.COMMAND, "x")
        else:
            elem.send_keys(Keys.CONTROL, "x")
        logger.info(f"🎹 control + x.")

    def copy(self) -> None:
        elem = self.__get_element(self.k, self.v)
        if platform.system().lower() == "darwin":
            elem.send_keys(Keys.COMMAND, "c")
        else:
            elem.send_keys(Keys.CONTROL, "c")
        logger.info(f"🎹 control + c.")

    def paste(self) -> None:
        elem = self.__get_element(self.k, self.v)
        if platform.system().lower() == "darwin":
            elem.send_keys(Keys.COMMAND, "v")
        else:
            elem.send_keys(Keys.CONTROL, "v")
        logger.info(f"🎹 control + v.")

    def backspace(self) -> None:
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.BACKSPACE)
        logger.info(f"🎹 backspace.")

    def delete(self) -> None:
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.DELETE)
        logger.info(f"🎹 delete.")

    def tab(self) -> None:
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.TAB)
        logger.info(f"🎹 tab.")

    def space(self) -> None:
        elem = self.__get_element(self.k, self.v)
        elem.send_keys(Keys.SPACE)
        logger.info(f"🎹 space.")

    def screenshots(self, filename=None):
        """
        selenium API
        Saves a screenshots of the current element to a PNG image file
        :param filename: The file name
        """

        if filename is None:
            filename = str(time()).split(".")[0] + ".png"
        elem = self.__get_element(self.k, self.v)
        elem.screenshot(filename)
        logger.info(f"✅ screenshot.")


class Elements(object):
    """
    Returns a set of element objects
    """

    def __init__(self,
                 selector: str = None,
                 id_: str = "",
                 name: str = "",
                 css: str = "",
                 xpath: str = "",
                 class_name: str = "",
                 context: bool = False,
                 describe: str = "",
                 timeout: int = 3,
                 **kwargs):
        self.desc = describe
        self.times = timeout
        if selector is not None:
            self.k, self.v = selection_checker(selector)
        else:
            if id_:
                kwargs['id_'] = id_
            elif name:
                kwargs['name'] = name
            elif css:
                kwargs['css'] = css
            elif xpath:
                kwargs['xpath'] = xpath
            elif class_name:
                kwargs['class_name'] = class_name
            if not kwargs:
                raise ValueError("Please specify a locator")
            if len(kwargs) > 1:
                raise ValueError("Please specify only one locator")
            by, self.v = next(iter(kwargs.items()))

            self.k = LOCATOR_LIST.get(by, None)
            if self.k is None:
                raise FindElementTypesError("Element positioning of type '{}' is not supported.".format(self.k))

        self.has_context = bool(context)

    def find(self, context):
        for i in range(self.times):
            elems = context.find_elements(self.k, self.v)
            if len(elems) > 0:
                break
            else:
                sleep(1)
        else:
            elems = []

        logger.info(f"✨ Find {len(elems)} elements through: {self.k}={self.v}. {self.desc}")
        return elems

    def __get__(self, instance, owner, context=None):
        if not instance:
            return None

        if not context and self.has_context:
            return lambda ctx: self.__get__(instance, owner, context=ctx)

        if not context:
            context = instance.driver

        return self.find(context)

    def __set__(self, instance, value):
        if self.has_context:
            raise PageElementError("Sorry, the set descriptor doesn't support elements with context.")
        elems = self.__get__(instance, instance.__class__)
        if not elems:
            raise PageElementError("Can't set value, no elements found")
        [elem.send_keys(value) for elem in elems]
