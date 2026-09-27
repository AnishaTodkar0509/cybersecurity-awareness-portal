offences = [
    {
        "id": "phishing",
        "title": "Phishing & Social Engineering",
        "definition": "A cybercrime in which a target or targets are contacted by email, telephone, or text message by someone posing as a legitimate institution to lure individuals into providing sensitive data.",
        "how_it_occurs": "Attackers send forged emails containing malicious links or attachments that lead to fake login pages.",
        "scenario": "A user receives an email that looks like it's from their bank saying their account is locked and they must click a link to verify their credentials.",
        "impact": "Loss of credentials, financial loss, identity theft.",
        "warning_signs": "Urgent or threatening language, mismatched URLs, unexpected attachments, requests for personal information.",
        "prevention": "Never click unverified links, use 2FA, verify sender addresses, do not share OTPs.",
        "action": "Change passwords immediately, contact the bank directly, report the phishing attempt."
    },
    {
        "id": "identity_theft",
        "title": "Identity Theft",
        "definition": "The deliberate use of someone else's identity, usually as a method to gain a financial advantage or obtain credit and other benefits.",
        "how_it_occurs": "Data breaches, physical theft of documents, phishing, or malware stealing personal information.",
        "scenario": "An attacker uses stolen Aadhaar and PAN card details to open a fraudulent loan account in the victim's name.",
        "impact": "Ruined credit score, financial debt, legal complications.",
        "warning_signs": "Unexplained bank withdrawals, failing to receive bills, notices for accounts you didn't open.",
        "prevention": "Shred sensitive documents, use strong passwords, monitor credit reports, do not overshare on social media.",
        "action": "File a police report (FIR), contact the credit bureau, freeze affected accounts."
    },
    {
        "id": "ransomware",
        "title": "Ransomware",
        "definition": "A type of malicious software designed to block access to a computer system until a sum of money is paid.",
        "how_it_occurs": "Typically spreads through phishing emails or by visiting infected websites.",
        "scenario": "A company employee downloads an invoice attachment which silently encrypts all files on the network and displays a Bitcoin demand screen.",
        "impact": "Complete data loss, business downtime, financial extortion.",
        "warning_signs": "Inability to open files, files with weird extensions (.encrypted), ransom notes popping up on screen.",
        "prevention": "Maintain offline backups, keep OS updated, use Endpoint Detection & Response (EDR) solutions.",
        "action": "Disconnect from the network immediately, do NOT pay the ransom, contact cyber authorities, restore from backup."
    }
]

scenarios = [
    {
        "id": 1,
        "scenario_text": "Rahul receives an SMS claiming his electricity bill is pending and power will be cut tonight. The SMS contains a link 'http://ebill-update-online.info'. Rahul panics, clicks the link, and enters his debit card details.",
        "questions": [
            {
                "q": "What cyber offence occurred?",
                "options": ["Ransomware", "Smishing (SMS Phishing)", "Cyberstalking", "DoS Attack"],
                "answer": "Smishing (SMS Phishing)",
                "explanation": "This is a social engineering attack via SMS, known as Smishing, intended to steal financial data."
            },
            {
                "q": "What psychological technique was used?",
                "options": ["Creating a false sense of urgency/fear", "Offering a reward", "Building trust", "Physical threat"],
                "answer": "Creating a false sense of urgency/fear",
                "explanation": "Threatening to cut power tonight creates panic, making the victim less likely to verify the link."
            },
            {
                "q": "What should Rahul do immediately?",
                "options": ["Delete the SMS", "Pay the bill again", "Block his debit card and report to the bank", "Reply to the SMS"],
                "answer": "Block his debit card and report to the bank",
                "explanation": "Since financial details were compromised, blocking the card is the critical first step to prevent unauthorized transactions."
            }
        ]
    }
]
