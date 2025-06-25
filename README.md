🚀 FastAPI Secure File-Share System

A lightweight, JWT-secured REST API for “Ops” users to upload `.pptx`/`.docx`/`.xlsx` files and generate opaque download links for clients. Built with FastAPI, Python-Jose, and in-memory UUID mapping.

📦 Features

- **JWT Authentication** for Ops users  
- **Upload** only `.pptx`, `.docx`, `.xlsx` via `/ops/upload-file`  
- **Download** via unique, unguessable UUID links  
- In-memory mapping (swap in DB for persistence)  
- Clean, modular code structure  

🔧 Prerequisites

- Python 3.10+  
- Git  
- (Optional) Docker  

---

⚙️ Installation

```bash
# Clone repo
git clone https://github.com/Harshitha8117/EZ.git
cd EZ/file-share-api

# Create & activate venv
python -m venv env
# Windows
.\env\Scripts\activate
# macOS/Linux
source env/bin/activate

# Install deps
pip install -r requirements.txt
````

---

🏃‍♂️ Running

```bash
uvicorn main:app --reload
```

* **API docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Health**: `GET /` → `{"message":"🚀 FastAPI File Vault with Auth is running!"}`

---
🔗 Endpoints

1. Ops User Login

```http
POST /auth/login
Content-Type: application/json

{
  "username": "opsuser",
  "password": "securepass"
}
```

> **Response**
>
> ```json
> { "access_token":"<JWT>", "token_type":"bearer" }
> ```

### 2. Upload File (Ops only)

```http
POST /ops/upload-file
Authorization: Bearer <JWT>
Content-Type: multipart/form-data

Key: file → choose `report.docx`
```

> **Response**
>
> ```json
> {
>   "download-link":"http://127.0.0.1:8000/download-file/<uuid>",
>   "message":"success"
> }
> ```

### 3. Download by UUID

```http
GET /download-file/{download_id}
```

> **Response**
>
> * `200`: Returns the binary file
> * `404`: `{ "detail":"Assignment ID not found" }`


🛠 Project Structure


file-share-api/
├── main.py
├── routers/
│   ├── auth.py
│   ├── upload.py
│   └── download.py
├── auth/
│   └── jwt_handler.py
├── utils/
│   └── file_validator.py
├── uploads/            # saved files
├── requirements.txt
└── .gitignore


## 🌱 Extending

* **Persist mapping** in PostgreSQL / Mongo
* **Client user signup**, email-verified URLs
* **Expiry + rate-limit** download links
* **S3 storage** for files

📄 License

[MIT](LICENSE) © 2025 Harshitha


