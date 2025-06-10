import streamlit as st
import pandas as pd
import plotly.express as px

# Title and description
st.set_page_config(page_title="NBA Hall of Fame Predictor", layout="wide")
st.title("🏀 NBA Hall of Fame Predictor")
st.markdown("This app uses a trained model to predict whether current NBA players are likely to be inducted into the Hall of Fame.")

# Load your prediction DataFrame
@st.cache_data
def load_data():
    df = pd.read_csv("hof_predictions.csv")  # Replace with your actual file
    return df

df = load_data()

# Threshold tuning section
st.sidebar.header("🔧 Threshold Setting")
threshold = st.sidebar.slider("Prediction Threshold", 0.0, 1.0, 0.37, 0.01)

# Apply threshold
df['HOF_predicted'] = (df['HOF_probability'] >= threshold).astype(int)

# Show overall metrics
st.metric("Players Predicted as Hall of Famers", int(df['HOF_predicted'].sum()))

# Show top 10 predictions
st.subheader("Top 10 Candidates by Probability")
top_10 = df.sort_values(by='HOF_probability', ascending=False).head(10)
st.dataframe(top_10[['player', 'HOF_probability', 'HOF_predicted']].style.format({"HOF_probability": "{:.2f}"}))

# Visualization
fig = px.bar(top_10, x='player', y='HOF_probability', color='HOF_predicted',
             labels={'HOF_probability': 'Probability'},
             title='Top 10 Predicted Hall of Fame Candidates')
st.plotly_chart(fig, use_container_width=True)

# Search by player
st.subheader("🔍 Search for a Player")
player_name = st.text_input("Enter full or partial name:")
if True:
    filtered = df[df['player'].str.contains(player_name, case=False)]
    if not filtered.empty:
        st.dataframe(filtered.style.format({"HOF_probability": "{:.2f}"}))
    else:
        st.warning("No players found.")

# Download predictions
st.subheader("📥 Download Results")
st.download_button("Download CSV", data=df.to_csv(index=False), file_name="hof_predictions_thresholded.csv", mime="text/csv")
