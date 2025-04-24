import numpy as np
import os
import face_recognition
from fastapi import UploadFile
from pathlib import Path
from uuid import uuid4
from shutil import copyfileobj

UPLOAD_DIR = Path("uploads")

KNOWN_DIR = Path("known_faces")

for directory in [UPLOAD_DIR, KNOWN_DIR]:
    directory.mkdir(exist_ok=True)


def save_and_process_image(name: str, image: UploadFile):
    temp_path = UPLOAD_DIR/f'{uuid4()}.jpg'
    with open(temp_path, "wb") as buffer:
        copyfileobj(image.file, buffer)

    loaded_image = face_recognition.load_image_file(temp_path)
    encodings = face_recognition.face_encodings(loaded_image)
    if not encodings:
        return {"error": "No face found in the image"}
    
    encoding = encodings[0]

    file_path = KNOWN_DIR/f"{name}.npy"
    with open(file_path, "wb") as f:
        import numpy as np
        np.save(f,encoding)
    return {"status":"success","name":name}





# KNOWN_DIR = Path("known_faces")

def load_known_encodings():
    encodings, names = [], []
    for file in KNOWN_DIR.glob("*.npy"):
        encodings.append(np.load(file))
        names.append(file.stem)
    return encodings, names

def recognize_face_in_image(image_path: Path, tolerance=0.6):
    # Load and encode the incoming image
    image = face_recognition.load_image_file(str(image_path))
    unknown_encodings = face_recognition.face_encodings(image)
    if not unknown_encodings:
        return {"status": "error", "detail": "No face found."}

    # Compare against known faces
    known_encodings, known_names = load_known_encodings()
    results = []
    for unknown in unknown_encodings:
        matches = face_recognition.compare_faces(known_encodings, unknown, tolerance=tolerance)
        distances = face_recognition.face_distance(known_encodings, unknown)
        if True in matches:
            best_index = distances.argmin()
            results.append({"match": known_names[best_index], "distance": float(distances[best_index])})
        else:
            results.append({"match": None, "distance": float(min(distances))})
    return {"status": "success", "results": results}
