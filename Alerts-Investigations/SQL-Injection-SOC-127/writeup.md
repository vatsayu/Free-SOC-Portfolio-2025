# LetsDefend Alert Investigation: SOC127 – SQL Injection Detected

**Date Investigated**: December 20, 2025  
**Alert Type**: Web Attack  
**Severity**: High  
**Event ID**: 235  
**Result**: True Positive  

## Alert Overview
The SIEM detected SQL injection attempts against webserver1000. The attacker used sqlmap to scan multiple hosts, receiving response code 200 with large payload sizes (86.65), indicating successful data retrieval.

## Investigation Steps (Following Playbook)

1. **Do You Need Tier 2 Escalation?**  
   Yes – successful exploitation confirmed.  
   *(+5 Points)*

2. **Was the Attack Successful?**  
   Yes – HTTP 200 responses and large data size returned.  
   *(+5 Points)*

3. **What is the Direction of Traffic?**  
   Inbound – external attacker targeting internal web server.  
   *(+5 Points)*

4. **Check if it is a Planned Test**  
   No – no authorized penetration test scheduled.  
   *(+5 Points)*

5. **What is the Attack Type?**  
   SQL Injection.  
   *(+5 Points)*

6. **Is Traffic Malicious?**  
   Yes – sqlmap tool signature and anomalous payload sizes.  
   *(+5 Points)*

## Findings & IOCs
- **Source IP**: China-based address (external)
- **Tool Used**: sqlmap (automated SQL injection scanner)
- **Target**: webserver1000
- **Indicators**: HTTP 200 responses, oversized payloads (86.65), consistent results across scans
- **Tactic**: Initial Access / Execution (Web Application Exploitation – SQL Injection)
- **Impact**: Potential data exfiltration from database

## Analyst Note
Attacker from China IP used sqlmap to successfully exploit SQL injection vulnerability on webserver1000. Response code 200 and large payload sizes confirm data retrieval. Immediate escalation to Tier 2 required for patching, input validation fixes, and IP blocking.

## Screenshots (Add Your Own)
![Alert Dashboard] <img width="1918" height="1107" alt="SOC-127-sql" src="https://github.com/user-attachments/assets/897118de-89a5-4313-bc03-ed607da0bc39" />
*Caption: Closed Alerts view showing SOC127*

![Endpoint/Logs]  <img width="1919" height="1057" alt="soc-127" src="https://github.com/user-attachments/assets/50a7b4a7-679e-4af5-8727-2ff3f795529c" />
*Caption: Web server logs showing injection attempts*

## Key Takeaways
- SQL injection remains one of the most critical web vulnerabilities (OWASP Top 10)
- Automated tools like sqlmap make exploitation fast and scalable
- Monitoring response codes and payload sizes helps detect successful exfiltration
- Always escalate successful web exploits immediately

**Points Earned**: ~30  
**Time Taken**: 30–40 minutes

---
*Part of my 60-Day Free SOC Analyst Bootcamp | Real web attack triage practice*
