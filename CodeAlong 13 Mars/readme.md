
WIDGETS
1. Läs in data
2. Hämta ut den relevanta datan och spara i variabler/funktioner
3. Skapa tuples av kolumner (Ett antal), labels(rubriker) och kpis (värden)
4. Loopa igenon dessa samtidigt med zip
5. med with col: skriv ut resultatet

CHART
1. Skapa en meny där allt sker (enklare att anropa i stället för att spara alla variabler)
2. Läs in data (igen) och spara till en variabel (df)
3. Kör df med duckdb.query och ställ fråga i SQL-format.
4. st.bar_chart(df, x="blabla", y="blabla")
5. Anropa denna funktion ifrån dashboarden

FILTRERA RESULTAT EFTER VALD SKOLA
0. Skapa en st.selectbox där man ombes välja bland dfs utbildningsanordnare
1. Skapa metod med en "provider" som inparameter (1-4)
2. Filtrera dataframe efter vald "provider"
3. Hämta resultat från provider ang antal sökningar och antal beviljade beslut
4. Returnera antalen ansökningar roch beviljade beslut
5. Skriv ut text med antal ansökningar och beslut



