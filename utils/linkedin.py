# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# def get_username(linkedin_url):
#     return linkedin_url.split("/in/")[1].split("/")[0]

# def fetch_linkedin_data(linkedin_url): #to fetch linkedin data using link of profile
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     driver.get("https://www.linkedin.com/login")
#     print("👉 Login manually...")
#     time.sleep(20)

#     driver.get(linkedin_url)
#     time.sleep(5)

#     # scroll content till end
#     for i in range(5):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)

#     # Extracting all text from page
#     full_text = driver.find_element(By.TAG_NAME, "body").text

#     username = get_username(linkedin_url)
#     activity_url = f"https://www.linkedin.com/in/{username}/recent-activity/all/"
#     driver.get(activity_url)
#     time.sleep(5)

#     for i in range(5):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(3)

#     posts = []

#     post_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'feed-shared-update-v2')]")

#     for post in post_elements[:5]:
#         try:
#             text = post.text
#             posts.append(text)
#         except:
#             continue

#     comments = []
#     try:
#         comment_elements = driver.find_elements(
#             By.XPATH,
#             "//span[contains(@class,'comments-comment-item')]"
#         )
#         for c in comment_elements[:5]:
#             text = c.text.strip()
#             if text:
#                 comments.append(text)
#     except:
#         pass

    
#     driver.quit()

#     return {
#         "raw_text": full_text,
#         "posts": posts,
#         "comments": comments
#     }


# def format_profile(profile):
#     text = profile["raw_text"]

#     # ADD POSTS
#     if profile["posts"]:
#         text += "\n\n=== POSTS ===\n"
#         for p in profile["posts"]:
#             text += f"\n- {p}"

#     # ADD COMMENTS
#     if profile["comments"]:
#         text += "\n\n=== COMMENTS ===\n"
#         for c in profile["comments"]:
#             text += f"\n- {c}"

#     return text

# -------------------------------


# //testing - Not stable
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service


# def get_username(url):
#     return url.split("/in/")[1].split("/")[0]


# def scroll_page(driver, times=5):
#     for _ in range(times):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)


# def fetch_linkedin_data(linkedin_url):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")

#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )

#     # 🔐 LOGIN
#     driver.get("https://www.linkedin.com/login")
#     print("👉 Login manually...")
#     time.sleep(20)

#     username = get_username(linkedin_url)

#     # =====================
#     # 🔹 PROFILE DATA
#     # =====================
#     driver.get(linkedin_url)
#     time.sleep(5)
#     scroll_page(driver, 3)

#     profile_text = driver.find_element(By.TAG_NAME, "body").text

#     # =====================
#     # 🔹 POSTS
#     # =====================
#     posts = []
#     driver.get(f"https://www.linkedin.com/in/{username}/recent-activity/posts/")
#     time.sleep(5)
#     scroll_page(driver, 5)

#     post_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'feed-shared-update-v2')]")

#     for post in post_elements[:5]:
#         try:
#             text = post.text.strip()
#             if text:
#                 posts.append(text)
#         except:
#             continue

#     # =====================
#     # 🔹 COMMENTS MADE BY USER
#     # =====================
#     comments_made = []
#     driver.get(f"https://www.linkedin.com/in/{username}/recent-activity/comments/")
#     time.sleep(5)
#     scroll_page(driver, 5)

#     comment_elements = driver.find_elements(By.XPATH, "//span[contains(@class,'comments-comment-item')]")

#     for c in comment_elements[:5]:
#         try:
#             txt = c.text.strip()
#             if txt:
#                 comments_made.append(txt)
#         except:
#             continue

#     # =====================
#     # 🔹 REACTIONS
#     # =====================
#     reactions = []
#     driver.get(f"https://www.linkedin.com/in/{username}/recent-activity/reactions/")
#     time.sleep(5)
#     scroll_page(driver, 5)

#     reaction_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'feed-shared-update-v2')]")

