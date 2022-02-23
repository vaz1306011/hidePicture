from PIL import Image
import tkinter
from tkinter import filedialog


def hidePicture(big_img: Image, small_img: Image) -> Image:
    big_w, big_h = big_img.size
    small_w, small_h = small_img.size

    dst_img = big_img.copy()

    stepx = big_w/small_w
    stepy = big_h/small_h

    for i in range(0, small_w):
        for j in range(0, small_h):
            map_x = int(i*stepx+stepx*0.5)
            map_y = int(j*stepy+stepy*0.5)
            if map_x < big_w and map_y < big_h:
                dst_img.putpixel((map_x, map_y), small_img.getpixel((i, j)))

    return dst_img


if __name__ == '__main__':
    tkinter.Tk().withdraw()
    big_img_path = filedialog.askopenfilename(
        initialdir='.', filetypes=[('png', 'png')])
    if not big_img_path:
        exit(1)
    small_img_path = filedialog.askopenfilename(filetypes=[('png', 'png')])
    if not small_img_path:
        exit(1)

    big_img = Image.open(big_img_path)
    small_img = Image.open(small_img_path)
    dst_img = hidePicture(big_img, small_img)

    dst_img_path = filedialog.asksaveasfilename(filetypes=[('png', 'png')])
    dst_img_path = dst_img_path + \
        '.png' if not dst_img_path.endswith('.png') else dst_img_path
    dst_img.save(dst_img_path)
