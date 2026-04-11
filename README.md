# 🤖 Sentiment Analysis Web App  
### 📌 Post Lab – Information Retrieval (IR) Practical.

---

## 📖 Overview:

This project is developed as part of the **Post Lab work for Information Retrieval (IR) Practical**.  
It demonstrates how textual data (simulating social media posts) can be processed and analyzed to determine user sentiment using Machine Learning techniques.

The system follows an **Information Retrieval (IR) pipeline**, including preprocessing, feature extraction, classification, and evaluation.

---

## 🎯 Objective:

- To acquire and preprocess text data  
- To extract meaningful features using TF-IDF  
- To classify text into **positive** or **negative** sentiment  
- To evaluate model performance  
- To build a simple web interface for real-time prediction  

---

## 🚀 Features:

- 🔍 Text preprocessing (lowercasing, cleaning, stopword removal)
- 🧠 Machine Learning model (TF-IDF + Logistic Regression)
- 🌐 Interactive web application using Flask
- ⚡ Real-time sentiment prediction
- 📢 Sample post analysis display
- 📊 Model accuracy evaluation

---

## 🛠️ Tech Stack:

| Category        | Technology Used        |
|----------------|----------------------|
| Programming    | Python               |
| Backend        | Flask                |
| ML Library     | Scikit-learn         |
| NLP            | NLTK                 |
| Frontend       | HTML, CSS            |

---

## ⚙️ System Architecture:

User Input → Preprocessing → TF-IDF Vectorization → ML Model → Prediction → Display Result.

---

## 🔄 Workflow:

1. User enters text (simulating social media post)  
2. Text is preprocessed:
   - Lowercasing  
   - Removing special characters  
   - Stopword removal  
3. TF-IDF converts text into numerical vectors  
4. Logistic Regression model predicts sentiment  
5. Result is displayed on the web interface  

---

## 📂 Project Structure:

sentiment_app/
│
├── app.py # Flask web application
├── model.py # ML model and preprocessing
├── data.csv # Dataset
└── templates/
└── index.html # Frontend UI

---

## ▶️ How to Run the Project:

1. Install dependencies (pip install flask pandas scikit-learn nltk)
2. Run the application
'python app.py'
3. Open in browser:
http://127.0.0.1:5000
