# Interface detail Fetcher

A sophisticated python script to provide the user with the interface details of a Linux machine depending on the user's input.

## Description

- This script takes the Interface Type, IP address and the MAC address as the input from the user.
-  This script is capable of connecting to any remote server via SSH.
- The script allows the user to choose from either a Strict match or a Flexible match with respect to the parameters given as input.
- The Strict match generates an output only if all the three user inputs match an interface description
- The Flexible match generates an output of one of the parameters satisfy. Consequently, this can lead to multiple types of output

## Modules used
- Netmiko
- re
- textfsm
- os

## Usage

- Make sure that the q3.textfsm file is in the same directory as that of the script (LAB_Q3.py)
- Run the python script using the command : python3 LAB_Q3.py
- An interactive interface where the user is prompted for details appears on the shell.

# Version
 - 1.0

Authors
----
Dhanraj Vedanth Raghunathan, Kashish Singh

# License

  - All rights reserved by the owner and NC State University.
  - Usage of the script can be done post approval from the above.