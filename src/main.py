import streamlit as st
from recommend import df, recommend_songs

# Modern header with gradient background
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    }
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        margin: 0;
        font-weight: 700;
    }
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    .filter-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 1rem;
    }
    .results-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>🎶 Instant Music Recommender</h1>
        <p>Discover your next favorite song based on what you love</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 🎵 Choose Your Song")
song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox(
    "Select a song to get recommendations:",
    song_list,
    label_visibility="collapsed"
)

st.markdown("### 🎚️ Settings")
top_n = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=20,
    value=5,
    help="How many similar songs would you like to see?"
)

# Artist filter in an expander for cleaner look
with st.expander("🎤 Advanced Filters (Optional)"):
    artist_filter = st.text_input(
        "Filter by artist name:",
        placeholder="e.g., Taylor Swift, Drake...",
        help="Leave empty to see recommendations from all artists"
    )

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# Recommend button
if st.button("🚀 Get Recommendations"):
    with st.spinner("✨ Finding similar songs..."):
        recommendations = recommend_songs(selected_song, top_n=50)

        if recommendations is not None and artist_filter:
            recommendations = recommendations[
                recommendations['artist'].str.contains(artist_filter, case=False, na=False)
            ]
            recommendations = recommendations.head(top_n)

        if recommendations is None or len(recommendations) == 0:
            st.error("😔 Sorry, no recommendations found matching your criteria.")
        else:
            st.markdown("""
                <div class="results-card">
                    <h3 style='text-align: center; color: #2d3748; margin-bottom: 1.5rem;'>
                        Top Similar Songs
                    </h3>
                </div>
            """, unsafe_allow_html=True)

            # Display as a clean table
            display_df = recommendations[['song', 'artist']].copy()
            display_df.columns = ['Song', 'Artist']
            display_df.index = range(1, len(display_df) + 1)

            st.dataframe(
                display_df,
                use_container_width=False,
                hide_index=False
            )