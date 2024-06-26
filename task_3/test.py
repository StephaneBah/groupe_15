import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import threading
from diffusers import DiffusionPipeline
import torch
import time

class ImageGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Generator")

        self.prompt_label = tk.Label(master, text="Description:")
        self.prompt_label.pack()

        self.prompt_entry = tk.Entry(master, width=50)
        self.prompt_entry.pack()

        self.generate_button = tk.Button(master, text="Generate Image", command=self.generate_image)
        self.generate_button.pack()

        self.spinner = ttk.Progressbar(master, mode='indeterminate')
        
        self.image_label = tk.Label(master)
        self.image_label.pack()

        self.legend_label = tk.Label(master, text="")
        self.legend_label.pack()

        # Load the pipeline
        self.pipeline = self.load_pipeline()

    def load_pipeline(self):
        try:
            pipeline = DiffusionPipeline.from_pretrained("segmind/tiny-sd", torch_dtype=torch.float16)
            pipeline.to("cpu")  # Use CPU
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model: {str(e)}")
            pipeline = None
        return pipeline

    def generate_image(self):
        prompt = self.prompt_entry.get()
        if not prompt:
            messagebox.showwarning("Input Error", "Please enter a description.")
            return
        
        self.spinner.pack()
        self.spinner.start()

        threading.Thread(target=self.generate_image_thread, args=(prompt,)).start()

    def generate_image_thread(self, prompt):
        start_time = time.time()
        try:
            image = self.pipeline(prompt).images[0]
            image.save("generated_image.png")
            
            img = Image.open("generated_image.png")
            img = img.resize((256, 256), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            
            self.image_label.configure(image=img)
            self.image_label.image = img
            self.legend_label.config(text=f"{prompt}\n(Generated in {time.time() - start_time:.2f} seconds)")
        except Exception as e:
            messagebox.showerror("Generation Error", f"Failed to generate image: {str(e)}")
        finally:
            self.spinner.stop()
            self.spinner.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    gui = ImageGeneratorGUI(root)
    root.mainloop()
