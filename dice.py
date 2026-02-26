import tkinter as tk
import random
import time

# Τα προσωπα του ζαριου
faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

def roll_it():
    # Κλειδωνω το κουμπι για να μην το πατανε απανωτα
    btn.config(state="disabled")
    
    # Κανουμε το εφε οτι γυρναει (το κανω να αλλαξει 10 φορες)
    for i in range(10):
        tyxaio = random.choice(faces)
        zari_lbl.config(text=tyxaio, fg="white")
        
        # Χωρις το update() το παραθυρο κολλαει και δεν δειχνει την αλλαγη
        window.update() 
        time.sleep(0.1) # Περιμενει 0.1 δευτερολεπτα
        
    # Το τελικο αποτελεσμα
    teliko = random.choice(faces)
    zari_lbl.config(text=teliko, fg="#4CAF50") # Το κανω πρασινο στο τελος
    
    
    # Ξεμπλοκαρω το κουμπι
    btn.config(state="normal") 

# Φτιαχνω το παραθυρο
window = tk.Tk()
window.title("Zari App")
window.geometry("300x350")
window.configure(bg="#2b2b2b")

# Τιτλος
tk.Label(window, text="Ρίξε το ζάρι!", font=("Arial", 18, "bold"), bg="#2b2b2b", fg="white").pack(pady=20)

# Εδω θα μπαινει το ζαρι
zari_lbl = tk.Label(window, text="🎲", font=("Helvetica", 120), bg="#2b2b2b", fg="white")
zari_lbl.pack(expand=True)

# Το κουμπι
btn = tk.Button(window, text="Ρίψη!", font=("Arial", 14, "bold"), bg="#ff5722", fg="white", command=roll_it)
btn.pack(pady=30)

window.mainloop()