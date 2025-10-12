from .models import SiteContent

def site_content(request):
    # 提供模板變數 sc（SiteContent 實例或 None）
    return {"sc": SiteContent.objects.first()}
