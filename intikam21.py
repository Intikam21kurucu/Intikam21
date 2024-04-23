#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyfiglet import Figlet
from colorama import Fore, init
import threading
import requests
import time
import sys
import os
import base64
import time as t

# colorama'yı başlat
init()

# ASCII sanatını yazdır
ASCII = """%%%%%%%%%%###############                                     
                               %%%%%%%%%%%%%%#####################                               
                            %%%%%%%%%%%%%%%%%########################                            
                         %%%%%%%%%%%%%%%%%%%########################### #                        
                     @%%%%%%%%%%%%%%#####%%%%%%##################### ########                     
                   %%%%%%%%%%%%##%%%%@@@@@@@@@@@@@@@%%%%########## ##########**                   
                 %%%%%%%%%%%##%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%### ###########*****                 
               @@%%%%%%%%#%%@@@@@@@@@@#++@@@+--*@@@@%%@@@@@@@@@ @%%#%########*******               
             @@@@%%%%%#%%@@@@@@@@#..=@: .%@@*#..#@@:..%@@@@@@@ @@@@@%%#%#####************             
           @@@@@@%%%#%%@@@@@@%=+@@@: ...: +@@*:.*@@@= -@@@@@@@@ %%@@@@@@%%####****************           
          @@@@@@@%%%%@@@@@@@*...:*@@* :+=*.-@%-:-:%@-. -@@@@@@+....+@@@@@%%###************          
         @@@@@@@%#%@@@@@*@@@@..-..-%@==%@@@@@@@@@@@@%#*@@@ @@*..#@*#@@*@@@@@%#%#************         
       @@@@@@@%#%@@@@@@:.*@@@+ :#+*@@@@@@%%%%%%%%%%%@@@@ @@@%..+#@@@*.-@@@@@@%#%#************       
      @@@@@@@%#%@@@@*.=+ .=*%%=%@@@@%%###%%%%%%%%%%%### %%@@@@#=#@@%..-..*@@@@%#%#**********       
     @@@@@@@#%%@@@@@#:..:=:.*@@@@%#%%%%%%%%%%%%%%%%%% %%%%%#%@@@@@#: .=#%@@@@@%%#%************     
    @@@@@@@#%@%::*#@@@*..-@@@@%#%%%%%%%%%%%%%%%%%% %%%%%%%%#%@@@**@@@@%=:*@@@@%#%#**********    
    @@@@@@#%@@@%*:.:+%@%*@@@%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%@@@@%*-..-.+@@@@%#%#*********    
   @@@@@@#%@@@@@@@*-..=@@@%%#%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%#%@@#..+::..%@@@@%#%**********   
  @@@@@@%%@@@@=:%@@@@+@@%#%%%*%%+.=@@@@@@@@@@@@@@@ @@@@@@@%.-#@#%%#%@@%:...#@@@@@%%#%**********  
  @@@@@%#%@@@*..:=%@@@@@%#%%%*.+:.+@@@@@@@@@@@@@@@@ @@@@@@@@%:.*.:%%%#%@@@@%@@@%*+@@@%#%#*********  
 @@@@@@#%@@@%-=*-..-@@@%%%%*:#.:.:=@@@@@@@@@@@@@@@ @@@@@@@@@#:.:.=+-%%%%@@@#-:....#@@@%#%#*********
 @@@@@%%%@@@@@@@@#%@@%#%%%+ ==--*%%#####%%%%@%@%@@% @@@@@@@@@%+:==:.%%%#%@@%..=.*:-@@@%%%%*********
@@@@@@#%%@@#=+*##%%@@%#%%*.*-::-#@@@@@%%#*****#%% %%@@@@@@@@@@%+:::+-:%%#%@@*:#*#%@@@@@%%#%#*********
@@@@@@#%%%%*=:. .:%%%%%%%#..=..#%%%%#****++++==*%%%@@@@@@@@@@@@=. --.=#%%%%%%%%%###%%%%#%#*********
@@@@@%%%%%%=. .:*%%%%#%%-.#=++%@@@@@@@@%*++*#%%*#%%#%@@@@@@@@@@ @*=*+= #%#%%%+ .%%%%%%************
@@@@@#%%%%#:....:#%%%#%%#:.:.+%@@@@%##%%%%%%%+-+ ++=-+*%@@@@@@@@%:.:.=%%#%%%%+:.:-.#%%%%#%*********
@@@@@#%%%%%%##*%%%%%*.+=-:*%@@@@%@@@%%%%%%-*%% %##%#*-+@@@@@@@@-:+=-:%%%%%%..+-:=%%%%#%#********
@@@@@%%%#*#++++++%%%%%%+:.:-%%@@@@@@@%%%%%#-#%@ %%%%%##**%@@@@@%*-:.-*%%%%%##%%%%%%%%#%#********
@@@@@#%%-:=::::::%%%%%%=.+=:.%%@@@@@@@%%%%%#+*#% @@@@@%@@@@@@@@@@=.+=-.%%%%%%%%%%%%%%%#%#********
@@@@@%%%%%%%%%%%%%%#%%+..:=#%@@@@@@@@@@%%%%%*+* ####%%%@@@@@@@@@==..:#%#%%%%%%%%%%%%%#%#********
@@@@@%%%%%%%%%%%%%%#%#.:=-.#%@@@@@@@@@@@@@@@%## %%@%%####%@@@@@-.==.-%#%%%%%%%%%%%%%%%*********
@@@@@@#%%%%%%%%%%%%%#+--+.#@@@@@@@@@@@@@@@@% @@@@@@%%%%%@@@@=:+:=*%%%%%%%%%%%%%%%#%%*********
@@@@@@#%%%%%%%%%%%%%#%*:--::+%@@@@@@@@@@@@@@@@ @@@@@@@@%%@%@@*=.--:-%#%%%%%%%%%%%%#%#*********
 @@@@@%#%########**##%#%%==-+ +%@@@@@@@@@@@@@@@@@@ @@@@@@@%@@@%.:+==*%#%%##*+########%#%%*********
 @@@@@@#%######*::###%%#%-....=.%@@@@@@@@@@@@@@@ @@@@@@@@@%@+:=....*#%%###-.-######%%#%#*********
  @@@@@@#%%##*-. ..:###%#%%#*+- #@@@@@@@@@@@@@@@@@@@@@@@@@@@-.=##% %#%%###:::..=###%#%%*********  
  @@@@@@%#%###-+*#+::###%%#%*-:-=%@@@@@@@@@@@@@@@@@ @@@@@@@@@@+=::+##%%##*::***=:###%#%%#*********  
   @@@@@@%%%###*-...-.+###%%#%%@@##@@@@@@@@@@@@@@@@@ @@@@@@@%#%@@%#%%####:.*##=*###%%%%#*********   
    @@@@@@%%%###-.=:++*+###%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%###*#+..-.:*##%%%%*********    
    @@@@@@%%%###=-+=:...*###%%%#%%%%%%%%%%%%%%%%%% %%%%%%%#%%%###*...-+==*##%%%#%%**********    
     @@@@@@@%#%%##*.:.-.-#-+####%%##%%%%%%%%%%%%%%%% %%%##%%####+-#:.=...+##%#%%%**********     
      @@@@@@@%#%%####: =*...#######%%%%###%%%%%%%###%% %%##-.*#=*-.=#:.-####%#%%#**********      
       @@@@@@@%%#%%###+=..:.:..=########%%%%%%%%%%%%### ####*:.-:.:..*#=*##%%#%%#**********       
         @@@@@@@%%%%##*=#=-..+##*::-####################+- :::=..+*-.:+###%%#%%##*********         
          @@@@@@@%%#%%####-:*##=.:..#-.-#==*==++###=:::-: -: .++..+#####%%%#%%#**********          
           @@@@@@%%%%#%%######-.::.:#...-.:= :-..*#- -:.*: :..- **####%%%#%%#************           
             @@@@%%%%%%##%%######+.-+ +: += -#. +#*..###*.=######%%%##%%###*********             
               @@%%%%%%%%%#%%%######*##=-#+..:-+###=+########%% %%#%%%######*******               
                 @%%%%%%%%%%%%#%%%%%##################%%%%%#%%% %%#########*****                 
                   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%### #########***                   
                     @%%%%%%%%%%%%%%%%%%#%%%%%%%#%%%%%%%%########## #######*                     
                        @%%%%%%%%%%%%%%%%%%%%%%%%%#################### #                         
                            %%%%%%%%%%%%%%%%%########################                            
                               %%%%%%%%%%%%%%#####################                               
                                     %%%%%%%%%################  """
print(ASCII)

# 'INTIKAM21 CYBER' metnini mavi renkte ve slant fontuyla yazdır
f = Figlet(font='slant')
print(Fore.BLUE + f.renderText('INTIKAM21 CYBER') + Fore.RESET)
while True:
# Kullanıcıdan 'help' komutunu girmesini iste
	print(Fore.BLUE + 'başlatmak için help yaz')
	help_input = input("┌──(intikam21-cyber@root[~]\n└─$ ")

	if help_input == "help":
  	  print("komutlar:" + Fore.BLUE + """
    1 = DDOS
    2 = SMS bomber
    3 = discord token grabber
    4 = bruteforce
    """)

	command = input("┌──(intikam21-cyber@root[~]\n└─$ ")

	if command == "2":
		os.system("python3 SMSBOMBER.py")

	if command == "1":
		print("bu program dúzgün çalíşmamaktadír")
		t.sleep(1)
		os.system("python3 DDOS.py")
	
	if command == "4":
		os.system("python3 BRUTEFORCE.py")

	if command == "3":
		os.system("python3 DISCORD.py")