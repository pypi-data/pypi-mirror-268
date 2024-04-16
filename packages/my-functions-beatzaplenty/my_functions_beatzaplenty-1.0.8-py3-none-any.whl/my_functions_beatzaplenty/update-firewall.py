import os, subprocess, socket, configparser
from datetime import datetime, timezone, timedelta

# Get script parent dir
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Timezone settings
timezone_offset = +10.0  # Pacific Standard Time (UTC−08:00)
tzinfo = timezone(timedelta(hours=timezone_offset))
tz_string_format = "%a %b %d at %H:%M"

# Init configparser
config = configparser.ConfigParser()
config.read(f'{parent_dir}/config.ini')
default_config = config['firewall']

LOG_FILE = default_config.get("log_file")

# Function to get the current IP address
def get_current_ip():
    try:
        return socket.gethostbyname("lan.ddnsgeek.com")
    except socket.gaierror:
        return None

# Function to read the last IP address from the INI file
def get_last_ip():
    try:
        return default_config.get("last_ip")
    except:
        return None

#Function to update config file with new values
def update_config(config_file, ip_address, tzinfo):
    edit = configparser.ConfigParser()
    edit.read(config_file)
    config_items = edit["firewall"]
    config_items["last_ip"] = ip_address
    config_items["last_change"] = datetime.now(tzinfo).strftime(tz_string_format)
    with open(config_file, "w") as config:
        edit.write(config)

# Function to update firewall rules
def update_firewall_rules(current_ip, last_ip):
    cmd_part_1 = default_config.get("cmd_part_1")
    cmd_part_2 = default_config.get("cmd_part_2")

    with open(LOG_FILE, "w") as log_file:
        log_file.write("Run time: " + str(datetime.now(tzinfo).strftime(tz_string_format)) + "\n")
        log_file.write("Last Change: " + str(default_config.get("last_change")) + "\n")

        if current_ip != last_ip:
            del_cmd = f"sudo ufw delete {cmd_part_1} {last_ip} {cmd_part_2}"
            add_cmd = f"sudo ufw {cmd_part_1} {current_ip} {cmd_part_2}"
            log_file.write("Last IP address: " + str(last_ip) + "\n")
            log_file.write("Current IP address: " + str(current_ip) + "\n")
            subprocess.run(del_cmd, shell = True, executable="/bin/bash",stdout=log_file)
            subprocess.run(add_cmd, shell = True, executable="/bin/bash",stdout=log_file)
            update_config(f'{parent_dir}/config.ini', current_ip, tzinfo)
        else:
            log_file.write("IP address is correct. No firewall changes needed\n")
        log_file.flush()

def main():
    current_ip = get_current_ip()
    last_ip = get_last_ip()

    update_firewall_rules(current_ip, last_ip)

if __name__ == "__main__":
    main()
