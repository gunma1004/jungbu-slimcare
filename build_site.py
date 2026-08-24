# -*- coding: utf-8 -*-
import os
import datetime

print("🚀 [중부 S슬림테라피] 하위 지역 페이지 및 사이트맵 자동 생성을 시작합니다...\n")

sub_template = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>{{PAGE_TITLE}}</title>
  <meta name="description" content="{{PAGE_DESC}}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://jungbu-slimcare.shop/{{region_path}}/">
  <meta name="theme-color" content="#08151f">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="중부 S슬림테라피">
  <meta property="og:title" content="{{PAGE_TITLE}}">
  <meta property="og:description" content="{{current_region}} 전지역 100% 후불제 안심 방문 힐링 케어.">
  <meta property="og:url" content="https://jungbu-slimcare.shop/{{region_path}}/">
  <meta property="og:image" content="https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80">
  <style>
    :root {
      --bg-main: #08151f; --bg-card: #0e2333; --text-main: #f0f4f8; --text-sub: #94a3b8;
      --accent: #ff7a18; --accent-gradient: linear-gradient(135deg, #ff7a18, #af002d);
      --border-color: rgba(255, 255, 255, 0.08); --max-w: 1100px;
      font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background-color: var(--bg-main); color: var(--text-main); line-height: 1.6; padding-bottom: 100px; }
    a { color: inherit; text-decoration: none; }
    .site-header { position: sticky; top: 0; display: flex; justify-content: space-between; align-items: center; padding: 16px 24px; background: rgba(8, 21, 31, 0.92); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border-color); z-index: 1000; }
    .brand { font-size: 1.15rem; font-weight: 800; }
    .breadcrumbs { max-width: var(--max-w); margin: 15px auto 0; padding: 0 20px; font-size: 0.85rem; color: var(--text-sub); }
    .breadcrumbs span { margin: 0 6px; }
    .section-shell { max-width: var(--max-w); margin: 0 auto; padding: 50px 20px; }
    .home-hero { max-width: var(--max-w); margin: 0 auto; padding: 40px 20px; display: grid; grid-template-columns: 1.2fr 0.8fr; align-items: center; gap: 30px; }
    .home-hero h1 { font-size: 2.2rem; line-height: 1.3; margin-bottom: 16px; font-weight: 800; }
    .home-hero h1 em { font-style: normal; background: var(--accent-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .hero-lead { color: var(--text-sub); font-size: 1.05rem; margin-bottom: 25px; }
    .hero-media { background: var(--bg-card); border-radius: 16px; overflow: hidden; border: 1px solid var(--border-color); aspect-ratio: 4/3; }
    .hero-media img { width: 100%; height: 100%; object-fit: cover; }
    .button { display: inline-flex; padding: 12px 24px; border-radius: 8px; font-weight: 700; background: var(--accent-gradient); color: #fff; }
    .promo-banner { max-width: var(--max-w); margin: 20px auto; padding: 0 20px; }
    .promo-banner__inner { background: linear-gradient(135deg, #132f45, #0e2333); border: 1px solid rgba(255, 122, 24, 0.3); border-radius: 16px; padding: 24px; text-align: center; }
    .course-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 30px; }
    .course-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 24px; }
    .course-card h3 { font-size: 1.2rem; color: var(--accent); margin-bottom: 12px; }
    .course-card dl div { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .sub-nav-box { max-width: var(--max-w); margin: 20px auto; padding: 24px; background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); }
    .sub-nav-links { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px; }
    .sub-nav-links a { background: rgba(255, 255, 255, 0.05); padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; border: 1px solid var(--border-color); }
    .sub-nav-links a:hover { background: var(--accent-gradient); color: #fff; }
    .contact-dock { position: fixed; bottom: 16px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px; width: calc(100% - 32px); max-width: 440px; z-index: 9999; }
    .contact-dock a { flex: 1; display: flex; align-items: center; justify-content: center; height: 48px; border-radius: 999px; font-weight: 700; background: var(--accent-gradient); color: #fff; }
    @media (max-width: 768px) { .home-hero { grid-template-columns: 1fr; text-align: center; } }
  </style>
</head>
<body>
  <header class="site-header">
    <a class="brand" href="/">중부 S슬림테라피</a>
    <a class="button" href="tel:0507-1280-3358" style="padding:6px 16px; font-size:0.9rem;">전화상담</a>
  </header>
  <div class="breadcrumbs">{{BREADCRUMBS}}</div>
  <main>
    <section class="home-hero">
      <div>
        <h1><span>{{current_region}} 하루의 끝을</span><br><span><em>내 방, 내 공간에서</em></span></h1>
        <p class="hero-lead">{{HERO_DESC}}</p>
        <a class="button" href="tel:0507-1280-3358">0507-1280-3358 전화 예약</a>
      </div>
      <div class="hero-media">
        <img src="https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1000&q=80" alt="{{current_region}} 배너">
      </div>
    </section>
    <div class="sub-nav-box">
      <h3>{{SUB_NAV_TITLE}}</h3>
      <div class="sub-nav-links">{{SUB_NAV_LINKS}}</div>
    </div>
    <section class="promo-banner">
      <div class="promo-banner__inner">
        <h3>중부 S슬림테라피 {{current_region}} 100% 후불제 안심 케어</h3>
        <p>선입금·예약금 전혀 없습니다! 테라피스트 도착 후 안심 결제하세요.</p>
      </div>
    </section>
    <section class="section-shell">
      <h2>코스 및 이용 요금</h2>
      <div class="course-grid">
        <article class="course-card">
          <h3>🔮 개운한 꾹꾹 건식</h3>
          <dl><div><dt>60분</dt><dd>50,000원</dd></div><div><dt>90분</dt><dd>70,000원</dd></div><div><dt>120분</dt><dd>80,000원</dd></div></dl>
        </article>
        <article class="course-card">
          <h3>🔮 촉촉한 아로마</h3>
          <dl><div><dt>60분</dt><dd>60,000원</dd></div><div><dt>90분</dt><dd>80,000원</dd></div><div><dt>120분</dt><dd>90,000원</dd></div></dl>
        </article>
        <article class="course-card" style="border-color: rgba(255, 122, 24, 0.4);">
          <h3>🔮 스페셜 코스</h3>
          <dl><div><dt>120분 (타이+아로마)</dt><dd>90,000원</dd></div><div><dt>150분 (타이+아로마+발)</dt><dd>120,000원</dd></div><div><dt>180분 (타이+아로마+발)</dt><dd>150,000원</dd></div></dl>
        </article>
        <article class="course-card">
          <h3>🔮 힐링 코스</h3>
          <dl><div><dt>60분</dt><dd>90,000원</dd></div><div><dt>90분</dt><dd>100,000원</dd></div><div><dt>120분</dt><dd>120,000원</dd></div></dl>
        </article>
        <article class="course-card" style="border-color: rgba(255, 122, 24, 0.4);">
          <h3>🔮 VIP 스웨디시</h3>
          <dl><div><dt>60분</dt><dd>100,000원</dd></div><div><dt>90분</dt><dd>120,000원</dd></div><div><dt>120분</dt><dd>150,000원</dd></div></dl>
        </article>
      </div>
    </section>
  </main>
  <aside class="contact-dock">
    <a href="tel:0507-1280-3358">📞 전화 상담</a>
    <a href="sms:0507-1280-3358" style="background:#132f45;">💬 문자 문의</a>
  </aside>
</body>
</html>"""

DESC_TEMPLATES = [
    "{loc} 전지역 24시간 출장마사지 전문 중부 S슬림테라피. 100% 후불제 안심 케어, 건식·아로마·스웨디시 25~35분 빠른 방문.",
    "{loc} 어디서나 편안하게 누리는 24시 프리미엄 출장마사지. 선입금·예약금 일체 없는 100% 후불제 시스템.",
    "{loc} 계신 곳으로 찾아가는 1:1 맞춤 출장마사지. 자택, 모텔, 호텔, 오피스텔 30분 내 도착 안심 테라피.",
    "{loc} 24시간 출장마사지 전문 S슬림테라피. 건식 지압, 아로마, VIP 스웨디시 1:1 맞춤 케어 코스.",
    "{loc} 전지역 빠른 방문 출장마사지. 지친 하루의 피로를 머무는 공간에서 100% 후불 결제로 시원하게 풀어드립니다."
]

desc_idx = 0
def get_next_desc(loc_name):
    global desc_idx
    template = DESC_TEMPLATES[desc_idx % len(DESC_TEMPLATES)]
    desc_idx += 1
    return template.format(loc=loc_name)

regions_data = {
    "daejeon": {
        "name": "대전·세종",
        "gus": {
            "yuseong": {"name": "유성구", "dongs": ["봉명동", "온천동", "궁동", "장대동", "도룡동", "지족동", "노은동", "반석동", "관평동", "송강동", "원신흥동", "상대동", "교은동", "덕명동", "신성동", "전민동", "문지동", "원촌동"]},
            "seo": {"name": "서구", "dongs": ["둔산동", "월평동", "갈마동", "탄방동", "괴정동", "용문동", "가장동", "내동", "변동", "도마동", "정림동", "복수동", "가수원동", "도안동", "관저동", "기성동", "만년동"]},
            "jung": {"name": "중구", "dongs": ["은행동", "선화동", "대흥동", "유천동", "태평동", "문화동", "오류동", "용두동", "목동", "중촌동", "산성동", "안영동", "석교동", "대사동", "부사동"]},
            "dong": {"name": "동구", "dongs": ["용전동", "가양동", "성남동", "홍도동", "자양동", "판암동", "용운동", "대동", "신흥동", "효동", "인동", "원동", "삼성동", "산내동", "낭월동"]},
            "daedeok": {"name": "대덕구", "dongs": ["신탄진동", "송촌동", "중리동", "법동", "비래동", "오정동", "대화동", "목상동", "석봉동", "덕암동", "평촌동"]},
            "sejong": {"name": "세종시", "dongs": ["나성동", "새롬동", "다정동", "어진동", "종촌동", "고운동", "아름동", "도담동", "보람동", "소담동", "대평동", "반곡동", "해밀동", "산울동", "조치원읍", "장군면", "금남면", "부강면", "연서면", "전의면"]}
        }
    },
    "chungcheong": {
        "name": "충남·충북",
        "gus": {
            "cheongju": {"name": "청주시", "dongs": ["복대동", "가경동", "봉명동", "강서동", "비하동", "율량동", "사천동", "오창읍", "오송읍", "내수읍", "용암동", "금천동", "탑동", "영운동", "분평동", "산남동", "성화동", "개신동", "수곡동", "모충동", "사직동", "우암동", "내덕동", "송절동", "문암동"]},
            "cheonan": {"name": "천안시", "dongs": ["두정동", "불당동", "백석동", "쌍용동", "신부동", "성정동", "원성동", "봉명동", "다가동", "청수동", "청당동", "삼룡동", "구성동", "신방동", "통정지구", "성성동", "차암동", "직산읍", "성환읍", "목천읍", "병천면", "입장면", "풍세면"]},
            "asan": {"name": "아산시", "dongs": ["온천동", "모종동", "용화동", "배방읍", "탕정면", "음봉면", "둔포면", "신창면", "인주면", "도고면", "영인면", "염치읍", "권곡동", "실옥동", "풍기동", "장존동", "좌부동"]},
            "gongju": {"name": "공주시", "dongs": ["신관동", "금흥동", "월송동", "옥룡동", "금학동", "중동", "산성동", "교동", "웅진동", "유구읍", "이인면", "탄천면", "계룡면", "반포면", "의당면", "정안면", "우성면", "사곡면", "신풍면"]},
            "gyeryong": {"name": "계룡시", "dongs": ["금암동", "엄사면", "신도안면", "두마면"]},
            "nonsan": {"name": "논산시", "dongs": ["취암동", "부창동", "강산동", "화지동", "내동", "관촉동", "강경읍", "연무읍", "성동면", "광석면", "노성면", "상월면", "부적면", "연산면", "벌곡면", "양촌면", "가야곡면", "은진면", "채운면"]},
            "okcheon": {"name": "옥천군", "dongs": ["옥천읍", "동이면", "안남면", "안내면", "청성면", "청산면", "이원면", "군서면", "군북면"]},
            "geumsan": {"name": "금산군", "dongs": ["금산읍", "금성면", "제원면", "부리면", "군북면", "남일면", "남이면", "진산면", "복수면", "추부면"]}
        }
    },
    "jeonbuk": {
        "name": "전북",
        "gus": {
            "jeonju": {"name": "전주시", "dongs": ["효자동", "신시가지", "서신동", "중화산동", "평화동", "삼천동", "송천동", "에코시티", "혁신도시", "만성동", "덕진동", "인후동", "아중리", "호성동", "우아동", "금암동", "팔복동", "중노송동", "동완산동", "서완산동", "고사동", "중앙동", "객사", "풍남동", "한옥마을"]},
            "iksan": {"name": "익산시", "dongs": ["영등동", "모현동", "어양동", "부송동", "신동", "대학로", "남중동", "중앙동", "창인동", "갈산동", "평화동", "인화동", "마동", "동산동", "금강동", "송학동", "함열읍", "오산면", "황등면", "함라면", "웅포면", "성당면", "용안면", "낭산면", "망성면", "여산면", "금마면", "왕궁면", "춘포면", "삼기면", "용동면"]}
        }
    }
}

count = 0
for sido_key, sido_val in regions_data.items():
    sido_dir = sido_key
    os.makedirs(sido_dir, exist_ok=True)
    gu_links = [f'<a href="/{sido_key}/{gk}/">{gv["name"]} 바로가기</a>' for gk, gv in sido_val["gus"].items()]
    breadcrumbs = f'<a href="/">홈</a> <span>&gt;</span> {sido_val["name"]}'
    
    page = sub_template
    page = page.replace("{{current_region}}", sido_val['name'])
    page = page.replace("{{region_path}}", sido_key)
    page = page.replace("{{BREADCRUMBS}}", breadcrumbs)
    page = page.replace("{{PAGE_TITLE}}", f"{sido_val['name']} 출장마사지 24시 홈케어 | 중부 S슬림테라피")
    page = page.replace("{{PAGE_DESC}}", get_next_desc(sido_val['name']))
    page = page.replace("{{HERO_DESC}}", f"{sido_val['name']} 전지역 25~35분 내에 빠르게 방문하는 24시 안심 출장마사지입니다.")
    page = page.replace("{{SUB_NAV_TITLE}}", f"📍 {sido_val['name']} 시·군·구 선택")
    page = page.replace("{{SUB_NAV_LINKS}}", "\\n".join(gu_links))
    
    with open(f"{sido_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(page)
    count += 1

for sido_key, sido_val in regions_data.items():
    for gu_key, gu_info in sido_val["gus"].items():
        gu_dir = f"{sido_key}/{gu_key}"
        os.makedirs(gu_dir, exist_ok=True)
        dong_links = [f'<a href="/{sido_key}/{gu_key}/{d}/">{d}</a>' for d in gu_info["dongs"]]
        breadcrumbs = f'<a href="/">홈</a> <span>&gt;</span> <a href="/{sido_key}/">{sido_val["name"]}</a> <span>&gt;</span> {gu_info["name"]}'
        full_gu_name = f"{sido_val['name']} {gu_info['name']}"
        relative_path = f"{sido_key}/{gu_key}"
        
        page = sub_template
        page = page.replace("{{current_region}}", full_gu_name)
        page = page.replace("{{region_path}}", relative_path)
        page = page.replace("{{BREADCRUMBS}}", breadcrumbs)
        page = page.replace("{{PAGE_TITLE}}", f"{full_gu_name} 출장마사지 24시 | 중부 S슬림테라피")
        page = page.replace("{{PAGE_DESC}}", get_next_desc(full_gu_name))
        page = page.replace("{{HERO_DESC}}", f"{gu_info['name']} 전지역 25~35분 내에 빠르게 방문하는 100% 후불제 출장마사지입니다.")
        page = page.replace("{{SUB_NAV_TITLE}}", f"📍 {gu_info['name']} 세부 동네 선택")
        page = page.replace("{{SUB_NAV_LINKS}}", "\\n".join(dong_links))
        
        with open(f"{gu_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(page)
        count += 1

for sido_key, sido_val in regions_data.items():
    for gu_key, gu_info in sido_val["gus"].items():
        neighbor_links = [f'<a href="/{sido_key}/{gu_key}/{d}/">{d}</a>' for d in gu_info["dongs"]]
        for dong in gu_info["dongs"]:
            target_dir = f"{sido_key}/{gu_key}/{dong}"
            os.makedirs(target_dir, exist_ok=True)
            breadcrumbs = f'<a href="/">홈</a> <span>&gt;</span> <a href="/{sido_key}/">{sido_val["name"]}</a> <span>&gt;</span> <a href="/{sido_key}/{gu_key}/">{gu_info["name"]}</a> <span>&gt;</span> {dong}'
            full_dong_name = f"{gu_info['name']} {dong}"
            relative_path = f"{sido_key}/{gu_key}/{dong}"
            
            page = sub_template
            page = page.replace("{{current_region}}", full_dong_name)
            page = page.replace("{{region_path}}", relative_path)
            page = page.replace("{{BREADCRUMBS}}", breadcrumbs)
            page = page.replace("{{PAGE_TITLE}}", f"{full_dong_name} 출장마사지 24시 | 중부 S슬림테라피")
            page = page.replace("{{PAGE_DESC}}", get_next_desc(full_dong_name))
            page = page.replace("{{HERO_DESC}}", f"{dong} 어디서나 25~35분 내에 빠르게 방문하는 100% 후불 안심 출장마사지입니다.")
            page = page.replace("{{SUB_NAV_TITLE}}", f"📍 {gu_info['name']} 인근 동네 둘러보기")
            page = page.replace("{{SUB_NAV_LINKS}}", "\\n".join(neighbor_links))
            
            with open(f"{target_dir}/index.html", "w", encoding="utf-8") as f:
                f.write(page)
            count += 1

print(f"✅ 하위 {count}개 구·동 페이지 UTF-8 정상 생성 완료!")

# 4. sitemap.xml 생성
BASE_URL = "https://jungbu-slimcare.shop"
today = datetime.date.today().isoformat()
url_list = []
EXCLUDE_DIRS = {".git", ".vscode", "assets", "css", "__pycache__"}

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    if "index.html" in files:
        rel_path = os.path.relpath(root, ".").replace("\\\\", "/")
        if rel_path == ".":
            loc = f"{BASE_URL}/"
            priority = "1.0"
            changefreq = "daily"
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

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"\\n".join(url_list)}
</urlset>"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"✅ sitemap.xml 생성 완료! (총 {len(url_list)}개 URL)")
print("\\n🎉🎉 [완료] 모든 사이트 파일이 완벽하게 빌드되었습니다!")