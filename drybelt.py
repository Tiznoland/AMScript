#!/usr/local/bin/python

import os
import platform

def showBanner():
	os.system("clear")
	print(" ")
	print("DDDDDDDDD     RRRRRRRR    YYYY        YYYY    BBBBBBBB     EEEEEEEE   LLLL     TTTTTTTTTTTT")
	print("DDDDDDDDDD    RRRRRRRRR    YYYY      YYYY     BBBBBBBBB    EEEEEEEE   LLLL     TTTTTTTTTTTT")
	print("DDDD   DDDD   RRRR  RRRR    YYYY    YYYY      BBBB  BBBB   EEEE       LLLL       TTTTTTTT")
	print("DDDD    DDDD  RRRR   RRRR    YYYY  YYYY       BBBB   BBBB  EEEE       LLLL         TTTT")
	print("DDDD     DDDD RRRR  RRRR      YYYYYYYY        BBBBBBBBBB   EEEEEE     LLLL         TTTT")
	print("DDDD    DDDD  RRRRRRRRR        YYYYYY         BBBB   BBBB  EEEE       LLLL         TTTT")
	print("DDDD   DDDD   RRRRRRRR          YYYY          BBBB  BBBB   EEEE       LLLL         TTTT")
	print("DDDDDDDDDD    RRRR RRRR         YYYY          BBBBBBBBB    EEEEEEEE   LLLLLLLL     TTTT")
	print("DDDDDDDD      RRRR  RRRR        YYYY          BBBBBBBB     EEEEEEEE   LLLLLLLL     TTTT")
	print(" ")
	print(" ")
	print("By Karel Sels")
	print(" ")
	print(" ")

def showOptions():
	print("Options:")
	print("1. Install dionaea honeypot")
	print("2. Install dashboard")
	print("3. Run dionaea honeypot")
	print("4. Run dashboard")
	print("5. Exit")

#options


def first():
	print("You have chosen to install the dionaea honeypot")
	print("The installation will now begin!")
	os.system("sudo apt-get update -y")
	os.system("sudo apt-get upgrade -y")
	os.system("sudo apt-get -y install software-properties-common")
	os.system("sudo add-apt-repository ppa:honeynet/nightly -y")
	os.system("sudo apt-get update -y")
	os.system("sudo apt-get --assume-yes install dionaea")
	os.system("sudo cp /opt/dionaea/etc/dionaea/ihandlers-available/log_json.yaml /opt/dionaea/etc/dionaea/ihandlers-enabled")


def second():
	print("You have chosen to install the dashboard")
	os.system("sudo add-apt-repository -y ppa:webupd8team/java")
	os.system("sudo apt-get update -y")
	os.system("sudo apt-get -y install oracle-java8-installer")
	os.system("sudo mkdir /var/metabase")
	os.system('sudo wget -O /var/metabase.jar "http://downloads.metabase.com/v0.23.1/metabase.jar"')

def third():
	print("You have chosen to run the dionaea honeypot")
	os.system("sudo service dionaea start")

def fourth():
	print("You have chosen to run the dashboard server")
	os.system("sudo java -jar /var/metabase.jar")

def fifth():
	showBanner()
	print("Bye Bye")

def main():
	while(True):
		showBanner()
		showOptions()
		input = raw_input("Choose an option:[1-5] ")
		input = input.split()
		if input[0] == '1':
			if platform.platform() == "Linux-4.4.0-31-generic-x86_64-with-Ubuntu-14.04-trusty":
				first()
			else:
				print("This will not work on this server, please use a Ubuntu 14.04 server")

		elif input[0] == '2':
			second()
		elif input[0] == '3':
			third()
		elif input[0] == '4':
			fourth()
		elif input[0] == '5':
			fifth()
			break
		else:
			print("This is not an option, please choose one of these:")
			showOptions()

main()

