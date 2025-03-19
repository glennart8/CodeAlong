import pandas as pd
import streamlit as st

def read_data():
    df = pd.read_csv("data/IceCreamData.csv")  # Din CSV fil
    return df

df = read_data()

def layout():
    st.markdown("# Ice Cream Shop Revenue Prediction")
    st.markdown("Enter the temperature in Celsius to predict revenue.")

    temperature = st.number_input("Temperature (Celsius)", min_value=-30.0, max_value=50.0, value=20.0, step=1.0)

    # Gruppera temperaturen baserat på de två första siffrorna
    group_key = int(temperature) // 1  # Ta bort decimalerna och konverterar till INT

    try:  # Lägg till felhantering
        # Gruppera datan och beräkna medelvärdet direkt
        grouped_data = df.groupby(df['Temperature'].apply(lambda x: int(x) // 1))['Revenue'].mean()

        # Hämta medelvärdet för den aktuella gruppen
        mean_revenue = grouped_data[group_key]
    except KeyError:  # Om gruppen inte existerar
        st.error(f"No revenue data found for temperatures starting with {group_key}.")
        return  # Avsluta funktionen
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return

    st.markdown("## Prediction")
    st.write(f"Predicted Revenue: ${mean_revenue:.2f}")

if __name__ == "__main__":
    layout()
