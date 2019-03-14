# Email-Enum-SEO
[![Version](https://img.shields.io/badge/Version-v0.5-brightgreen.svg)](https://shields.io/)
[![Status](https://img.shields.io/badge/Status-Initial-brightgreen.svg)](https://shields.io/)
[![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey.svg)](https://shields.io/)
[![Browser](https://img.shields.io/badge/Browser-Firefox-brightgreen.svg)](https://shields.io/)
[![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**Email-Enum SEO Edition searches mainstream SEO websites and tells you if an email is registered!**

This will search a list of popular webmaster, SEO, and marketing tools and let you know if the email has an account on any of those services. Users of these services and websites often have direct access to many companies servers, CMS logins, API keys, and more. 

Doing recon on these users can be helpful when trying to identify key users or services to gain a foothold in a company or business.

Inspired by https://github.com/Frint0/email-enum


![Demo Photo](https://raw.githubusercontent.com/Frint0/email-enum/master/demo.png)

## Dependencies
* Firefox
* Selenium => 3.14
* Click => 7.0
* Termcolor => 1.1

## Installation

Do not run **setup.sh** as root!

```
git clone https://github.com/spmedia/email-enum.git
cd email-enum
chmod +x setup.sh
./setup.sh
```

## Usage

`python3 check.py email@gmail.com` or `./check.py email@gmail.com`

## To-Do's

* More Websites
* Username Enumeration
* Increased Verbosity
* More arguments

*and much more...*

## Disclaimer

This program is done entirely by web scraping, if a website changes its element variables or layout, you might need to wait for an updated version of Email-Enum SEO Edition or feel free to contribute.
