import os
import google.generativeai as genai

def generate_script():
    api_key = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    # Desteklenen modelleri otomatik listele ve uygun olanı seç
    model_name = 'gemini-1.5-flash'
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            if '1.5' in m.name:
                model_name = m.name
                break

    print(f"Kullanılan Model: {model_name}")
    model = genai.GenerativeModel(model_name)
    
    prompt = "YouTube Shorts için 50 saniyelik, sürükleyici ve gizem dolu bir mini dizi senaryosu yaz. Kesinlikle başlığı, görsel tasvirleri ve seslendirme metnini belirt."
    
    response = model.generate_content(prompt)
    print("--- ÜRETİLEN SENARYO ---")
    print(response.text)
    
    os.makedirs("output", exist_ok=True)
    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    generate_script()
