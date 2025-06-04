#!/usr/bin/env python3
from datetime import datetime
from zoneinfo import ZoneInfo
from colorama import init, Fore, Style

init(autoreset=True)

# Current local time
local_time = datetime.now().astimezone()
print(Fore.GREEN + "Local time:" + Style.RESET_ALL, local_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

# UTC time
utc = datetime.now(ZoneInfo("UTC"))
print(Fore.CYAN + "UTC time:" + Style.RESET_ALL, utc.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

# Tuvalu time (Pacific/Funafuti)
funafuti = datetime.now(ZoneInfo("Pacific/Funafuti"))
print(Fore.MAGENTA + "Tuvalu time (zoneinfo):" + Style.RESET_ALL, funafuti.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