#     for r in reaction_elements[:5]:
#         try:
#             txt = r.text.strip()
#             if txt:
#                 reactions.append(txt)
#         except:
#             continue

#     # =====================
#     # 🔹 COMMENTS ON POSTS (IMPORTANT 🔥)
#     # =====================
#     post_comments = []

#     for post in post_elements[:3]:  # open few posts
#         try:
#             post.click()
#             time.sleep(3)

#             # scroll comments
#             scroll_page(driver, 2)

#             comment_items = driver.find_elements(
#                 By.XPATH,
#                 "//span[contains(@class,'comments-comment-item__main-content')]"
#             )

#             for cm in comment_items[:3]:
#                 txt = cm.text.strip()
#                 if txt:
#                     post_comments.append(txt)

#             driver.back()
#             time.sleep(3)

#         except:
#             continue

#     driver.quit()

#     return {
#         "profile": profile_text,
#         "posts": posts,
#         "comments_made": comments_made,
#         "reactions": reactions,
#         "post_comments": post_comments
#     }


# def format_profile(data):
#     text = data["profile"]

#     if data["posts"]:
#         text += "\n\n=== POSTS ===\n"
#         for p in data["posts"]:
#             text += f"\n- {p}"

#     if data["comments_made"]:
#         text += "\n\n=== COMMENTS MADE ===\n"
#         for c in data["comments_made"]:
#             text += f"\n- {c}"

#     if data["reactions"]:
#         text += "\n\n=== REACTIONS ===\n"
#         for r in data["reactions"]:
#             text += f"\n- {r}"

#     if data["post_comments"]:
#         text += "\n\n=== COMMENTS ON POSTS ===\n"
#         for pc in data["post_comments"]:
#             text += f"\n- {pc}"

#     return text

# -------------------------
# ANOTHER TESTING - ALSO NOT STABLE
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service


# def get_username(url):
#     return url.split("/in/")[1].split("/")[0]


# def scroll_page(driver, times=5):
#     for _ in range(times):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)


# def fetch_linkedin_data(linkedin_url):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")

#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )

#     # 🔐 LOGIN
#     driver.get("https://www.linkedin.com/login")
#     print("👉 Login manually...")
#     time.sleep(20)

#     username = get_username(linkedin_url)

#     # =====================
#     # 🔹 PROFILE
#     # =====================
#     driver.get(linkedin_url)
#     time.sleep(5)
#     scroll_page(driver, 3)

#     profile_text = driver.find_element(By.TAG_NAME, "body").text

#     # =====================
#     # 🔹 POSTS
#     # =====================
#     posts = []
#     driver.get(f"https://www.linkedin.com/in/{username}/recent-activity/posts/")
#     time.sleep(5)
#     scroll_page(driver, 5)

#     post_elements = driver.find_elements(By.TAG_NAME, "article")

#     for post in post_elements[:5]:
#         try:
#             text = post.text.strip()
#             if len(text) > 80:
#                 posts.append(text[:500])
#         except:
#             continue

#     # =====================
#     # 🔹 COMMENTS MADE BY USER
#     # =====================
#     comments_made = []
#     driver.get(f"https://www.linkedin.com/in/{username}/recent-activity/comments/")
#     time.sleep(5)
#     scroll_page(driver, 5)

#     comment_elements = driver.find_elements(By.TAG_NAME, "article")

#     for c in comment_elements[:5]:
#         try:
#             txt = c.text.strip()
#             if len(txt) > 50:
#                 comments_made.append(txt[:300])
#         except:
#             continue

#     # =====================
#     # 🔹 COMMENTS ON POSTS
#     # =====================
#     post_comments = []

#     driver.get(f"https://www.linkedin.com/in/{username}/recent-activity/posts/")
#     time.sleep(5)
#     scroll_page(driver, 3)

#     post_elements = driver.find_elements(By.TAG_NAME, "article")

#     for post in post_elements[:3]:
#         try:
#             # try expanding comments
#             buttons = post.find_elements(By.XPATH, ".//button")

