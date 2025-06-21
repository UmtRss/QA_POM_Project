# 🧪 POM Login Automation Framework

This is a login test framework using Selenium and PyTest with the Page Object Model (POM) structure.

## 🔧 Technologies Used
- Python
- Selenium
- PyTest
- POM Design Pattern

## 📁 Folder Structure

- `pages/` → Contains reusable page classes (BasePage, LoginPage)
- `tests/` → Contains test files (valid and invalid login tests)
- `conftest.py` → Optional: Contains fixtures for driver setup
- `requirements.txt` → Required packages
- `pytest.ini` → Optional config for pytest settings

## ▶️ How to Run

```bash
pip install -r requirements.txt
pytest tests/
