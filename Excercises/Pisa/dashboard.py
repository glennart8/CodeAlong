# PISA performance usually get a lot of media attention on how good it's going for the school in your country. 
# It has gotten a lot of media attention at least in Sweden where I live. 
# Use this dataset of pisa performance and create a dashboard. It should contain a minimum of this:

# basic statistics of the data (number of records, number of locations, subjects, and time periods)
# show a table with sample data
# bar chart showing average PISA scores by location
# plot trends that can be filtered for each country
# Bonus:

# more interactive filtering to drill down to specific locations, time period, subjects, ...
# this filtering should be displayed on a side panel

import pandas as pd
import streamlit as st
import plotly.express as px

def read_data():
    df = pd.read_csv("data/OECD PISA data.csv")
    return df

df = read_data()

print(df.columns) # Index(['index', 'LOCATION', 'INDICATOR', 'SUBJECT', 'TIME', 'Value'], dtype='object')
print(df.head())

def layout():
    st.markdown("# Dasboard for PISA data")

# ---- Basic statistics ----
    number_of_records = len(df)
    number_of_locations = len(df["LOCATION"].unique())
    subjects = df["SUBJECT"].unique()
    time_periods = df["TIME"].unique()
    
    cols = st.columns(4)
    kpis = (number_of_records, number_of_locations, len(subjects), len(time_periods))
    labels = ("Number of records", "Number of locations", "Number of subjects", "Number of time periods")
    
    for i, (col, label, kpi) in enumerate(zip(cols, labels, kpis)):
        with col:
            st.metric(label=label, value=kpi)
    
# ---- Show a table with sample data ----
    st.markdown("## Sample data")
    st.dataframe(df)
    
# ---- Bar chart showing average PISA scores by location ----
    st.markdown("## Average PISA scores by location")
    df_grouped = df.groupby("LOCATION")["Value"].mean().reset_index(name="Average PISA score") # Beräknar medelvärdet för alla år. Gör en ny kolumn med medelvärdet för varje land
    fig = px.bar(df_grouped, x="LOCATION", y="Average PISA score", title="Average PISA scores by location", color="Average PISA score", color_continuous_scale="Blues")
    st.plotly_chart(fig)

# ---- plot trends that can be filtered for each country ----
    st.markdown("## Trends by location")
    location = st.selectbox("Select location", df["LOCATION"].unique())
    subject = st.selectbox("Select subject", df["INDICATOR"].unique())
    df_filtered = df[df["LOCATION"] == location]
    df_filtered = df_filtered[df_filtered["INDICATOR"] == subject]
    df_filtered = df_filtered[df_filtered["SUBJECT"] != "TOT"]  # Filtrera bort 'TOT'

    fig = px.line(df_filtered, x="TIME", y="Value", color="SUBJECT",  # SUBJECT är kön, inte ämne :S
                  title=f"Trends in {subject}, for {location}", #Använd subject variabeln i titeln
                  labels={"TIME": "Time", "Value": "Value", "SUBJECT": "Gender"}, #Fler lablar
                  color_discrete_sequence=["skyblue", "pink"])  # Justera färgerna

    st.plotly_chart(fig)


if __name__ == "__main__":
    layout()