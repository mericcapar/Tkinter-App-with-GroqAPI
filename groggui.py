import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from dotenv import load_dotenv
from groq import Groq

# Load .env file (for secure API key storage)
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Check API key
if not api_key:
    messagebox.showerror("Hata", "API key bulunamadi! Lutfen .env dosyanizi kontrol edin.")
    exit()

# Initialize Groq client
client = Groq(api_key=api_key)

# Function to fetch information
def get_info():
    person_name = entry.get().strip()
    
    if not person_name:
        messagebox.showwarning("Uyari", "Lutfen bir isim girin!")
        return
    
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Sen sadece sorulan kisiler hakkinda yas, cinsiyet, nerede oturdugu gibi temel bilgiler ve guncel isleri veya ugrasilari hakkinda bilgi veren bir asistansin ve her zaman Turkce cevap vereceksin."},
            {"role": "user", "content": f"{person_name} kimdir?"}
        ],
        model="llama-3.3-70b-versatile",
        )
        
    response = chat_completion.choices[0].message.content

    text_area.delete("1.0", tk.END)  # Clear previous text
    text_area.insert(tk.END, response)



# tkinter ile gui yapimi
root = tk.Tk()
root.title("Kisi Bilgi Sorgulama")
root.geometry("500x400")

#pencereyi önde tutmak icin
root.attributes('-topmost', True)
#ortalamak icin
root.eval('tk::PlaceWindow . center')


tk.Label(root, text="Kisi adi girin:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Search button
search_button = tk.Button(root, text="Bilgi Al", font=("Arial", 12), command=get_info)
search_button.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
text_area.pack(pady=10)

root.mainloop()
