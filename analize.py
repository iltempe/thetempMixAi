import sys
import time
import os
import glob
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv
import socket

# --- CONFIGURAZIONE ---
if socket.gethostname() == "MacBook-Pro-di-Matteo-2":
    load_dotenv(".env")
else:
    load_dotenv("config.env")
API_KEY = os.getenv("GEMINI_API_KEY")
BOUNCE_DIR = os.getenv("BOUNCE_DIR")
MODEL_TYPE = os.getenv("MIXAI_MODEL", "gemini")  # gemini (default), ollama, openai, huggingface
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
HUGGINGFACE_API_URL = os.getenv("HUGGINGFACE_API_URL")
HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "facebook/musicgen-small")

if not API_KEY:
    print("❌ ERRORE: Manca la API KEY nel file .env")
    sys.exit(1)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

PROMPT = """
Sei un Senior Mixing Engineer.
Analizza questo mix basandoti su:
1. AUDIO: Ascolta bilanciamento, dinamica, transienti.
2. VISUAL (Screenshot): Guarda il mixer/arrangiamento per trovare conferme visive (es. fader, EQ).

OUTPUT RICHIESTO:
- Sezione iniziale: indica KEY (tonalità), BPM e GENERE musicale del brano in modo sintetico.
- Analisi Critica (Cosa senti vs Cosa vedi). Focus sul mixing della voce
- Azioni correttive immediate e numerate.
- Tono: Professionale, sintetico, italiano. Niente preamboli.
"""

def get_latest_bounce():
    """Trova l'ultimo file MP3 o WAV creato nella cartella dei bounce."""
    if not BOUNCE_DIR or not os.path.exists(BOUNCE_DIR):
        print(f"❌ Errore percorso: {BOUNCE_DIR} non esiste o non è configurato.")
        return None
    
    # Cerca mp3 e wav
    list_of_files = glob.glob(os.path.join(BOUNCE_DIR, '*.mp3')) + \
                    glob.glob(os.path.join(BOUNCE_DIR, '*.wav'))
    
    if not list_of_files:
        return None
    
    # Restituisce il file con data di creazione più recente
    return max(list_of_files, key=os.path.getctime)

def analyze_with_gemini(audio_file, image_file):
    prompt_inputs = [PROMPT, audio_file]
    if image_file:
        prompt_inputs.append(image_file)
    response = model.generate_content(prompt_inputs)
    return response.text

def analyze_with_ollama(audio_path, screenshot_path):
    import requests
    files = {'audio': open(audio_path, 'rb')}
    if screenshot_path and os.path.exists(screenshot_path):
        files['image'] = open(screenshot_path, 'rb')
    data = {'prompt': PROMPT, 'model': OLLAMA_MODEL}
    response = requests.post(f"{OLLAMA_URL}/api/generate", data=data, files=files)
    return response.text if response.ok else f"Errore Ollama: {response.text}"

def analyze_with_openai(audio_path, screenshot_path):
    import openai
    openai.api_key = OPENAI_API_KEY
    # Qui puoi personalizzare la chiamata a OpenAI (es. invio prompt, file, ecc.)
    # Esempio base:
    response = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[{"role": "system", "content": PROMPT}],
    )
    return response.choices[0].message['content']

def analyze_with_huggingface(audio_path, screenshot_path):
    import requests
    files = {'audio': open(audio_path, 'rb')}
    if screenshot_path and os.path.exists(screenshot_path):
        files['image'] = open(screenshot_path, 'rb')
    data = {'inputs': PROMPT, 'model': HUGGINGFACE_MODEL}
    response = requests.post(HUGGINGFACE_API_URL, data=data, files=files)
    return response.text if response.ok else f"Errore HuggingFace: {response.text}"

def main():
    # 1. Trova il file audio (Manuale o Automatico)
    take_screenshot = True
    audio_path = None
    # Controllo parametri
    for arg in sys.argv[1:]:
        if arg.lower() in ["--no-screenshot", "-ns"]:
            take_screenshot = False
        elif not audio_path:
            audio_path = arg.strip().replace('"', '').replace("'", "")
    if not audio_path:
        print("🔎 Cerco l'ultimo bounce fatto...")
        audio_path = get_latest_bounce()
    
    if not audio_path:
        print("❌ Nessun file audio trovato nella cartella Bounces.")
        return

    print(f"🎧 Analizzo: {os.path.basename(audio_path)}")
    
    # 2. Screenshot opzionale tramite parametro
    screenshot_path = os.path.join(os.path.dirname(audio_path), "temp_screen.png")
    image_file = None
    if take_screenshot:
        try:
            subprocess.run(["screencapture", "-x", "-m", "-t", "png", screenshot_path], check=True)
            print("📸 Screenshot preso.")
            image_file = genai.upload_file(path=screenshot_path)
        except Exception as e:
            print(f"❌ Errore screenshot: {e}")
            screenshot_path = None
    else:
        print("⏭️ Screenshot saltato.")

    # 3. Analisi AI
    print(f"🚀 Invio a {MODEL_TYPE.capitalize()}...")
    if MODEL_TYPE == "gemini":
        audio_file = genai.upload_file(path=audio_path)
        while audio_file.state.name == "PROCESSING":
            time.sleep(1)
            audio_file = genai.get_file(audio_file.name)
        if audio_file.state.name == "FAILED":
            raise ValueError("Errore Google Audio.")
        result_text = analyze_with_gemini(audio_file, image_file)
    elif MODEL_TYPE == "ollama":
        result_text = analyze_with_ollama(audio_path, screenshot_path if take_screenshot else None)
    elif MODEL_TYPE == "openai":
        result_text = analyze_with_openai(audio_path, screenshot_path if take_screenshot else None)
    elif MODEL_TYPE == "huggingface":
        result_text = analyze_with_huggingface(audio_path, screenshot_path if take_screenshot else None)
    else:
        print(f"❌ Modello non supportato: {MODEL_TYPE}")
        return

    # 4. Salvataggio
    report_path = audio_path + "_ANALISI.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(result_text)
    
    # 5. AUTO-APERTURA REPORT (La magia)
    print("✅ Fatto! Apro il report...")
    subprocess.run(["open", report_path])
    
    subprocess.run(["say", "Analisi del mix pronta"])
    
    # Pulizia
    if screenshot_path and os.path.exists(screenshot_path):
        os.remove(screenshot_path)
    if audio_file:
        audio_file.delete()
    if image_file:
        image_file.delete()

if __name__ == "__main__":
    main()