topics = [
    {
        "title": "Public Wi-Fi & Evil Twin Attacks",
        "description": "Connecting to unsecured public Wi-Fi networks exposes your data to interception. An 'Evil Twin' is a fake Wi-Fi access point setup by an attacker that looks like a legitimate network.",
        "prevention": "Use a VPN on public Wi-Fi, avoid financial transactions, and verify the network name with staff."
    },
    {
        "title": "Mobile Malware & Malicious Apps",
        "description": "Apps downloaded from unofficial sources may contain malware, spyware, or keyloggers designed to steal credentials and personal data.",
        "prevention": "Only install apps from official stores (Play Store/App Store), read reviews, and check requested permissions."
    },
    {
        "title": "Smishing & SIM Swapping",
        "description": "Smishing uses SMS to trick users into clicking malicious links. SIM Swapping occurs when an attacker convinces your carrier to transfer your number to their SIM to steal OTPs.",
        "prevention": "Never click unverified SMS links. Use authenticator apps instead of SMS for 2FA."
    },
    {
        "title": "Lost/Stolen Device Risks",
        "description": "If a mobile device is lost or stolen without adequate protection, attackers can access emails, photos, and financial apps.",
        "prevention": "Use strong screen locks, enable biometric authentication, encrypt the device, and turn on 'Find My Device' to remote wipe if needed."
    }
]

quiz = {
    "title": "Mobile & Wireless Security Quiz",
    "questions": [
        {
            "q": "You are at a coffee shop and see a free Wi-Fi network named 'CoffeeShop_Free_WiFi'. What is the safest action?",
            "options": [
                "Connect immediately and check your bank balance.",
                "Verify the exact network name with the staff before connecting.",
                "Connect but only use it to download apps.",
                "Turn off your firewall to get a better connection."
            ],
            "answer": "Verify the exact network name with the staff before connecting.",
            "explanation": "Attackers often set up 'Evil Twin' networks with names similar to the real one to intercept your traffic."
        },
        {
            "q": "An app you downloaded to change your wallpaper requests permission to read your SMS and access your contacts. What should you do?",
            "options": [
                "Grant the permissions; apps need them to work.",
                "Deny the permissions and uninstall the app.",
                "Grant them temporarily.",
                "Ignore it."
            ],
            "answer": "Deny the permissions and uninstall the app.",
            "explanation": "A wallpaper app has no legitimate reason to read SMS or contacts. This is a strong indicator of a malicious application."
        },
        {
            "q": "Which of the following is the best defense against a SIM Swapping attack?",
            "options": [
                "Using an Authenticator App (like Google Authenticator) for 2FA instead of SMS.",
                "Changing your phone number every month.",
                "Keeping your phone on airplane mode.",
                "Using a complex screen lock PIN."
            ],
            "answer": "Using an Authenticator App (like Google Authenticator) for 2FA instead of SMS.",
            "explanation": "Authenticator apps generate tokens locally on the device and are not tied to your phone number, making them immune to SIM swapping."
        }
    ]
}
