# Analiza danych dotyczących przestępczości

Główny notebook projeku: [MainNotebook](./Notebooks/MainNotebook.ipynb)

## Opis projektu
### Zbiory danych:

Zbiór danych, który będziemy analizować opisuje amerykańskie społeczności oraz posterunki policji w kontekście ilości popełnionych przestępstw.

Nieznormalizowany, którego będziemy używac do eksploracyjnej analizy danych: Communities and Crime Data Set https://archive.ics.uci.edu/ml/datasets/Communities+and+Crime+Unnormalized

Znormalizowany, którego będziemy używac przy uczeniu: Communities and Crime Data Set

https://archive.ics.uci.edu/ml/datasets/Communities+and+Crime

W celu utworzenia wykresów będziemy korzystać z danych geograficznych uzyskanych poprzez API https://opencagedata.com/api. Pobieranie danych realizuje [skrypt](./Scripts/cities_lat_long_downloader.py).

## Cel projektu:
Znalezienie współczynnika ilości przestępstw.

## Etapy projektu
### Eksploracyjna analiza danych
+ sprawdzenie zależności między posiadanymi danymi,
+ zbadanie ich zakresów i stopnia zmienności,
+ analiza stopnia wypełnienia danych,
+ wizualizacja.

### Opracowanie modelu
+ opracowanie modelu regresjii,
+ dobór cech,
+ regularyzacja,
+ wyciągnięcie wniosków z zależności.

## Wykorzystane modele
+ Linear Regression
+ Ridge Regression
+ LASSO Regression
+ ElasticNet Regression

## Rozwój projektu
Projekt może być rozwijany w kilku obszarach:

1. Dodanie cech łączących posiadane.
2. Dołączenie danych z innych źródeł, np. więcej danych dotyczących policji.
3. Wypróbowanie innych modeli, np. drzew decyzyjnych lub sieci neuronowych.