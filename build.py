"""Generates the static pages. Edit the content here, then run: python3 build.py"""
from pathlib import Path
import html

SITE = "https://jeheekim.com"
ROOT = Path(__file__).parent

PROJECTS = [
    {
        "slug": "quality-system",
        "kind": "서비스 기획",
        "year": "2025",
        "title": "제조 품질관리 시스템",
        "sub": "신뢰성 시험 관리 서비스",
        "summary": "엑셀과 종이 성적서로 흩어진 시험 과정을 하나의 흐름으로",
        "cover": ("covers/quality-system.webp", 1800, 900),
        "meta": [("고객", "자동차 부품 제조사"), ("역할", "서비스 기획, 화면 설계"), ("시기", "2025")],
        "body": [
            "차량 부품 제조사의 품질 데이터베이스 중 신뢰성 시험 영역을 맡았습니다. 엑셀 일정표와 종이 성적서로 흩어져 있던 시험 과정을 세 흐름으로 묶었습니다. 일정을 파악하고 예약하는 단계, 진행 중인 시험 데이터를 실시간으로 확인하는 단계, 결과를 확인하고 보고서를 자동으로 만드는 단계입니다.",
            "챔버별 진행 현황을 한눈에 보는 대시보드, 빈 시간을 골라 바로 예약하는 일정 화면, 온도·습도 데이터를 모니터링하는 화면을 AS-IS와 TO-BE로 나란히 설계해 실무진 검토를 받았습니다.",
        ],
        "gallery": [
            ("wide", "qms/00.webp", 2000, 1125, "대시보드. 오늘의 시험 현황과 챔버별 예약 가능 여부"),
            ("half", "qms/01.webp", 2000, 1125, "엑셀 일정표를 간트형 일정 화면으로"),
            ("half", "qms/03.webp", 2000, 1125, "시험 데이터 실시간 모니터링"),
        ],
    },
    {
        "slug": "pet-food",
        "kind": "상세페이지 기획",
        "year": "2021",
        "title": "반려견 생식 구독 브랜드",
        "sub": "상세페이지 리뉴얼",
        "summary": "경쟁 브랜드 9곳을 비교해 첫 구매의 망설임을 줄이는 구성으로",
        "cover": ("covers/pet-food.webp", 1800, 900),
        "meta": [("회사", "펫푸드 구독 스타트업"), ("역할", "경쟁사 조사, 페이지 구성 기획"), ("시기", "2021")],
        "body": [
            "구독형 반려견 생식 브랜드의 상세페이지를 다시 짰습니다. 경쟁·참고 브랜드 9곳의 페이지 길이와 구성, 강점과 약점을 비교한 조사표를 만들고, 구매 결정 단계인 유입, 공감, 설득, 구매에 맞춰 목차를 새로 설계했습니다.",
            "처음 생식을 시도하는 보호자를 위한 스타터 레시피 안내, 건식 사료와의 비교, 가격 비교, 자주 묻는 질문을 배치해 첫 구매의 망설임을 줄이는 데 집중했습니다. 같은 회사에서 구독 취소 고객 설문으로 이탈 원인을 찾아 상품 변경 과정을 개선하기도 했습니다.",
        ],
        "phones": [
            ("petfood/02-first.webp", 660, 2576, "첫 생식 안내"),
            ("petfood/03-why.webp", 747, 7681, "선택 이유와 건식 비교"),
            ("petfood/04-faq.webp", 524, 2576, "자주 묻는 질문"),
            ("petfood/05-review.webp", 384, 2576, "후기와 판매 실적"),
        ],
    },
    {
        "slug": "vip-concierge",
        "kind": "광고 콘텐츠",
        "year": "2025",
        "title": "VIP 컨시어지 서비스",
        "sub": "해외 광고 콘텐츠",
        "summary": "고객마다 다른 상황을 한 문장의 광고로",
        "cover": ("covers/vip-concierge.webp", 1800, 900),
        "dark": True,
        "meta": [("형태", "개인 외주"), ("역할", "콘텐츠·웹 기획, 디자인"), ("도구", "Figma, Canva"), ("시기", "2025.08")],
        "body": [
            "해외 임원을 대상으로 한국 체류 중 비서, 의전, 메디컬 일정을 돕는 컨시어지 서비스입니다. 세부 서비스마다 다른 고객의 상황을 한 문장으로 정리해 메타 광고 소재로 기획했고, 서비스 소개 웹페이지 구성까지 맡았습니다.",
        ],
        "posters": [
            ("concierge/03.webp", "Land on Monday, perform by Tuesday"),
            ("concierge/01.webp", "Settle the circle, free the leader"),
            ("concierge/04.webp", "K-Art Medicine"),
            ("concierge/00.webp", "Invest in your time"),
            ("concierge/02.webp", "Your bespoke K-medical concierge"),
            ("concierge/05.webp", "K-beauty, sealed for VIPs"),
        ],
    },
    {
        "slug": "design-education",
        "kind": "SNS 콘텐츠",
        "year": "2022",
        "title": "디자인 교육 브랜드",
        "sub": "SNS·블로그 콘텐츠",
        "summary": "끝까지 넘겨보게 만드는 카드뉴스의 구성",
        "cover": ("covers/design-education.webp", 1800, 900),
        "meta": [("회사", "온라인 교육 기업"), ("역할", "마케팅 어시스턴트"), ("도구", "Figma, Meta·Google Ads"), ("시기", "2022.08 – 2023.01")],
        "body": [
            "디자인 교육 브랜드의 인스타그램 카드뉴스와 강의 상품을 알리는 블로그 콘텐츠를 기획했습니다. 강의 내용을 요약하고, 중고거래와 지도 서비스의 이용 흐름을 비교하는 사례 분석으로 이야기를 엮어 사용자가 끝까지 넘겨보게 만드는 구성을 연습했습니다.",
        ],
        "cards": [
            ("edu/00.webp", "개인화 서비스는 어떻게 만드나요"),
            ("edu/01.webp", "본인의 이야기를 주고 싶은 디자이너"),
            ("edu/04.webp", "다른 중고거래 서비스와 비교하기"),
            ("edu/05.webp", "중고거래 서비스를 선호하는 이유"),
            ("edu/08.webp", "지도 서비스가 가장 잘할 수 있는 것"),
            ("edu/09.webp", "지도 서비스 이용 흐름 분석"),
        ],
    },
    {
        "slug": "fashion-brand",
        "kind": "브랜드 패키지",
        "year": "2020",
        "title": "여성 의류 브랜드",
        "sub": "런칭 패키지 디자인",
        "summary": "행택부터 실링 스티커까지 같은 목소리로",
        "cover": ("covers/fashion-brand.webp", 1800, 900),
        "meta": [("형태", "대학원 재학 중 외주"), ("역할", "브랜딩·패키지 디자인"), ("도구", "Illustrator, Photoshop"), ("시기", "2020.09 – 2020.12")],
        "body": [
            "가치를 기준으로 소비하는 여성을 위한 의류 브랜드의 런칭에 참여했습니다. 행택, 봉투, 쇼핑백, 포장지, 테이프, 실링 스티커까지 브랜드 경험이 처음부터 끝까지 같은 목소리를 내도록 디자인했고, 재질과 인쇄 방식, 재단 방법을 직접 비교해 골랐습니다.",
        ],
        "mosaic": [
            ("a", "fashion/05.webp", "브랜드 행택"),
            ("b", "fashion/03.webp", "브랜드 화보"),
            ("c", "fashion/11.webp", "패턴 포장지와 실링 스티커"),
            ("d", "fashion/10.webp", "실링 왁스로 봉한 포장"),
            ("e", "fashion/13.webp", "브랜드 문구가 인쇄된 포장 테이프"),
            ("f", "fashion/09.webp", "브로슈어와 화보 카드"),
        ],
    },
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Hahmlet:wght@200;300;400;500&family=IBM+Plex+Sans+KR:wght@300;400;500&display=swap" rel="stylesheet">')

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>"
           "<rect width='64' height='64' rx='14' fill='%237B2B23'/>"
           "<text x='32' y='45' font-size='36' text-anchor='middle' fill='%23E9ECEA' font-family='serif'>제</text></svg>")

