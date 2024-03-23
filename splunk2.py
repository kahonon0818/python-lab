import os
import time

print("Download the Splunk Enterprise tar file")
os.system("sudo rm -rf /opt/splunk*")
os.chdir("/opt")
os.system("sudo wget -O splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz "
          "\"https://download.splunk.com/products/splunk/releases/9.0.4.1/linux/"
          "splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz\"")

print("Extract the tar file to /opt")
os.system("sudo tar -zxvf splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz -C /opt")
os.chdir("/opt/splunk/bin/")

print("Start Splunk Enterprise and set up the admin user and password")
os.system("sudo ./splunk start --accept-license --answer-yes --no-prompt --seed-passwd \"abcd1234\"")

print("Enable Splunk at startup")
os.system("sudo ./splunk enable boot-start")

print("Please go to the browser and access Splunk on port 8000")
print("Username: admin")
print("Password: abcd1234")

# Sleep for 4 seconds before exiting (if desired)
time.sleep(4)
