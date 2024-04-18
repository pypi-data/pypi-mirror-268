import tkinter as tk
from tkinter import filedialog
import h5py
from PIL import Image, ImageTk
import os
import numpy as np

class DataValidation:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Validation")

        self.image_index = 0
        self.accepted_images = {}

        self.label_var = tk.StringVar()
        self.label_var.set("Label: ")

        self.image_label = tk.Label(root, textvariable=self.label_var)
        self.image_label.pack()

        self.image_canvas = tk.Canvas(root, width=300, height=300)
        self.image_canvas.pack()

        self.info_label = tk.Label(root, text="Image: 0/0 - 0%")
        self.info_label.pack()

        self.accept_button = tk.Button(root, text="Accept", command=self.accept_image)
        self.accept_button.pack(side=tk.LEFT)

        self.reject_button = tk.Button(root, text="Reject", command=self.reject_image)
        self.reject_button.pack(side=tk.RIGHT)

        self.back_button = tk.Button(root, text="Back", command=self.backtrack_image)
        self.back_button.pack()

        self.load_button = tk.Button(root, text="Load H5 File", command=self.load_h5_file)
        self.load_button.pack()

    def load_h5_file(self):
        file_path = filedialog.askopenfilename(title="Select H5 file", filetypes=(("H5 files", "*.h5"),))
        if file_path:
            self.h5_file = h5py.File(file_path, "r")
            self.images = self.h5_file["images"]
            self.labels = self.h5_file["labels"]
            self.reset_state()
            self.display_image()

    def display_image(self):
        total_images = len(self.images)
        if self.image_index < total_images:
            img_data = self.images[self.image_index]
            label = self.labels[self.image_index]
            image = Image.fromarray(img_data)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.image_canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.image_canvas.image = photo
            self.label_var.set("Label: " + str(label))
            self.info_label.config(text=f"Image: {self.image_index + 1}/{total_images} - {((self.image_index + 1) / total_images) * 100:.2f}% completed")
        else:
            self.save_accepted_images()
            self.reset_state()

    def accept_image(self):
        self.accepted_images[self.image_index] = (self.images[self.image_index], self.labels[self.image_index])
        self.next_image()

    def reject_image(self):
        self.next_image()

    def backtrack_image(self):
        if self.image_index > 0:
            del self.accepted_images[self.image_index - 1]
            self.image_index -= 1
            self.image_canvas.delete("all")
            self.display_image()

    def next_image(self):
        self.image_index += 1
        self.image_canvas.delete("all")
        self.display_image()

    def reset_state(self):
        self.image_index = 0
        self.accepted_images = {}

    def save_accepted_images(self):
        save_path = filedialog.asksaveasfilename(title="Save H5 File", filetypes=(("H5 files", "*.h5"),))
        if save_path:
            directory, file_name = os.path.split(save_path)
            new_file_name = "NEW_" + file_name  # Append "NEW_" to the beginning of the file name
            new_save_path = os.path.join(directory, new_file_name)
            with h5py.File(new_save_path, "w") as hf:
                images_data = np.array([img for img, _ in self.accepted_images.values()])
                labels_data = np.array([label for _, label in self.accepted_images.values()])

                hf.create_dataset("images", data=images_data)
                hf.create_dataset("labels", data=labels_data)

root = tk.Tk()
app = DataValidation(root)
root.mainloop()
