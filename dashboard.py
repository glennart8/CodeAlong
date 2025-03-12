# ===========================
# SWEDEN OLYMPICS DASGBOARD
# ===========================


# === SET UP ===
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

import read_data


# Kör i webbläsare med kommando: streamlit run dashboard.py

# ==========================
# DASHBOARD COMPONENTS
# ==========================

url = "https://en.wikipedia.org/wiki/Sweden_at_the_Olympics"
df = read_data.read_olympics_data(url)

# Markdown Title
st.write("## Sweden olympic medal history from 1960s")

## Dropdown list
selected_year = st.selectbox("Select Year", ["All"] + sorted(df["Year"].unique()))

## DataFrame filtered by dropdown list
if selected_year != "All":
    filtered_df = df[df["Year"] == selected_year] # Filtrerar listan efter valt år
else:
    filtered_df = df
    
st.dataframe(filtered_df.reset_index(drop=True))

## Three graphs
st.write("### Graphsby different libraries")

# by matplotlib
st.write("#### By Matplotlib")

fig, ax = plt.subplots()
ax.bar(filtered_df["Year"], filtered_df["Total"])
ax.set_xlabel("Year")
ax.set_ylabel("Total medals")
ax.set_title("Total medals by year")
st.pyplot(fig)

# by plotly_express
st.write("#### By Plotly_express")
fig = px.bar(filtered_df, x="Year", y="Total", title="Total medals by year")
st.plotly_chart(fig)

# by streamlit 
st.write("#### By Streamlit")
st.bar_chart(df.set_index("Year")) # Bar chart

