import matplotlib.pyplot as plt
import numpy as np
import wave
import cv2

def color_match(weight):
    return f"\033[38;2;{weight[2]};{weight[1]};{weight[0]}m▒\033[0m"

def under_sampling_color(arr, size=5):
    img_size = arr.shape
    RATIO = img_size[0] / img_size[1]
    REAL_WIDTH = size*10
    REAL_HEIGHT = int(size*10 * RATIO)    

    dst = cv2.resize(arr, dsize=(REAL_WIDTH, REAL_HEIGHT), interpolation=cv2.INTER_AREA)
    return dst, (REAL_WIDTH, REAL_HEIGHT)


def colorshow_arr(arr, size=5):
    d_arr, real = under_sampling_color(arr, size=size)
    for line in d_arr:
        for var in line:
            val = color_match(var)
            print(val, end="")
            print(val, end="")
        print()

def colorshow(path, size=5):
    arr = cv2.imread(path)
    colorshow_arr(arr, size=size)

def audioshow(path, size=4):
    spf = wave.open(path, "r")

    # Extract Raw Audio from Wav File
    signal = spf.readframes(-1)
    # use from buffer
    # signal = np.fromstring(signal, np.int16)
    signal = np.frombuffer(signal, np.int16)

    # If Stereo
    if spf.getnchannels() == 2:
        # Change to mono    
        signal = signal[::2]
        print("WARN: Stereo audio is converted to mono")
    
    fig = plt.figure(1)
    canvas = fig.canvas
    ax = fig.gca()
    ax.axis("off")

    ax.plot(signal, "r")
    canvas.draw()

    # use buffer_rgba
    image_flat = np.frombuffer(canvas.buffer_rgba(), np.uint8)
    image = image_flat.reshape(canvas.get_width_height()[::-1] + (4,))

    colorshow_arr(image, size)


def run_cli():
    import argparse
    import os
    parser = argparse.ArgumentParser(description="Show image in terminal")
    parser.add_argument("path", nargs="*", help="Path to image")
    parser.add_argument("--size", type=int, default=4, help="Size of image")

    args = parser.parse_args()
    path = args.path[0]
    if os.path.basename(path).split(".")[1] == "wav":
        audioshow(path, size=args.size)
    else:
        colorshow(path, size=args.size)


if __name__ == "__main__":
    run_cli()