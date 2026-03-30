# 📰 Fake News Detection System

## 📌 Overview

This project is a Machine Learning-based system that detects whether a news article is **Fake** or **Real**.
It uses Natural Language Processing (NLP) techniques and a classification model to analyze text data.

---

## 🚀 Features

* Detects fake vs real news
* Uses TF-IDF for feature extraction
* Machine Learning model (Logistic Regression)
* Simple and interactive UI using Streamlit
* Easy to use and extend

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK
* Streamlit

---

## 📂 Project Structure

```
fake-news-detector/
│
├── data/
├── src/
├── models/
├── app/
├── utils/
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone <your-repo-link>
cd fake-news-detector
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Train Model

```
python main.py
```

### Step 2: Run App

```
streamlit run app/app.py
```

---

## 🧪 Example

Input:

```
Aliens landed in India and met officials
```

Output:

```
Fake News
```

---

## 📊 Model Details

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF
* Problem Type: Binary Classification

---

## 🚀 Future Improvements

* Use Deep Learning (LSTM / BERT)
* Add real-time news API
* Improve accuracy with larger datasets
* Multi-language support

---

## 👨‍💻 Author

* Your Name

---

## 📜 License

This project is for educational purposes.
