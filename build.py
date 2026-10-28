"""Generates every page in Korean and English. Edit content here, then run: python3 build.py"""
from pathlib import Path
import html

SITE = "https://jeheekim.com"
ROOT = Path(__file__).parent
e = html.escape

# ---------------------------------------------------------------- content
FINANCE = {
    "slug": "insurance-ux", "year": "2018", "cover": "covers/finance.webp",
    "ko": {"kind": "금융 UX 리서치", "title": "생명보험사 디지털 채널", "sub": "고객·설계사 서비스 UX 컨설팅",
           "summary": "고객과 설계사 60여 명을 인터뷰해 보험 가입의 디지털 접점을 다시 설계",
           "meta": [("고객", "생명보험사"), ("역할", "UX 리서치, 화면 설계 (4인 팀)"), ("소속", "UX 컨설팅 에이전시"), ("시기", "2018.01 – 2019.02")],
           "body": ["보험 가입과 유지의 접점을 디지털 서비스로 옮기는 프로젝트에서 리서치를 맡았습니다. 보험을 사는 고객과 파는 설계사, 두 사용자를 각각 인터뷰해 문제를 나누어 정의하고, 그 결과를 재무 분석 서비스와 보험 지식 카드뉴스 화면으로 이어 설계했습니다.",
                    "대외비 프로젝트라 일부 내용은 변경·재가공했습니다."],
           "flow": ["트렌드·데스크 리서치", "고객 FGD·설계사 IDI", "퍼소나·여정 지도", "재무 분석·카드뉴스 설계"],
           "stats": [("30+", "고객 인터뷰"), ("30+", "설계사 인터뷰"), ("12", "퍼소나")],
           "caps": ["금융·보험 환경 변화와 사용자 가설 검증", "사용자 목소리에서 문제와 솔루션으로", "고객 6명, 설계사 6명의 퍼소나", "보험 가입 여정 지도", "여정에서 도출한 설계사 디지털 채널 방향"]},
    "en": {"kind": "Financial UX research", "title": "Life Insurer Digital Channels", "sub": "UX consulting for customers & planners",
           "summary": "Interviewing 60+ customers and planners to redesign the digital touchpoints of buying insurance",
           "meta": [("Client", "Life insurance company"), ("Role", "UX research, screen design (team of 4)"), ("Team", "UX consulting agency"), ("Year", "2018.01 – 2019.02")],
           "body": ["I led research on a project moving insurance sign-up and retention onto digital channels. I interviewed both users, the customers who buy and the planners who sell, defined their problems separately, and carried the findings into a financial analysis service and insurance-knowledge card news screens.",
                    "This was a confidential project, so some details have been altered."],
           "flow": ["Trend & desk research", "Customer FGD, planner IDI", "Personas & journey map", "Financial analysis & card news"],
           "stats": [("30+", "customer interviews"), ("30+", "planner interviews"), ("12", "personas")],
           "caps": ["Industry shifts and hypothesis validation", "From user voice to problems and solutions", "Six customer and six planner personas", "Insurance sign-up journey map", "Digital channel direction for planners"]},
    "gallery": [("wide", "finance/00.webp", 2000, 1125), ("wide", "finance/01.webp", 2000, 1125), ("wide", "finance/02.webp", 2000, 1125), ("half", "finance/03.webp", 2000, 1125), ("half", "finance/04.webp", 2000, 1125)],
}
COMMERCE = {
    "slug": "pet-food", "year": "2021", "cover": "covers/pet-food.webp",
    "ko": {"kind": "커머스 서비스 기획", "title": "반려견 생식 구독 커머스", "sub": "웹사이트 개선과 상세페이지",
           "summary": "해지 고객 설문에서 시작해 주문·결제·맞춤 설문을 다시 설계",
           "meta": [("회사", "펫푸드 구독 스타트업"), ("역할", "서비스 기획, 기능명세, 화면 설계"), ("시기", "2021.05 – 2022.02")],
           "body": ["정기구독 해지 고객 설문에서 결제가 번거롭고 홈페이지가 보기 어렵다는 불만이 공동 1위로 나왔습니다. 정보 구조를 다시 짜고 주문서, 결제, 맞춤 설문, 구독 일시정지 기능을 PC와 모바일 전체에 걸쳐 개선했습니다.",
                    "경쟁 브랜드 9곳을 비교해 상세페이지도 구매 단계에 맞춰 새로 구성했습니다."],
           "flow": ["해지 고객 설문", "문제 정의", "정보 구조·기능명세", "화면 설계·디자인"],
           "stats": [("30%", "불만 문의 감소"), ("80%", "구독 유지 비율 증가"), ("40%", "고객 유입 증가")],
           "caps": ["해지 고객 설문. 결제와 홈페이지 사용성이 공동 1위 불만", "기능 추가에 따른 정보 구조", "주문서·결제 페이지 개선", "맞춤 설문 개선과 결과 리포트", "상세페이지 리뉴얼", "모바일 전체 디자인"],
           "pcaps": ["첫 생식 안내", "선택 이유와 건식 비교", "자주 묻는 질문", "후기와 판매 실적"]},
    "en": {"kind": "Commerce service planning", "title": "Raw Dog Food Subscription", "sub": "Website improvement & product pages",
           "summary": "Starting from churned-subscriber surveys to redesign ordering, payment and onboarding",
           "meta": [("Company", "Pet food subscription startup"), ("Role", "Service planning, specs, screen design"), ("Year", "2021.05 – 2022.02")],
           "body": ["A survey of cancelled subscribers put a clumsy checkout and a hard-to-read website tied at the top of the complaints. I rebuilt the information architecture and improved the order form, payment, the onboarding survey and subscription pause across PC and mobile.",
                    "I also benchmarked nine brands and restructured the product pages around the purchase journey."],
           "flow": ["Churn survey", "Define problems", "IA & specs", "Screens & design"],
           "stats": [("30%", "fewer complaints"), ("80%", "higher retention rate"), ("40%", "more inbound traffic")],
           "caps": ["Churn survey: checkout and site usability tied as top complaints", "Information architecture for new features", "Order and payment pages, before and after", "Onboarding survey and results report", "Product page redesign", "Full mobile design"],
           "pcaps": ["First-time guide", "Why us, vs. dry food", "FAQ", "Reviews and sales"]},
    "gallery": [("wide", "commerce/00.webp", 2000, 1125), ("wide", "commerce/01.webp", 2000, 1125), ("half", "commerce/02.webp", 2000, 1125), ("half", "commerce/03.webp", 2000, 1125), ("wide", "commerce/04.webp", 2000, 1125), ("wide", "commerce/05.webp", 2000, 1125)],
    "phones": [("petfood/02-first.webp", 660, 2576), ("petfood/03-why.webp", 747, 7681), ("petfood/04-faq.webp", 524, 2576), ("petfood/05-review.webp", 384, 2576)],
}
ESG = {
    "slug": "zero-waste", "year": "2023", "cover": "covers/esg.webp", "dark": True,
    "ko": {"kind": "UX 연구 · 석사 논문", "title": "제로웨이스트 행동유도", "sub": "게이미피케이션 서비스 제안",
           "summary": "행동유도 이론으로 탄소중립 실천을 오래 지속하게 만드는 앱",
           "meta": [("형태", "대학원 졸업논문, 개인 프로젝트"), ("역할", "리서치, 기획, 화면 설계"), ("시기", "2021.03 – 2023.11")],
           "body": ["제로웨이스트를 시작한 사람이 좌절하지 않고 계속하도록 돕는 서비스를 연구했습니다. 실천가와 업계 실무자를 직접 섭외해 인터뷰하고, 행동유도 이론을 여정 지도에 적용해 미션, 보상, 소셜 기능을 설계한 뒤 사용자 테스트로 다듬었습니다."],
           "flow": ["이론·서비스 조사", "실천가 인터뷰", "행동유도 여정 지도", "프로토타입·사용자 테스트"],
           "stats": [("8", "인터뷰 참여자"), ("3", "핵심 설계 원칙")],
           "caps": ["행동유도 이론을 적용한 여정 지도", "스스로 돌아보며 의지를 갖게 하는 화면", "좌절감 없이 뿌듯함을 키우는 화면"]},
    "en": {"kind": "UX research · master's thesis", "title": "Zero-Waste Nudging", "sub": "A gamified service proposal",
           "summary": "Using behavior-change theory so carbon-neutral habits last",
           "meta": [("Type", "Master's thesis, solo project"), ("Role", "Research, planning, screen design"), ("Year", "2021.03 – 2023.11")],
           "body": ["I researched a service that keeps zero-waste beginners from giving up. I recruited practitioners and industry professionals for interviews, applied behavior-change theory to the journey map to design missions, rewards and social features, then refined them through user testing."],
           "flow": ["Theory & service review", "Practitioner interviews", "Behavior-change journey map", "Prototype & user test"],
           "stats": [("8", "interviewees"), ("3", "design principles")],
           "caps": ["Journey map built on behavior-change theory", "Screens that build self-reflection and will", "Screens that grow pride without frustration"]},
    "gallery": [("wide", "esg/02.webp", 2000, 1125), ("half", "esg/03.webp", 2000, 1125), ("half", "esg/04.webp", 2000, 1125)],
}
ROUTINE = {
    "slug": "solo-routine", "year": "2022", "cover": "covers/routine.webp",
    "ko": {"kind": "UX 연구 · 팀 프로젝트", "title": "청년 1인 가구 루틴", "sub": "자기 관리 게이미피케이션",
           "summary": "해빗 루프로 혼자 사는 청년의 건강한 습관을 돕는 서비스",
           "meta": [("형태", "대학원 팀 프로젝트 (3인)"), ("역할", "UX 리서치, 화면 설계"), ("시기", "2022.09 – 2022.12")],
           "body": ["혼자 사는 청년이 미래보다 당장의 귀찮음을 먼저 느낀다는 인사이트에서 출발했습니다. 세 차례 1:1 인터뷰를 점진적으로 설계해 퍼소나를 만들고, 신호·열망·반응·보상의 해빗 루프에 미션, 팀 클럽, 피드백을 붙여 프로토타입을 만들었습니다. 이후 교내 창업 대회에도 도전했습니다."],
           "flow": ["신호", "열망", "반응", "보상"],
           "stats": [("3", "차례 심층 인터뷰"), ("3", "퍼소나")],
           "caps": ["해빗 루프를 적용한 UX 시나리오", "신호와 열망 단계 프로토타입", "반응과 보상 단계 프로토타입"]},
    "en": {"kind": "UX research · team project", "title": "Routines for Living Alone", "sub": "Gamified self-care",
           "summary": "A habit-loop service for young adults living on their own",
           "meta": [("Type", "Graduate team project (3)"), ("Role", "UX research, screen design"), ("Year", "2022.09 – 2022.12")],
           "body": ["We started from the insight that young adults living alone feel today's hassle before tomorrow's benefit. Three rounds of progressive one-on-one interviews shaped our personas, and we built a prototype that adds missions, team clubs and feedback to the cue, craving, response and reward habit loop. We later entered it in a campus startup competition."],
           "flow": ["Cue", "Craving", "Response", "Reward"],
           "stats": [("3", "rounds of interviews"), ("3", "personas")],
           "caps": ["UX scenario built on the habit loop", "Prototype: cue and craving", "Prototype: response and reward"]},
    "gallery": [("wide", "routine/01.webp", 2000, 1125), ("half", "routine/02.webp", 2000, 1125), ("half", "routine/03.webp", 2000, 1125)],
}

