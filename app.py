import joblib
import gradio as gr

# Load model and vectorizer
model = joblib.load("models/spam_classifier_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

# Prediction function
def classify_message(text):
    X = tfidf.transform([text])
    prediction = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]
    label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
    return label, f"{prob:.2%} spam probability"

# Gradio Interface
iface = gr.Interface(
    fn=classify_message,
    inputs=gr.Textbox(lines=5, placeholder="Enter your message here..."),
    outputs=["text", "text"],
    title="📩 Spam Message Detector",
    description="Classify a message as spam or not spam using a trained ML model."
)

if __name__ == "__main__":
    iface.launch()