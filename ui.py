import tkinter as tk
from PIL import Image, ImageTk
import os

# ================= FUNCTIONS ================= #

def start_camera():
    os.system("python test_camera.py")

def start_hand_tracking():
    os.system("python hand_tracking.py")

def start_mouse():
    os.system("python virtual_mouse.py")

def start_air_canvas():
    os.system("python air_canvas.py")

def exit_app():
    root.destroy()

# ================= WINDOW ================= #

root = tk.Tk()
root.title("Hand Gesture Control System")
root.geometry("900x750")
root.resizable(False, False)

# ================= BACKGROUND IMAGE ================= #

bg_image = Image.open("bg.jpeg")
bg_image = bg_image.resize((900, 750))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ================= TITLE ================= #

title = tk.Label(
    root,
    text="HAND GESTURE CONTROL SYSTEM",
    font=("Arial Black", 26, "bold"),
    fg="#00F5FF",
    bg="#000814"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Control Your Computer Using AI Hand Gestures",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#000814"
)
subtitle.pack()

# ================= MAIN FRAME ================= #

main_frame = tk.Frame(root, bg="#1e293b", bd=0)
main_frame.pack(pady=25)

# ================= LOAD ICON FUNCTION ================= #

def load_icon(path):
    img = Image.open(path)
    img = img.resize((50, 50))
    return ImageTk.PhotoImage(img)

# ================= LOAD ICONS ================= #

camera_icon = load_icon("camera.jpeg")
hand_icon = load_icon("hand.jpeg")
mouse_icon = load_icon("mouse.jpeg")
air_icon = load_icon("air.jpeg")
exit_icon = load_icon("exit.jpeg")

# ================= BUTTON STYLE ================= #

button_font = ("Arial", 15, "bold")
button_width = 320
button_height = 80

# ================= CAMERA BUTTON ================= #

btn_camera = tk.Button(
    main_frame,
    text="  Camera Test",
    image=camera_icon,
    compound="left",
    command=start_camera,
    bg="#3b82f6",
    fg="white",
    activebackground="#2563eb",
    activeforeground="white",
    font=button_font,
    width=button_width,
    height=button_height,
    bd=0,
    cursor="hand2"
)
btn_camera.grid(row=0, column=0, padx=20, pady=15)

# ================= HAND TRACKING BUTTON ================= #

btn_hand = tk.Button(
    main_frame,
    text="  Hand Tracking",
    image=hand_icon,
    compound="left",
    command=start_hand_tracking,
    bg="#8b5cf6",
    fg="white",
    activebackground="#7c3aed",
    activeforeground="white",
    font=button_font,
    width=button_width,
    height=button_height,
    bd=0,
    cursor="hand2"
)
btn_hand.grid(row=0, column=1, padx=20, pady=15)

# ================= MOUSE BUTTON ================= #

btn_mouse = tk.Button(
    main_frame,
    text="  Virtual Mouse",
    image=mouse_icon,
    compound="left",
    command=start_mouse,
    bg="#10b981",
    fg="white",
    activebackground="#059669",
    activeforeground="white",
    font=button_font,
    width=button_width,
    height=button_height,
    bd=0,
    cursor="hand2"
)
btn_mouse.grid(row=1, column=0, padx=20, pady=15)

# ================= AIR CANVAS BUTTON ================= #

btn_air = tk.Button(
    main_frame,
    text="  Air Canvas",
    image=air_icon,
    compound="left",
    command=start_air_canvas,
    bg="#ec4899",
    fg="white",
    activebackground="#db2777",
    activeforeground="white",
    font=button_font,
    width=button_width,
    height=button_height,
    bd=0,
    cursor="hand2"
)
btn_air.grid(row=1, column=1, padx=20, pady=15)

# ================= EXIT BUTTON ================= #

btn_exit = tk.Button(
    main_frame,
    text="  Exit",
    image=exit_icon,
    compound="left",
    command=exit_app,
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    activeforeground="white",
    font=button_font,
    width=button_width,
    height=button_height,
    bd=0,
    cursor="hand2"
)
btn_exit.grid(row=2, column=0, columnspan=2, padx=20, pady=15)

# ================= PROJECT OVERVIEW ================= #

project_title = tk.Label(
    root,
    text="✨ AI BASED HAND GESTURE CONTROL SYSTEM ✨",
    font=("Arial Black", 18, "bold"),
    fg="#00F5FF",
    bg="#000814"
)
project_title.pack(pady=8)

overview = tk.Label(
    root,
    text="This project is based on Artificial Intelligence and Computer Vision techniques that allow users to control computer functions using hand gestures through a webcam.",
    font=("Arial", 12, "bold"),
    fg="#ffffff",
    bg="#000814",
    wraplength=820,
    justify="center"
)
overview.pack(pady=5)

# ================= DEVELOPER INFO ================= #

developer_frame = tk.Frame(
    root,
    bg="#111827",
    highlightbackground="#00F5FF",
    highlightthickness=2
)
developer_frame.pack(pady=15)

developer_label = tk.Label(
    developer_frame,
    text="👩‍💻 Developed By: Sanchi\n🎓 Branch: CS(AIFT)",
    font=("Arial", 13, "bold"),
    fg="#00FFB3",
    bg="#111827",
    padx=20,
    pady=10,
    justify="center"
)
developer_label.pack()

# ================= FOOTER ================= #

footer = tk.Label(
    root,
    text="Developed by Sanchi 🚀",
    font=("Arial", 12, "bold"),
    fg="#cbd5e1",
    bg="#000814"
)
footer.pack(side="bottom", pady=15)

# ================= RUN ================= #

root.mainloop()