# =============================================================================
# INFORMATION ABOUT CODE         Coding: ISO 9001:2015
# =============================================================================
# IRCTC Automation with GUI
# For booking Tatkal or General ticket with COD option.(Verified)
# Change tkinter name in Python 2
# Author: Prajinkya Pimpalghare
# Date: 2-November-2017
# Version: 1.0
# Input Variable: From GUI. All fields are mandatory
# Note: Please put same station name as well as date mentioned in IRCTC.
# Basic Requirement Selenium module, and Web driver for chrome
# =============================================================================

import time
from tkinter import Frame, Tk, Label, Entry, E, Button, LEFT
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class BookingGui(Frame):
    def __init__(self, master, labels):
        """
        For Creating interactive GUI for IRCTC automation
        :param master:
        :param labels:
        """
        super().__init__(master)
        self.label = labels
        self.passenger = ["PassengersDetail:", "Psg:One", "Psg:Two", "Psg:Three", "Psg:Four"]
        self.entry = {}
        self.values = {}

    def main_gui(self):
        """
        For creating interactive GUI for IRCTC Automation
        """
        for label_index, label_value in enumerate(self.label):
            Label(self, text=label_value).grid(row=label_index + 1, column=0)
            self.entry[label_value] = Entry(self, show="*") if label_value == "Password" else Entry(self)
            self.entry[label_value].grid(row=label_index + 1, column=1)
        
        for passenger_index, passenger_label in enumerate(self.passenger):
            Label(self, text=passenger_label).grid(row=10, column=passenger_index)
        
        for index, value in enumerate(self.label[10:], start=12):
            Label(self, text=value).grid(row=index, column=0)
            for extra_index in range(4):
                self.entry[value + str(extra_index)] = Entry(self)
                self.entry[value + str(extra_index)].grid(row=index, column=extra_index + 1)
        
        Button(self, text="Book Tatkal Ticket", command=self._login_btn_clicked).grid(row=5, column=3)

    def _login_btn_clicked(self):
        """
        It will start the portal with provided value
        """
        for label in self.label[:10]:
            self.values[label] = self.entry[label].get()
        
        for temp_index in self.label[10:]:
            for extra_index in range(4):
                self.values[temp_index + str(extra_index)] = self.entry[temp_index + str(extra_index)].get()
        
        booking = Booking(self.values)
        booking.main()

class Booking:
    def __init__(self, values):
        """
        It will hold the main class for executing Chrome Browser
        :param values:
        """
        self.browser = None
        self.values = values

    def main(self):
        """
        It will be having main script for Chrome automation
        """
        try:
            self.browser = webdriver.Chrome()
            self.browser.get("https://www.irctc.co.in/nget/train-search")
            login_page = self.browser.find_element("id", "loginFormId")
            login_page.find_element("id", "usernameId").send_keys(self.values["UserID"])
            login_page.find_element("name", "j_password").send_keys(self.values["Password"])
            time.sleep(10)
            login_page.find_element("id", "loginbutton").click()
            main_page = self.browser.find_element("class name", "container")
            main_page.find_element("id", "quickbookTab:header:inactive").click()
            main_page.find_element("id", "qbform:trainNUmber").send_keys(self.values["TrainNo"])
            main_page.find_element("id", "qbform:fromStation").send_keys(self.values["FromStation"])
            main_page.find_element("id", "qbform:toStation").send_keys(self.values["ToStation"])
            main_page.find_element("id", "qbform:qbJrnyDateInputDate").send_keys(self.values["Date"])
            main_page.find_element("id", "qbform:class").send_keys(self.values["Class"])
            main_page.find_element("id", "qbform:quota").send_keys(self.values["Quota"])
            main_page.find_element("id", "qbform:quickBookSubmit").click()
            for index in range(3):
                self.browser.find_element("id",
                    f"addPassengerForm:psdetail:{index}:j_idt567").find_element("tag name",
                    "input").send_keys(
                    self.values[f"Name{index}"])
                self.browser.find_element("id", f"addPassengerForm:psdetail:{index}:psgnAge").send_keys(
                    self.values[f"Age{index}"])
                self.browser.find_element("id", f"addPassengerForm:psdetail:{index}:psgnGender").send_keys(
                    self.values[f"Gender{index}"])
                self.browser.find_element("id", "addPassengerForm:mobileNo").send_keys(self.values["MobileNo"])
            self.browser.find_element("id", "nlpAnswer").send_keys("")
            time.sleep(10)
            self.browser.find_element("id", "COD").click()
            self.browser.find_elements("css selector", "input[type='radio'][value='100']")[0].click()
            self.browser.find_element("id", "validate").click()
            exit(0)
        except BaseException as error:
            raise error

if __name__ == '__main__':
    FIELDS = ["UserID", "Password", "TrainNo", "FromStation", "ToStation", "Date", "Class", "Quota",
              "MobileNo", "PassengersDetail:", "Name", "Age", "Gender"]
    ROOT = Tk()
    BOOKING = BookingGui(ROOT, FIELDS)
    BOOKING.main_gui()
    BOOKING.pack(side=LEFT)
    ROOT.mainloop()