#             for b in buttons:
#                 if "comment" in b.text.lower():
#                     try:
#                         b.click()
#                         time.sleep(2)
#                         break
#                     except:
#                         continue

#             # extract comments text inside post
#             comment_texts = post.find_elements(By.XPATH, ".//span")

#             for ct in comment_texts[:5]:
#                 txt = ct.text.strip()
#                 if len(txt) > 30:
#                     post_comments.append(txt)

#         except:
#             continue

#     driver.quit()

#     return {
#         "profile": profile_text,
#         "posts": posts,
#         "comments_made": comments_made,
#         "post_comments": post_comments
#     }


# def format_profile(data):
#     text = data["profile"]

#     if data["posts"]:
#         text += "\n\n=== LINKEDIN POSTS (CONTENT CREATED BY USER) ===\n"
#         for p in data["posts"]:
#             text += f"\n- {p}"

#     if data["comments_made"]:
#         text += "\n\n=== COMMENTS MADE BY USER ===\n"
#         for c in data["comments_made"]:
#             text += f"\n- {c}"

#     if data["post_comments"]:
#         text += "\n\n=== COMMENTS ON USER POSTS ===\n"
#         for pc in data["post_comments"]:
#             text += f"\n- {pc}"

#     return text
# --------------------------

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service


# def get_username(url):
#     return url.split("/in/")[1].split("/")[0]


# def scroll_page(driver, times=6):
#     for _ in range(times):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(3)


# # 🔥 EXTRACT POSTS FROM /all/
# def extract_posts_from_all(driver, username):
#     url = f"https://www.linkedin.com/in/{username}/recent-activity/all/"
#     driver.get(url)
#     time.sleep(5)

#     scroll_page(driver, 6)

#     posts = []

#     elements = driver.find_elements(
#         By.XPATH,
#         "//div[contains(@class,'update-components-text')]"
#     )

#     print("🔍 Activity blocks:", len(elements))

#     for el in elements[:12]:
#         try:
#             text = el.text.strip()
#             lower = text.lower()

#             if len(text) < 30:
#                 continue

#             # ❗ FILTER OUT COMMENTS
#             if "commented on" in lower or "replied" in lower:
#                 continue

#             posts.append(text[:400])

#         except:
#             continue

#     return posts


# # 🔥 EXTRACT COMMENTS (CLEAN SOURCE)
# def extract_comments(driver, username):
#     url = f"https://www.linkedin.com/in/{username}/recent-activity/comments/"
#     driver.get(url)
#     time.sleep(5)

#     scroll_page(driver, 5)

#     comments = []

#     elements = driver.find_elements(
#         By.XPATH,
#         "//span[contains(@class,'comments-comment-item__main-content')]"
#     )

#     print("🔍 Comments found:", len(elements))

#     for el in elements[:12]:
#         try:
#             txt = el.text.strip()

#             if len(txt) > 10:
#                 comments.append(txt[:300])
#         except:
#             continue

#     return comments


# def fetch_linkedin_data(linkedin_url):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")

#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )

#     # LOGIN
#     driver.get("https://www.linkedin.com/login")
#     print("👉 Login manually...")
#     time.sleep(20)

#     username = get_username(linkedin_url)

#     # PROFILE
#     driver.get(linkedin_url)
#     time.sleep(5)
#     scroll_page(driver, 3)

#     try:
#         profile_text = driver.find_element(By.TAG_NAME, "body").text
#     except:
#         profile_text = ""

#     # 🔥 DATA EXTRACTION
#     posts = extract_posts_from_all(driver, username)
#     comments = extract_comments(driver, username)

#     driver.quit()

#     return {
#         "profile": profile_text,
#         "posts": posts,
#         "comments_made": comments
#     }


# def format_profile(data):
#     text = data["profile"]

#     if data["posts"]:
#         text += "\n\n=== LINKEDIN POSTS (ORIGINAL CONTENT) ===\n"
#         for p in data["posts"]:
#             text += f"\n- {p}"
#     else:
#         text += "\n\n=== LINKEDIN POSTS ===\nNo recent posts found."

