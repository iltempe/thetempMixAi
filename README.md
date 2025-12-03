# thetempMixAi

## Descrizione
ThetempMixAi è un progetto Python che utilizza modelli generativi AI di Google per analisi e test. Il repository contiene script per l'analisi automatizzata e test dei modelli AI.

## Struttura del progetto
- `analize.py`: Script principale per l'analisi tramite modelli generativi AI di Google.
- `test_models.py`: Script per il testing dei modelli AI.
- `requirements.txt`: Elenco delle dipendenze Python necessarie.

## Requisiti
- Python 3.8+
- Connessione Internet
- File `.env` locale con le chiavi API necessarie

## Come creare il file .env
Crea un file chiamato `.env` nella root del progetto e aggiungi le tue chiavi API Google:
```
GOOGLE_API_KEY=la_tua_chiave_api
ALTRE_VARIABILI=valore
```
Assicurati di non committare il file `.env` su GitHub.

## Installazione
1. Clona il repository:
   ```bash
   git clone https://github.com/<tuo-username>/LogicMixAI.git
   cd LogicMixAI
   ```
2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

## Utilizzo
### Analisi con modelli generativi AI
Esegui lo script principale:
```bash
python analize.py
```

### Test dei modelli
Esegui i test:
```bash
python test_models.py
```

## Dipendenze principali
- `google-generativeai`: SDK per l'accesso ai modelli AI di Google

## Contributi
Sono benvenuti contributi tramite pull request. Apri una issue per suggerimenti o bug.

## Licenza
Questo progetto è distribuito sotto licenza MIT.

---

# English Instructions

## Description
ThetempMixAi is a Python project that uses Google's generative AI models for analysis and testing. The repository contains scripts for automated analysis and model testing.

## Project Structure
- `analize.py`: Main script for analysis using Google's generative AI models.
- `test_models.py`: Script for testing AI models.
- `requirements.txt`: List of required Python dependencies.

## Requirements (English)
- Python 3.8+
- Internet connection
- Local `.env` file with required API keys

## How to create the .env file
Create a file named `.env` in the project root and add your Google API keys:
```
GOOGLE_API_KEY=your_api_key
OTHER_VARIABLES=value
```
Make sure not to commit the `.env` file to GitHub.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/iltempe/LogicMixAI.git
   cd LogicMixAI
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Analysis with generative AI models
Run the main script:
```bash
python analize.py
```

### Model testing
Run the tests:
```bash
python test_models.py
```

## Main dependencies
- `google-generativeai`: SDK to access Google's AI models

## Contributions
Contributions are welcome via pull request. Open an issue for suggestions or bugs.

## License
This project is distributed under the MIT license.
