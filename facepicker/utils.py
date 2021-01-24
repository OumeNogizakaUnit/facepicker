import face_recognition
from pathlib import Path
from PIL import Image


def save_face(filepath, savedir, name):
    imagefilename = filepath.stem
    savedirpath = Path(savedir, name)
    if not savedirpath.exists():
        savedirpath.mkdir(parents=True)

    image = face_recognition.load_image_file(filepath)
    locations = face_recognition.face_locations(image)
    for (index, location) in enumerate(locations):
        x1, y1, x2, y2 = location
        x_start = min(x1, x2)
        x_end = max(x1, x2)
        y_start = min(y1, y2)
        y_end = max(y1, y2)
        facearray = image[x_start:x_end, y_start:y_end]
        pil_image = Image.fromarray(facearray)
        pil_image_name = f'{imagefilename}_face{index:0>2}{filepath.suffix}'
        pil_image_path = Path(savedir, name, pil_image_name)
        print(pil_image_path)
        pil_image.save(pil_image_path)
