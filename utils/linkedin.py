# import requests

# API_KEY = "YOUR_PROXYCURL_KEY"

# def fetch_linkedin_data(linkedin_url):
#     url = "https://nubela.co/proxycurl/api/v2/linkedin"

#     headers = {
#         "Authorization": f"Bearer {API_KEY}"
#     }

#     params = {"url": linkedin_url}

#     res = requests.get(url, headers=headers, params=params)

#     if res.status_code != 200:
#         return None

#     data = res.json()

#     return {
#         "name": data.get("full_name"),
#         "headline": data.get("headline"),
#         "experience": data.get("experiences", []),
#         "education": data.get("education", []),
#         "skills": data.get("skills", [])
#     }


# def format_profile(profile):
#     text = f"""
#     Name: {profile['name']}
#     Headline: {profile['headline']}
#     """

#     for exp in profile['experience']:
#         text += f"\n{exp.get('title')} at {exp.get('company')}"

#     for edu in profile['education']:
#         text += f"\n{edu.get('school')} - {edu.get('degree')}"

#     text += "\nSkills: " + ", ".join(profile['skills'])

#     return text

import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BRIGHTDATA_API_KEY")
ZONE = os.getenv("BRIGHTDATA_ZONE")

def fetch_linkedin_data(linkedin_url):
    url = "https://api.brightdata.com/request"

    payload = {
        "zone": ZONE,  # from Bright Data dashboard
        "url": linkedin_url,
        "format": "json"
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        res = requests.post(url, headers=headers, json=payload)

        if res.status_code != 200:
            print("Error:", res.text)
            return fallback_data()

        data = res.json()

        return parse_linkedin_data(data)

    except Exception as e:
        print("Exception:", e)
        return fallback_data()


def parse_linkedin_data(data):
    # This depends on Bright Data response format
    # Adjust fields as needed

    return {
        "name": data.get("name", "Unknown"),
        "headline": data.get("headline", ""),
        "experience": data.get("experience", []),
        "education": data.get("education", []),
        "skills": data.get("skills", [])
    }


def fallback_data():
    return {
        "name": "Demo User",
        "headline": "AI Developer",
        "experience": [
            {"title": "Engineer", "company": "ABC"},
        ],
        "education": [
            {"school": "Your College", "degree": "BTech"}
        ],
        "skills": ["Python", "Flask"]
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