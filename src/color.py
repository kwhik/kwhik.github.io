import colorsys

def hex_to_hsl(hex_str):
    # Clean the string and remove the '#' if present
    hex_str = hex_str.lstrip('#')

    # Handle shorthand hex codes (e.g., "fff" -> "ffffff")
    if len(hex_str) == 3:
        hex_str = ''.join([char*2 for char in hex_str])

    # Convert HEX to RGB integers (0-255)
    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)

    # Normalize RGB values to the 0.0 - 1.0 range for colorsys
    r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0

    # colorsys uses HLS (Hue, Lightness, Saturation) order
    h, l, s = colorsys.rgb_to_hls(r_norm, g_norm, b_norm)

    # Scale to conventional HSL bounds: H: 0-360, S: 0-100%, L: 0-100%
    h = round(h * 360)
    s = round(s * 100)
    l = round(l * 100)

    return h, s, l

# Example Usage:

h, s, l = hex_to_hsl("#ffff00"); print(h,s,l)
h, s, l = hex_to_hsl("#D1E231"); print(h,s,l)
h, s, l = hex_to_hsl("#CCCCFF"); print(h,s,l)
h, s, l = hex_to_hsl("#00A693"); print(h,s,l)
h, s, l = hex_to_hsl("#EC5800"); print(h,s,l)
h, s, l = hex_to_hsl("#DF00FF"); print(h,s,l)
h, s, l = hex_to_hsl("#93C572"); print(h,s,l)
h, s, l = hex_to_hsl("#BE4F62"); print(h,s,l)
h, s, l = hex_to_hsl("#E1CA7A"); print(h,s,l)
h, s, l = hex_to_hsl("#701C1C"); print(h,s,l)
h, s, l = hex_to_hsl("#FF7518"); print(h,s,l)
h, s, l = hex_to_hsl("#9C51B6"); print(h,s,l)
h, s, l = hex_to_hsl("#FBAB60"); print(h,s,l)
h, s, l = hex_to_hsl("#D4F457"); print(h,s,l)