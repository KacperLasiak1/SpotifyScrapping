# Music Event Planner (MEP)

## 1. Charakterystyka oprogramowania

### a. Nazwa skrócona
**MEP**

### b. Nazwa pełna
**Music Event Planner**

### c. Krótki opis ze wskazaniem celów
Music Event Planner to oprogramowanie zaprojektowane do zarządzania wydarzeniami muzycznymi. Główne cele systemu to:
- Analiza popularności artystów.
- Wyliczanie ich kosztów.
- Umożliwienie wyboru najlepszych artystów w określonym budżecie.

Dodatkowo, aplikacja umożliwia wyszukiwanie popularnych miejsc koncertowych w różnych krajach, integrując dane o cenach, dostępności i popularności artystów z funkcjonalnością wyszukiwania lokalizacji koncertów.

---

## 2. Prawa autorskie

### a. Autorzy
- **Kacper Łąsiak**
- **Paweł Kos**

### b. Warunki licencyjne
Oprogramowanie Music Event Planner jest objęte licencją **MIT**.

---

## 3. Specyfikacja wymagań

| **Identyfikator** | **Nazwa**                        | **Opis**                                                                             | **Priorytet** | **Kategoria**  |
|--------------------|----------------------------------|-------------------------------------------------------------------------------------|---------------|----------------|
| 001                | Wyliczanie cen artystów         | System powinien obliczać ceny artystów na podstawie kraju i popularności.           | 1             | Funkcjonalne   |
| 002                | Wybór artystów                  | Umożliwienie użytkownikowi wyboru artystów zgodnie z budżetem i preferencjami.      | 1             | Funkcjonalne   |
| 003                | Wyszukiwanie miejsc koncertowych| System powinien umożliwiać wyszukiwanie popularnych miejsc koncertowych w różnych krajach. | 1         | Funkcjonalne   |
| 004                | Obsługa danych Spotify          | Integracja z API Spotify do pobierania danych o utworach i artystach.               | 2             | Funkcjonalne   |
| 005                | Obsługa błędów                  | System powinien zarządzać i raportować błędy.                                       | 1             | Funkcjonalne   |

---

## 4. Architektura systemu

| **Nazwa**          | **Przeznaczenie**                | **Numer wersji** |
|---------------------|----------------------------------|-------------------|
| Python              | Główny język programowania      | 3.9+              |
| Pandas              | Przetwarzanie i analiza danych  | 1.3.0+            |
| NumPy               | Operacje matematyczne i statystyki | 1.21+          |
| Requests            | Obsługa żądań HTTP (API Spotify)| 2.25+             |
| Google Maps API     | Wyszukiwanie lokalizacji koncertów | Najnowsza       |
| Base64              | Kodowanie danych (autoryzacja)  | Wbudowana w Python |
| Git                 | System kontroli wersji          | Najnowsza         |
| Pycharm             | Edytor kodu                     | Najnowsza         |
| JSON                | Obsługa danych w formacie JSON  | Wbudowana w Python |
| Flask | Podłoże wizualne | 3.1.0+ |

---

## 5. Testy

| **Identyfikator** | **Scenariusz testowy**             | **Kroki do wykonania**                                                                   | **Oczekiwany rezultat**                                                                    | **Status** |
|--------------------|------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|------------|
| 001                | Wybór artystów z odpowiednim budżetem | 1. Uruchom aplikację. 2. Wprowadź budżet 50 000 zł. 3. Wybierz liczbę artystów: 3.         | Aplikacja wyświetla listę artystów, których można wybrać w podanym budżecie.               | Sukces     |
| 002                | Analiza kraju z wykluczeniem artystów explicit | 1. Wprowadź kraj: "Poland". 2. Wybierz opcję wykluczenia artystów explicit.               | Wynikiem jest lista artystów w Polsce bez treści explicit.                                 | Sukces     |
| 003                | Wyszukiwanie miejsc koncertowych  | 1. Uruchom aplikację. 2. Wprowadź kod kraju: "PL".                                       | Aplikacja wyświetla listę popularnych miejsc koncertowych w Polsce.                        | Sukces     |
| 004                | Kalkulacja cen artystów           | 1. Wybierz kraj: "Germany". 2. Wprowadź liczbę artystów: 5. 3. Podaj budżet: 70 000 zł.   | Aplikacja wyświetla listę artystów wraz z kosztami i ich popularnością.                    | Sukces     |
