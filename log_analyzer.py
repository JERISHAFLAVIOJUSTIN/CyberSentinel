from collections import Counter
import re

log_file = "sample.log"

failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            ip = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if ip:
                failed_ips.append(ip.group())

ip_counts = Counter(failed_ips)

print("\n===== CYBER THREAT REPORT =====\n")

for ip, count in ip_counts.items():

    threat_score = count * 10

    if threat_score < 30:
        level = "LOW"
    elif threat_score < 60:
        level = "MEDIUM"
    else:
        level = "HIGH"

    print(f"IP Address   : {ip}")
    print(f"Failed Logins: {count}")
    print(f"Threat Score : {threat_score}/100")
    print(f"Risk Level   : {level}")
    print("-" * 40)