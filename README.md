# 🏀 NBA Hall of Fame Predictor

This project uses machine learning to predict whether NBA players are likely to be inducted into the Basketball Hall of Fame (HOF). It processes historical player statistics and builds a classification model to score active players based on their chances of HOF induction.

---

## 📌 Project Overview

- **Goal**: Classify players as HOF inductees (1) or not (0) and score current (active) players (2) by probability.
- **Data Source**: NBA player statistics with an `In_Hall_of_Fame` label (0 = Not Inducted, 1 = Inducted, 2 = Active).
- **Model**: Random Forest Classifier (or another binary classification model).
- **Frontend**: Built with Streamlit for easy interactive exploration and visualization.

---

## 📂 Project Structure

NBA_HOF_PROJECT/
│
├── hof_app.py # Streamlit frontend app
├── hof_predictions.csv # Output with HOF probabilities (for active players)
├── requirements.txt # Python dependencies
├── README.md # Project overview and guide

---

## ⚙️ How It Works

### 1. **Preprocessing**
- All players with `In_Hall_of_Fame == 2` (active) are separated for prediction.
- Only `0` and `1` labeled data is used to train the model.

### 2. **Model Training**
- A binary classifier is trained to distinguish between Hall of Famers and others.
- The best threshold for classification (e.g., 0.37) is found using ROC curve tuning.

### 3. **Prediction**
- Probabilities are generated for active players using `predict_proba`.
- Players are marked as predicted HOF (`1`) if their probability exceeds the threshold.

### 4. **Visualization**
- Top candidates are shown using interactive bar plots.
- Search and filter functionality to find individual players.
- Option to download prediction results.

---

## 🖥️ Run the App

1. **Install dependencies**:

```bash
pip install -r requirements.txt
streamlit run app.py
```

🧪 Features of the Web App
🔍 Search for any player

📊 Visualize top candidates

🎯 Tune Threshold and see live updates

📥 Download results in CSV

🚀 Clean and responsive interface

🛠 Future Improvements
Add model training interface to retrain with new data

Add more advanced visualizations (e.g., career progression, clustering)

Deploy via Streamlit Cloud or Hugging Face Spaces

👤 Author
Somin Shah
B.Tech in Electronics and Computer Science
KJ Somaiya College of Engineering

