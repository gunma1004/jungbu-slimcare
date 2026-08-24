# -*- coding: utf-8 -*-
import os
import datetime

# ==========================================
# 공식 도메인 설정
# ==========================================
BASE_URL = "https://jungbu-slimcare.shop"

today = datetime.date.today().isoformat()
url_list = []

# 사이트맵 탐색에서 제외할 폴더
EXCLUDE_DIRS = {".git", ".vscode", "assets", "css", "__pycache__"}

print("🚀 [중부 S슬림테라피] sitemap.xml 생성을 시작합니다...\n")

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    
    if "index.html" in files:
        rel_path = os.path.relpath(root, ".").replace("\\", "/")
        
        # 메인 페이지 (index.html)
        if rel_path == ".":
            loc = f"{BASE_URL}/"
            priority = "1.0"
            changefreq = "daily"
        # 하위 지역 페이지 (/daejeon/, /daejeon/yuseong/, /daejeon/yuseong/봉명동/ 등)
        else:
            loc = f"{BASE_URL}/{rel_path}/"
            depth = rel_path.count("/")
            priority = "0.8" if depth == 0 else ("0.7" if depth == 1 else "0.6")
            changefreq = "weekly"
        
        url_list.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

# sitemap.xml 조립
sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(url_list)}
</urlset>"""

# UTF-8 파일로 저장
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"✅ 완료! {BASE_URL} 기준 총 {len(url_list)}개의 URL이 sitemap.xml로 정상 생성되었습니다.")