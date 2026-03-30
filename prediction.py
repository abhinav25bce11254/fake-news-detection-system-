import pickle

def load_model():
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
        
    with open('models/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
        
    return model, vectorizer

def predict(text, model, vectorizer):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    
    return "Fake News" if prediction == 0 else "Real News"