UI = {
    "ko": {"work": "작업", "about": "소개", "skip": "본문 바로가기", "all": "작업 전체", "next": "다음 작업",
           "role": "서비스·사업 기획자", "theme": "화면 모드 전환", "other": "EN", "other_label": "English",
           "lede": "고객의 문제를 사업 기회로 연결합니다. 금융, 헬스케어, 구독 커머스, 제조 현장에서 들은 목소리를 실행 가능한 개선안으로 만듭니다.",
           "more": "일하는 방식과 경력", "hint": "각 화면 안에서 스크롤해 전체 페이지를 볼 수 있습니다.",
           "close": "닫기", "zoom": "이미지 크게 보기", "process": "진행 흐름",
           "site": "김제희 포트폴리오", "home_title": "김제희 · 서비스·사업 기획자",
           "home_desc": "고객의 문제를 사업 기회로 연결해온 기획자 김제희의 포트폴리오입니다."},
    "en": {"work": "Work", "about": "About", "skip": "Skip to content", "all": "All work", "next": "Next project",
           "role": "Service & Business Planner", "theme": "Toggle color mode", "other": "한국어", "other_label": "한국어",
           "lede": "I turn customer problems into business opportunities, taking what I hear in finance, healthcare, subscription commerce and manufacturing and shaping it into improvements teams can ship.",
           "more": "How I work and career", "hint": "Scroll inside each screen to see the full page.",
           "close": "Close", "zoom": "Enlarged image", "process": "Process",
           "site": "Jehee Kim Portfolio", "home_title": "Jehee Kim · Service & Business Planner",
           "home_desc": "Portfolio of Jehee Kim, a planner who connects customer problems to business opportunities."},
}
NAME = {"ko": "김제희", "en": "Jehee Kim"}