e = html.escape


def head(title, desc, path, og):
    url = SITE + path
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="김제희 포트폴리오">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og/{og}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#E9ECEA">
<link rel="icon" href="{FAVICON}">
{FONTS}
<link rel="stylesheet" href="/style.css">
</head>
"""


def header(active):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<body>
<a class="skip" href="#main">본문 바로가기</a>
<header class="top">
  <a class="mark" href="/">김제희</a>
  <nav aria-label="주요 메뉴">
    {a('/', '작업', 'work')}
    {a('/about', '소개', 'about')}
  </nav>
</header>
"""


FOOT = """<footer class="foot">
  <span>© 2026 김제희</span>
  <a href="/about">소개</a>
</footer>
<dialog class="lightbox" aria-label="이미지 크게 보기">
  <button class="lb-close" type="button">닫기</button>
  <img alt="">
</dialog>
<script src="/main.js" defer></script>
</body>
</html>
"""


def img(src, alt, w=None, h=None, cls="", lazy=True, zoom=False, vt=None):
    attrs = [f'src="/assets/{src}"', f'alt="{e(alt)}"']
    if w: attrs.append(f'width="{w}" height="{h}"')
    if lazy: attrs.append('loading="lazy"')
    if cls: attrs.append(f'class="{cls}"')
    if zoom: attrs.append('data-zoom')
    if vt: attrs.append(f'style="view-transition-name:{vt}"')
    return "<img " + " ".join(attrs) + ">"


