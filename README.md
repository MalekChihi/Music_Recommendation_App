# 🎶 Music Recommendation App

A **music recommendation system** built with Python and Streamlit that suggests songs similar to your selection, with optional filtering by artist.

---

## 🚀 Features

- Browse and select from thousands of songs in the dataset
- Get personalized song recommendations based on similarity
- **Filter recommendations by specific artist** (optional)
- **Adjust number of recommendations** with an interactive slider (1-20 songs)
- Modern, gradient-styled UI with responsive design

---

## 🧰 Technologies Used

- **Python 3**
- **Streamlit** - Interactive web app interface
- **Pandas** - Data manipulation and analysis
- **NLTK** - Natural language processing for text preprocessing
- **Scikit-learn** - TF-IDF vectorization and cosine similarity
- **Joblib** - Model and data serialization

---

## 📂 Dataset

This project uses the **Spotify Million Songs Dataset**, publicly available on Kaggle:  
[Spotify Million Songs Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)

> ⚠️ **Important:** The dataset CSV file is **not included** in this repository due to its large size.  
> Please download it from Kaggle and place it at `src/spotify_millsongdata.csv` before running the app.

---

## 🏃 How to Run

1. **Clone the repository:**
```bash
   git clone https://github.com/MalekChihi/Music_Recommendation_App.git
   cd Music_Recommendation_App
```

2. **Download the dataset:**
   - Get the dataset from [Kaggle](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)
   - Place `spotify_millsongdata.csv` in the `src/` folder

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Run the app:**
```bash
   cd src
   streamlit run main.py
```

5. **Open your browser** and navigate to the local URL shown in the terminal (usually `http://localhost:8501`)

---

## 📝 Credits

- Inspired by [Siddhardhan's YouTube tutorial](https://www.youtube.com/watch?v=ic1tlRD0VoE&t=454s)
- Dataset from [Kaggle - Spotify Million Songs Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)

---



## 👤 Author

**Malek Chihi**  
GitHub: [@MalekChihi](https://github.com/MalekChihi)