# AI-Based URL Phishing Detector (Beginner Level)
# Simple and easy project for school assignment

def check_phishing(url):
    score = 0

    # Rule 1: Long URL
    if len(url) > 30:
        score += 1

    # Rule 2: Contains suspicious symbols
    if "@" in url or "-" in url or "_" in url:
        score += 1

    # Rule 3: Too many dots (subdomains)
    if url.count(".") > 3:
        score += 1

    # Rule 4: No HTTPS
    if not url.startswith("https"):
        score += 1

    # Rule 5: Suspicious keywords
    keywords = ["login", "secure", "verify", "update", "bank"]
    for word in keywords:
        if word in url.lower():
            score += 1
            break

    # Final Decision
    if score >= 3:
        return "⚠️ Phishing URL Detected!"
    else:
        return "✅ Safe URL"


# Main Program
print("🔍 AI-Based URL Phishing Detector")
print("-----------------------------------")

url = input("Enter a URL: ")

result = check_phishing(url)

print("\nResult:", result)