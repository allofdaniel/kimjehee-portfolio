"""Generates every page in Korean and English. Edit content here, then run: python3 build.py"""
from pathlib import Path
import html

SITE = "https://jeheekim.com"
ROOT = Path(__file__).parent
e = html.escape

# ---------------------------------------------------------------- content
UI = {
    "ko": {"work": "작업", "about": "소개", "skip": "본문 바로가기", "all": "작업 전체", "next": "다음 작업",
           "role": "서비스·사업 기획자", "theme": "화면 모드 전환", "other": "EN", "other_label": "English",
           "lede": "고객의 문제를 사업 기회로 연결합니다. 재활 로봇, 구독 커머스, 보험, 제조 현장에서 들은 목소리를 실행 가능한 개선안으로 만듭니다.",
           "more": "일하는 방식과 경력", "hint": "각 화면 안에서 스크롤해 전체 페이지를 볼 수 있습니다.",
           "close": "닫기", "zoom": "이미지 크게 보기", "process": "진행 흐름",
           "site": "김제희 포트폴리오", "home_title": "김제희 · 서비스·사업 기획자",
           "home_desc": "고객의 문제를 사업 기회로 연결해온 기획자 김제희의 포트폴리오입니다."},
    "en": {"work": "Work", "about": "About", "skip": "Skip to content", "all": "All work", "next": "Next project",
           "role": "Service & Business Planner", "theme": "Toggle color mode", "other": "한국어", "other_label": "한국어",
           "lede": "I turn customer problems into business opportunities, taking what I hear in rehab robotics, subscription commerce, insurance and manufacturing and shaping it into improvements teams can ship.",
           "more": "How I work and career", "hint": "Scroll inside each screen to see the full page.",
           "close": "Close", "zoom": "Enlarged image", "process": "Process",
           "site": "Jehee Kim Portfolio", "home_title": "Jehee Kim · Service & Business Planner",
           "home_desc": "Portfolio of Jehee Kim, a planner who connects customer problems to business opportunities."},
}
NAME = {"ko": "김제희", "en": "Jehee Kim"}

