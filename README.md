# 🚀 Cloud Deployed Gen AI E-Commerce Chatbot with CI/CD Pipeline

An end-to-end **Production-Ready Generative AI E-Commerce Chatbot** built using **Llama 3.3, GROQ, RAG, ChromaDB, SQL Querying, Docker, GitHub Actions CI/CD, AWS ECR, and AWS EC2 Deployment**.

This project demonstrates how modern AI applications are designed, containerized, tested, deployed, and automatically updated in cloud environments using real-world DevOps workflows.

---

# 🌐 Live Demo

🚀 Live Application:

👉 http://3.228.14.39:8501

---

# 🎥 Project Demo Video

👉 https://www.loom.com/share/4c4b5e7447c540f695e395d0ff441f22

---

# 💻 GitHub Repository

👉 https://github.com/aslam347/E-Commerce-RAG

---

# 🧠 Project Overview

This AI-powered chatbot helps e-commerce customers:

✅ Ask product-related questions  
✅ Search products using natural language  
✅ Get instant FAQ responses  
✅ Query product database conversationally  
✅ Receive AI-generated intelligent answers  

The application combines:

- Retrieval-Augmented Generation (RAG)
- LLM-based SQL query generation
- Semantic routing
- Vector search
- Cloud deployment
- Docker containerization
- Automated CI/CD pipeline

---

# 🏗️ End-to-End Cloud Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
Semantic Router
  ↓
 ┌─────────────────────┬─────────────────────┐
 │                     │                     │
FAQ Intent         SQL Intent
 │                     │
ChromaDB RAG       SQL Query Generation
 │                     │
Llama 3.3 via GROQ SQLite Product Database
 │                     │
 └──────── Final AI Response ────────┘


CI/CD FLOW

Developer Pushes Code to GitHub
                ↓
GitHub Actions CI/CD Pipeline
                ↓
Run Automated Tests (Pytest)
                ↓
Build Docker Image
                ↓
Push Image to Docker Hub
                ↓
Push Image to AWS ECR
                ↓
GitHub Actions SSH into EC2
                ↓
EC2 Pulls Latest Image from ECR
                ↓
Run Updated Docker Container
                ↓
Application Auto Deployed on AWS Cloud
```

---

# ☁️ Cloud & DevOps Highlights

✅ Dockerized Gen AI Application  
✅ GitHub Actions CI/CD Pipeline  
✅ Automated Testing using Pytest  
✅ Docker Hub Integration  
✅ AWS ECR Container Registry  
✅ AWS EC2 Cloud Deployment  
✅ SSH-Based Automated Deployment  
✅ Environment Variable Security using GitHub Secrets  
✅ Real-world MLOps / DevOps Workflow  
✅ Production-style Deployment Architecture  

---

# 🧠 Core Features

## ✅ FAQ AI Assistant

Supports intelligent customer support questions:

- Return policy
- Refund process
- Payment methods
- Shipping details
- Promo code support
- Order cancellation
- Damaged product help

---

## ✅ AI Product Search Engine

Supports natural language product search:

- Nike shoes below ₹3000
- Puma shoes with discount
- Shoes under ₹2000
- Cheapest running shoes
- Top-rated sports shoes
- Women sports shoes

---

# 🧠 Tech Stack

## AI / ML

- Llama 3.3
- GROQ API
- RAG
- ChromaDB
- Sentence Transformers
- Semantic Router

## Backend

- Python
- SQLite
- SQLAlchemy
- Pandas

## Frontend

- Streamlit

## Cloud / DevOps

- Docker
- Docker Hub
- GitHub Actions
- AWS EC2
- AWS ECR
- Linux
- SSH Automation

## Testing

- Pytest

---

# 📷 Project Screenshots

## Product Search Output

![product screenshot](resources/product-ss.png)

---

## Architecture Diagram

![architecture diagram](resources/architecture-diagram.png)

---

# 📁 Project Structure

```bash
E-Commerce-RAG/
│
├── app/
│   ├── main.py
│   ├── faq.py
│   ├── sql.py
│   ├── router.py
│   ├── style.css
│   └── db.sqlite
│
├── resources/
│   ├── faq_data.csv
│   ├── product-ss.png
│   ├── architecture-diagram.png
│   └── ecommerce_data_final.csv
│
├── tests/
│   ├── conftest.py
│   ├── test_faq.py
│   ├── test_sql.py
│   ├── test_router.py
│   └── test_smoke.py
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── requirements.txt
├── Dockerfile
├── pytest.ini
├── .dockerignore
├── .gitignore
└── README.md
```

---

# ⚙️ Local Setup

## Clone Repository

```bash
git clone https://github.com/aslam347/E-Commerce-RAG.git
```

## Move into Project

```bash
cd E-Commerce-RAG
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest -q
```

## Run Application

```bash
streamlit run app/main.py
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t ecommerce-rag .
```

## Run Docker Container

```bash
docker run --env-file app/.env -p 8501:8501 ecommerce-rag
```

---

# 🐳 Docker Hub

## Pull from Docker Hub

```bash
docker pull mohamedaslam2001/ecommerce-rag
```

## Run Container

```bash
docker run --env-file app/.env -p 8501:8501 mohamedaslam2001/ecommerce-rag
```

---

# ☁️ AWS Deployment

This project is deployed on AWS Cloud using:

- AWS EC2
- AWS ECR
- GitHub Actions CI/CD

## Deployment Workflow

```text
GitHub Push
    ↓
GitHub Actions
    ↓
Run Tests
    ↓
Build Docker Image
    ↓
Push to Docker Hub
    ↓
Push to AWS ECR
    ↓
SSH into EC2
    ↓
Pull Latest Image
    ↓
Run Updated Container
```

---

# 🔐 GitHub Secrets Used

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_ACCOUNT_ID
AWS_REGION
EC2_HOST
EC2_USER
EC2_SSH_KEY
GROQ_API_KEY
GROQ_MODEL
```

---

# 🔐 Environment Variables

Create `.env` file inside `app/`

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

---

# 🧪 Automated Testing

This project includes CI/CD-integrated automated testing using Pytest.

Test coverage includes:

✅ FAQ flow  
✅ SQL flow  
✅ Semantic router  
✅ Application smoke testing  

Run locally:

```bash
pytest -q
```

---

# 💡 Real-World Business Use Cases

✅ E-commerce AI assistant  
✅ Customer support automation  
✅ AI shopping assistant  
✅ Conversational commerce platform  
✅ AI-powered FAQ system  
✅ Intelligent product discovery  
✅ Retail support chatbot  

---

# 🔥 Engineering Challenges Solved

- Semantic intent routing
- LLM-generated SQL queries
- Vector database integration
- ChromaDB RAG pipeline
- SQLite integration with LLM workflow
- Docker containerization
- GitHub Actions CI/CD automation
- AWS cloud deployment
- Secure secret management
- Production deployment troubleshooting

---

# 📚 Key Learnings

- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Semantic Routing
- ChromaDB Vector Search
- LLM-based SQL Generation
- Streamlit Application Development
- Docker & Containerization
- CI/CD Pipeline Automation
- AWS EC2 & ECR Deployment
- DevOps for AI Applications
- Production AI Deployment Architecture

---

# 🙌 Author

# Mohamed Aslam

Passionate about:

- Generative AI
- AI Engineering
- AI Agents
- MLOps
- Cloud AI Deployment
- Real-world AI Applications

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

---

# 📜 License

This project is licensed under the MIT License.
