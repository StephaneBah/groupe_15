from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, font as tkFont
import tkinter.messagebox as messagebox
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from diffusers import DiffusionPipeline
import os
import json
import threading

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/HP\Downloads/Telegram Desktop/groupe_15-1/groupe_15/task_3/assets/frame0")
PIPELINE_PATH = OUTPUT_PATH / "saved_pipeline"
CONFIG_FILE = OUTPUT_PATH / "model_config.json"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

current_model_name = "hf-internal-testing/tiny-stable-diffusion-torch"

def save_model_config(model_name):
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"model_name": model_name}, f)

def load_model_config():
    if CONFIG_FILE.exists() and CONFIG_FILE.stat().st_size > 0:  # Vérifier si le fichier existe et n'est pas vide
        with open(CONFIG_FILE, 'r') as f:
            try:
                return json.load(f).get("model_name", "")
            except json.JSONDecodeError:
                return ""  # Si le fichier est corrompu, retournez une chaîne vide
    return ""

# Charger la configuration du modèle précédent
previous_model_name = load_model_config()

# Vérifier si le modèle a changé
if previous_model_name != current_model_name or not PIPELINE_PATH.exists():
    # Télécharger le pipeline et le sauvegarder localement
    pipe = DiffusionPipeline.from_pretrained(current_model_name)
    pipe.save_pretrained(PIPELINE_PATH)
    save_model_config(current_model_name)
else:
    # Charger le pipeline sauvegardé localement
    pipe = DiffusionPipeline.from_pretrained(PIPELINE_PATH)

window = tk.Tk()

window.title("SIA")
window.geometry("700x500")
window.configure(bg = "#828282")


canvas = Canvas(window, bg = "#828282", height = 500, width = 700, bd = 0, highlightthickness = 0, relief = "ridge")

entry_font = tkFont.Font(family="Helvetica", size=12)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(350.0, 32.0, image=image_image_1)

canvas.create_text(65.0, 13.0, anchor="nw", text="Image Generator", fill="#828282", font=("Karma Bold", 24 * -1))

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(32.0, 28.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(667.0, 30.0, image=image_image_3)

def generate_image(prompt, width=319, height=329):
    image = pipe(prompt).images[0]
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

spinner_running = False

def animate_spinner(frame=0):
    if not spinner_running:
        return
    frame = (frame + 1) % len(spinner_frames)
    spinner_label.config(image=spinner_frames[frame])
    spinner_label.image = spinner_frames[frame]  
    window.after(100, animate_spinner, frame)

def on_click_button():
    prompt = entry_1.get()
    if prompt == "":
        messagebox.showerror("Error", "Input is empty")
        return
    button_1.pack_forget()
    spinner_label.place(x=454.0, y=92.0, width=86.0, height=35.0)
    window.after(100, animate_spinner)
    threading.Thread(target=generate_and_display_images).start()

def generate_and_display_images():
    prompt = entry_1.get()
    image1 = generate_image(prompt, 319, 329)
    image2 = generate_image(prompt, 319, 329)

    canvas.image1 = image1
    canvas.create_image((19.0 + 338.0) / 2, (142.0 + 471.0) / 2, image=image1)
    
    canvas.image2 = image2
    canvas.create_image((359.0 + 678.0) / 2, (142.0 + 471.0) / 2, image=image2)

    # Revenir au thread principal pour mettre à jour l'interface utilisateur
    window.after(0, on_image_generated)

def on_image_generated():
    global spinner_running
    spinner_running = False  # Arrêter le spinner
    spinner_label.place_forget()  # Masquer le label du spinner
    button_1.place(x=454.0, y=92.0, width=86.0, height=35.0)


button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=on_click_button, relief="flat")
button_1.place(x=454.0, y=92.0, width=86.0, height=35.0)

# Charger le GIF du spinner
spinner_gif_path = ASSETS_PATH / "spinner.gif"
spinner_gif = Image.open(spinner_gif_path)
spinner_frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(spinner_gif)]
# Créer un label pour afficher le spinner
spinner_label = tk.Label(window)

def entry_focus_in(event):
    if entry_1.get() == "Ecrivez votre prompt":
        entry_1.delete(0, 'end')
        entry_1.config(fg="Black")
def entry_focus_out(event):
    if entry_1.get() == "":
        entry_1.insert(0, "Ecrivez votre prompt")
        entry_1.config(fg="Black")

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(219.0, 107.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font=entry_font)
entry_1.place(x=27.0, y=83.0, width=384.0, height=47.0)
entry_1.insert(0, "Ecrivez votre prompt",)
entry_1.bind("<Enter>", entry_focus_in)
entry_1.bind("<Leave>", entry_focus_out)

canvas.create_text(200.0, 471.0, anchor="nw", text="SIA, the best image generator", fill="#000000", font=("Karma Regular", 20 * -1))

canvas.create_rectangle(19.0, 142.0, 338.0, 471.0, fill="#E0E0E0", outline="")
canvas.create_rectangle(359.0, 142.0, 678.0, 471.0, fill="#E0E0E0", outline="")

window.resizable(False, False)
window.mainloop()
