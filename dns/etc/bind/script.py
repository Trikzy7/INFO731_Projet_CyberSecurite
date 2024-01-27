import argparse
import subprocess

NAMED_CONF_PATH = "/etc/bind/named.conf"
DB_ERROR_PATH = "/etc/bind/db.forbiden"

def add_forbiden_url(url: str):
    with open(NAMED_CONF_PATH, "a") as f:
        f.write(f'\nzone "{url}" {{\n    type master;\n    file "{DB_ERROR_PATH}";\n}};\n')
    f.close()

def check_url_already_blocked(url: str):
    with open(NAMED_CONF_PATH, "r") as f:
        return any(url in line for line in f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=True)
    args = parser.parse_args()
    
    resp = input(f"[WARNING] Are you sure you want to block {args.url}? (y/n)")

    if resp.lower() != 'y' or check_url_already_blocked(args.url):
        print("Aborting")
    else:
        add_forbiden_url(args.url)
        subprocess.run("service bind restart", shell=True)
        print(f"{args.url} has been successfully blocked")
