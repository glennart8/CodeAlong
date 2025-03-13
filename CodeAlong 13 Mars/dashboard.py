# ===============
# MYH dashboard
# ===============

# -- set up --
import streamlit as st
from read_data import read_data 
from kpis import approved_percentage, number_of_approved, total_applications, number_of_not_approved

# -- reading data --
df = read_data()

# -- dashboard components --

#title
st.markdown("# YH dashboard 2024 application")

#description
st.markdown("This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard.")

#kpi components for horizontal layout
st.markdown("## KPIs in Sweden")

labels = ("Total applications", "Approved applications", "Denied applications", "Approved percentage") #Rubrikerna för kolumnerna
kpis = (total_applications, number_of_approved, number_of_not_approved, approved_percentage) #Värdena vi hämtar från kpis.py
cols = st.columns(3)

for col, label, kpi in zip(cols, labels, kpis):
    with col:
        st.metric(label=label, value=kpi)


#data table
st.markdown("## Raw data")
st.dataframe(df)

