# LetsDefend Alert Investigation: SOC205 – Malicious Macro has been executed

**Date Investigated**: December 16, 2025  
**Alert Type**: Malware  
**Severity**: Medium  
**Event ID**: 231  
**Result**: True Positive  

## Alert Overview
The SIEM detected execution of a malicious Office macro on an endpoint after a user opened a password-protected .zip attachment from a phishing email.

## Investigation Steps (Following Playbook)

1. **Check if Someone Requested the C2**  
   Analyzed network traffic – observed outbound connection attempt to grayhathacker.net/tools/messbox.exe.  
   *(+5 Points)*

2. **Analyze Malware**  
   Reviewed the DOCX file with embedded macro. Macro attempted to download and execute payload.  
   *(+5 Points)*

3. **Check if the malware is quarantined/cleaned**  
   Confirmed endpoint security tool quarantined the file and blocked execution (partial success – 404 response).  
   *(+5 Points)*

## Findings & IOCs
- **Email**: From jake.admin@cybercommunity.info to jayne – password-protected zip attachment (edit1-Invoice.docm.zip)
- **Behavior**: User downloaded, unzipped, and opened DOCX → macro triggered download attempt
- **C2 Domain**: grayhathacker.net/tools/messbox.exe (404 – failed download)
- **Tactic**: Initial Access (Phishing T1566) → Execution (Malicious Macro)

## Analyst Note
Phishing email led to malicious macro execution attempt. Host isolated and email deleted from mailbox. User likely entered zip password. Recommend additional user training and stricter macro policies (disable macros by default).


## Screenshots 
![Alert Dashboard] <img width="1919" height="1099" alt="Malicious_macro" src="https://github.com/user-attachments/assets/6aa8a6bf-9ee2-4f8a-baaa-96081b983436" />
*Caption: Closed Alerts view showing SOC205*

## Key Takeaways
- Password-protected zips are common phishing vectors
- Office macros remain a top execution method
- Quick isolation prevented full compromise

**Points Earned**: ~15–20  
**Time Taken**: 25–35 minutes

---
*Part of my 60-Day Free SOC Analyst Bootcamp | Real malware triage practice*
