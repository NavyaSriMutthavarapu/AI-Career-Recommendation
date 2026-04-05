import joblib
import numpy as np

# Load model + encoder
model = joblib.load("career_pipeline.pkl")
label_encoder = joblib.load("label_encoder.pkl")


def predict_top_roles_with_scores(text):
    probs = model.predict_proba([text])[0]
    top_indices = probs.argsort()[-3:][::-1]

    roles = label_encoder.inverse_transform(top_indices)
    scores = probs[top_indices]

    #  BOOST LOGIC (ADD HERE)
   

    text_lower = text.lower()
    for i, role in enumerate(roles):
        if role == "Data Analyst":
            if any(skill in text_lower for skill in ["sql", "excel", "power bi", "tableau", "dashboard"]):
                scores[i] += 0.15
            elif role == "Data Scientist":
                if any(skill in text_lower for skill in ["machine learning", "deep learning", "nlp", "model", "tensorflow"]):
                    scores[i] += 0.15
            elif role == "Business Analyst":
                if any(skill in text_lower for skill in ["requirements", "stakeholders", "documentation", "use case"]):
                    scores[i] += 0.15
            elif role == "Web Developer":
                if any(skill in text_lower for skill in ["html", "css", "javascript", "react", "angular"]):
                    scores[i] += 0.10
            elif role == "PHP Developer":
                if any(skill in text_lower for skill in ["php", "laravel", "codeigniter", "wordpress"]):
                    scores[i] += 0.20
            elif role == "Java Developer":
                if any(skill in text_lower for skill in ["java", "spring", "hibernate", "j2ee"]):
                    scores[i] += 0.15
            elif role == "Python Developer":
                if "python" in text_lower:
                    scores[i] += 0.15
            elif role == "Mobile Developer":
                if any(skill in text_lower for skill in ["android", "ios", "flutter", "react native"]):
                    scores[i] += 0.15
            elif role == "QA Engineer":
                if any(skill in text_lower for skill in ["testing", "selenium", "automation", "test cases"]):
                    scores[i] += 0.15
            elif role == "DevOps Engineer":
                if any(skill in text_lower for skill in ["docker", "kubernetes", "ci/cd", "jenkins", "aws"]):
                    scores[i] += 0.15
            elif role == "Database Engineer":
                if any(skill in text_lower for skill in ["oracle", "sql", "database", "pl/sql"]):
                    scores[i] += 0.15
            elif role == "Network Engineer":
                if any(skill in text_lower for skill in ["network", "routing", "switching", "tcp/ip"]):
                    scores[i] += 0.15
            elif role == "System Administrator":
                if any(skill in text_lower for skill in ["linux", "unix", "server", "administration"]):
                    scores[i] += 0.15
            elif role == "Support Engineer":
                if any(skill in text_lower for skill in ["support", "troubleshooting", "help desk"]):
                    scores[i] += 0.15
            elif role == "Software Engineer":
                if any(skill in text_lower for skill in ["software engineer", "sdlc", "debugging", "api", "system design",
                                                 "backend", "flask", "node", "c++", ".net"]):
                     scores[i] += 0.20   # slightly higher boost

   
    sorted_idx = scores.argsort()[::-1]

    roles = roles[sorted_idx]
    scores = scores[sorted_idx]

    return roles.tolist(), scores.tolist()

def get_confidence_label(score):
    if score > 0.75:
        return "High Confidence 🔥"
    elif score > 0.5:
        return "Moderate Confidence 👍"
    else:
        return "Low Confidence ⚠️"