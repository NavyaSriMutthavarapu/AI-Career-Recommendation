# 🚀 AI Career Recommendation

AI Career Advisor is an end-to-end Machine Learning application that analyzes a user’s resume or skills and recommends the most suitable tech career role.

The system predicts career roles, evaluates profile strength, identifies skill gaps, and provides a personalized action plan to help users improve their career readiness.

# 📌 Features

* Career Role Prediction
* Top Career Match Suggestions
* Skill Match Score
* Skill Gap Analysis
* Personalized Action Plan
* Resume PDF Upload Support
* Related Job Role Suggestions
* Interactive Streamlit Interface


# 🛠️ Tech Stack

## Programming Language

* Python

## Libraries & Frameworks

* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Streamlit
* PyPDF
* Matplotlib
* Seaborn

## Machine Learning & NLP

* TF-IDF Vectorization
* Text Preprocessing
* Classification Models
* Hyperparameter Tuning
* Macro F1 Score Evaluation

## Tools

* Jupyter Notebook
* VS Code
* GitHub



# 📂 Project Structure

```bash
AI-Career-Advisor/
│
├── app.py                     # Main Streamlit application
├── model_utils.py             # Prediction logic
├── skill_utils.py             # Skill matching & score calculation
├── role_data.py               # Roles and required skills
├── resume_utils.py            # PDF text extraction
│
├── career_pipeline.pkl        # Trained ML pipeline
├── label_encoder.pkl          # Encoded labels
├── clean_role_to_titles.pkl   # Role mapping data
│
├── requirements.txt
├── README.md
└── notebook.ipynb             # Model building notebook


# 📊 Project Workflow

## 1. Data Collection

* Used a resume dataset containing resume text and job role labels.

## 2. Data Preprocessing

* Converted text into lowercase
* Removed extra spaces
* Removed duplicate resumes
* Cleaned and standardized job roles

## 3. Feature Engineering

* Applied TF-IDF Vectorization
* Used bigrams for better text understanding

## 4. Model Building

Trained multiple machine learning models:

* Naive Bayes
* Logistic Regression
* Random Forest
* Linear SVM
* XGBoost

## 5. Model Evaluation

* Evaluated models using Macro F1 Score
* Compared model performance
* Selected the best-performing model

## 6. Hyperparameter Tuning

* Tuned Linear SVM parameters
* Improved model performance using cross-validation

## 7. Deployment

* Saved trained models using `.pkl` files
* Built frontend using Streamlit
* Deployed as a web application



# 🧠 How the System Works

1. User enters skills or uploads a resume
2. Resume text is processed
3. ML model predicts the career role
4. Skill matching logic calculates:

   * Match Score
   * Matched Skills
   * Skill Gap
5. System generates:

   * Top Career Matches
   * Action Plan
   * Related Job Roles



# ⚙️ Installation

## Clone the Repository


git clone <your-github-repo-link>

## Navigate to Project Folder

cd AI-Career-Advisor

## Install Dependencies

pip install -r requirements.txt

## Run the Application

streamlit run app.py

# 📷 Application Features

The application provides:

* Predicted Career Role
* Confidence Level
* Top Career Matches
* Match Score
* Matched Skills
* Skill Gap
* Personalized Action Plan
* Related Job Titles



# 🌐 Live Demo

🔗 https://career-recommendations-ng8nh55kurza6ewlsvipax.


# 🎥 Project Demo Video

🔗 https://www.linkedin.com/posts/navya-sri-mutthavarapu-1188a8287_machinelearning-datascience-ai-ugcPost-7453353170078146560-7tko?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEW4sKQBR0k7gyvr2MYYQ53QF0EJ3mJTkM)


# 📈 Future Enhancements

* Add more career domains
* Improve resume parsing
* Add course recommendations
* Integrate Generative AI guidance
* Add real-time job recommendations



# 👩‍💻 Author

**Navya Sri**



