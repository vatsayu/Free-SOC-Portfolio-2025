# LetsDefend Alert Investigation: SOC282 – Phishing Alert – Deceptive Mail Detected

**Date Investigated**: December 16, 2025  
**Alert Type**: Exchange (Email Security)  
**Severity**: Medium  
**Event ID**: 257  
**Result**: True Positive  

## Alert Overview
The SIEM detected a suspicious email delivered to a user’s mailbox. The rule "SOC282 – Phishing Alert – Deceptive Mail Detected" triggered based on known phishing indicators (malicious URL or attachment).

## Investigation Steps (Following Playbook)

1. **Check if Mail Was Delivered to User**  
   Verified the email reached the recipient’s inbox.  
   *(+5 Points)*

2. **Analyze URL/Attachment**  
   - Inspected email body for suspicious links or attachments.  
   - Found a clickable URL/shortened link leading to a potential phishing site.  
   - No malicious attachment was present in this case.  
   *(+5 Points)*

3. **Determine if Attachments or URLs Exist**  
   - Confirmed presence of a deceptive URL designed to steal credentials.  
   - Used built-in Threat Intel tool to check reputation (flagged as malicious).  
   *(+5 Points)*

## Findings & IOCs
- **Indicator of Compromise**: Malicious URL (redacted for report: hxxp://fake-login[.]example[.]com)
- **Tactic**: Phishing (Initial Access – T1566)
- **User Impact**: Email delivered – potential credential theft risk

## Analyst Note
After analysis, the alert is confirmed as a true positive. The email contained a deceptive link mimicking a legitimate login page. Recommended actions: quarantine email, notify user for awareness training, and block the domain at proxy level.

## Screenshots 
![Alert Dashboard](<img width="1920" height="1200" alt="Screenshot 2025-12-12 230618" src="https://github.com/user-attachments/assets/a4774dc6-e637-4b60-8642-56129238dfeb" />
)  


![Playbook Answers]( <img width="1919" height="1106" alt="Screenshot 2025-12-16 002801" src="https://github.com/user-attachments/assets/3868357c-418c-4ace-a559-b5841c017162" />
 )  
*Caption: Playbook questions and my answers*

![ main channel ]( <img width="1920" height="1200" alt="Screenshot 2025-12-12 230804" src="https://github.com/user-attachments/assets/fd86b940-ffc5-48d1-aa94-12841a1a36a6" />
 )  
*Caption: Main Channel view showing SOC282 alert*

![Threat Intel Check](threat-intel.png)  
*Caption: Reputation check confirming malicious domain*

## Key Takeaways
- Always verify delivery status first in phishing alerts.
- URLs are more common than attachments in modern phishing campaigns.
- Quick threat intel lookup saves time during triage.

**Points Earned**: ~15–20  
**Time Taken**: 25 minutes

---
*Part of my 60-Day Free SOC Analyst Bootcamp | Daily hands-on triage practice*
