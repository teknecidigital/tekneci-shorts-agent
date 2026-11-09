import os
import requests
import json

def generate_script():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("API anahtarı bulunamadı!")
        return

    # Doğrudan Google Gemini REST API uç noktası
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": "YouTube Shorts için 50 saniyelik, sürükleyici ve gizem dolu bir mini dizi senaryosu yaz. Başlığı, görsel tasvirleri ve seslendirme metnini belirt."}]
        }]
    }
    
    print("Senaryo üretiliyor...")
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        result = response.json()
        script_text = result['candidates'][0]['content']['parts'][0]['text']
        print("--- ÜRETİLEN SENARYO ---")
        print(script_text)
        
        os.makedirs("output", exist_ok=True)
        with open("output/script.txt", "w", encoding="utf-8") as f:
            f.write(script_text)
        print("Senaryo başarıyla kaydedildi!")
    else:
        print("Hata Detayı:", response.text)
        raise Exception("API bağlantısı başarısız.")

if __name__ == "__main__":
    generate_script()
