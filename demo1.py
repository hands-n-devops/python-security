# vulnerable_example.py

import os
import subprocess
import sqlite3
import requests  # requests is fine, but let's use it insecurely below

# Hardcoded credentials (should be detected)
DB_PASSWORD = "SuperSecret123"

def run_command(user_input):
    # Command injection vulnerability
    os.system("ping " + user_input)

def run_command_subprocess(user_input):
    # Command injection vulnerability
    subprocess.call("ping " + user_input, shell=True)

def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # SQL injection vulnerability
    cursor.execute("SELECT * FROM users WHERE id = '%s'" % user_id)
    return cursor.fetchall()

def download_website(url):
    # Insecure HTTP request (should use HTTPS)
    response = requests.get("http://" + url)
    return response.text

def insecure_hash(data):
    import hashlib
    # Use of weak hash function (MD5)
    return hashlib.md5(data.encode()).hexdigest()

def main():
    user_input = input("Enter host to ping: ")
    run_command(user_input)
    run_command_subprocess(user_input)
    user_id = input("Enter user id: ")
    print(get_user_data(user_id))
