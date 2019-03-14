#!/usr/bin/python3
import os
import sys
import click
from termcolor import colored
import subprocess

def asciiBanner():
    import pyfiglet
    banner = pyfiglet.figlet_format("Email Enum SEO")
    return banner

@click.command()
@click.argument('email', nargs=1)
def emailEnum(email):
    print(colored(asciiBanner(), 'magenta'))
    print(colored("Author: ", 'green') + "spmedia")
    print(colored("Version: ", 'green') + colored("v0.01", 'yellow'))
    print("\n\n")
    try:
        firefox_check = subprocess.check_output(['which', 'firefox'])
    except subprocess.CalledProcessError as exc:
        print(colored("Firefox not installed or isn't in PATH, exiting...", 'yellow'))
        sys.exit()
    import sites
    moz_response = sites.mozCheck(email)
    print("[*] Moz: " + moz_response)
    twit_response = sites.twitterCheck(email)
    print("[*] Twitter: " + twit_response)
    open_response = sites.opencartCheck(email)
    print("[*] OpenCart: " + open_response)
    sites.quitSelenium()

emailEnum()
