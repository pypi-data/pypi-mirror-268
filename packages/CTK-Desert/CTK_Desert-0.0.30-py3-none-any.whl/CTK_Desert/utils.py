def hvr_clr_g(color, mode, gain=20):
    
    hvr_clr = "#"
    if len(color) == 7 and color[0]=="#":
        color = color [1:]

    if mode == "L" or mode == "l" or mode == "Light" or mode == "light":
        for i in range(0, 6, 2): #generate hover color for light mode
            lit_255 = color[i:i+2]    # FF
            if lit_255 == "00":
                hvr_clr += lit_255
                continue
            num_255 = int(lit_255, 16)  # 255
            if num_255-gain < 0 :
                hex_255 = "0x00"
            else:
                hex_255 = hex(num_255-gain)    # 254 -> 0xFE    ,minus 1 to get darker color, then convert it back to hex 
            if len(hex_255[2:]) == 1:
                hex_255 = "0"+hex_255[2:]
                hvr_clr += hex_255
            else:
                hex_255 = hex_255[2:]
                hvr_clr += hex_255
                    
    elif mode == "D" or mode == "d" or mode == "Dark" or mode == "dark":
        for i in range(0, 6, 2): #generate hover color for dark mode
            lit_255 = color[i:i+2]    # 38
            if lit_255 == "FF" or lit_255 == "ff":
                hvr_clr += lit_255
                continue
            num_255 = int(lit_255, 16)  # 56
            if num_255+gain > 255:
                hex_255 = "0xff"
            else:
                hex_255 = hex(num_255+gain)    # 57 -> 0x39    ,plus 1 to get lighter color, then convert it back to hex 
            if len(hex_255[2:]) == 1:
                hex_255 = "0"+hex_255[2:]
                hvr_clr += hex_255
            else:
                hex_255 = hex_255[2:]
                hvr_clr += hex_255    

    return hvr_clr

########################################################################################

import numpy as np
import os
from PIL import Image
from CTK_Desert.Theme import ICONS
def change_pixel_color(icon_path, color):
    """change the color of a filled icon to the target color

    Args:
        icon_path (raw string): the path of the icon
        color (string or tuple): the target color in hex or rgb format
    """
    # Open the image and convert it to RGBA mode
    img = Image.open(icon_path).convert("RGBA")

    # Convert the image to a NumPy array
    img_array = np.array(img)

    #chack if the color is rgb or hex if hex convert it to rgb
    if color[0] == "#":
        color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

    # Apply the target color to non-transparent pixels
    img_array[img_array[..., 3] != 0, :3] = color

    # Create a new image from the modified array
    modified_img = Image.fromarray(img_array, "RGBA")

    # Save the modified image
    folder = os.path.dirname(icon_path)
    file= os.path.basename(icon_path)
    modified_img.save(os.path.join(folder, f"{os.path.splitext(file)[0]}{color}{os.path.splitext(file)[1]}"))
