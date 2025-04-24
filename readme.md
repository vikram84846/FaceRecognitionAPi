# 🧠 Face Recognition API with FastAPI

A simple and fast face recognition API built with [FastAPI](https://fastapi.tiangolo.com/) and the [face-recognition](https://github.com/ageitgey/face_recognition) Python library. Package management is handled by [uv](https://github.com/astral-sh/uv).

---

## 🚀 Features

- 🔍 Detect and recognize faces from images
- 📝 Register new known faces via API
- 🧠 Uses deep learning via `dlib` under the hood
- 🧪 FastAPI-powered RESTful API

---

## 📦 Tech Stack

- `FastAPI` — lightning-fast web framework
- `face-recognition` — powerful face detection and recognition
- `uv` — blazing-fast Python package manager
- `dlib`, `numpy`, `Pillow` — backend tools for image processing

---

## 🛠️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/face-recognition-api.git
   cd face-recognition-api
2. **Create a virtual enviornment using uv package manager**
    ```bash
    uv venv
    .venv\Scripts\activate
**note: make sure u have uv package manager installed if not follow the link**
    ```bash
    pip install uv
3. **Install dependecies from requirement.txt**
    ```bash
    uv pip install -r requirements.txt
4. **Run project**
    ```bash
    uvicorn app.main:app --reload

# Project Structure
    ```bash
    face-recognition-api/
    │
    ├── main.py                  # FastAPI app with routes
    ├── face_utils.py            # Utility functions (encode, save, compare)
    ├── known_faces/             # Folder with .npy encodings
    ├── uploads/                 # Uploaded images for registration
    ├── requirements.txt         # Project dependencies
    └── README.md                # You're here!
```
# API ENDPOINTS
Register a New Face
POST /register/

Form-data:

name: person's name

file: image file (jpg/png)

Recognize Face
POST /recognize/

Form-data:

file: image file (jpg/png)

# 📌 TODO
 Add SQLModel for user DB

 Add support for video input

 Deploy on Railway/Fly.io

 Return face previews in API response

# 🧑‍💻 Author
Built with ❤️ by Vikram

# 📄 License
MIT
