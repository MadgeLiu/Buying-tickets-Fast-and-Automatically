# Author: Yarong Liu
# Function: Using selenium package in python which can achieve  operate the website automatically
#           I use this package to achieve order train ticket in Chinese Website automatically

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText as mt
import time
import smtplib

class Auto_buy(object):
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="/Users/liuyarong/Downloads/chromedriver")
        self.url_login = "https://kyfw.12306.cn/otn/resources/login.html"
        self.url_Cinit = "https://kyfw.12306.cn/otn/view/index.html"
        self.url_search = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.url_passenger = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        self.c = 0

    def _input(self):
        self.from_station = input("From Sation:")
        self.to_station = input("To Station:")
        self.date = input("Departure:(eg:2019-09-09):")
        self.people = input("Passengers Name(if has many names, use comma to split):")
        self.passengers = self.people.split("，")
        self.t_number = input("Train number(if has many numbers, use comma to split):")
        self.train_numbers = self.t_number.split("，")
        self.reciever_address = input("your receiver_address:")   #"yaliu0915@gmail.com"  #input("your receiver_address:")

    def _login(self):
        self.browser.get(self.url_login)
        WebDriverWait(self.browser,1000).until(EC.url_to_be(self.url_Cinit))
        self.browser.get(self.url_search)

    def _orderticket(self):
        WebDriverWait(self.browser,1000).until(EC.text_to_be_present_in_element_value((By.ID,"fromStationText"),self.from_station))
        WebDriverWait(self.browser,1000).until(EC.text_to_be_present_in_element_value((By.ID,"toStationText"),self.to_station))
        WebDriverWait(self.browser,1000).until(EC.text_to_be_present_in_element_value((By.ID,"train_date"),self.date))
        WebDriverWait(self.browser,1000).until(EC.element_to_be_clickable((By.ID,"query_ticket")))
        self._findTicket()

    def _findTicket(self):
        while self.c == 0:
            self.LookforButton = self.browser.find_element_by_id("query_ticket")
            self.LookforButton.click()
            WebDriverWait(self.browser, 1000).until(EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr")))
            tr_list = self.browser.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
            for tr in tr_list:
                train_number = tr.find_element_by_class_name("number").text
                # print(train_number)
                if train_number in self.train_numbers:
                    ticket_tr = tr.find_element_by_xpath(".//td[4]").text
                    if ticket_tr =="有" or ticket_tr.isdigit():
                        self.c = 1
                        orderButton = tr.find_element_by_class_name("btn72")
                        orderButton.click()
                        WebDriverWait(self.browser,1000).until(EC.url_to_be(self.url_passenger))
                        WebDriverWait(self.browser,1000).until(EC.presence_of_element_located((By.XPATH,".//ul[@id='normal_passenger_id']/li")))
                        passenger_lables = self.browser.find_elements_by_xpath(".//ul[@id='normal_passenger_id']/li/label")
                        for passenger_lable in passenger_lables:
                            time.sleep(0.3)
                            name = passenger_lable.text
                        # print(name)
                            if name in self.passengers:
                                passenger_lable.click()
                        submitButton = self.browser.find_element_by_id("submitOrder_id")
                        submitButton.click()
                        WebDriverWait(self.browser,1000).until(EC.presence_of_element_located((By.CLASS_NAME,"dhtmlx_wins_body_outer")))
                        WebDriverWait(self.browser,1000).until(EC.presence_of_element_located((By.ID,"qr_submit_id")))
                        confirmButton = self.browser.find_element_by_id("qr_submit_id")
                        confirmButton.click()
                        self.browser.close()
                        print("Buying ticket Successfully")
                        break

    def sendTo(self):
        mail_host = "smtp.gmail.com"  # set you mail host
        host_user = "yaliu0915@gmail.com"  # host to send email
        host_password = "kuaile54"  # password of host
        email_subject = "Buying Train Ticket Successfully"  # the subject of you email
        self.send_message = "The ticket you want to buy has been ordered, Please pay it in time" +'''
        Here is the information '''+'''
        ''' + self.people +'''
        ''' + self.t_number + "  " + self.from_station + " ===> " + self.to_station + '''
        ''' + self.date
        msg = mt(self.send_message, _subtype='plain')
        msg['Subject'] = email_subject
        msg['Form'] = host_user

        server = smtplib.SMTP(mail_host, 587)
        server.starttls()
        server.login(host_user, host_password)
        server.sendmail(host_user, self.reciever_address, msg.as_string())
        server.close()
        print("Send Email Successfully")

    def run(self):
        self._input()
        self._login()
        self._orderticket()
        if self.c == 1:
            self.sendTo()
            return True
        return False

if __name__== '__main__' :    #__name__ is a variable that equal the doucument which running
    train_ticket = Auto_buy()
    train_ticket.run()