#     if data["comments_made"]:
#         text += "\n\n=== COMMENTS MADE BY USER ===\n"
#         for c in data["comments_made"]:
#             text += f"\n- {c}"

#     return text

# --------------------------

# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service


# # 🔹 Extract username
# def get_username(url):
#     return url.split("/in/")[1].split("/")[0]


# # # 🔥 SMART SCROLL (DOWN → UP → DOWN)
# # def smart_scroll(driver):
# #     # 🔽 scroll down
# #     for _ in range(5):
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(random.uniform(1.5, 2.5))

# #     # 🔼 scroll up
# #     for _ in range(3):
# #         driver.execute_script("window.scrollTo(0, 0);")
# #         time.sleep(random.uniform(1.5, 2.5))

# #     # 🔽 scroll down again
# #     for _ in range(5):
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(random.uniform(1.5, 2.5))

# #sunday try 1ST
# # def smart_scroll(driver):
# #     # down
# #     for _ in range(4):
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(random.uniform(1.5, 2.5))

# #     # up
# #     for _ in range(2):
# #         driver.execute_script("window.scrollTo(0, 0);")
# #         time.sleep(random.uniform(1.5, 2.5))

# #     # down again
# #     for _ in range(4):
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(random.uniform(1.5, 2.5))

# # def smart_scroll(driver, max_scrolls=15):
# #     last_height = driver.execute_script("return document.body.scrollHeight")

# #     for i in range(max_scrolls):
# #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# #         time.sleep(2)

# #         new_height = driver.execute_script("return document.body.scrollHeight")

# #         print(f"Scroll {i+1}: height {new_height}")

# #         if new_height == last_height:
# #             print("✅ No more content loading")
# #             break

# #         last_height = new_height

# #     # 🔼 optional small scroll up
# #     driver.execute_script("window.scrollTo(0, 0);")
# def human_scroll(driver):
#     import random

#     total_height = driver.execute_script("return document.body.scrollHeight")
#     current_position = 0

#     while current_position < total_height:
#         scroll_step = random.randint(300, 700)

#         driver.execute_script(f"window.scrollBy(0, {scroll_step});")
#         current_position += scroll_step

#         time.sleep(random.uniform(0.8, 1.5))

#         total_height = driver.execute_script("return document.body.scrollHeight")
#     time.sleep(2)

# # 🔥 EXTRACT POSTS FROM /all/
# def extract_posts_from_all(driver, username):
#     url = f"https://www.linkedin.com/in/{username}/recent-activity/all/"
#     driver.get(url)
#     time.sleep(5)

#     smart_scroll(driver)

#     posts = []

#     elements = driver.find_elements(
#         By.XPATH,
#         "//div[contains(@class,'update-components-text')]"
#     )

#     print("🔍 Found activity blocks:", len(elements))

#     for el in elements[:20]:  # increased window
#         try:
#             text = el.text.strip()
#             lower = text.lower()

#             if len(text) < 30:
#                 continue

#             # ❗ FILTER OUT COMMENTS
#             if "commented on" in lower or "replied" in lower:
#                 continue

#             posts.append(text[:400])

#         except:
#             continue

#     return posts


# # 🔥 EXTRACT COMMENTS (CLEAN SOURCE)
# def extract_comments(driver, username):
#     url = f"https://www.linkedin.com/in/{username}/recent-activity/comments/"
#     driver.get(url)
#     time.sleep(5)

#     smart_scroll(driver)

#     comments = []

#     elements = driver.find_elements(
#         By.XPATH,
#         "//span[contains(@class,'comments-comment-item__main-content')]"
#     )

#     print("🔍 Found comments:", len(elements))

#     for el in elements[:20]:
#         try:
#             txt = el.text.strip()

#             if len(txt) > 10:
#                 comments.append(txt[:300])
#         except:
#             continue

#     return comments


