from pyscreenshot import grab

def scr_shot(name, path):
    photo = grab()
    photo.save(f"{path}\\{name}")