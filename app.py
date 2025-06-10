import streamlit as st
import pandas as pd

st.title("🏀 NBA Hall of Fame Predictions")

df = pd.read_csv("hof_predictions.csv")  # Your final df_active

threshold = 0.37
df['HOF_predicted'] = (df['HOF_probability'] >= threshold).astype(int)

st.dataframe(df[['player', 'HOF_probability', 'HOF_predicted']].sort_values(by='HOF_probability', ascending=False))

st.bar_chart(df.set_index('player')['HOF_probability'].head(10))
