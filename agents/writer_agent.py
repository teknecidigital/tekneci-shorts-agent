import os
import google.generativeai as genai

def generate_script():
    api_key = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    # Sırayla denenecek model listesi (Hangisi destekleniyorsa anında onu seçer)
    candidate_models = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro', 'chat-bison-001']
    
    model = None
    active_model_name = ""
    
    for model_name in candidate_models:
        try:
            print(f"Denenen model: {model_name}")
            test_model = genai.GenerativeModel(model_name)
            # Küçük bir test çağrısı ile modelin çalışıp çalışmadığını kontrol et
            response = test_model.generate_content("Test")
            model = test_model
            active_model_name = model_name
            print(f"Başarılı! Kullanılan model: {active_model_name}")
            break
        except Exception as e:
            print(f"{model_name} desteklenmiyor veya hata verdi, sıradakine geçiliyor... Hata: {e}")
            continue
            
    if model is None:
        raise Exception("Hiçbir Gemini modeli bu API anahtarı ile eşleşmedi. Lütfen API anahtarınızı kontrol edin.")

    prompt = "YouTube Shorts için 50 saniyelik, sürükleyici ve gizem dolu bir mini dizi senaryosu yaz. +18 olmasın. Kesinlikle başlığı, görsel tasvirleri ve seslendirme metnini belirt."
    
    response = model.generate_content(prompt)
    print("--- ÜRETİLEN SENARYO ---")
    print(response.text)
    
    os.makedirs("output", exist_ok=True)
    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    generate_script()