PROJECTS = [
    {
        "slug": "quality-system", "year": "2025", "cover": "covers/quality-system.webp",
        "ko": {"kind": "서비스 기획", "title": "제조 품질관리 시스템", "sub": "신뢰성 시험 관리 서비스",
               "summary": "엑셀과 종이 성적서로 흩어진 시험 과정을 하나의 흐름으로",
               "meta": [("고객", "자동차 부품 제조사"), ("역할", "서비스 기획, 화면 설계"), ("시기", "2025")],
               "body": ["자동차 부품 제조사의 품질 데이터베이스 중 신뢰성 시험 영역을 맡았습니다. 엑셀 일정표와 종이 성적서로 흩어져 있던 시험 과정을 세 흐름으로 묶고, 화면마다 AS-IS와 TO-BE를 나란히 설계해 실무진 검토를 받았습니다."],
               "flow": ["일정 파악·예약", "실시간 데이터 확인", "결과 확인·자동 보고서"],
               "caps": ["대시보드. 오늘의 시험 현황과 챔버별 예약 가능 여부", "엑셀 일정표를 간트형 일정 화면으로", "시험 데이터 실시간 모니터링"]},
        "en": {"kind": "Service planning", "title": "Manufacturing Quality System", "sub": "Reliability test management",
               "summary": "Bringing scattered spreadsheets and paper reports into one flow",
               "meta": [("Client", "Automotive parts maker"), ("Role", "Service planning, screen design"), ("Year", "2025")],
               "body": ["I took on the reliability-testing module of an automotive parts maker's quality database. Test work was scattered across Excel schedules and paper reports, so I organized it into three flows and designed each screen as a side-by-side AS-IS and TO-BE for review with the client's engineers."],
               "flow": ["Check & book schedules", "Monitor live data", "Results & auto reports"],
               "caps": ["Dashboard showing today's tests and chamber availability", "From an Excel schedule to a Gantt-style planner", "Live monitoring of test data"]},
        "gallery": [("wide", "qms/00.webp", 2000, 1125), ("half", "qms/01.webp", 2000, 1125), ("half", "qms/03.webp", 2000, 1125)],
    },
    {
        "slug": "pet-food", "year": "2021", "cover": "covers/pet-food.webp",
        "ko": {"kind": "상세페이지 기획", "title": "반려견 생식 구독 브랜드", "sub": "상세페이지 리뉴얼",
               "summary": "경쟁 브랜드 9곳을 비교해 첫 구매의 망설임을 줄이는 구성으로",
               "meta": [("회사", "펫푸드 구독 스타트업"), ("역할", "경쟁사 조사, 페이지 구성 기획"), ("시기", "2021")],
               "body": ["경쟁·참고 브랜드 9곳의 페이지 구성과 강약점을 비교하고, 구매 결정 단계에 맞춰 목차를 새로 설계했습니다. 처음 생식을 시도하는 보호자를 위해 스타터 레시피, 건식 비교, 가격 비교, 자주 묻는 질문을 배치했습니다."],
               "flow": ["유입", "공감", "설득", "구매"],
               "caps": ["첫 생식 안내", "선택 이유와 건식 비교", "자주 묻는 질문", "후기와 판매 실적"]},
        "en": {"kind": "Product page planning", "title": "Raw Dog Food Subscription", "sub": "Product page redesign",
               "summary": "Benchmarking nine brands to ease the first purchase",
               "meta": [("Company", "Pet food subscription startup"), ("Role", "Competitive research, page structure"), ("Year", "2021")],
               "body": ["I compared the page structure, strengths and weaknesses of nine competing and reference brands, then rebuilt the table of contents around the purchase journey. For first-time raw feeders I added a starter recipe guide, a dry-food comparison, a price comparison and an FAQ."],
               "flow": ["Discover", "Relate", "Persuade", "Purchase"],
               "caps": ["First-time guide", "Why us, vs. dry food", "FAQ", "Reviews and sales"]},
        "stat": {"ko": ("9", "비교 분석한 브랜드"), "en": ("9", "brands benchmarked")},
        "phones": [("petfood/02-first.webp", 660, 2576), ("petfood/03-why.webp", 747, 7681), ("petfood/04-faq.webp", 524, 2576), ("petfood/05-review.webp", 384, 2576)],
    },
    {
        "slug": "vip-concierge", "year": "2025", "cover": "covers/vip-concierge.webp", "dark": True,
        "ko": {"kind": "광고 콘텐츠", "title": "VIP 컨시어지 서비스", "sub": "해외 광고 콘텐츠",
               "summary": "고객마다 다른 상황을 한 문장의 광고로",
               "meta": [("형태", "개인 외주"), ("역할", "콘텐츠·웹 기획, 디자인"), ("도구", "Figma, Canva"), ("시기", "2025.08")],
               "body": ["한국에 머무는 해외 임원의 비서·의전·메디컬 일정을 돕는 서비스입니다. 세부 서비스마다 다른 고객의 상황을 한 문장으로 정리해 메타 광고 소재로 만들고, 서비스 소개 웹페이지 구성까지 맡았습니다."],
               "flow": ["고객 상황 정의", "한 문장 메시지", "메타 광고 소재"]},
        "en": {"kind": "Ad content", "title": "VIP Concierge Service", "sub": "Overseas ad content",
               "summary": "Turning each client's situation into a one-line ad",
               "meta": [("Type", "Freelance"), ("Role", "Content & web planning, design"), ("Tools", "Figma, Canva"), ("Year", "2025.08")],
               "body": ["A service that handles secretarial, protocol and medical schedules for foreign executives staying in Korea. I distilled each service's client situation into one line for Meta ad creatives and planned the structure of the service web page."],
               "flow": ["Define the situation", "One-line message", "Meta ad creative"]},
        "posters": ["concierge/03.webp", "concierge/01.webp", "concierge/04.webp", "concierge/00.webp", "concierge/02.webp", "concierge/05.webp"],
        "poster_alt": ["Land on Monday, perform by Tuesday", "Settle the circle, free the leader", "K-Art Medicine", "Invest in your time", "Your bespoke K-medical concierge", "K-beauty, sealed for VIPs"],
    },
    {
        "slug": "design-education", "year": "2022", "cover": "covers/design-education.webp",
        "ko": {"kind": "SNS 콘텐츠", "title": "디자인 교육 브랜드", "sub": "SNS·블로그 콘텐츠",
               "summary": "끝까지 넘겨보게 만드는 카드뉴스의 구성",
               "meta": [("회사", "온라인 교육 기업"), ("역할", "마케팅 어시스턴트"), ("도구", "Figma, Meta·Google Ads"), ("시기", "2022.08 – 2023.01")],
               "body": ["디자인 교육 브랜드의 인스타그램 카드뉴스와 강의 홍보 블로그를 기획했습니다. 강의 내용을 요약하고 중고거래·지도 서비스의 이용 흐름을 비교하는 사례 분석으로 엮어, 마지막 장까지 넘겨보게 만드는 구성을 연습했습니다."],
               "flow": ["강의 요약", "서비스 사례 분석", "카드뉴스·블로그 발행"],
               "alts": ["개인화 서비스는 어떻게 만드나요", "본인의 이야기를 주고 싶은 디자이너", "다른 중고거래 서비스와 비교하기", "중고거래 서비스를 선호하는 이유", "지도 서비스가 가장 잘할 수 있는 것", "지도 서비스 이용 흐름 분석"]},
        "en": {"kind": "Social content", "title": "Design Education Brand", "sub": "Social & blog content",
               "summary": "Card news people swipe through to the end",
               "meta": [("Company", "Online education company"), ("Role", "Marketing assistant"), ("Tools", "Figma, Meta & Google Ads"), ("Year", "2022.08 – 2023.01")],
               "body": ["I planned Instagram card news and course-promotion blog posts for a design education brand, summarizing lectures and weaving in case studies that compare user flows of second-hand marketplaces and map apps, so readers keep swiping to the last card."],
               "flow": ["Summarize the course", "Analyze service cases", "Publish cards & posts"],
               "alts": ["How personalized services are made", "A designer you would like to introduce", "Comparing second-hand marketplaces", "Why users prefer one marketplace", "What a map app does best", "Map app user flow analysis"]},
        "cards": ["edu/00.webp", "edu/01.webp", "edu/04.webp", "edu/05.webp", "edu/08.webp", "edu/09.webp"],
    },
    {
        "slug": "fashion-brand", "year": "2020", "cover": "covers/fashion-brand.webp",
        "ko": {"kind": "브랜드 패키지", "title": "여성 의류 브랜드", "sub": "런칭 패키지 디자인",
               "summary": "행택부터 실링 스티커까지 같은 목소리로",
               "meta": [("형태", "대학원 재학 중 외주"), ("역할", "브랜딩·패키지 디자인"), ("도구", "Illustrator, Photoshop"), ("시기", "2020.09 – 2020.12")],
               "body": ["가치를 기준으로 소비하는 여성을 위한 의류 브랜드의 런칭에 참여했습니다. 행택, 봉투, 쇼핑백, 포장지, 테이프, 실링 스티커가 같은 목소리를 내도록 디자인하고 재질과 인쇄 방식을 직접 비교해 골랐습니다."],
               "flow": ["브랜드 무드", "적용 품목 설계", "재질·인쇄 선정"],
               "alts": ["브랜드 행택", "브랜드 화보", "패턴 포장지와 실링 스티커", "실링 왁스로 봉한 포장", "브랜드 문구가 인쇄된 포장 테이프", "브로슈어와 화보 카드"]},
        "en": {"kind": "Brand packaging", "title": "Women's Fashion Brand", "sub": "Launch packaging",
               "summary": "One voice from hang tag to seal sticker",
               "meta": [("Type", "Freelance during grad school"), ("Role", "Branding & packaging design"), ("Tools", "Illustrator, Photoshop"), ("Year", "2020.09 – 2020.12")],
               "body": ["I joined the launch of a clothing brand for women who shop by their values, designing hang tags, envelopes, bags, wrapping paper, tape and seal stickers to speak with one voice, and comparing materials and print methods myself."],
               "flow": ["Brand mood", "Item design", "Materials & print"],
               "alts": ["Hang tag", "Brand photography", "Patterned wrap and seal sticker", "Wax-sealed package", "Printed packing tape", "Brochure and photo card"]},
        "mosaic": [("a", "fashion/05.webp"), ("b", "fashion/03.webp"), ("c", "fashion/11.webp"), ("d", "fashion/10.webp"), ("e", "fashion/13.webp"), ("f", "fashion/09.webp")],
    },
]

