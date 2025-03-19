import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def read_data():
    df = pd.read_csv("data/Supahcoolsoft.csv")
    
    return df

df = read_data()

print(df)
print(df.columns)

def layout():
    st.markdown("# Executive dashboard")
    st.markdown("This is a simple dashboard about employees at Supahcoolsoft. The results from the employees can be filtered in this dashboard.")
    
    # ------- basic statistics on employees (total count, average age, average salary) --------
    
    total_records = len(df)
    average_age = df["Age"].mean()
    average_salary = f"${df['Salary_SEK'].mean():.2f}" # för att kunna formatera till två decimaler
    
    cols = st.columns(3)  # Skapa 3 kolumner
    kpis = (total_records, average_age, average_salary)
    labels = ("Total employees", "Average age", "Average salary")

    # Iterera över kolumnerna och visa KPI:erna i respektive kolumn
    for i, (col, label, kpi) in enumerate(zip(cols, labels, kpis)):
        with col:  # Använd 'with' för att specificera vilken kolumn vi skriver till
            st.metric(label=label, value=kpi)

    # ----- show a table with employee details -------
    
    st.markdown("## Employee details")
    st.dataframe(df)
    
    # ----- bar chart showing number of employees accross departments -------
    
    st.markdown("## Number of employees per department")
    df_grouped = df.groupby("Department").size().reset_index(name="Number of employees")
    fig = px.bar(df_grouped, x="Department", y="Number of employees", title="Number of employees per department", labels={"Department": "Department", "Number of employees": "Number of employees"}, color="Number of employees", color_continuous_scale="Blues")
    st.plotly_chart(fig)
    
    # ----- histogram of salary distribution -------
    st.markdown("## Salary distribution - histogram with plotly express")
    fig = px.histogram(df, x="Salary_SEK", title="Salary Distribution") # Histogram-funktionen "vet" att den ska räkna antalet förekomster av varje värde
    st.plotly_chart(fig)

    # ----- box plot of salaries by department -------
    st.markdown("## Salary distribution by department - box plot with plotly express")
    fig = px.box(df, x="Department", y="Salary_SEK", title="Salary distribution by department")
    st.plotly_chart(fig)
    
    # ----- histogram of age distribution -------
    st.markdown("## Age distribution - histogram with plotly express")
    fig = px.histogram(df, x="Age", title="Age Distribution")
    st.plotly_chart(fig)
    
    # ----- box plot of ages by department -------
    st.markdown("## Age distribution by department - box plot with plotly express")
    fig = px.box(df, x="Department", y="Age", title="Age distribution by department") # Bara skriv med det du vill ha med :)
    st.plotly_chart(fig)
    

if __name__ == "__main__":
    layout()
