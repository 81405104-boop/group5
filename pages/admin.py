from django.contrib import admin
from .models import SiteContent

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ("home_headline", "contact_email", "updated_at")
    fieldsets = (
        ("首頁", {"fields": ("home_headline",)}),
        ("關於", {"fields": ("about_text",)}),
        ("聯繫", {"fields": ("contact_email","social_x","social_ig","social_fb")}),
    )

    def has_add_permission(self, request):
        # 限制只允許存在一筆設定
        if SiteContent.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
