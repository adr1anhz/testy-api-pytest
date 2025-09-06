# Automatyczne testy API (Pytest)

Projekt zawiera zestaw automatycznych testów dla publicznego API [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## 🔹 Funkcjonalności

- Testy endpointów `users` i `posts`
- Weryfikacja poprawnych i błędnych odpowiedzi
- Testy wykorzystują `pytest fixtures` oraz dane z pliku JSON
- Możliwość generowania raportów HTML

## ▶️ Uruchamianie testów

1. Utwórz środowisko wirtualne:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows