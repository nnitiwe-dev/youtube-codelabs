
# 🚀 FastAPI Starter Tutorials

Welcome to your journey into building high-performance APIs with **FastAPI**! This project contains two beginner-friendly subdirectories that walk you through building:

1. A **basic REST API** (`hello_api`)
2. An **AI-powered API** that removes backgrounds from images using Stability AI (`ai_api_101`)

---

## 📁 Project Structure

```
.
├── hello_api/         # FastAPI basics: CRUD endpoints with in-memory DB
│   └── main.py
│
├── ai_api_101/        # AI-powered API: Remove image background using Stability AI
│   ├── main.py
│   └── services/
│       └── bg_remover.py
│
└── README.md          # You're here!
```

---

## 🔰 1. `hello_api` — FastAPI for Beginners

Learn the fundamentals of FastAPI:
- Create RESTful endpoints
- Define request/response schemas using `pydantic`
- Use in-memory data storage
- Explore Swagger UI for automatic API docs

### ▶️ To Run:
```bash
cd hello_api
uvicorn main:app --reload
```

Open in browser: `http://localhost:8000/docs`

---

## 🤖 2. `ai_api_101` — AI Background Remover API

An example of using external AI services inside a FastAPI app. This project uses:
- FastAPI + `UploadFile`
- Stability AI's [Remove Background API](https://platform.stability.ai/docs/api-reference#tag/Edit/paths/~1v2beta~1stable-image~1edit~1remove-background/post)
- `requests` to call external services

### ⚙️ Setup
> 🔐 Replace `sk-MYAPIKEY` in `bg_remover.py` with your Stability AI API key.

### ▶️ To Run:
```bash
cd ai_api_101
uvicorn main:app --reload
```

Go to `http://localhost:8000/docs` and upload an image to `/remove-bg`.

---

## 💡 Want More?

These projects are great stepping stones to:
- AI-powered chatbots
- Computer vision tools
- PDF summarizers
- Resume analyzers
- And more!

If you'd like to keep building, reach out or explore ways to plug in OpenAI, Hugging Face, or even custom ML models.

---

## ✨ Created By
Samuel Nnitiwe Theophilus  
Data & ML Engineer | AI Engineer | Educator  
AI Blog: [Nnitiwe's AI Blog](https://blog.nnitiwe.io/)  
Twitter: [@nnitiwe](https://twitter.com/nnitiwe)
Website: [nnitiwe.io](https://nnitiwe.io/)