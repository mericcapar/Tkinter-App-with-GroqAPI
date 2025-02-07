from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# API key'i kontrol et
if not api_key:
    raise ValueError("API key not found! Please check your .env file.")

client = Groq(api_key=api_key)

# Kullanici adini al
person_name = input("Kimin hakkinda bilgi almak istiyorsunuz? ")

# API cagrisi yap
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "Sen sadece sorulan kisiler hakkinda yas, cinsiyet, nerede oturdugu gibi temel bilgiler ve guncel isleri veya ugrasilari hakkinda bilgi veren bir asistansin eger ki o kisi hakkinda bilgi vermekte zorlaniyorsan bu kisi hakkinda bilgi bulunamadi de ve her zaman Turkce cevap vereceksin."},
        {"role": "user", "content": f"{person_name} kimdir?"}
    ],
    model="llama-3.3-70b-versatile",
)

# cevabi kaydet
response = chat_completion.choices[0].message.content

# txt'ye yazdir
with open("kisi_bilgi.txt", "w", encoding="utf-8") as file:
    file.write(f"{person_name} hakkinda bilgi:\n\n{response}")

print(f"{person_name} hakkindaki bilgiler 'kisi_bilgi.txt' dosyasina kaydedildi")
