from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load models only once
emotion_model = "bhadresh-savani/distilbert-base-uncased-emotion"
toxicity_model = "unitary/unbiased-toxic-roberta"

emotion_classifier = pipeline("text-classification", model=emotion_model, return_all_scores=True)
toxicity_classifier = pipeline("text-classification", model=toxicity_model, top_k=None)

class CommentRequest(BaseModel):
    comment: str

@app.post("/analyze")
def analyze_comment_api(request: CommentRequest):
    comment = request.comment
    emotion_result = emotion_classifier(comment)[0]
    toxicity_result = toxicity_classifier(comment)[0]

    # Filter low-signal toxic labels
    toxicity_result = [label for label in toxicity_result if label['score'] > 0.01]

    return {
        "emotion": sorted(emotion_result, key=lambda x: x['score'], reverse=True),
        "toxicity": sorted(toxicity_result, key=lambda x: x['score'], reverse=True)
    }
