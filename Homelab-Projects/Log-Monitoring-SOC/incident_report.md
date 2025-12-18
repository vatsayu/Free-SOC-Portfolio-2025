## Incident Report: SSH Brute Force Attempt

### Date:
2025-xx-xx

### Detection Method:
Log Monitoring (auth.log)

### Description:
Multiple failed SSH login attempts detected from a single IP address.

### Indicators of Compromise (IOCs):
- IP Address: 192.168.1.50
- Event: Failed SSH logins

### Severity:
Medium

### Recommended Action:
- Block IP using firewall
- Enforce SSH key authentication