ABOUT = {
    "ko": {
        "title": "소개 | 김제희", "desc": "현장에서 듣고, 원인을 정의하고, 이해관계자를 정렬해 결과물로 만드는 기획자 김제희입니다.",
        "lead": "고객과 기술, 사업과 현장 사이에서 같은 방향을 만듭니다.",
        "stats": [("7", "경험한 산업"), ("5", "대표 프로젝트"), ("4", "일하는 단계")],
        "process_h": "일하는 방식",
        "process": [("듣기", "현장의 목소리부터"), ("정의", "원인을 하나로 좁힌다"), ("정렬", "모두를 한 방향으로"), ("실행", "손에 잡히는 결과물로")],
        "matrix_h": "산업과 역할",
        "cols": ["리서치", "서비스 기획", "콘텐츠·마케팅", "디자인"],
        "rows": ["헬스케어·로봇", "보험", "제조", "펫푸드 커머스", "교육", "컨시어지", "패션"],
        "timeline_h": "작업 연표",
        "career_h": "경력",
        "career": [("헬스케어·로봇 기술 기업", "서비스 기획", "재활 로봇 치료 서비스, 대학병원 인터뷰·사용성 테스트"),
                   ("보험 디지털 전환 프로젝트", "리서처, 서비스 기획", "고객사 만족도 우수 평가"),
                   ("펫푸드 구독 스타트업", "기획, 마케팅", "이탈 원인을 찾아 구독 유지율 개선"),
                   ("온라인 교육 기업", "마케팅 어시스턴트", "2022 – 2023 · SNS·블로그 콘텐츠"),
                   ("프리랜서", "기획·마케팅", "2025 – · 홈페이지 구축, 메타 광고, AI 교육")],
        "tools_h": "도구",
    },
    "en": {
        "title": "About | Jehee Kim", "desc": "Jehee Kim listens on the ground, defines the cause, aligns stakeholders and ships tangible work.",
        "lead": "I bring customers and technology, business and the field, into one direction.",
        "stats": [("7", "industries"), ("5", "featured projects"), ("4", "steps in my process")],
        "process_h": "How I work",
        "process": [("Listen", "Start on the ground"), ("Define", "Narrow it to one cause"), ("Align", "Get everyone facing one way"), ("Make", "Ship something tangible")],
        "matrix_h": "Industries and roles",
        "cols": ["Research", "Service planning", "Content & marketing", "Design"],
        "rows": ["Healthcare & robotics", "Insurance", "Manufacturing", "Pet food commerce", "Education", "Concierge", "Fashion"],
        "timeline_h": "Timeline",
        "career_h": "Career",
        "career": [("Healthcare & robotics company", "Service planner", "Rehab robot therapy service; hospital interviews and usability tests"),
                   ("Insurance digitization project", "Researcher, service planner", "Rated excellent by the client"),
                   ("Pet food subscription startup", "Planning, marketing", "Found churn causes and improved retention"),
                   ("Online education company", "Marketing assistant", "2022 – 2023 · social and blog content"),
                   ("Freelance", "Planning & marketing", "2025 – · websites, Meta ads, AI training")],
        "tools_h": "Tools",
    },
}
# which roles were done in each industry (rows x cols), derived from the projects above
MATRIX = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
TOOLS = ["Figma", "Canva", "Illustrator", "Photoshop", "PowerPoint", "Excel", "Meta Ads", "Google Ads"]

