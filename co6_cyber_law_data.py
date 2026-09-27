laws = [
    {
        "section": "Section 43 & 66",
        "title": "Unauthorized Access (Hacking)",
        "description": "Deals with unauthorized access, downloading, or copying of data from a computer system. Section 66 prescribes punishment for computer-related offences (fraudulently or dishonestly committing acts referred to in Sec 43).",
        "penalty": "Imprisonment up to 3 years or fine up to ₹5 Lakh, or both."
    },
    {
        "section": "Section 66C",
        "title": "Identity Theft",
        "description": "Punishment for fraudulently or dishonestly making use of the electronic signature, password, or any other unique identification feature of any other person.",
        "penalty": "Imprisonment up to 3 years and fine up to ₹1 Lakh."
    },
    {
        "section": "Section 66D",
        "title": "Cheating by Personation",
        "description": "Punishment for cheating by personation by using computer resource. This is heavily applicable to Phishing and fake social media profiles used to defraud.",
        "penalty": "Imprisonment up to 3 years and fine up to ₹1 Lakh."
    },
    {
        "section": "Section 67",
        "title": "Publishing Obscene Material",
        "description": "Punishes the publishing or transmitting of obscene material in electronic form.",
        "penalty": "First conviction: Imprisonment up to 3 years and fine up to ₹5 Lakh."
    },
    {
        "section": "IT Act (General)",
        "title": "Digital Signatures & Electronic Records",
        "description": "The IT Act provides legal recognition to electronic records and digital signatures, enabling e-commerce and secure digital governance in India.",
        "penalty": "N/A - Regulatory Framework"
    }
]

scenarios = [
    {
        "id": 1,
        "scenario_text": "Anish's laptop is left unlocked at a cafe. A person sits down, accesses his computer without authorization, and copies proprietary code files to a pendrive.",
        "questions": [
            {
                "q": "What type of cyber issue is involved?",
                "options": ["Identity Theft", "Unauthorized Access and Data Theft", "Cyber Terrorism", "Phishing"],
                "answer": "Unauthorized Access and Data Theft",
                "explanation": "Accessing someone's computer and downloading files without permission constitutes unauthorized access."
            },
            {
                "q": "Which legal provision under the IT Act 2000 is primarily applicable for unauthorized access and data extraction?",
                "options": ["Section 43 read with Section 66", "Section 67", "Section 66C", "Section 66F"],
                "answer": "Section 43 read with Section 66",
                "explanation": "Section 43 deals with damage to computers (including data extraction), and Section 66 provides the punishment for dishonestly doing so."
            }
        ]
    },
    {
        "id": 2,
        "scenario_text": "A fraudster creates a fake Facebook profile using Neha's name and photos. The fraudster then messages Neha's friends asking for money, claiming an emergency.",
        "questions": [
            {
                "q": "Which cyber law section deals specifically with cheating by personation using a computer resource?",
                "options": ["Section 66A", "Section 66D", "Section 43", "Section 67"],
                "answer": "Section 66D",
                "explanation": "Section 66D of the IT Act punishes cheating by personation using a computer resource or communication device."
            }
        ]
    }
]
