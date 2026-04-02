import re
from role_data import job_roles


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def normalize_skill(skill):
    return skill.lower().replace(".", " ").replace("-", " ").strip()


def calculate_skill_score(role, user_input):
    if role not in job_roles:
        return 0, []

    required = job_roles[role]["skills_required"]

    text = clean_text(user_input)
    words = set(text.split())

    matched = []
    score_count = 0

    for skill in required:
        norm = normalize_skill(skill)
        tokens = norm.split()

        if norm in text:
            matched.append(skill)
            score_count += 1

        elif any(token in words for token in tokens):
            matched.append(skill)
            score_count += 0.5

        elif norm.replace(" ", "") in text.replace(" ", ""):
            matched.append(skill)
            score_count += 1

    total = len(required)
    score = (score_count / total) * 100 if total else 0

    return round(min(score, 100), 2), list(set(matched))


def get_skill_gap(role, user_input):
    if role not in job_roles:
        return [], []

    required = job_roles[role]["skills_required"]

    text = clean_text(user_input)
    words = set(text.split())

    missing = []

    for skill in required:
        norm = normalize_skill(skill)
        tokens = norm.split()

        if (
            norm in text
            or any(token in words for token in tokens)
            or norm.replace(" ", "") in text.replace(" ", "")
        ):
            continue
        else:
            missing.append(skill)

    return required, missing