def home():
    rows = []
    for p in PROJECTS:
        s, w, h = p["cover"]
        rows.append(f"""    <li>
      <a class="row" href="/work/{p['slug']}">
        <span class="row-kind">{p['kind']}</span>
        <span class="row-title"><span>{p['title']}</span><span class="row-sub">{p['sub']}</span></span>
        <span class="row-year">{p['year']}</span>
        <span class="row-img">{img(s, '', w, h, vt='cover-' + p['slug'])}</span>
      </a>
    </li>""")
    return (head("김제희 · 서비스·사업 기획자", "고객의 문제를 사업 기회로 연결해온 기획자 김제희의 포트폴리오입니다.", "/", "home")
            + header("work") + f"""<main id="main">
  <section class="hero">
    <h1 class="name" aria-label="김제희"><span>김</span><span>제</span><span>희</span></h1>
    <div class="hero-side">
      <p class="role">서비스·사업 기획자</p>
      <p class="lede">고객의 문제를 사업 기회로 연결해 왔습니다. 재활 로봇 서비스, 구독 커머스, 보험 디지털 전환, 제조 품질 시스템까지. 현장의 목소리에서 출발해 실행 가능한 개선안으로 만듭니다.</p>
      <a class="text-link" href="/about">일하는 방식과 경력</a>
    </div>
  </section>
  <section class="index" aria-labelledby="idx">
    <h2 id="idx" class="index-title">작업</h2>
    <ul class="rows">
{chr(10).join(rows)}
    </ul>
  </section>
</main>
""" + FOOT)


def gallery(p):
    out = []
    if "gallery" in p:
        out.append('<div class="g-shots">')
        for kind, s, w, h, cap in p["gallery"]:
            out.append(f'<figure class="g-{kind}">{img(s, cap, w, h, zoom=True)}<figcaption>{cap}</figcaption></figure>')
        out.append("</div>")
    if "phones" in p:
        out.append('<p class="hint">각 화면 안에서 스크롤해 전체 페이지를 볼 수 있습니다.</p><div class="phones">')
        for s, w, h, cap in p["phones"]:
            out.append(f'<figure class="phone"><div class="phone-screen" tabindex="0" aria-label="{cap} 화면">{img(s, cap, w, h)}</div><figcaption>{cap}</figcaption></figure>')
        out.append("</div>")
    if "posters" in p:
        out.append('<div class="posters">')
        for s, cap in p["posters"]:
            out.append(f'<figure>{img(s, cap + " 광고 소재", 900, 1125, zoom=True)}</figure>')
        out.append("</div>")
    if "cards" in p:
        out.append('<div class="cards">')
        for s, cap in p["cards"]:
            out.append(f'<figure>{img(s, cap + " 카드뉴스", 900, 900, zoom=True)}</figure>')
        out.append("</div>")
    if "mosaic" in p:
        out.append('<div class="mosaic">')
        for k, s, cap in p["mosaic"]:
            out.append(f'<figure class="mo-{k}">{img(s, cap, zoom=True)}</figure>')
        out.append("</div>")
    return "\n".join(out)


def project(i, p):
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    s, w, h = p["cover"]
    ns, nw, nh = nxt["cover"]
    meta = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["meta"])
    body = "".join(f"<p>{t}</p>" for t in p["body"])
    dark = ' class="is-dark"' if p.get("dark") else ""
    return (head(f"{p['title']} · {p['sub']} | 김제희", p["summary"], f"/work/{p['slug']}", p["slug"])
            .replace("<body>", "") + header("work").replace("<body>", f"<body{dark}>") + f"""<main id="main" class="case">
  <a class="back" href="/">작업 전체</a>
  <header class="case-head">
    <p class="case-kind">{p['kind']}</p>
    <h1>{p['title']}<span>{p['sub']}</span></h1>
  </header>
  <figure class="case-cover">{img(s, p['title'] + ' 대표 이미지', w, h, lazy=False, vt='cover-' + p['slug'])}</figure>
  <div class="case-intro">
    <dl class="meta">{meta}</dl>
    <div class="case-body">{body}</div>
  </div>
  <section class="case-gallery" aria-label="작업물">
{gallery(p)}
  </section>
  <a class="next" href="/work/{nxt['slug']}">
    <span class="next-label">다음 작업</span>
    <span class="next-title">{nxt['title']}<span>{nxt['sub']}</span></span>
    <span class="next-img">{img(ns, '', nw, nh, vt='cover-' + nxt['slug'])}</span>
  </a>
</main>
""" + FOOT)


