from read_data import read_data
import streamlit as st

df = read_data()

# MED .query-metoden
approved = df.query("Beslut == 'Beviljad'")
not_approved = df.query("Beslut == 'Avslag'")

#calcylate kpis
number_of_approved = len(approved)
number_of_not_approved = len(not_approved)
total_applications = len(df)
approved_percentage = f"{number_of_approved / total_applications*100:.1f}%"

# Med vanlig panda-syntax
# approved = df[df["Beslut"] == "Beviljad"]

if __name__ == "__main__":
    #for tesing purpose
    approved
    
    st.write(f"Number of approved applications: {number_of_approved} ")
    st.write(f"Number of denied applications: {number_of_not_approved} ")