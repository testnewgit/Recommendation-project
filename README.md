# 🏍️ AI-Powered Product Recommendation System

This is a full-stack **AI-powered product recommendation engine** built for an eCommerce scenario. It uses **Google Gemini** to generate **personalized product suggestions** based on user preferences and browsing behavior.

---

## 📖 What I Did in This Project

This project involved end-to-end development of an AI-powered recommendation engine. Here’s a high-level summary of what I implemented and solved:

### ✅ Backend (FastAPI + Gemini)

* Set up FastAPI server with clean API architecture.
* Integrated **Google Gemini** API for generating smart recommendations.
* Engineered prompts for accurate, JSON-structured outputs.
* Added environment configurations like:

  * `MODEL_NAME=gemini-2.0-flash`
  * `MAX_TOKENS=1024`
  * `TEMPERATURE=0.7`
  * `DATA_PATH=data/products.json`
* Configured CORS to allow frontend access.

### ✅ Frontend (React.js)

* Built modular React components (`Catalog`, `UserPreferences`, `Recommendations`, `BrowsingHistory`).
* Implemented dynamic **filtering and sorting** (by price/rating, asc/desc).
* Designed UI using **CSS Grid** and **Flexbox**.

Screnshots of frontend
![msedge_4DIfcQgvKB](https://github.com/user-attachments/assets/2a820a40-14b3-4694-b636-01296395b079)


![msedge_7uLY6RN0Qp](https://github.com/user-attachments/assets/bd840da9-cd79-4da1-aba0-7c1ed228b117)


### ✅ Issues Faced and Solved

* **OpenAI API quota exceeded** — Switched to **Google Gemini**.
* **Missing Python packages** — Installed `google-generativeai` and `python-dotenv`.
* **React crash due to missing `react-scripts`** — Fixed using `npm install`.
* **CORS policy errors** — Solved by enabling FastAPI `CORSMiddleware`.
* **Gemini returning malformed JSON** — Refined prompts and parsed manually.
* **Backend/Frontend connection issues** — Matched ports, confirmed `localhost:8000`.

---



---

## 🧰 Tech Stack

| Layer      | Tools              |
| ---------- | ------------------ |
| LLM API    | Google Gemini      |
| Backend    | FastAPI, Python    |
| Frontend   | React.js           |
| Styling    | CSS Grid & Flexbox |
| Deployment | Run locally        |

---

## 🚀 Getting Started

### 📁 Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/recommendation-system.git
cd recommendation-system
```

---

### ⚙️ Backend Setup (FastAPI)

📍 Navigate to the backend folder:

```bash
cd backend
```

📦 Create & activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

📅 Install dependencies:

```bash
pip install -r requirements.txt
```

🔑 Add your **Gemini API Key**

Create a `.env` file or edit `config.py`:

```python
config = {
    "GEMINI_API_KEY": "your-gemini-key",
    "MODEL_NAME": "gemini-2.0-flash",
    "MAX_TOKENS": 1024,
    "TEMPERATURE": 0.7,
    "DATA_PATH": "data/products.json"
}
```

▶️ Start the backend server:

```bash
uvicorn app:app --reload --port 8000
```

✅ Your backend will run on: `http://localhost:8000/api`

---

### 💻 Frontend Setup (React)

📍 Navigate to the frontend folder:

```bash
cd ../frontend
```

📅 Install frontend dependencies:

```bash
npm install
```

▶️ Run the app:

```bash
npm start
```

✅ Frontend will open at: `http://localhost:3000`

---

## 🧪 How It Works

1. Choose your **price range**, **categories**, and **brands**
2. Click on any product to **simulate browsing**
3. Click **"Get Personalized Recommendations"**
4. **Gemini API** returns **5 intelligent suggestions** with explanations and confidence scores

---

## 📂 Project Structure

```
recommendation-system/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── services/
│   │   ├── llm_service.py
│   │   └── product_service.py
│   └── data/
│       └── products.json
│
├── frontend/
│   ├── src/
      ├── components/
      ├── services/
      ├── App.js
      └── styles/

```

---

## ✅ Key Implementation Highlights

* Uses **Google Gemini** for contextual reasoning and smart recommendations
* Efficient **prompt engineering** with price/category filtering
* Clean RESTful API with request/response validation
* Responsive UI with component-based architecture
* Graceful error handling and dev-friendly logging
* 💡 **Newly added sorting and filtering for product catalog (Frontend)**

---


---

## 🌟 Stretch Goals Implemented

✅ Login using **JWT token-based authentication**
✅ Modular LLM integration for flexibility

---

Checking of api working properly using postman
![Postman_9fQ2Ci1OmB](https://github.com/user-attachments/assets/99d437bb-2fae-4695-8166-b177dbc77ff1)






