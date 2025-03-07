# YouTube Comment Sentiment Analysis

## Overview
This project provides a **Chrome extension** and an **ML-powered backend** to analyze the sentiment of YouTube comments in real-time. The backend is powered by **FastAPI**, **MLflow for experiment tracking**, and **DVC for dataset versioning**.

## Features
- **Chrome Extension**: Extracts YouTube comments and displays sentiment analysis results.
- **FastAPI Backend**: Serves an ML model for sentiment classification.
- **MLflow Integration**: Tracks model training and versioning.
- **DVC for Data Management**: Ensures dataset versioning and reproducibility.

## HLD
![HLD](docs\yt-hld.png)

## Repository Structure
```
yt-comment-sentiment-analysis/
│── backend/                    # ML API Backend
│   ├── models/                  # Pre-trained ML models
│   ├── src/
│   │   ├── main.py               # FastAPI entry point
│   │   ├── sentiment_analyzer.py  # ML model for sentiment analysis
│   │   ├── train.py              # Model training script with MLflow tracking
│   │   ├── database.py           # (Optional) Database interactions
│   │   ├── config.py             # API configurations
│   ├── requirements.txt          # Dependencies
│   ├── Dockerfile                # Docker container setup
│── data/                        # DVC-managed dataset storage
│   ├── raw/                      # Raw YouTube comment data
│   ├── processed/                # Preprocessed comment data
│   ├── .dvc/                     # DVC metadata
│── mlflow/                      # MLflow tracking & experiments
│   ├── mlruns/                   # MLflow experiment storage
│   ├── config.yaml               # MLflow config (optional)
│── extension/                   # Chrome Extension Frontend
│   ├── src/
│   │   ├── content.js            # Extracts YouTube comments
│   │   ├── popup.js              # Handles UI interactions
│   │   ├── background.js         # Manages API calls
│   │   ├── manifest.json         # Chrome extension config
│   │   ├── styles.css            # UI styling
│   ├── icons/                    # Extension icons
│   ├── index.html                # Popup HTML
│── tests/                        # Unit tests
│── README.md                     # Project Documentation
│── .gitignore                    # Ignore unnecessary files
│── dvc.yaml                      # DVC pipeline configuration
│── mlflow_tracking.py            # MLflow tracking script
│── train.py                      # Model training with DVC & MLflow
```
