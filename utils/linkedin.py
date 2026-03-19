import requests

API_KEY = "YOUR_PROXYCURL_KEY"

def fetch_linkedin_data(linkedin_url):
    url = "https://nubela.co/proxycurl/api/v2/linkedin"

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {"url": linkedin_url}

    res = requests.get(url, headers=headers, params=params)

    if res.status_code != 200:
        return None

    data = res.json()

    return {
        "name": data.get("full_name"),
        "headline": data.get("headline"),
        "experience": data.get("experiences", []),
        "education": data.get("education", []),
        "skills": data.get("skills", [])
    }


def format_profile(profile):
    text = f"""
    Name: {profile['name']}
    Headline: {profile['headline']}
    """

    for exp in profile['experience']:
        text += f"\n{exp.get('title')} at {exp.get('company')}"

    for edu in profile['education']:
        text += f"\n{edu.get('school')} - {edu.get('degree')}"

    text += "\nSkills: " + ", ".join(profile['skills'])

    return text