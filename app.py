from urllib.parse import urlparse

from flask import Flask, render_template, request 

app = Flask(__name__)


import re

def check_url(url):
    score = 0
    reasons = []

    if "@" in url:
        score += 40
        reasons.append("@ symbol found")

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 30
        reasons.append("IP address used")

    if "-" in url:
        score += 10
        reasons.append("Hyphen (-) found")

    if len(url) > 75:
        score += 10
        reasons.append("Very long URL")

    if not url.startswith("https://"):
        score += 10
        reasons.append("Not using HTTPS")

    if "login" in url.lower():
        score += 10
        reasons.append("Login keyword found")

    if "verify" in url.lower():
        score += 10
        reasons.append("Verify keyword found")

    if "update" in url.lower():
        score += 10
        reasons.append("Update keyword found")

    if "secure" in url.lower():
        score += 5
        reasons.append("Secure keyword found")

    if score >= 50:
        return "🔴 Phishing Website", score, reasons 
    elif score >= 20:
        return "🟡 Suspicious Website", score, reasons
    else:
        return "🟢 Safe Website", score, reasons


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    url = None
    score=0
    reasons = []
    domain =""

    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        if url:
            domain = urlparse(url).netloc
            result,score,reasons =  check_url(url)

    return render_template('index.html', result=result, score=score, url=url, domain=domain,reasons=reasons)


if __name__ == '__main__':
    app.run(debug=True)