# ---------------------------------------------------------------- chrome
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Hahmlet:wght@200;300;400;500&family=IBM+Plex+Sans+KR:wght@300;400;500&display=swap" rel="stylesheet">')
FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
           "<rect width='64' height='64' rx='14' fill='%237B2B23'/>"
           "<text x='32' y='45' font-size='36' text-anchor='middle' fill='%23E9ECEA' font-family='serif'>제</text></svg>")
THEME_BOOT = ("<script>try{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}catch(e){}</script>")
SUN = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg>'
MOON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.6A8.2 8.2 0 0 1 9.4 4a8.2 8.2 0 1 0 10.6 10.6z"/></svg>'


def pre(lang):
    return "/en" if lang == "en" else ""


def head(lang, title, desc, path, og):
    other = "en" if lang == "ko" else "ko"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{pre(lang)}{path}">
<link rel="alternate" hreflang="{lang}" href="{SITE}{pre(lang)}{path}">
<link rel="alternate" hreflang="{other}" href="{SITE}{pre(other)}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{UI[lang]['site']}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{pre(lang)}{path}">
<meta property="og:image" content="{SITE}/assets/og/{lang}-{og}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{'ko_KR' if lang == 'ko' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{FAVICON}">
{THEME_BOOT}
{FONTS}
<link rel="stylesheet" href="/style.css">
</head>
"""


def header(lang, active, path, dark=False):
    u = UI[lang]
    other = "en" if lang == "ko" else "ko"
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<body{' class="is-night"' if dark else ''}>
<a class="skip" href="#main">{u['skip']}</a>
<header class="top">
  <a class="mark" href="{pre(lang)}/">{NAME[lang]}</a>
  <nav aria-label="menu">
    {a(pre(lang) + '/', u['work'], 'work')}
    {a(pre(lang) + '/about', u['about'], 'about')}
    <span class="tools-nav">
      <a class="lang" href="{pre(other)}{path}" hreflang="{other}" lang="{other}">{u['other']}</a>
      <button class="theme" type="button" aria-label="{u['theme']}"><span class="i-sun">{SUN}</span><span class="i-moon">{MOON}</span></button>
    </span>
  </nav>
</header>
"""


