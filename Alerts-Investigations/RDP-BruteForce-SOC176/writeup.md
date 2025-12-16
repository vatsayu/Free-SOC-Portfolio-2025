# LetsDefend Alert Investigation: SOC176 – RDP Brute Force Detected

**Date Investigated**: December 16, 2025  
**Alert Type**: Brute Force  
**Severity**: Medium  
**Event ID**: 234  
**Result**: True Positive  

## Alert Overview
The SIEM detected multiple failed RDP login attempts followed by a successful login from an external IP, indicating a brute force attack on Remote Desktop Protocol (RDP).

## Investigation Steps (Following Playbook)

1. **Should the Device Be Isolated?**  
   Yes – successful compromise achieved. Immediate isolation recommended to prevent lateral movement.  
   *(+5 Points)*

2. **Log Management**  
   Reviewed Windows Security Event Logs for Event IDs 4625 (failed logon) and 4624 (successful logon). Multiple failed attempts observed.  
   *(+5 Points)*

3. **Determine the Scope**  
   Attacker tried common usernames (admin, guest, sysadmin) before succeeding with "matthew" account.  
   *(+5 Points)*

4. **Traffic Analysis**  
   Confirmed RDP traffic (port 3389) from external IP to victim machine.  
   *(+5 Points)*

5. **IP Reputation Check**  
   Source IP from China – flagged in Threat Intel as known malicious range.  
   *(+5 Points)*

6. **Enrichment & Context**  
   Successful authentication after brute force indicates credential compromise. Potential post-exploitation risk.  
   *(+5 Points)*

## Findings & IOCs
- **Source IP**: [Redacted – e.g., China-based malicious range]
- **Target Account**: matthew
- **Protocol**: RDP (port 3389)
- **Tactic**: Brute Force (Credential Access – T1110)
- **Impact**: Successful remote access gained

## Analyst Note
Attacker brute-forced multiple usernames and successfully compromised the "matthew" account via RDP. Immediate actions: isolate host, reset password, enforce MFA, restrict RDP to VPN only, and scan for persistence.

## Screenshots 
!Closed Alert <img width="1920" height="1103" alt="RDP" src="https://github.com/user-attachments/assets/17b49e7f-d80b-4381-b3d1-47806d28b908" />


*Caption: Closed Alerts view showing SOC176*


## Key Takeaways
- RDP is a top target for brute force – always restrict external access.
- Monitoring failed logons (Event ID 4625) is critical for early detection.
- Successful login after failures = high-priority escalation.

**Points Earned**: ~30  
**Time Taken**: 25–30 minutes

---
*Part of my 60-Day Free SOC Analyst Bootcamp | Building real triage experience*
