import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
from kpis import approved_percentage, number_approved, total_applications, approved, provider_kpis # Man kan importera både funktioner och variabler
from read_data import read_data
from charts import approved_by_area_bar, approved_by_area_bar_matplotlib, approved_by_area_bar_plotly

df = read_data()

def layout():
    st.markdown("# YH dashboard 2024 application")
    st.markdown("This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard.")
    
    st.markdown("## KPIs in Sweden")
    
    cols = st.columns(3) # Skapar tre kolumner
    labels = ("Total applications", "Number approved", "Approved percentage") # En tuple som innehåller tre strängar ("Rubriker")
    kpis = (total_applications, number_approved, approved_percentage) # En tuple som innehåller tre VÄRDEN (siffror)

    for col, label, kpi in zip(cols, labels, kpis): # Loopar igenom tre listor samtidigt
        # col är en kolumn, label är en sträng och kpi är en siffra
        with col:  # Skapar ett context där allt innehåll inom blocket (with) kommer att visas i den aktuella kolumnen (col).
            st.metric(label=label, value=kpi) # label är rubriken och value är värdet som hämtas från kpi

    st.markdown("## CHART - Aproved by area")
    approved_by_area_bar()
    st.markdown("## CHART - With Matplotlib")
    approved_by_area_bar_matplotlib() # Visar inget i streamlit
    st.markdown("## CHART - Plotly Express")
    approved_by_area_bar_plotly() # Öppnas i en separat flik

    st.markdown("## Simple statistics on a given provide")
    st.markdown("Search for an educational provider")

    provider = st.selectbox("Choose educational provider", df["Utbildningsanordnare administrativ enhet"].unique(),)
    provider_applications, provider_approved = provider_kpis(provider)
    st.markdown(f"This education provider {provider} has applied for {provider_applications} educations and gotten {provider_approved} educations approved")

    st.markdown("## Raw data")
    st.dataframe(df)



if __name__ == "__main__":
    layout()


#use matplotlib, plotly express and streamlit for graphs separately