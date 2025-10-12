from django.db import models

class SiteContent(models.Model):
    home_headline = models.CharField("首頁歡迎頭條", max_length=120, default="歡迎來到我的網站！")
    about_text = models.TextField("關於－簡短簡介", default="這裡放你的簡介、背景與興趣。")
    contact_email = models.EmailField("聯繫 Email", blank=True, null=True)
    social_x = models.URLField("X / Twitter", blank=True)
    social_ig = models.URLField("Instagram", blank=True)
    social_fb = models.URLField("Facebook", blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "網站內容設定"
        verbose_name_plural = "網站內容設定"

    def __str__(self):
        return "網站內容（請只保留一筆）"
