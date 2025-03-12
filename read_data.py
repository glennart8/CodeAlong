import pandas as pd

def read_olympics_data(url):
    df = pd.read_html(url)[2]  # tredje tabellen 
    
    #data_cleaning
    df = df[13:-3] # Skippa 13 och de sista 3 (framtiden)
    df["Year"] = df["Games"].str[:4] # Skapar en ny kolumn: Tar de 4 första (årtalet i gameskolumnen)
    df["Year"] = df["Year"].astype(int)
    df["Total"] = df["Total"].astype(int)
    df = df[["Year", "Total"]]
    return df


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Sweden_at_the_Olympics"
    df = read_olympics_data(url)

    print(df)
    # print(df.info())

