import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_username(url):
    return url.split("/in/")[1].split("/")[0]

def balanced_scroll(driver): #function for balaced scroll that fetches whole kb
    import random
    import time

    for _ in range(10):
        driver.execute_script(f"window.scrollBy(0, {random.randint(400,700)});")
        time.sleep(random.uniform(0.5, 0.9))

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    for _ in range(6):
        driver.execute_script(f"window.scrollBy(0, {random.randint(500,800)});")
        time.sleep(random.uniform(0.5, 0.9))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def extract_posts_from_all(driver, username):#extract posts
    url = f"https://www.linkedin.com/in/{username}/recent-activity/all/"
    driver.get(url)
    time.sleep(5)

    balanced_scroll(driver)#instance of scroll

    time.sleep(3)  # allow final render

    posts = []

    elements = driver.find_elements(
        By.XPATH,
        "//div[contains(@class,'update-components-text')]"
    )

    print("🔍 Found activity blocks:", len(elements))

    for el in elements[:30]:  # bigger window
        try:
            text = el.text.strip()
            lower = text.lower()

            if len(text) < 30:
                continue

            # FILTER OUT COMMENTS
            if "commented on" in lower or "replied" in lower:
                continue

            posts.append(text[:400])

        except:
            continue

    return posts


def extract_comments(driver, username): #extract comments
    url = f"https://www.linkedin.com/in/{username}/recent-activity/comments/"
    driver.get(url)
    time.sleep(5)

    balanced_scroll(driver) #instance of scroll

    time.sleep(2)

    comments = []

    elements = driver.find_elements(
        By.XPATH,
        "//span[contains(@class,'comments-comment-item__main-content')]"
    )

    print("🔍 Found comments:", len(elements))

    for el in elements[:30]:
        try:
            txt = el.text.strip()

            if len(txt) > 10:
                comments.append(txt[:300])
        except:
            continue

    return comments

def fetch_linkedin_data(linkedin_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://www.linkedin.com/login")
    print("👉 Login manually...")
    time.sleep(20)

    username = get_username(linkedin_url)
    
    driver.get(linkedin_url)
    time.sleep(5)

    balanced_scroll(driver)

    try:
        profile_text = driver.find_element(By.TAG_NAME, "body").text
    except:
        profile_text = ""

    posts = extract_posts_from_all(driver, username)

    comments = extract_comments(driver, username)

    driver.quit()

    return {
        "profile": profile_text,
        "posts": posts,
        "comments_made": comments
    }

def format_profile(data):
    text = data["profile"]

    if data["posts"]:
        text += "\n\n=== LINKEDIN POSTS (ORIGINAL CONTENT) ===\n"
        for p in data["posts"]:
            text += f"\n- {p}"
    else:
        text += "\n\n=== LINKEDIN POSTS ===\nNo recent posts found."

    if data["comments_made"]:
        text += "\n\n=== COMMENTS MADE BY USER ===\n"
        for c in data["comments_made"]:
            text += f"\n- {c}"

    return text
