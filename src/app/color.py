from matplotlib.colors import LinearSegmentedColormap

def create_color(r, g, b):
    
    return [r/256, g/256, b/256]

 
def get_custom_color_palette_hash():

    return LinearSegmentedColormap.from_list("", [
        
        '#c7dfdf','#a3c3cb','#86a5b8',
        '#687c9c',
        '#494c6e', '#373451', '#29243b'
    ])