def foot(lang):
    u = UI[lang]
    return f"""<footer class="foot">
  <span>© 2026 {NAME[lang]}</span>
  <a href="{pre(lang)}/about">{u['about']}</a>
</footer>
<dialog class="lightbox" aria-label="{u['zoom']}">
  <button class="lb-close" type="button">{u['close']}</button>
  <img alt="">
</dialog>
<script src="/main.js" defer></script>
</body>
</html>
"""


def img(src, alt, w=None, h=None, lazy=True, zoom=False, vt=None):
    attrs = [f'src="/assets/{src}"', f'alt="{e(alt)}"']
    if w: attrs.append(f'width="{w}" height="{h}"')
    if lazy: attrs.append('loading="lazy"')
    if zoom: attrs.append('data-zoom')
    if vt: attrs.append(f'style="view-transition-name:{vt}"')
    return "<img " + " ".join(attrs) + ">"


def flow(steps, label):
    items = "".join(f'<li style="--i:{i}"><span class="f-dot"></span><span class="f-txt">{e(s)}</span></li>' for i, s in enumerate(steps))
    return f'<ol class="flow" data-reveal aria-label="{e(label)}" style="--n:{len(steps)}">{items}</ol>'


# ---------------------------------------------------------------- pages
def home(lang):
    u = UI[lang]
    rows = []
    for p in PROJECTS:
        c = p[lang]
        rows.append(f"""    <li>
      <a class="row" href="{pre(lang)}/work/{p['slug']}">
        <span class="row-kind">{c['kind']}</span>
        <span class="row-title"><span>{c['title']}</span><span class="row-sub">{c['sub']}</span></span>
        <span class="row-year">{p['year']}</span>
        <span class="row-img">{img(p['cover'], '', 1800, 900, vt='cover-' + p['slug'])}</span>
      </a>
    </li>""")
    name = "".join(f"<span>{ch}</span>" for ch in (NAME[lang] if lang == "ko" else "Jehee Kim".split(" ")))
    return (head(lang, u["home_title"], u["home_desc"], "/", "home") + header(lang, "work", "/") + f"""<main id="main">
  <section class="hero">
    <h1 class="name name-{lang}" aria-label="{NAME[lang]}">{name}</h1>
    <div class="hero-side">
      <p class="role">{u['role']}</p>
      <p class="lede">{u['lede']}</p>
      <a class="text-link" href="{pre(lang)}/about">{u['more']}</a>
    </div>
  </section>
  <section class="index" aria-labelledby="idx">
    <h2 id="idx" class="label">{u['work']}</h2>
    <ul class="rows">
{chr(10).join(rows)}
    </ul>
  </section>
</main>
""" + foot(lang))


