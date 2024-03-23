import subprocess
import time

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e}")

print("Download the Splunk Enterprise tar file")
run_command("sudo rm -rf /opt/splunk*")
run_command("sudo wget -O /opt/splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz "
            "\"https://download.splunk.com/products/splunk/releases/9.0.4.1/linux/"
            "splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz\"")

print("Extract the tar file to /opt")
run_command("sudo tar -zxvf /opt/splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz -C /opt/splunk")

print("Start Splunk Enterprise and set up the admin user and password")
run_command("sudo /opt/splunk/bin/splunk start --accept-license --answer-yes --no-prompt --seed-passwd \"abcd1234\"")

print("Enable Splunk at startup")
run_command("sudo /opt/splunk/bin/splunk enable boot-start")

print("Please go to the browser and access Splunk on port 8000")
print("Username: admin")
print("Password: abcd1234")

# Sleep for 4 seconds before exiting (if desired)
time.sleep(4)
