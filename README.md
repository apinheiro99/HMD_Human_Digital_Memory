# 🚀 HDM — Human Digital Memory

**HDM (Human Digital Memory)** is a local-first system designed to organize, classify, and index massive collections of images and videos (1TB–50TB+) using advanced computer vision, multimodal embeddings, semantic clustering, and dynamic ontology generation — all running **100% offline** and accelerated by GPU.

HDM creates a structured “digital memory” from raw unorganized media using a fully modular, scalable, and incremental architecture.

---

## 🔥 Key Features

### 🧠 Multimodal Embeddings
Fusion of:
- CLIP
- DINOv2
- MobileNet
- Optional Vision-LLM  
Combined into a single unified vector representation.

### 🧩 Semantic Classification
Automatic detection of:
- landscapes
- documents
- memes
- screenshots
- selfies
- WhatsApp content
- objects
- NSFW (local-only)
- and more…

### 📷 Face Engine
- Face detection  
- Embeddings (ArcFace/InsightFace)  
- Person clustering (HDBSCAN)  
- Persistent identity tracking  

### 🔁 Duplicate Detection
- Perceptual hashing (pHash, aHash, wHash)  
- Deep embedding similarity  
- Direct + semantic duplicate identification  

### 🌫️ Blur & Quality Analysis
- Laplacian variance  
- SVD sharpness  
- Aesthetic scoring  

### 🧠 Ontology Builder
Creates dynamic, human-friendly categories such as:
- “Beach Trip 2023”
- “Documents — Invoices”
- “WhatsApp Screenshots with John”
- “Family — Mom”

### 🔍 Vector Indexing
- FAISS or Qdrant  
- Incremental upsert  
- k-NN semantic search  

---

## 🏗️ Architecture Overview

HDM is organized into four immutable macro-layers:

```
Application Layer      → CLI, Web UI, API  
HDM Core Layer         → Pipelines, Embeddings, Face Engine, Classifiers, Ontology, Reasoner  
Data & Storage Layer   → Vector DB, Metadata Store, Cache  
System Layer           → Filesystem, IO, CUDA/GPU  
```

Pipeline:

```
SCAN → LOAD → EMBED → BLUR/DUPLICATES → FACES → SEMANTIC/NSFW  
→ CLUSTER → ONTOLOGY → REASONER → INDEX → ORGANIZER
```

---

## ⚙️ Core Principles

- Local-first (no cloud uploads)
- Modular architecture
- Scalable to tens of millions of files
- Incremental processing
- GPU-accelerated
- Fully interpretable (logs + semantic reasoning)
- Extensible and model-agnostic
- TDD-first development methodology

---

## 📁 Project Structure

```
HDM/
 ├── hdm_core/
 │    ├── io/
 │    ├── embeddings/
 │    ├── clustering/
 │    ├── models/
 │    ├── ontology/
 │    ├── reasoner/
 │    ├── pipelines/
 │    ├── index/
 │    └── utils/
 ├── hdm_cli/
 ├── hdm_web/
 └── tests/
```

---

## 🚀 Roadmap

### ✔ Completed
- Foundation Spec  
- High-Level Architecture  

### 🏗 In Progress
- Interfaces (Protocols)  
- Technical Contracts  
- Detailed Pipelines  
- Base Implementations (ImageLoader, EmbeddingEngine)

### ⏭ Planned
- Full Orchestration Engine  
- Web Interface  
- Person Timeline  
- Memory Search System  
- Offline Vision-LLM integration

---

## 🔐 Privacy & Security

- 100% offline  
- No media files leave the user's system  
- NSFW classification runs locally  
- No personal data included in repo  

---

## 📜 License

Open Software License ("OSL") v 3.0)

---

## 🧑‍💻 Author

HDM — Human Digital Memory  
Andre Pinheiro
