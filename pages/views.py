from django.shortcuts import render


# 📌 首頁 View
def home(request):
    """
    首頁 View
    對應 templates/pages/home.html
    """
    # 成員基本資料（可改為 Model 資料庫存取）
    members = [
        {"name": "張小誌(老大)", "name_en": "Kevin Chang", "id": "p1", "img": "images/p1.jpg"},
        {"name": "王小程", "name_en": "Jason Wang", "id": "p2", "img": "images/p2.jpg"},
        {"name": "張大同", "name_en": "Tony Chang", "id": "p3", "img": "images/p3.jpg"},
        {"name": "林依依", "name_en": "Ivy Lin", "id": "p4", "img": "images/p4.jpg"},
        {"name": "陳阿華", "name_en": "Howard Chen", "id": "p5", "img": "images/p5.jpg"},
        {"name": "黃志強", "name_en": "Jimmy Huang", "id": "p6", "img": "images/p6.jpg"},
    ]
    return render(request, 'pages/home.html', {"members": members})


# 📌 關於我 View
def about(request):
    """
    關於我 View
    對應 templates/pages/about.html
    """
    intro = {
        "title": "關於我們 | About Us",
        "desc_zh": "我們是一群熱愛科技、設計與創意的夥伴，致力於打造兼具美感與實用性的網站。",
        "desc_en": "We are a team passionate about technology, design, and creativity. Our goal is to build websites that combine aesthetics with functionality.",
        "mission_zh": "使命：用技術與創意，讓更多人感受到數位生活的便利與溫度。",
        "mission_en": "Mission: To bring convenience and warmth to digital life through technology and creativity."
    }
    return render(request, 'pages/about.html', {"intro": intro})


# 📌 聯絡我 View
def contact(request):
    """
    聯絡我 View
    對應 templates/pages/contact.html
    """
    contact_info = {
        "email": "info@team5site.com",
        "phone": "+886-2-1234-5678",
        "address": "台北市信義區松智路100號",
        "socials": {
            "facebook": "https://facebook.com/team5site",
            "instagram": "https://instagram.com/team5site",
            "linkedin": "https://linkedin.com/company/team5site"
        },
        "desc_zh": "歡迎透過以下方式聯絡我們，無論是合作提案、問題回饋或單純打聲招呼都可以！",
        "desc_en": "Feel free to reach out for collaborations, questions, or just to say hi!"
    }
    return render(request, 'pages/contact.html', {"contact_info": contact_info})


# 📌 成員個人介紹頁面
def member_detail(request, member_id):
    """
    成員詳細介紹頁
    例如：http://127.0.0.1:8000/member/p1/
    """
    member_profiles = {
        "p1": {
            "name": "張小誌",
            "name_en": "Kevin Chang",
            "img": "images/p1.jpg",
            "intro_zh": "大家好，我是張小誌，喜歡銅線搬電線，幫電線去皮...賣錢。",
            "intro_en": "Hi everyone, I’m Kevin Chang. I enjoy collecting and stripping copper wires — and selling them for cash.",
            "skills": ["電機設計", "Python", "籃球策略分析"]
        },
        "p2": {
            "name": "王小程",
            "name_en": "Jason Wang",
            "img": "images/p2.jpg",
            "intro_zh": "嗨～我是王小程，喜歡閱讀、看電影，目前是張小誌的徒弟。",
            "intro_en": "Hi, I'm Wang Xiaocheng. I enjoy reading and watching movies, and I am currently an apprentice to Zhang Xiaozhi.",
            "skills": ["前端設計", "JavaScript", "UI/UX"]
        },
        "p3": {
            "name": "張大同",
            "name_en": "Tony Chang",
            "img": "images/p3.jpg",
            "intro_zh": "我是張大同，對 AI 與資料分析充滿熱情，期望用數據創造價值。",
            "intro_en": "I'm Tony Chang, passionate about AI and data analytics, aiming to create value through data-driven insights.",
            "skills": ["AI分析", "資料視覺化", "機器學習"]
        },
        "p4": {
            "name": "林依依",
            "name_en": "Ivy Lin",
            "img": "images/p4.jpg",
            "intro_zh": "大家好，我是林依依，喜歡攝影、設計與自然風景，專注於前端體驗設計。",
            "intro_en": "Hi, I'm Ivy Lin. I love photography, design, and nature — focusing on front-end user experience design.",
            "skills": ["前端設計", "攝影", "視覺美學"]
        },
        "p5": {
            "name": "陳阿華",
            "name_en": "Howard Chen",
            "img": "images/p5.jpg",
            "intro_zh": "哈囉～我是阿華，後端工程師一枚，也愛打電動與研究雲端架構。",
            "intro_en": "Hey there! I'm Howard Chen, a backend engineer who loves gaming and exploring cloud architecture.",
            "skills": ["後端開發", "Django", "雲端部署"]
        },
        "p6": {
            "name": "黃志強",
            "name_en": "Jimmy Huang",
            "img": "images/p6.jpg",
            "intro_zh": "嗨～我是志強，熱衷於新技術與創業挑戰，喜歡參加黑客松與社群活動。",
            "intro_en": "Hi! I'm Jimmy Huang, passionate about emerging tech and entrepreneurship, often joining hackathons and developer communities.",
            "skills": ["創業規劃", "Hackathon", "創新設計"]
        },
    }

    profile = member_profiles.get(member_id)
    if not profile:
        return render(request, 'pages/member_not_found.html', {"member_id": member_id})

    return render(request, 'pages/member_detail.html', {"profile": profile})