# # 🔹 MAIN FUNCTION
# def fetch_linkedin_data(linkedin_url):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")

#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )

#     # 🔐 LOGIN
#     driver.get("https://www.linkedin.com/login")
#     print("👉 Login manually...")
#     time.sleep(20)

#     username = get_username(linkedin_url)

#     # =====================
#     # 🔹 PROFILE
#     # =====================
#     driver.get(linkedin_url)
#     time.sleep(5)
#     smart_scroll(driver)

#     try:
#         profile_text = driver.find_element(By.TAG_NAME, "body").text
#     except:
#         profile_text = ""

#     # =====================
#     # 🔹 POSTS (FROM /all/)
#     # =====================
#     posts = extract_posts_from_all(driver, username)

#     # =====================
#     # 🔹 COMMENTS
#     # =====================
#     comments = extract_comments(driver, username)

#     driver.quit()

#     return {
#         "profile": profile_text,
#         "posts": posts,
#         "comments_made": comments
#     }


# # 🔹 FORMAT FOR RAG
# def format_profile(data):
#     text = data["profile"]

#     if data["posts"]:
#         text += "\n\n=== LINKEDIN POSTS (ORIGINAL CONTENT) ===\n"
#         for p in data["posts"]:
#             text += f"\n- {p}"
#     else:
#         text += "\n\n=== LINKEDIN POSTS ===\nNo recent posts found."

#     if data["comments_made"]:
#         text += "\n\n=== COMMENTS MADE BY USER ===\n"
#         for c in data["comments_made"]:
#             text += f"\n- {c}"

#     return text

# ------------------------

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# 🔹 Extract username
def get_username(url):
    return url.split("/in/")[1].split("/")[0]

def balanced_scroll(driver):
    import random
    import time

    # 🔽 FIRST PASS (main load)
    for _ in range(10):
        driver.execute_script(f"window.scrollBy(0, {random.randint(400,700)});")
        time.sleep(random.uniform(0.5, 0.9))

    # 🔼 SMALL RESET
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # 🔽 SECOND PASS (capture missed content)
    for _ in range(6):
        driver.execute_script(f"window.scrollBy(0, {random.randint(500,800)});")
        time.sleep(random.uniform(0.5, 0.9))

    # 🔽 FINAL SNAP
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# 🔥 EXTRACT POSTS FROM /all/
def extract_posts_from_all(driver, username):
    url = f"https://www.linkedin.com/in/{username}/recent-activity/all/"
    driver.get(url)
    time.sleep(5)

    # 🔥 USE HUMAN SCROLL
    balanced_scroll(driver)

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

            # ❗ FILTER OUT COMMENTS
            if "commented on" in lower or "replied" in lower:
                continue

            posts.append(text[:400])

        except:
            continue

    return posts


# 🔥 EXTRACT COMMENTS
def extract_comments(driver, username):
    url = f"https://www.linkedin.com/in/{username}/recent-activity/comments/"
    driver.get(url)
    time.sleep(5)

    # 🔥 HUMAN SCROLL
    balanced_scroll(driver)

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


# 🔹 MAIN FUNCTION
def fetch_linkedin_data(linkedin_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # 🔐 LOGIN
    driver.get("https://www.linkedin.com/login")
    print("👉 Login manually...")
    time.sleep(20)

    username = get_username(linkedin_url)

    # =====================
    # 🔹 PROFILE
    # =====================
    driver.get(linkedin_url)
    time.sleep(5)

    balanced_scroll(driver)

    try:
        profile_text = driver.find_element(By.TAG_NAME, "body").text
    except:
        profile_text = ""

    # =====================
    # 🔹 POSTS
    # =====================
    posts = extract_posts_from_all(driver, username)

    # =====================
    # 🔹 COMMENTS
    # =====================
    comments = extract_comments(driver, username)

    driver.quit()

    return {
        "profile": profile_text,
        "posts": posts,
        "comments_made": comments
    }


# 🔹 FORMAT FOR RAG
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