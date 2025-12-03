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
Crea un file chiamato `.env` nella root del progetto e aggiungi le variabili necessarie:

### Esempio per Gemini (default)
```
GEMINI_API_KEY=la_tua_chiave_api
BOUNCE_DIR=/percorso/alla/cartella/bounce
MIXAI_MODEL=gemini
```

### Esempio per Ollama
```
MIXAI_MODEL=ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama2
BOUNCE_DIR=/percorso/alla/cartella/bounce
```

### Esempio per modello locale con Ollama
```
MIXAI_MODEL=ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=nome_modello_locale
BOUNCE_DIR=/percorso/alla/cartella/bounce
```

### Esempio per OpenAI
```
MIXAI_MODEL=openai
OPENAI_API_KEY=la_tua_chiave_openai
OPENAI_MODEL=gpt-3.5-turbo
BOUNCE_DIR=/percorso/alla/cartella/bounce
```

### Esempio per HuggingFace
```
MIXAI_MODEL=huggingface
HUGGINGFACE_API_URL=https://api-inference.huggingface.co/models/facebook/musicgen-small
HUGGINGFACE_MODEL=facebook/musicgen-small
BOUNCE_DIR=/percorso/alla/cartella/bounce
```

Assicurati che il server Ollama sia avviato in locale e che il modello sia disponibile. Puoi avviare Ollama con:
```bash
ollama serve
```
E caricare un modello locale con:
```bash
ollama pull nome_modello_locale
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

## Output

I report vengono generati in formato HTML nella cartella `output/` con nome basato sul file analizzato, data e ora. Anche gli screenshot (se abilitati) vengono salvati lì.

Per abilitare/disabilitare la cattura screenshot, imposta la variabile `TAKE_SCREENSHOT` nel file `.env`:
```
TAKE_SCREENSHOT=true  # oppure false
```

## Configurazione ambiente

Per motivi di sicurezza, usa **solo il file `.env` locale** per le tue chiavi reali. Non committare mai `.env` su GitHub!

- Copia il file `.env.example` in `.env` e inserisci le tue chiavi e percorsi reali.
- `.env.example` contiene solo valori di esempio/fake.
- Il file `.env` è già ignorato dal `.gitignore`.

Esempio:
```
GEMINI_API_KEY=la_tua_chiave_api
BOUNCE_DIR=/Users/iltempe/Music/Logic/Bounces
MIXAI_MODEL=gemini
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
Create a file named `.env` in the project root and add the required variables:

### Example for Gemini (default)
```
GEMINI_API_KEY=your_api_key
BOUNCE_DIR=/path/to/bounce/folder
MIXAI_MODEL=gemini
```

### Example for Ollama
```
MIXAI_MODEL=ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama2
BOUNCE_DIR=/path/to/bounce/folder
```

### Example for local model with Ollama
```
MIXAI_MODEL=ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=your_local_model_name
BOUNCE_DIR=/path/to/bounce/folder
```

### Example for OpenAI
```
MIXAI_MODEL=openai
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-3.5-turbo
BOUNCE_DIR=/path/to/bounce/folder
```

### Example for HuggingFace
```
MIXAI_MODEL=huggingface
HUGGINGFACE_API_URL=https://api-inference.huggingface.co/models/facebook/musicgen-small
HUGGINGFACE_MODEL=facebook/musicgen-small
BOUNCE_DIR=/path/to/bounce/folder
```

Make sure the Ollama server is running locally and the model is available. You can start Ollama with:
```bash
ollama serve
```
And load a local model with:
```bash
ollama pull your_local_model_name
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

## API keys management
For security reasons, your Gemini key (and other sensitive keys) should never be committed to GitHub.

- Locally, use the `.env` file with your real keys (this file is ignored by Git).
- Remotely or on GitHub, use only `config.env` with example/fake keys.

The script automatically loads `.env` locally and `config.env` remotely, so your key stays private.

## Output

Reports are generated in HTML format in the `output/` folder, named after the analyzed file, date and time. Screenshots (if enabled) are also saved there.

To enable/disable screenshot capture, set the `TAKE_SCREENSHOT` variable in the `.env` file:
```
TAKE_SCREENSHOT=true  # or false
```

## Environment configuration

For security reasons, use **only the local `.env` file** for your real keys. Never commit `.env` to GitHub!

- Copy the `.env.example` file to `.env` and enter your real keys and paths.
- `.env.example` contains only example/fake values.
- The `.env` file is already ignored by `.gitignore`.

Example:
```
GEMINI_API_KEY=your_api_key
BOUNCE_DIR=/Users/iltempe/Music/Logic/Bounces
MIXAI_MODEL=gemini
```

## Main dependencies
- `google-generativeai`: SDK to access Google's AI models

## Contributions
Contributions are welcome via pull request. Open an issue for suggestions or bugs.

## License
This project is distributed under the MIT license.
