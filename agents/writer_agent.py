import os
import google.generativeai as genai

def generate_script():
    api_key = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    # Güncel ve desteklenen model tanımı
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "YouTube Shorts için 50 saniyelik, sürükleyici ve gizem dolu bir mini dizi senaryosu yaz. Kesinlikle başlığı, görsel tasvirleri ve seslendirme metnini belirt."
    
    response = model.generate_content(prompt)
    print("--- ÜRETİLEN SENARYO ---")
    print(response.text)
    
    os.makedirs("output", exist_ok=True)
    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    generate_script()
