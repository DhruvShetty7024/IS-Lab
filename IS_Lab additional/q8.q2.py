import subprocess
import time
import os

# Function to configure Snort by adding a custom rule
def add_custom_rule():
    rule = 'alert tcp any any -> any 80 (msg:"HTTP connection detected"; sid:1000001; rev:1;)'
    rules_path = '/etc/snort/rules/local.rules'
    
    # Check if the rule already exists
    with open(rules_path, 'r') as file:
        if rule in file.read():
            print("Rule already exists. Skipping addition.")
        else:
            with open(rules_path, 'a') as file:
                file.write(f"\n{rule}\n")
            print("Custom rule added successfully.")

# Function to run Snort as NIDS
def run_snort(interface='eth0'):
    print(f"Starting Snort on interface {interface}...")
    try:
        subprocess.run(
            ['sudo', 'snort', '-A', 'console', '-q', '-c', '/etc/snort/snort.conf', '-i', interface],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running Snort: {e}")

# Function to check the Snort log for alerts
def analyze_snort_logs():
    log_path = '/var/log/snort/alert'
    if os.path.exists(log_path):
        with open(log_path, 'r') as log_file:
            logs = log_file.read()
            if logs:
                print("\n--- Snort Alerts ---")
                print(logs)
            else:
                print("\nNo alerts detected.")
    else:
        print("No log file found. Make sure Snort is configured correctly.")

# Menu-driven program
def menu():
    while True:
        print("\n=== Snort NIDS Automation Menu ===")
        print("1. Add Custom Snort Rule")
        print("2. Start Snort NIDS")
        print("3. Analyze Snort Logs")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            add_custom_rule()
        elif choice == '2':
            interface = input("Enter the network interface to monitor (e.g., eth0): ")
            run_snort(interface)
        elif choice == '3':
            analyze_snort_logs()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    menu()
