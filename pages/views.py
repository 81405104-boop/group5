from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                subject=f"[聯繫表單] {cd['name']}",
                message=f"來自：{cd['name']} <{cd['email']}>\n\n{cd['message']}",
                from_email=None,
                recipient_list=["owner@example.com"],
            )
            messages.success(request, "已送出！我會盡快回覆你。")
            return redirect("contact")
        else:
            messages.error(request, "請確認表單內容是否正確。")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

# ====== 6 個卡片內頁資料（先放示例，可自行修改）======
CARDS = [
    {
        "title_zh": "自我介紹",
        "title_en": "Self Introduction",
        "image": "images/p1.jpg",
        "body_zh": "嗨！我們是第五組。我擅長 Python、Django 與前端基礎，喜歡拍照與記錄學習。",
        "body_en": "Hi! We are Group 5. I focus on Python/Django and front-end basics, and I love photography and learning.",
    },
    {
        "title_zh": "我的興趣",
        "title_en": "My Interests",
        "image": "images/p2.jpg",
        "body_zh": "運動、音樂與旅行。透過興趣拓展觀點與靈感。",
        "body_en": "Sports, music, and travel. Hobbies broaden perspectives and inspire creativity.",
    },
    {
        "title_zh": "學習成果",
        "title_en": "Learning Projects",
        "image": "images/p3.jpg",
        "body_zh": "近期完成幾個 Django 小專題，練習模板、表單與部署。",
        "body_en": "Recently built small Django projects to practice templates, forms, and deployment.",
    },
    {
        "title_zh": "照片作品",
        "title_en": "Photo Works",
        "image": "images/p4.jpg",
        "body_zh": "挑選幾張喜歡的作品，記錄生活與城市。",
        "body_en": "A small selection of photos capturing daily life and the city.",
    },
    {
        "title_zh": "團隊分工",
        "title_en": "Team Roles",
        "image": "images/p5.jpg",
        "body_zh": "我主要負責後端與部署，夥伴負責設計與前端。",
        "body_en": "I focus on backend and deployment; teammates handle design and front-end.",
    },
    {
        "title_zh": "聯絡方式",
        "title_en": "Get in Touch",
        "image": "images/p6.jpg",
        "body_zh": "想合作或交流，歡迎到聯繫頁面留言或寫 Email。",
        "body_en": "For collaboration or questions, visit the Contact page or send an email.",
    },
]

def card(request, n: int):
    # n 介於 1~6，超出時顯示 404 模板
    if n < 1 or n > len(CARDS):
        return render(request, "404.html", status=404)
    item = CARDS[n-1]
    return render(request, "card.html", {"item": item, "n": n})