PROJECTS = [FINANCE, COMMERCE,

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
PROJECTS[3:3] = [ESG, ROUTINE]

EMAIL = "kjh012677@gmail.com"
ABOUT = {
    "ko": {
        "title": "소개 | 김제희", "desc": "현장에서 듣고, 원인을 정의하고, 이해관계자를 정렬해 결과물로 만드는 기획자 김제희입니다.",
        "lead": "고객과 기술, 사업과 현장 사이에서 같은 방향을 만듭니다.",
        "stats": [("5+", "년 실무 경력"), ("8", "경험한 산업"), ("60+", "인터뷰한 사용자")],
        "process_h": "일하는 방식",
        "process": [("듣기", "현장의 목소리부터"), ("정의", "원인을 하나로 좁힌다"), ("정렬", "모두를 한 방향으로"), ("실행", "손에 잡히는 결과물로")],
        "matrix_h": "산업과 역할",
        "cols": ["리서치", "서비스 기획", "콘텐츠·마케팅", "디자인"],
        "rows": ["금융·보험", "헬스케어·로봇", "제조", "구독·이커머스", "ESG·라이프스타일", "교육", "컨시어지·브랜드", "패션"],
        "timeline_h": "작업 연표",
        "career_h": "경력",
        "career": [("2025.07 –", "프리랜서", "기획·마케팅", "브랜드 론칭 메시지 설계, 웹페이지 기획·디자인, 메타 광고"),
                   ("2025.09 – 2026.03", "이커머스 플랫폼 CX팀", "UX 리서치 코디네이터", "리서치 운영, VOC·데이터 구조화, 리크루팅 고객 관리 100% 유지"),
                   ("2024.05 – 2025.04", "헬스케어·로봇 기술 기업", "서비스 기획 대리", "재활 게임, 비대면 진료, 골격근 검사, 제조 품질 시스템"),
                   ("2022.12 – 2023.05", "온라인 교육 기업", "마케터", "SNS 콘텐츠, 홍보 기사, 메타·구글·X 광고 운영"),
                   ("2021.05 – 2022.02", "펫푸드 구독 스타트업", "서비스 기획·마케팅", "웹 UX 개선, 광고 데이터 분석, 인스타그램 전략"),
                   ("2020.09 – 2021.02", "브랜드 스타트업 · 대학 산학 연구", "브랜딩·서비스 기획", "패키지 디자인, 멘탈 케어 앱 기획"),
                   ("2017.12 – 2019.06", "UX 컨설팅 에이전시", "UX 리서처", "생명보험사 디지털 전환, 은행 사용성 평가, 트렌드 리포트"),
                   ("2017.02 – 2017.05", "디지털 에이전시", "인턴", "웹·앱 리뉴얼 리서치, 서비스 디자인")],
        "more_h": "그 밖의 작업",
        "more": ["뇌졸중 환자 상지 재활 게임 콘텐츠", "비대면 재활 진료 플랫폼", "초·중학교 골격근 검사 서비스", "차량 램프 원격 제어 앱", "연구기관 VR/AR 전시 시나리오", "센서 신사업 UI/UX 리서치", "은행 대면 채널 사용성 평가", "챗봇·인공지능 트렌드 리포트", "멘탈 케어 앱 기획"],
        "edu_h": "학력",
        "edu": [("2020 – 2024", "연세대학교 커뮤니케이션대학원", "커뮤니케이션디자인 석사 · 인터랙션 디자인, 정량·정성 UX 조사"),
                ("2013 – 2017", "한남대학교", "디자인학과 · 미디어영상학과 복수전공")],
        "research_h": "연구와 수상",
        "research": [("2024", "석사 논문", "제로웨이스트 행동유도를 위한 게이미피케이션 모바일 서비스 제안"),
                     ("2022", "KCI 등재 · 공동저자", "K-pop 아티스트 소통 특화 서비스 UX 디자인 가이드라인"),
                     ("2021", "한국HCI학회 학술대회", "액티브 시니어층의 구독 콘텐츠 UX 가이드라인 연구"),
                     ("2017", "창업 아이디어 공모전 장려상", "챗봇을 활용한 홈케어 진단 서비스"),
                     ("2015", "대한민국디자인전람회 입선", "층간소음 완화와 이웃 소통을 위한 서비스 디자인")],
        "lang_h": "언어",
        "langs": ["영어 · 일상 회화", "중국어 · 일상 회화"],
        "tools_h": "도구",
        "contact_h": "연락",
        "contact": "함께 이야기 나누고 싶다면 메일 주세요.",
    },
    "en": {
        "title": "About | Jehee Kim", "desc": "Jehee Kim listens on the ground, defines the cause, aligns stakeholders and ships tangible work.",
        "lead": "I bring customers and technology, business and the field, into one direction.",
        "stats": [("5+", "years of experience"), ("8", "industries"), ("60+", "users interviewed")],
        "process_h": "How I work",
        "process": [("Listen", "Start on the ground"), ("Define", "Narrow it to one cause"), ("Align", "Get everyone facing one way"), ("Make", "Ship something tangible")],
        "matrix_h": "Industries and roles",
        "cols": ["Research", "Service planning", "Content & marketing", "Design"],
        "rows": ["Finance & insurance", "Healthcare & robotics", "Manufacturing", "Subscription & e-commerce", "ESG & lifestyle", "Education", "Concierge & brand", "Fashion"],
        "timeline_h": "Timeline",
        "career_h": "Career",
        "career": [("2025.07 –", "Freelance", "Planning & marketing", "Brand launch messaging, web planning and design, Meta ads"),
                   ("2025.09 – 2026.03", "E-commerce platform, CX team", "UX research coordinator", "Research operations, structured VOC data, 100% participant retention"),
                   ("2024.05 – 2025.04", "Healthcare & robotics company", "Service planner", "Rehab games, telehealth, posture screening, manufacturing quality"),
                   ("2022.12 – 2023.05", "Online education company", "Marketer", "Social content, press releases, Meta, Google and X ads"),
                   ("2021.05 – 2022.02", "Pet food subscription startup", "Service planning & marketing", "Web UX, ad data analysis, Instagram strategy"),
                   ("2020.09 – 2021.02", "Brand startup · university research", "Branding & service planning", "Packaging design, mental care app planning"),
                   ("2017.12 – 2019.06", "UX consulting agency", "UX researcher", "Life insurer digital shift, bank usability study, trend reports"),
                   ("2017.02 – 2017.05", "Digital agency", "Intern", "Web and app renewal research, service design")],
        "more_h": "Other work",
        "more": ["Upper-limb rehab games for stroke patients", "Remote rehab telehealth platform", "School posture screening service", "Vehicle lamp remote-control app", "VR/AR exhibition scenario for a research institute", "UI/UX research for a sensor business", "Bank branch usability evaluation", "Chatbot and AI trend report", "Mental care app planning"],
        "edu_h": "Education",
        "edu": [("2020 – 2024", "Yonsei University, Graduate School of Communication", "M.A. Communication Design · interaction design, quantitative and qualitative UX research"),
                ("2013 – 2017", "Hannam University", "B.A. Design · double major in Media & Film")],
        "research_h": "Research & awards",
        "research": [("2024", "Master's thesis", "A gamified mobile service to encourage zero-waste behavior"),
                     ("2022", "KCI journal · co-author", "UX design guidelines for K-pop artist–fan communication services"),
                     ("2021", "HCI Korea conference", "UX guidelines for subscription content for active seniors"),
                     ("2017", "Startup idea contest, honorable mention", "Chatbot-based home care diagnosis service"),
                     ("2015", "Korea Design Exhibition, selected", "Service design to ease noise between neighbors")],
        "lang_h": "Languages",
        "langs": ["English · conversational", "Mandarin · conversational"],
        "tools_h": "Tools",
        "contact_h": "Contact",
        "contact": "I'd be glad to hear from you.",
    },
}
# roles practised in each industry (rows x cols), derived from the projects and career above
MATRIX = [[1, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [1, 1, 1, 1], [1, 1, 0, 1], [0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
TOOLS = ["Figma", "Adobe XD", "Illustrator", "Photoshop", "Canva", "Notion", "Slack", "Trello", "PowerPoint", "Excel", "SPSS", "Meta Ads", "Google Ads"]

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
  <a href="mailto:{EMAIL}">{EMAIL}</a>
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
        for (s, w, h), cap in zip(p["phones"], c.get("pcaps", c["caps"])):
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


def stats_block(c):
    if not c.get("stats"):
        return ""
    items = "".join(f'<div class="stat"><span class="stat-n">{e(n)}</span><span class="stat-l">{e(l)}</span></div>' for n, l in c["stats"])
    return f'  <section class="case-stats"><div class="stats stats-{len(c["stats"])}" data-reveal>{items}</div></section>'


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
{stats_block(c)}
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
        marks.append(f'<a class="tl-item {side}" style="--x:{pos:.1f}%;--k:{k % 3}" href="{pre(lang)}/work/{p["slug"]}"><span class="tl-dot"></span><span class="tl-card"><span class="tl-y">{p["year"]}</span>{p[lang]["title"]}</span></a>')
    ticks = "".join(f'<span style="--x:{(y - span[0]) / (span[1] - span[0]) * 100:.1f}%">{y}</span>' for y in range(span[0], span[1] + 1))
    career = "".join(f'<li><span class="r-date">{d}</span><h3>{n}</h3><p class="r-what">{r}</p><p class="r-note">{t}</p></li>' for d, n, r, t in a["career"])
    more = "".join(f"<li>{m}</li>" for m in a["more"])
    edu = "".join(f'<li><span class="r-date">{d}</span><h3>{n}</h3><p class="r-note">{t}</p></li>' for d, n, t in a["edu"])
    research = "".join(f'<li><span class="rs-y">{y}</span><span class="rs-w">{w}</span><span class="rs-t">{t}</span></li>' for y, w, t in a["research"])
    langs = "".join(f"<li>{x}</li>" for x in a["langs"])
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

  <section class="block" aria-labelledby="cr">
    <h2 id="cr" class="label">{a['career_h']}</h2>
    <ol class="career-list">{career}</ol>
  </section>

  <section class="block" aria-labelledby="mo">
    <h2 id="mo" class="label">{a['more_h']}</h2>
    <ul class="chips chips-lg">{more}</ul>
  </section>

  <section class="block two" aria-labelledby="ed">
    <div>
      <h2 id="ed" class="label">{a['edu_h']}</h2>
      <ol class="career-list">{edu}</ol>
      <h2 class="label label-gap">{a['research_h']}</h2>
      <ol class="research">{research}</ol>
    </div>
    <div>
      <h2 class="label">{a['tools_h']}</h2>
      <ul class="chips">{tools}</ul>
      <h2 class="label label-gap">{a['lang_h']}</h2>
      <ul class="plain">{langs}</ul>
    </div>
  </section>

  <section class="contact" aria-labelledby="ct">
    <h2 id="ct" class="label">{a['contact_h']}</h2>
    <p>{a['contact']}</p>
    <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
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
