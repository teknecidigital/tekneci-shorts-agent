import os
import requests
import json

def generate_script():
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("HATA: GEMINI_API_KEY bulunamadı!")
        raise Exception("API anahtarı eksik.")

    # Doğrudan Google Gemini REST API uç noktası (Kütüphane ve model hatası ihtimali sıfır)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    payload = {
        "contents": [{
            "parts": [{
                "text": "YouTube Shorts için 50 saniyelik, sürükleyici ve gizem dolu bir mini dizi senaryosu yaz. Kesinlikle başlığı, görsel tasvirleri ve seslendirme metnini belirt."
            }]
        }]
    }
    
    print("Google Gemini API'ye doğrudan istek gönderiliyor...")
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    print(f"API Yanıt Kodu: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        try:
            script_text = result['candidates'][0]['content']['parts'][0]['text']
            print("--- ÜRETİLEN SENARYO ---")
            print(script_text)
            
            os.makedirs("output", exist_ok=True)
            with open("output/script.txt", "w", encoding="utf-8") as f:
                f.write(script_text)
            print("Senaryo output/script.txt dosyasına başarıyla kaydedildi!")
        except Exception as e:
            print(f"Yanıt işlenirken hata oluştu: {e}")
            print("Gelen ham yanıt:", response.text)
            raise e
    else:
        print(f"API Hatası Detayı: {response.text}")
        raise Exception(f"API bağlantısı başarısız oldu (Kod: {response.status_code})")

if __name__ == "__main__":
    generate_script()
