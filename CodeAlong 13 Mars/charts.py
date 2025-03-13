from read_data import read_data
import duckdb
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# Plots som ska visa antal godkända ansökningar per utbildningsområde (grupperade efter utbildningsområde)

# --- streamlit plot ---
def approved_by_area_bar():
    df = read_data()
    df = duckdb.query(""" 
                    SELECT utbildningsområde, COUNT(*) AS Beviljade
                    FROM df
                    WHERE beslut = 'Beviljad'
                    GROUP BY utbildningsområde
                    ORDER BY Beviljade
                    DESC
                    """).df()
    
    st.bar_chart(df, x = "Utbildningsområde", y = "Beviljade")

# --- matplotlib plot --- 
def approved_by_area_bar_matplotlib():
    df = read_data()
    df_filtered = df[df["Beslut"] == "Beviljad"]
    df_grouped = df_filtered.groupby("Utbildningsområde").size().reset_index(name="Beviljade")# Grupp för att räkna godkända ansökningar per utbildningsområde

    plt.figure(figsize=(10, 6))  
    plt.bar(df_grouped["Utbildningsområde"], df_grouped["Beviljade"], color='skyblue')  
    plt.xlabel('Utbildningsområde') 
    plt.ylabel('Antal Beviljade Ansökningar')  
    plt.title('Godkända Ansökningar per Utbildningsområde')  
    plt.xticks(rotation=45, ha="right")  
    plt.tight_layout()  # För att justera layouten så att alla etiketter syns
    # plt.show()
    st.bar_chart(df_grouped, x = "Utbildningsområde", y = "Beviljade")
    
# --- plotly express plots ---
def approved_by_area_bar_plotly():
    df = read_data()
    df_filtered = df[df["Beslut"] == "Beviljad"]
    df_grouped1 = df_filtered.groupby("Utbildningsområde").size().reset_index(name="Beviljade")

    fig = px.bar(df_grouped1, x="Utbildningsområde", y="Beviljade", 
                 title="Godkända Ansökningar per Utbildningsområde", 
                 labels={"Utbildningsområde": "Utbildningsområde", "Beviljade": "Antal Beviljade Ansökningar"},
                 color="Beviljade", 
                 color_continuous_scale="Blues")  # Fejdar på blåskala, mkt snyggare
    fig.update_xaxes(tickangle=45)  # Roterar x-axelns etiketter för bättre läsbarhet
    
    # fig.show()
    st.plotly_chart(fig)
    
if __name__ == "__main__":
    print(approved_by_area_bar_matplotlib())