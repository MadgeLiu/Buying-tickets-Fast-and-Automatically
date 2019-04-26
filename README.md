# Buying-tickets-Fast-and-Automatically
This is a individual project of course EE551 Python.

|Author|Yarong Liu|
|---|---
|E-mail|yliu255@stevens.edu

## [Introduction](#Introduction)
Nowadays more and more people prefer to buy tickets, like air tickets, train tickets online. But there are always some bad situations that our favorite tickets or the tickets fit our schedule have been sold out. In this case, what we really want to have is a monitor, which could help us monitor whether the website have a seat that fit the requirement of passengers at every second, if the monitor finds this specific ticket, it could place the order fast and automatically. This project is to using Python to create a machine helping passengers order train tickets what they want automatically. <br>
<br>
In China🇨🇳, going home and being with family in Spring Festival is necessary to everyone who do not work at hometown. However, it may difficult to everyone to buy favorite train tickets or the tickets fit schedule because there are also so many people buy it at same time. In this case, I want to use Python to write algorithm to help people monitor [ticket ofiical website](https://www.12306.cn "a chinese train website") (which is all chinese website) whether there is a ticket what we need, and if there is, it can help people order it immediately and automatically, people then will receive email that this program help you order it successfully, so you can make a payment right now. 


## [Project-Solution](#Project-Solution)
In Python, there is selenium package which can achieve operate the website automatically, so I use this package to achieve order train ticket in Chinese Train Offical Website automatically. Methods and Classes in this package such as webdriver, WebDriverWait, expected_conditions etc. is really useful to me to achieve my project. Using that I achieve the following functions:
* Automatically open and switch the website we want. 
* Read kinds of information on the website.
* Press the specific buttons on the website.
* Automatically add information of passengers.
* Send email to customers when the machine monitor the ticket which fits passenger requirement.
* Simultaneously monitor different kind of train tickets.
### flowchart of algorithm
![](https://github.com/MidgeLiu/Buying-tickets-Fast-and-Automatically/raw/master/flowchart.png "flowchart")

## [Conclusion](#Conclusion)
Finally, this project help people order ticket immediately and automatically. I recorded a video when code was running so You can see that in Github. About the test program, because pytest cannot run input() function, I just creat a new python file First_two.py and the only difference between two files is that all the input information in First_one.py has been changed to immutable information in First_two.py.

## [Future-Plan](#Future-Plan)
If I could achieve the basic function in advance, I will try my best to achieve other function as following:
Do another similar project which help customers buying discounted product successfully in a very short time.
