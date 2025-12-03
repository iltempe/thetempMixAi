import sys
import time
import os
import glob
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# --- CONFIGURAZIONE ---
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
BOUNCE_DIR = os.getenv("BOUNCE_DIR")

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

def main():
    # 1. Trova il file audio (Manuale o Automatico)
    if len(sys.argv) > 1:
        audio_path = sys.argv[1].strip().replace('"', '').replace("'", "")
    else:
        print("🔎 Cerco l'ultimo bounce fatto...")
        audio_path = get_latest_bounce()
    
    if not audio_path:
        print("❌ Nessun file audio trovato nella cartella Bounces.")
        return

    print(f"🎧 Analizzo: {os.path.basename(audio_path)}")
    
    # 2. Screenshot "Brute Force" (Tutto lo schermo)
    # Non serve countdown perché useremo la scorciatoia da tastiera mentre Logic è aperto
    screenshot_path = os.path.join(os.path.dirname(audio_path), "temp_screen.png")
    
    try:
        # Scatta subito (presuppone che Logic sia visibile)
        # -x (muto), -m (main monitor), -t png
        subprocess.run(["screencapture", "-x", "-m", "-t", "png", screenshot_path], check=True)
        print("📸 Screenshot preso.")

        # 3. Analisi AI
        print("🚀 Invio a Gemini...")
        audio_file = genai.upload_file(path=audio_path)
        image_file = genai.upload_file(path=screenshot_path)

        while audio_file.state.name == "PROCESSING":
            time.sleep(1)
            audio_file = genai.get_file(audio_file.name)
            
        if audio_file.state.name == "FAILED":
            raise ValueError("Errore Google Audio.")

        response = model.generate_content([PROMPT, audio_file, image_file])

        # 4. Salvataggio
        report_path = audio_path + "_ANALISI.txt"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        # 5. AUTO-APERTURA REPORT (La magia)
        print("✅ Fatto! Apro il report...")
        subprocess.run(["open", report_path])

        # Voce (Mac OS default voice)
        # Se hai voci italiane installate userà quelle, altrimenti una generica
        subprocess.run(["say", "Analisi del mix pronta"])
        
        # Pulizia
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
        audio_file.delete()
        image_file.delete()

    except Exception as e:
        print(f"❌ Errore: {e}")

if __name__ == "__main__":
    main()