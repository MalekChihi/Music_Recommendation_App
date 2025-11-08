# 🎶 Music Recommendation App

This is a **music recommendation system** built with Python and Streamlit.  
It suggests songs similar to the one you choose, with optional filtering by artist.

---

## 🚀 Features

- Select any song from the dataset.
- Optional filter to get recommendations from a specific artist.
- Top-N recommendations adjustable with a slider.
- Modern, responsive UI with Streamlit.

---

## 🧰 Technologies Used

- **Python 3**
- **Streamlit** for the web app interface
- **Pandas, NLTK** for data preprocessing
- **Scikit-learn** for TF-IDF vectorization and cosine similarity
- **Joblib** for saving preprocessed data

---

## 📂 Dataset

This project uses the **Spotify Million Songs Dataset**, publicly available on Kaggle:  
[Spotify Million Songs Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)

> ⚠️ The dataset CSV file is **not included** in this repo due to its large size.  
> Please download it from Kaggle and place it in `src/spotify_millsongdata.csv` before running the app.

---

## 📝 Credits

- Inspired by [Siddhardhan's YouTube tutorial](https://www.youtube.com/watch?v=ic1tlRD0VoE&t=454s).  
- Dataset from Kaggle (link above).

---

## 🏃 How to Run

```bash
git clone https://github.com/MalekChihi/Music_Recommendation_App.git
cd Music_Recommendation_App/src
pip install -r requirements.txt
streamlit run main.py
