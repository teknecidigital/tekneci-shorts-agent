import os
import requests
import json

def generate_script():
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("HATA: GEMINI_API_KEY bulunamadı!")
        return

    # Doğrudan Google Gemini REST API adresi (Model takıntısı yok, en güncel flash sürümü)
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
    
    print("Gemini API'ye doğrudan istek gönderiliyor...")
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
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
            print("API Yanıtı:", response.text)
    else:
        print(f"API Hatası (Kod {response.status_code}):", response.text)
        raise Exception("API bağlantısı başarısız oldu.")

if __name__ == "__main__":
    generate_script()
