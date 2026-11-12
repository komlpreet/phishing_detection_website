# 🔐 Phishing Website Detection System

## 📌 Project Overview

The **Phishing Website Detection System** is a web-based application developed using Python and Flask to identify potentially malicious websites. It helps users analyze website URLs and determine whether a website is Safe, Suspicious, or Phishing.

The system uses a rule-based URL analysis technique to detect common characteristics associated with phishing websites. It calculates a risk score based on predefined URL patterns and displays the detection result along with the reasons behind the classification.

## 🎯 Objectives

- To identify potentially harmful and fraudulent website URLs.
- To analyze URL structures and detect suspicious patterns.
- To calculate a risk score for submitted URLs.
- To provide users with clear and understandable detection results.
- To promote awareness about phishing attacks and online security.

## ✨ Key Features

- **URL Detection:** Analyze website URLs to identify suspicious characteristics.
- **Risk Score Calculation:** Assign points based on predefined security rules.
- **Website Classification:** Classify websites into Safe, Suspicious, or Phishing categories.
- **Reason Identification:** Display the specific URL patterns responsible for the risk score.
- **Domain Extraction:** Extract and display the domain name from the submitted URL.
- **User-Friendly Interface:** Simple web interface for entering and checking URLs.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming and detection logic |
| Flask | Web application framework |
| HTML | Webpage structure |
| CSS | User interface styling |
| JavaScript | Frontend interactions |
| Regular Expressions | Detect suspicious URL patterns |

## ⚙️ Working Methodology

The system follows these steps:

1. The user enters a website URL.
2. The Flask application receives the submitted URL.
3. The system analyzes the URL using predefined rules.
4. Risk points are assigned to suspicious URL characteristics.
5. All points are combined to calculate the final risk score.
6. The system classifies the website based on the calculated score.
7. The result, domain, risk score, and detected reasons are displayed to the user.

## 📊 Risk Detection Rules

The application checks the following URL characteristics:

| Detection Rule | Risk Score |
|---|---:|
| @ symbol found | 40 |
| IP address used | 30 |
| Hyphen found | 10 |
| URL length greater than 75 characters | 10 |
| HTTPS not used | 10 |
| Login keyword found | 10 |
| Verify keyword found | 10 |
| Update keyword found | 10 |
| Secure keyword found | 5 |

### Website Classification

- 🟢 **Safe Website:** Risk score below 20.
- 🟡 **Suspicious Website:** Risk score between 20 and 49.
- 🔴 **Phishing Website:** Risk score of 50 or above.

## 💻 Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### Step 2: Open the Project Directory

```bash
cd your-repository-name
```

### Step 3: Install Required Library

```bash
pip install flask
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

Visit the following address:

```text
http://127.0.0.1:5000/
```

The application is now ready to use.

## 📁 Project Structure

```text
Phishing-Detection-Website/
│
├── app.py
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

*Note: The folder structure above represents the expected Flask project organization. Adjust filenames according to your actual repository.*

## 🔍 Applications

- Identifying suspicious website URLs.
- Basic phishing awareness and education.
- Understanding common phishing URL characteristics.
- Demonstrating web application development using Python and Flask.
- Learning basic cybersecurity concepts.

## 🚀 Future Enhancements

- Integration with machine learning algorithms for improved detection.
- Connection with real-time phishing URL databases.
- Advanced URL feature extraction.
- Improved URL validation and security analysis.
- Scan history and detailed reporting.
- Enhanced detection accuracy using threat intelligence services.

## ⚠️ Limitations

This project currently uses predefined rule-based techniques rather than machine learning or real-time threat intelligence. Therefore, the results are indicative and cannot guarantee that a website is completely safe or malicious.

## 👨‍💻 Conclusion

The Phishing Website Detection System provides a simple and effective approach to analyzing website URLs using Python and Flask. By identifying suspicious URL patterns and calculating risk scores, the application helps users understand potential phishing threats and improves basic awareness of online security.

---

**Project Name:** Phishing Website Detection System

**Domain:** Cybersecurity / Web Development

**Programming Language:** Python

**Framework:** Flask
