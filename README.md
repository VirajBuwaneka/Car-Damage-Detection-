# 🚗 Car Damage Detection – Deep Learning Web App

[![Python](https://img.shields.io/badge/python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![PyTorch](https://img.shields.io/badge/PyTorch-1.16-orange?logo=pytorch&logoColor=white)](https://pytorch.org/) 
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)


A **deep learning–based web app** to detect **car damages** from uploaded images using **PyTorch**.  
Users can classify the severity of damage instantly via a **Streamlit** interface.

---

## 🔥 Features
- Upload any car image for **instant damage detection**  
- **PyTorch CNN model** for accurate predictions  
- Displays **classification label**  
- **Interactive Streamlit interface**  
- **FastAPI endpoint** for programmatic access to predictions  

---

## 📸 Streamlit UI Screenshot

![Streamlit UI](image.png)

> This is the main interface of the Car Damage Detection app, where users can upload images and view damage predictions instantly.

## ⚡ FastAPI Endpoint Screenshot

![FastAPI Postman Test](postman.png)

> This screenshot shows the FastAPI endpoint working in Postman, returning damage predictions for uploaded car images.

---

## 🧠 Model Overview
| Component | Description |
|----------|-------------|
| Model Type | Convolutional Neural Network (CNN) |
| Framework | PyTorch |
| Task | Car Damage Image Classification |
| Input | Car image (.jpg / .png) |
| Output | Damage level prediction |

---

## 🛠️ Tech Stack
| Area | Tools |
|------|-------|
| Deep Learning | PyTorch |
| Programming | Python |
| Web App | Streamlit |
| API | FastAPI |
| Utilities | NumPy, Pillow, scikit-learn |
