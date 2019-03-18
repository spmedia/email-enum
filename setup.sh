#!/usr/bin/env bash
if [[ $EUID -eq 0 ]]; then 
	echo "This script must NOT be run as root" 1>&2
		exit 1
	fi

pip3 install click --user
pip3 install termcolor --user
pip3 install selenium --user
pip3 install pyfiglet --user
mkdir -p ~/.local/bin/
if [[ ! -x "geckodriver" ]]
then
	chmod +x geckodriver
fi
mv geckodriver ~/.local/bin/geckodriver
