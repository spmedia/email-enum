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
    botify_response = sites.botifyCheck(email)
    print("[*] Botify: " + botify_response)
    raven_response = sites.ravenCheck(email)
    print("[*] Raven Tools: " + raven_response)
    scream_response = sites.screamCheck(email)
    print("[*] Screaming Frog: " + scream_response)
    woo_response = sites.wooCheck(email)
    print("[*] WooRank: " + woo_response)
    answer_response = sites.answerCheck(email)
    print("[*] AnswerThePublic: " + answer_response)
    spy_response = sites.spyCheck(email)
    print("[*] SpyFu: " + spy_response)
    micro_response = sites.microCheck(email)
    print("[*] MicroSiteMasters: " + micro_response)
    buzzsumo_response = sites.buzzsumoCheck(email)
    print("[*] BuzzSumo: " + buzzsumo_response)
    ninja_response = sites.ninjaCheck(email)
    print("[*] NinjaOutreach: " + ninja_response)
    sites.quitSelenium()

emailEnum()
