from collections import Counter

log_file = "/var/log/auth.log"
threshold = 5

ips = []

with open(log_file, "r") as f:
    for line in f:
        if "Failed password" in line:
            ip = line.split()[-4]
            ips.append(ip)

count = Counter(ips)

for ip, attempts in count.items():
    if attempts >= threshold:
        print(f"[ALERT] Brute-force suspected from {ip} ({attempts} attempts)")

