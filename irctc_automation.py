"""============================================================================
INFORMATION ABOUT CODE         Coding: ISO 9001:2015
===============================================================================
IRCTC Automation with GUI
For booking Tatkal or General ticket with COD option.(Verified)
Author: Prajinkya Pimpalghare
Date: 2-November-2017
Version: 1.0
Input Variable: From GUI. All fields are mandatory
Note: Please put the same station name as well as date mentioned in IRCTC.
Basic Requirement Selenium module, and Web driver for chrome
============================================================================"""
import time
from tkinter import Frame, Tk, Label, Entry, Button, LEFT
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
        self.master = master
        self.label = labels
        self.passenger = ["PassengersDetail:", "Psg:One", "Psg:Two", "Psg:Three", "Psg:Four"]
        self.entry = {}
        self.values = {}

    def main_gui(self):
        """
        For creating an interactive GUI for IRCTC Automation
        """
        for label_index, label_value in zip(range(1, 10), self.label):
            Label(self.master, text=label_value).grid(row=label_index, column=0)
            self.entry[label_value] = Entry(self.master, show="*") if label_value == "Password" else Entry(self.master)
            self.entry[label_value].grid(row=label_index, column=1)
        for passenger_index, passenger_label in zip(range(0, 5), self.passenger):
            Label(self.master, text=passenger_label).grid(row=label_index + 1, column=passenger_index)
        for index, value in zip(range(label_index + 2, 14), self.label[label_index + 1:]):
            Label(self.master, text=value).grid(row=index, column=0)
            for extra_index in range(0, 4):
                self.entry[value + str(extra_index)] = Entry(self.master)
                self.entry[value + str(extra_index)].grid(row=index, column=extra_index + 1)
        Button(self.master, text="Book Tatkal Ticket", command=self._login_btn_clicked).grid(row=5, column=3)

    def _login_btn_clicked(self):
        """
        It will start the portal with provided value
        """
        for label, index in zip(self.label, range(1, 10)):
            self.values[label] = self.entry[label].get()
        for temp_index in zip(self.label[10:]):
            for extra_index in range(0, 4):
                self.values[temp_index[0] + str(extra_index)] = self.entry[temp_index[0] + str(extra_index)].get()
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
        It will be having the main script for Chrome automation
        """
        try:
            self.browser = webdriver.Chrome()
            self.browser.get("https://www.irctc.co.in/nget/train-search")
            login_page = self.browser.find_element_by_id("loginFormId")
            login_page.find_element_by_id("usernameId").send_keys(self.values["UserID"])
            login_page.find_element_by_name("j_password").send_keys(self.values["Password"])
            time.sleep(10)
            login_page.find_element_by_id("loginbutton").click()
            main_page = self.browser.find_element_by_class_name("container")
            main_page.find_element_by_id("quickbookTab:header:inactive").click()
            main_page.find_element_by_id("qbform:trainNUmber").send_keys(self.values["TrainNo"])
            main_page.find_element_by_id("qbform:fromStation").send_keys(self.values["FromStation"])
            main_page.find_element_by_id("qbform:toStation").send_keys(self.values["ToStation"])
            main_page.find_element_by_id("qbform:qbJrnyDateInputDate").send_keys(self.values["Date"])
            main_page.find_element_by_id("qbform:class").send_keys(self.values["Class"])
            main_page.find_element_by_id("qbform:quota").send_keys(self.values["Quota"])
            main_page.find_element_by_id("qbform:quickBookSubmit").click()
            for index in range(0, 3):
                self.browser.find_element_by_id(
                    "addPassengerForm:psdetail:" + str(index) + ":j_idt567").find_element_by_tag_name(
                    "input").send_keys(
                    self.values["Name" + str(index)])
                self.browser.find_element_by_id("addPassengerForm:psdetail:" + str(index) + ":psgnAge").send_keys(
                    self.values["Age" + str(index)])
                self.browser.find_element_by_id("addPassengerForm:psdetail:" + str(index) + ":psgnGender").send_keys(
                    self.values["Gender" + str(index)])
                self.browser.find_element_by_id("addPassengerForm:mobileNo").send_keys(self.values["MobileNo"])
            self.browser.find_element_by_id("nlpAnswer").send_keys("")
            time.sleep(10)
            self.browser.find_element_by_id("COD").click()
            self.browser.find_elements_by_css_selector("input[type='radio'][value='100']")[0].click()
            self.browser.find_element_by_id("validate").click()
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
