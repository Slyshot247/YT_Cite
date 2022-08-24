#Modlue for encrypting base64 

from calendar import c
import pprint as pp
import re
from tkinter import Y
from bs4 import BeautifulSoup
import requests
import sqlite3
import os.path
import keyboard 



while True:
      #___________________ PULL DATA FROM USER INPUT ___________________

      print('''
      Author: Brian C.
      Website:  https: // brianclark88.wixsite.com/mysite
      Description: The program scrapes youtube for APA7 citation puts into notepad.
      Date: 8/19/2022
      References: Pythoncode https: // www.thepythoncode.com/article/get-youtube-data-python
      Crummy(2022) Beautiful Soup Documentation.Crummy. https: // www.crummy.com/software/BeautifulSoup/bs4/doc/\n\n
      Donate only if you can: Cashapp: $TcfTradingGroupLLC | Venmo: @ Brian-Clark-386 | Paypal: https: // paypal.me/tcftrading?country.x=US & locale.x=en_US
      Instructions: Cut the youtube link and right click once in the space provided to paste the link, the output will show up in notepad file.
            ''')
      page = requests.get(input("____________________\n \nYouTube Cite Version 1.4 \n____________________\n\n Paste Youtube Url :"))
      soup = BeautifulSoup(page.content, "html.parser")


      #_________________________________________________________________


      #_________________________________________________________________
      #FIND THE HTML ELEMENT AND STORE IT IN A VARIABLE
      #_________________________________________________________________

      channel_name = soup.find("span", itemprop="author").next.next['content']
      result = soup.find("meta", itemprop="datePublished")['content']

      channel_title = soup.title.string
      channel_title_two = soup.find("meta", itemprop="name")["content"]
      channel_url = soup.find("span", itemprop="author").next['href']
      website = "YouTube"


      #_________________________________________________________________
      #_______________OPEN OUPUT TEXT FILE & PASTE IN DATA______________
      #_________________________________________________________________


      def do_this():

            text_file = open("output.txt", "a")
            text_file.write(channel_name+". ("+result+"). " +
                              channel_title_two+". "+website+". "+channel_url+".\n\n\n")


      do_this()

      #open file

      os.system("output.txt")
      #https://www.youtube.com/watch?v=WHaPQoxFVYQend_program = input("\n\nPress Any Key to end program")
      
      #___________Choose to end program or continue the program _____________
      cont = input("\n\nWould You like to end the program y/n?: ")
      
      if cont == "no" and "n":
            continue
      else: 
         input("Press any key to exit")   
      exit()
      
               