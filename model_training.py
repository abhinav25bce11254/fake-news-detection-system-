from sklearn.linear_model import LogisticRegression
import pickle

def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def save_model(model, vectorizer):
    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)
        
    with open('models/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)