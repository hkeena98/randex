"""
Author: Henry Keena
Version: 1.0
Description: Simple Script to Automate and Randomize Connections to ExpressVPN Servers
"""

#Imports Subprocess Module
import subprocess as sub

#Imports Secrets Module
import secrets as sec

#Imports Advanced Python Scheduler
from apscheduler.schedulers.blocking import BlockingScheduler

"""
Function: randomize_vpn()
Description: Primary Function to Randomize and Run Expressvpn Connections on a Timed Basis
"""
def randomize_vpn():
    server_list = ["hk2", "usny", "ussf", "usch", "uswd", "usda", "usla2", "usmi2", "usse", "cato", "cato2", "defr1", "ukdo", "ukel", "nlth", "nlam", "nlro", "ch2", "frpa1", "itmi", "jpto1", "ausy", "kr2"]
    server_len = len(server_list)
    secret_number = sec.randbelow(server_len)
    secret_server = server_list[secret_number]
    sub.run(["expressvpn","status"])
    sub.run(["expressvpn", "disconnect"])
    sub.run(["expressvpn", "connect", str(secret_server)])

"""
Function: main()
Description: Main Function to Effectively Run the Script Optimally
"""
def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(randomize_vpn, 'interval', hours=1)
    scheduler.start()

#Calls Main Funciton
if __name__ == '__main__':
    main()
