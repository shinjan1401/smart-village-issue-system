# Smart Village Issue Reporting System

A role-based digital governance platform designed to improve transparency, efficiency, and accountability in village-level issue management.

---

## 🧩 Problem Statement
In many Indian villages, issues related to roads, water supply, sanitation, electricity, healthcare, and education are often reported verbally or on paper. These methods lead to delays, lack of prioritization, and absence of transparency in the resolution process.

---

## 💡 Proposed Solution
The Smart Village Issue Reporting System provides a digital platform where village-level issues can be:
- Reported with photo evidence
- Tracked with real-time status
- Verified and approved by authorities
- Viewed publicly for transparency

---

## 👥 User Roles
### 1. Gram Sachiv
- Submits village issues with **before-work photos**
- Marks work as completed by uploading **after-work photos**

### 2. BDO (Block Development Officer)
- Verifies before and after photos
- Approves or rejects completed work

### 3. Public (Villagers)
- Can view all issues and their current status
- Ensures transparency and accountability

---

## 🤖 Google Technology Used
### Google Gemini AI
- **Gemini Embeddings** are used to analyze and group similar village issues using semantic similarity.
- **Gemini Pro (Chat Model)** is used to provide an AI-powered assistant for intelligent insights and explanations.

This helps authorities identify recurring problems and prioritize development work efficiently.

---

## ✨ Key Features
- Photo-based issue verification
- Role-based dashboards (Sachiv, BDO, Public)
- Status lifecycle tracking (Pending → Waiting Approval → Approved)
- AI-assisted issue grouping
- Clean and user-friendly UI with background imagery and glassmorphism design

---

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, JavaScript
- **AI:** Google Gemini (via Generative AI API)
- **Tools:** GitHub, Localhost server

---

## ▶️ How to Run the Project Locally
### Backend
```bash
python -m uvicorn main:app --reload
# smart-village-issue-system
Smart Village Issue Reporting System (GDG Project)
