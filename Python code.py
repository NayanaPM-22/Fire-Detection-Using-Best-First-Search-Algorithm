#!/usr/bin/env python3
import cv2
import numpy as np
import heapq
import threading
import winsound
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence

# --- FIRE DETECTION LOGIC ---

def best_first_search(gray_image, brightness_threshold=200):
    rows, cols = gray_image.shape
    visited = np.zeros((rows, cols), dtype=bool)
    fire_regions = []
    pq = []

    gray_image = gray_image.astype(np.int32)
    start = np.unravel_index(np.argmax(gray_image, axis=None), gray_image.shape)
    heapq.heappush(pq, (-int(gray_image[start]), start))
    visited[start] = True

    while pq:
        neg, (i, j) = heapq.heappop(pq)
        val = -neg
        if val < brightness_threshold:
            continue
        fire_regions.append((i, j))
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < rows and 0 <= nj < cols and not visited[ni,nj]:
                visited[ni,nj] = True
                if gray_image[ni, nj] >= brightness_threshold:
                    heapq.heappush(pq, (-int(gray_image[ni, nj]), (ni, nj)))
    return fire_regions

def detect_fire(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(5,5),0)
    regions = best_first_search(blurred)
    fire = len(regions)>0
    if fire:
        for x,y in regions:
            cv2.circle(frame,(y,x),1,(0,0,255),-1)
        cv2.putText(frame,"Fire Detected!",(20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    return fire, frame

def alarm():
    winsound.Beep(4000,500)

# --- GUI ---

def process_image(path):
    global orig_img, proc_img
    if path.lower().endswith(".gif"):
        process_gif(path)
        return

    img = cv2.imread(path)
    if img is None:
        status_label.config(text="Error loading image")
        return
    fire, out = detect_fire(img.copy())
    if fire:
        threading.Thread(target=alarm,daemon=True).start()

    orig_img, proc_img = img, out
    show_images()

def process_gif(path):
    global orig_img, proc_img
    gif = Image.open(path)
    frames, procs = [], []
    for f in ImageSequence.Iterator(gif):
        f = f.convert("RGB")
        arr = cv2.cvtColor(np.array(f),cv2.COLOR_RGB2BGR)
        fire, out = detect_fire(arr.copy())
        frames.append(Image.fromarray(cv2.cvtColor(arr,cv2.COLOR_BGR2RGB)))
        procs.append(Image.fromarray(cv2.cvtColor(out,cv2.COLOR_BGR2RGB)))
        if fire: threading.Thread(target=alarm,daemon=True).start()

    orig_img, proc_img = frames[0], procs[0]
    show_images()

def show_images():
    orig = (orig_img if isinstance(orig_img, Image.Image)
            else Image.fromarray(cv2.cvtColor(orig_img,cv2.COLOR_BGR2RGB)))
    proc = (proc_img if isinstance(proc_img, Image.Image)
            else Image.fromarray(cv2.cvtColor(proc_img,cv2.COLOR_BGR2RGB)))

    for im in (orig, proc):
        im.thumbnail((300,300))

    o_tk = ImageTk.PhotoImage(orig)
    p_tk = ImageTk.PhotoImage(proc)
    original_label.config(image=o_tk); original_label.image=o_tk
    processed_label.config(image=p_tk); processed_label.image=p_tk
    status_label.config(text="Processing complete")
    done_btn.pack()

def reset():
    original_label.config(image='')
    processed_label.config(image='')
    status_label.config(text="Select an image or GIF.")
    done_btn.pack_forget()

def browse():
    f = filedialog.askopenfilename(
        filetypes=[("Images","*.png;*.jpg;*.jpeg;*.gif")])
    if f:
        status_label.config(text="Running detector...")
        process_image(f)

# --- MAIN WINDOW ---

if __name__=="__main__":
    import PIL.Image as Image  # for isinstance check

    root = tk.Tk()
    root.title("Fire Detector")
    root.geometry("700x600")

    tk.Button(root,text="Select Image/GIF",command=browse,
              font=("Arial",14)).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack()
    original_label = tk.Label(frame)
    original_label.pack(side=tk.LEFT,padx=10)
    processed_label = tk.Label(frame)
    processed_label.pack(side=tk.RIGHT,padx=10)

    status_label = tk.Label(root,text="Select an image or GIF.",
                            font=("Arial",12))
    status_label.pack(pady=10)

    done_btn = tk.Button(root,text="Done",command=reset,
                         font=("Arial",14))
    done_btn.pack_forget()

    root.mainloop()
