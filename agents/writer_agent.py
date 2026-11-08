import os
import google.generativeai as genai

def generate_script():
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # 1. Kontrol: Anahtar var mı?
    if not api_key:
        print("HATA: GEMINI_API_KEY GitHub Secrets'tan okunamadı!")
        raise Exception("API anahtarı bulunamadı.")
    else:
        print(f"API Anahtarı başarıyla okundu (Uzunluk: {len(api_key)})")

    genai.configure(api_key=api_key)
    
    # 2. Hesabının erişebildiği tüm modelleri ekrana yazdır (Teşhis için)
    print("Hesabınızın erişebildiği modeller listeleniyor:")
    supported_model = None
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f" - Desteklenen Model: {m.name}")
                if not supported_model:
                    supported_model = m.name
    except Exception as e:
        print(f"Model listelenirken hata oluştu: {e}")

    if not supported_model:
        # Eğer liste boş dönerse doğrudan standart ismi zorla
        supported_model = 'gemini-1.5-flash'

    print(f"Seçilen aktif model: {supported_model}")
    model = genai.GenerativeModel(supported_model)
    
    prompt = "YouTube Shorts için 50 saniyelik, sürükleyici ve gizem dolu bir mini dizi senaryosu yaz. Kesinlikle başlığı, görsel tasvirleri ve seslendirme metnini belirt."
    
    response = model.generate_content(prompt)
    print("--- ÜRETİLEN SENARYO ---")
    print(response.text)
    
    os.makedirs("output", exist_ok=True)
    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Senaryo output/script.txt dosyasına başarıyla kaydedildi!")

if __name__ == "__main__":
    generate_script()
