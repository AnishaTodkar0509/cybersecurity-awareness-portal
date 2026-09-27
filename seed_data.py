import database

def seed():
    with database.get_db() as conn:
        cursor = conn.cursor()
        
        # Seed Threats
        threats = [
            ("Virus", "Malware", "A malicious program that attaches itself to legitimate files and spreads when the file is executed.", "System slowdown, file corruption, unexpected pop-ups.", "Use updated antivirus, do not run unknown executables."),
            ("Phishing", "Social Engineering", "Fraudulent attempts to obtain sensitive information by disguising as a trustworthy entity.", "Suspicious emails with urgent requests, mismatched URLs.", "Verify sender addresses, never click suspicious links."),
            ("Ransomware", "Malware", "Malware that encrypts the user's data and demands payment for the decryption key.", "Inability to open files, ransom demand screen.", "Maintain offline backups, avoid suspicious downloads."),
            ("Trojan Horse", "Malware", "Malicious software disguised as legitimate software.", "Unexpected system behavior, unauthorized remote access.", "Download software only from official sources.")
        ]
        
        for t in threats:
            cursor.execute('SELECT * FROM threats WHERE name = ?', (t[0],))
            if not cursor.fetchone():
                cursor.execute('INSERT INTO threats (name, category, description, symptoms, prevention) VALUES (?, ?, ?, ?, ?)', t)
                
        # Seed CO1 Quiz Questions
        questions = [
            ("You receive an email claiming your bank account will be blocked unless you click a link. What type of attack is this?",
             "Virus", "Phishing", "Worm", "Trojan", "B", 
             "Phishing relies on social engineering to trick victims into clicking malicious links by creating a false sense of urgency.",
             "CO1", "Threat Identification"),
            ("Which of the following self-replicates without needing a host file?",
             "Virus", "Trojan", "Worm", "Keylogger", "C",
             "Worms are standalone malicious programs that can self-replicate and spread independently.",
             "CO1", "Threat Identification")
        ]
        
        for q in questions:
            cursor.execute('SELECT * FROM questions WHERE question_text = ?', (q[0],))
            if not cursor.fetchone():
                cursor.execute('INSERT INTO questions (question_text, option_a, option_b, option_c, option_d, correct_option, explanation, co_code, category) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', q)
                
        conn.commit()
        print("Database seeded with sample data.")

if __name__ == "__main__":
    seed()