def about():
    return (head("소개 | 김제희", "현장에서 듣고, 원인을 정의하고, 이해관계자를 정렬해 보이는 결과물로 만드는 기획자 김제희입니다.", "/about", "about")
            + header("about") + """<main id="main" class="about">
  <section class="about-lead">
    <h1>고객과 기술, 사업과 현장 사이에서 같은 방향을 만드는 일을 합니다.</h1>
    <p>재활 로봇 서비스 기획으로 시작해 구독 커머스, 보험 디지털 전환, 제조 품질 시스템을 거쳤습니다. 최근에는 프리랜서로 홈페이지 구축, 광고 운영, AI 교육 프로젝트를 직접 발굴하고 수주하며 사업을 운영하는 관점까지 배웠습니다.</p>
  </section>

  <section class="approach" aria-labelledby="ap">
    <h2 id="ap">일하는 방식</h2>
    <ol class="steps">
      <li><h3>현장에서 듣습니다</h3><p>대학병원 의료진과 환우 인터뷰, 구독 취소 고객 설문, 공장 생산·물류 흐름 분석처럼 사용자가 실제로 겪는 장면을 먼저 확인합니다.</p></li>
      <li><h3>원인을 정의합니다</h3><p>의견을 모으는 것보다 문제의 원인을 하나로 좁히는 데 시간을 씁니다. 구독 이탈의 주원인이 상품 변경 과정의 불편함이라는 걸 찾아낸 방식입니다.</p></li>
      <li><h3>이해관계자를 정렬합니다</h3><p>고객사, 운영, 개발 조직의 요구가 부딪힐 때 사용자 조사와 사업 목표를 기준으로 우선순위를 정리하고 결정을 돕습니다.</p></li>
      <li><h3>보이는 결과물로 만듭니다</h3><p>화면 설계서, 상세페이지, 광고 콘텐츠, 브랜드 패키지까지 기획을 손에 잡히는 형태로 직접 완성합니다.</p></li>
    </ol>
  </section>

  <section class="career" aria-labelledby="cr">
    <h2 id="cr">경력과 경험</h2>
    <ul class="roles">
      <li><h3>헬스케어·로봇 기술 기업</h3><p class="r-what">서비스 기획</p><p>재활 로봇 기반 치료 서비스를 기획했습니다. 대학병원 의료진·환우 인터뷰와 사용성 테스트로 현장의 요구를 확인하고 개발자와 기술적 제약을 조율했습니다. 확보한 사용자 인사이트는 사업 제안과 수주에도 쓰였습니다. 이후 차량 부품 제조사의 공장 내부 품질 시스템 기획에 참여했습니다.</p></li>
      <li><h3>보험 가입 디지털 전환</h3><p class="r-what">리서처, 서비스 기획</p><p>보험 가입 절차를 디지털화하는 프로젝트에서 고객사·운영·개발 조직의 요구를 사용자 조사와 사업 목표 기준으로 정리하고 의사결정을 지원했습니다. 고객사로부터 만족도 우수 평가를 받았습니다.</p></li>
      <li><h3>펫푸드 구독 스타트업</h3><p class="r-what">서비스 기획, 마케팅</p><p>구독 유지율 하락 원인을 취소 고객 설문과 만족도 조사로 찾고, 상품 변경 과정을 개선해 구독 유지 비율을 높였습니다. 상세페이지 리뉴얼을 기획했습니다.</p></li>
      <li><h3>온라인 교육 기업</h3><p class="r-what">마케팅 어시스턴트, 2022 – 2023</p><p>디자인 교육 브랜드의 SNS 카드뉴스와 블로그 콘텐츠를 기획하고 Meta·Google Ads 운영을 지원했습니다.</p></li>
      <li><h3>프리랜서</h3><p class="r-what">기획·마케팅, 2025 –</p><p>홈페이지 구축, 메타 광고 기획·운영, AI 교육 프로젝트를 직접 발굴해 제안하고 수주했습니다.</p></li>
    </ul>
    <div class="tools"><h3>쓰는 도구</h3><p>Figma, Canva, Illustrator, Photoshop, PowerPoint, Excel, Meta Ads, Google Ads</p></div>
  </section>

  <a class="next next-plain" href="/"><span class="next-label">작업 보기</span><span class="next-title">작업 전체<span>다섯 개의 프로젝트</span></span></a>
</main>
""" + FOOT)


if __name__ == "__main__":
    (ROOT / "index.html").write_text(home(), encoding="utf-8")
    (ROOT / "about.html").write_text(about(), encoding="utf-8")
    (ROOT / "work").mkdir(exist_ok=True)
    for i, p in enumerate(PROJECTS):
        (ROOT / "work" / f"{p['slug']}.html").write_text(project(i, p), encoding="utf-8")
    print("built", 2 + len(PROJECTS), "pages")
