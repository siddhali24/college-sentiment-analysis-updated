from django.shortcuts import render
import os
from django.conf import settings
import pandas as pd
from django.http import JsonResponse
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from django.shortcuts import redirect

# Load model from Hugging Face Hub
MODEL_NAME = "SiddhaliK/sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def predict_sentiment(text):
    """Helper function to predict sentiment using Hugging Face model"""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits).item()
    
    # Map class IDs to labels (adjust based on your model's output)
    label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
    return label_map.get(predicted_class_id, "Unknown")

# Load dataset 
DATA_PATH = os.path.join(settings.BASE_DIR, '..', 'balanced_reviews (1).csv')
df = pd.read_csv(DATA_PATH)

def index(request):
    return render(request, 'index.html')

def Aboutus(request):
    return render(request, 'Aboutus.html')

def college_info(request):
    college_list = sorted(df['college'].dropna().unique().tolist())
    return render(request, 'college_info.html', {'college_list': college_list})
# Load dataset 
DATA_PATH = os.path.join(settings.BASE_DIR, '..', 'balanced_reviews (1).csv')
df = pd.read_csv(DATA_PATH)

def get_college_reviews(request):
    college_name = request.GET.get('college')
    if not college_name:
        return JsonResponse({'error': 'No college provided'}, status=400)
    college_reviews = df[df['college'] == college_name]

    if college_reviews.empty:
        return JsonResponse({'error': f'No reviews found for {college_name}'}, status=404)
    sentiment_counts = college_reviews['text_sentiment'].value_counts().to_dict()
    top_reviews = college_reviews['review'].head(3).tolist()
    pos = sentiment_counts.get('positive', 0)
    neg = sentiment_counts.get('negative', 0)
    neu = sentiment_counts.get('neutral', 0)

    if pos > neg and pos > neu:
        overall_sentiment = "Positive"
    elif neg > pos and neg > neu:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"

    response_data = {
        'college': college_name,
        'sentiment': overall_sentiment,
        'reviews': top_reviews,
    }

    return JsonResponse(response_data)

def review(request):
   return render(request, 'review.html')

def override_prediction(review, model_prediction):
    review_lower = review.lower()
    positive_phrases = ["not bad", "positive","not negative","not terrible", "not horrible", "not the worst", "not disgusting","discipliined"]
    for phrase in positive_phrases:
        if phrase in review_lower:
            return "Positive"
    negative_keywords = [
        "hate", "worst", "bad", "not satisfied", "not good", "terrible",
        "awful", "regret", "pathetic", "horrible", "disgusting", "trash",
        "useless", "scam","noisy","undisciplined","not positive","negative"
    ]
    
    if model_prediction != "Negative":
        if any(neg in review_lower for neg in negative_keywords):
            return "Negative"
    
    return model_prediction

def sentiment_analysis_view(request):
    if request.method == "POST":
        review_text = request.POST.get("review_text")
        if review_text:
            # Use the new predict_sentiment function
            model_prediction = predict_sentiment(review_text)
            result = override_prediction(review_text, model_prediction)
            request.session['last_result'] = result
            request.session['last_review'] = review_text
            return redirect('sentiment-review')  

    else:  
        result = request.session.pop('last_result', None)
        review_text = request.session.pop('last_review', "")

        return render(request, "review.html", {"result": result, "review_text": review_text})
