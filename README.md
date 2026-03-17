---
title: College Sentiment Analysis
emoji: 🎓
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# College Sentiment Analysis

A Django web application for analyzing sentiment of college reviews using a fine-tuned BERT model.

## Features

- Sentiment analysis of college reviews (Positive/Negative/Neutral)
- College information and review browsing
- Interactive web interface with custom CSS styling
- Real-time sentiment prediction using Hugging Face transformers

## Model

This application uses the `SiddhaliK/sentiment` model from Hugging Face Model Hub, which is a fine-tuned BERT model for sentiment classification.

## Usage

1. Navigate to the review page
2. Enter your college review text
3. Get instant sentiment analysis results
4. Browse college information and existing reviews

## Technology Stack

- Django 4.0+
- Hugging Face Transformers
- PyTorch
- Bootstrap CSS
- SQLite Database