def gallery(p, lang):
    c = p[lang]
    out = []
    if "gallery" in p:
        out.append('<div class="g-shots">')
        for (kind, s, w, h), cap in zip(p["gallery"], c["caps"]):
            out.append(f'<figure class="g-{kind}">{img(s, cap, w, h, zoom=True)}<figcaption>{cap}</figcaption></figure>')
        out.append("</div>")
    if "phones" in p:
        out.append(f'<p class="hint">{UI[lang]["hint"]}</p><div class="phones">')
        for (s, w, h), cap in zip(p["phones"], c["caps"]):
            out.append(f'<figure class="phone"><div class="phone-screen" tabindex="0" aria-label="{cap}">{img(s, cap, w, h)}</div><figcaption>{cap}</figcaption></figure>')
        out.append("</div>")
    if "posters" in p:
        out.append('<div class="posters">')
        for s, alt in zip(p["posters"], p["poster_alt"]):
            out.append(f'<figure>{img(s, alt, 900, 1125, zoom=True)}</figure>')
        out.append("</div>")
    if "cards" in p:
        out.append('<div class="cards">')
        for s, alt in zip(p["cards"], c["alts"]):
            out.append(f'<figure>{img(s, alt, 900, 900, zoom=True)}</figure>')
        out.append("</div>")
    if "mosaic" in p:
        out.append('<div class="mosaic">')
        for (k, s), alt in zip(p["mosaic"], c["alts"]):
            out.append(f'<figure class="mo-{k}">{img(s, alt, zoom=True)}</figure>')
        out.append("</div>")
    return "\n".join(out)


def project(lang, i, p):
    u = UI[lang]
    c = p[lang]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    nc = nxt[lang]
    path = f"/work/{p['slug']}"
    meta = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in c["meta"])
    body = "".join(f"<p>{t}</p>" for t in c["body"])
    return (head(lang, f"{c['title']} · {c['sub']} | {NAME[lang]}", c["summary"], path, p["slug"])
            + header(lang, "work", path, p.get("dark")) + f"""<main id="main" class="case">
  <a class="back" href="{pre(lang)}/">{u['all']}</a>
  <header class="case-head">
    <p class="case-kind">{c['kind']}</p>
    <h1>{c['title']}<span>{c['sub']}</span></h1>
  </header>
  <figure class="case-cover">{img(p['cover'], c['title'], 1800, 900, lazy=False, vt='cover-' + p['slug'])}</figure>
  <div class="case-intro">
    <dl class="meta">{meta}</dl>
    <div class="case-body">{body}</div>
  </div>
  <section class="case-flow" aria-label="{u['process']}">
    {flow(c['flow'], u['process'])}
  </section>
  <section class="case-gallery" aria-label="{c['title']}">
{gallery(p, lang)}
  </section>
  <a class="next" href="{pre(lang)}/work/{nxt['slug']}">
    <span class="label">{u['next']}</span>
    <span class="next-title">{nc['title']}<span>{nc['sub']}</span></span>
    <span class="next-img">{img(nxt['cover'], '', 1800, 900, vt='cover-' + nxt['slug'])}</span>
  </a>
</main>
""" + foot(lang))


