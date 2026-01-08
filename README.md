# ReelWriter AI

ReelWriter AI is a full-stack web application that generates engaging **captions and hashtags for TikTok and Instagram Reels** using AI.  
It is built as a clean, portfolio-ready project with a modern tech stack and clear separation between backend and frontend.

---

## ✨ Features

- AI-generated captions for short-form video content
- Automatic hashtag suggestions
- Platform-aware generation (TikTok / Instagram)
- Clean REST API (FastAPI)
- Modern UI built with Next.js
- Secure configuration (no secrets in repository)
- Portfolio-ready project structure

---

## 🧱 Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic
- OpenAI API

### Frontend
- Next.js (App Router)
- TypeScript
- Tailwind CSS

### Dev / Ops
- Git & GitHub
- Virtual environment (venv)
- Docker (currently disabled for local development)

---

## 📁 Project Structure

```text
reelwriter-ai/
├─ rw_backend/
│  ├─ rw_app/
│  │  ├─ rw_main.py
│  │  ├─ rw_routes_generate.py
│  │  ├─ rw_schemas.py
│  │  └─ rw_config.py
│  ├─ rw_uvicorn_app.py
│  ├─ rw_requirements.txt
│  └─ .env.example
│
├─ rw_frontend/
│  ├─ app/
│  ├─ public/
│  ├─ package.json
│  └─ next.config.ts
│
├─ .gitignore
└─ README.md


---------------------------------------------------------------------------


 How to Run Locally
 1️⃣ Backend (FastAPI):
 cd rw_backend
--
    .\venv\Scripts\Activate.ps1
    uvicorn rw_uvicorn_app:app --reload --port 8010
--
Backend will be available at:

http://127.0.0.1:8010


2️⃣ Frontend (Next.js):
--
  cd rw_frontend
    npm install
    npm run dev
--

Frontend will be available at:

http://127.0.0.1:3000

-------------------------------------

🔐 Environment Variables

Backend uses environment variables for sensitive configuration.

Example (rw_backend/.env.example):
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE
    APP_ENV=dev
⚠️ .env files are ignored by Git and never pushed to the repository.

-------------------------------------

🔌 API Overview
Generate captions & hashtags

Endpoint

POST /api/generate


Description
Generates AI-based captions and hashtags for short-form video content.

-------------------------------------

🚀 Status

Backend: ✅ Working

Frontend: ✅ Working

OpenAI API: ✅ Integrated

Docker: ❌ Disabled (local development mode)

-------------------------------------


🎯 Use Cases

Content creators

Social media managers

Marketing agencies

AI-powered SaaS products

Portfolio showcase for full-stack / AI developers

-------------------------------------


📌 Notes

This project is part of a larger portfolio focused on:

AI-powered tools

Automation

Clean backend architecture

Real-world SaaS-style applications

-------------------------------------


👤 Author

Developed by Tornike Tetradze
GitHub: https://github.com/tetradzetornike-oss