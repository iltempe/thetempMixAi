import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("🔍 CHIEDO A GOOGLE LA LISTA DEI MODELLI...")
try:
    for m in genai.list_models():
        # Filtriamo solo quelli che generano contenuti (chat)
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ NOME VALIDO: {m.name}")
except Exception as e:
    print(f"❌ Errore: {e}")