# recommend.py
import joblib
import logging
import pandas as pd

# -------------------- Logging Setup --------------------
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("recommend.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logging.info("🔁 Loading preprocessed data...")

try:
    df: pd.DataFrame = joblib.load('df_cleaned.pkl')
    cosine_sim = joblib.load('cosine_sim.pkl')
    logging.info("✅ Data loaded successfully.")
except Exception as e:
    logging.error("❌ Failed to load required files: %s", str(e))
    raise e


def recommend_songs(song_name: str, top_n: int = 5) -> pd.DataFrame | None:
    """
    Recommend similar songs based on cosine similarity.

    :param song_name: Name of the song to find recommendations for
    :param top_n: Number of similar songs to return
    :return: DataFrame of recommended songs or None if not found
    """
    logging.info("🎵 Recommending songs for: '%s'", song_name)
    idx = df[df['song'].str.lower() == song_name.lower()].index
    if len(idx) == 0:
        logging.warning("⚠️ Song not found in dataset.")
        return None
    idx = idx[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    song_indices = [i[0] for i in sim_scores]

    result_df = df[['artist', 'song']].iloc[song_indices].reset_index(drop=True)
    result_df.index = result_df.index + 1  # Start from 1
    result_df.index.name = "S.No."
    logging.info("✅ Top %d recommendations ready.", top_n)
    return result_df