def about(lang):
    a = ABOUT[lang]
    stats = "".join(f'<div class="stat"><span class="stat-n" data-count="{n}">{n}</span><span class="stat-l">{l}</span></div>' for n, l in a["stats"])
    proc = "".join(f'<li style="--i:{i}"><span class="p-node">{i + 1}</span><h3>{h}</h3><p>{t}</p></li>' for i, (h, t) in enumerate(a["process"]))
    head_cells = "".join(f'<th scope="col"><span>{c}</span></th>' for c in a["cols"])
    rows = []
    for ri, (r, marks) in enumerate(zip(a["rows"], MATRIX)):
        cells = "".join(
            f'<td style="--d:{ri * 4 + ci}">{"<span class=dot></span><span class=sr>●</span>" if m else ""}</td>'
            for ci, m in enumerate(marks))
        rows.append(f"<tr><th scope=\"row\">{r}</th>{cells}</tr>")
    years = sorted({p["year"] for p in PROJECTS})
    span = (int(years[0]), int(years[-1]))
    marks = []
    for k, p in enumerate(sorted(PROJECTS, key=lambda x: (x["year"], x["slug"]))):
        pos = (int(p["year"]) - span[0]) / (span[1] - span[0]) * 100
        side = "tl-r" if pos > 75 else ("tl-l" if pos < 15 else "")
        marks.append(f'<a class="tl-item {side}" style="--x:{pos:.1f}%;--k:{k % 2}" href="{pre(lang)}/work/{p["slug"]}"><span class="tl-dot"></span><span class="tl-card"><span class="tl-y">{p["year"]}</span>{p[lang]["title"]}</span></a>')
    ticks = "".join(f'<span style="--x:{(y - span[0]) / (span[1] - span[0]) * 100:.1f}%">{y}</span>' for y in range(span[0], span[1] + 1))
    career = "".join(f'<li><h3>{n}</h3><p class="r-what">{r}</p><p class="r-note">{t}</p></li>' for n, r, t in a["career"])
    tools = "".join(f"<li>{t}</li>" for t in TOOLS)
    return (head(lang, a["title"], a["desc"], "/about", "about") + header(lang, "about", "/about") + f"""<main id="main" class="about">
  <section class="about-lead">
    <h1>{a['lead']}</h1>
    <div class="stats" data-reveal>{stats}</div>
  </section>

  <section class="block" aria-labelledby="ap">
    <h2 id="ap" class="label">{a['process_h']}</h2>
    <ol class="process" data-reveal>{proc}</ol>
  </section>

  <section class="block" aria-labelledby="mx">
    <h2 id="mx" class="label">{a['matrix_h']}</h2>
    <div class="matrix-wrap"><table class="matrix" data-reveal><thead><tr><td></td>{head_cells}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>
  </section>

  <section class="block" aria-labelledby="tl">
    <h2 id="tl" class="label">{a['timeline_h']}</h2>
    <div class="timeline" data-reveal><div class="tl-axis"></div><div class="tl-ticks">{ticks}</div>{''.join(marks)}</div>
  </section>

  <section class="block two" aria-labelledby="cr">
    <div>
      <h2 id="cr" class="label">{a['career_h']}</h2>
      <ul class="roles">{career}</ul>
    </div>
    <div>
      <h2 class="label">{a['tools_h']}</h2>
      <ul class="chips">{tools}</ul>
    </div>
  </section>
</main>
""" + foot(lang))


if __name__ == "__main__":
    count = 0
    for lang in ("ko", "en"):
        base = ROOT / ("en" if lang == "en" else "")
        (base / "work").mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(home(lang), encoding="utf-8")
        (base / "about.html").write_text(about(lang), encoding="utf-8")
        count += 2
        for i, p in enumerate(PROJECTS):
            (base / "work" / f"{p['slug']}.html").write_text(project(lang, i, p), encoding="utf-8")
            count += 1
    print("built", count, "pages")
