#!/usr/bin/env python3
"""
포르쉐 카드뉴스 — 12개 SVG 생성 스크립트
- 캔버스: 1080 × 1350
- 사진은 base64로 embed
- 텍스트는 <text> 요소로 (Figma에서 편집 가능)
"""
import base64
import os

ROOT = "/Users/ykr/클로드/카드뉴스"
PHOTOS = os.path.join(ROOT, "photos")
SVG_OUT = os.path.join(ROOT, "svg")

cards = [
    {
        "num": 1, "type": "cover",
        "photo": "photo-014.jpg",
        "title": ["포르쉐,", "전기차였다."],
        "subtitle": "슈투트가르트 뮤지엄에서 본 6가지",
    },
    {
        "num": 2, "type": "intro",
        "photo": "photo-024.jpg",
        "label": "INTRO",
        "subtitle_lines": ["독일 슈투트가르트,", "포르쉐의 본진."],
        "text_lines": [
            "75년 브랜드 헤리티지가 한 자리에 모인 곳,",
            "포르쉐 뮤지엄. 그곳에서 마주한 사실들은",
            "우리가 알던 포르쉐와는 조금 달랐다.",
        ],
    },
    {
        "num": 3, "type": "body",
        "photo": "photo-017.jpg",
        "label": "FACT",
        "subtitle_lines": ["첫 포르쉐는,", "전기차였다."],
        "text_lines": [
            "1900년. 25살의 페르디난트 포르쉐가 만든",
            "'Lohner-Porsche'. 휠 안에 모터를 넣은 인-휠",
            "전기차였다. 가솔린이 자동차의 전부였던",
            "시대에, 포르쉐는 전기로 시작했다.",
        ],
    },
    {
        "num": 4, "type": "body",
        "photo": "photo-023.jpg",
        "label": "FACT",
        "subtitle_lines": ["양산차의 시작은 비틀과", "80% 똑같았다."],
        "text_lines": [
            "페르디난트 포르쉐는 폭스바겐 비틀의",
            "설계자였다. 1939년 그가 만든 'Porsche Type",
            "64'는 비틀의 섀시와 엔진을 그대로 가져왔다.",
            "두 차의 DNA는 사실상 형제다.",
        ],
    },
    {
        "num": 5, "type": "body",
        "photo": "photo-012.jpg",
        "label": "DETAIL",
        "subtitle_lines": ["비틀이 없었다면,", "911도 없었다."],
        "text_lines": [
            "비틀의 RR(후방 엔진·후륜구동) 레이아웃은",
            "그대로 356, 그리고 911로 이어졌다. 80년이",
            "지난 지금도 911의 엔진은 차체 뒤쪽에 있다.",
        ],
    },
    {
        "num": 6, "type": "body",
        "photo": "photo-021.jpg",
        "label": "FACT",
        "subtitle_lines": ["포르쉐의 진짜 DNA는,", "레이싱이다."],
        "text_lines": [
            "도로 위 포르쉐는 절반의 이야기다. 나머지",
            "절반은 서킷에서 쓰였다. 창립 첫 해부터",
            "지금까지, 포르쉐는 단 한 번도 레이스를",
            "멈춘 적이 없다.",
        ],
    },
    {
        "num": 7, "type": "body",
        "photo": "photo-016.jpg",
        "label": "LE MANS",
        "subtitle_lines": ["1970년대, 르망 24시를", "점령한 그 시대."],
        "text_lines": [
            "마티니 레이싱 컬러를 입은 포르쉐는 70년대",
            "르망을 지배했다. 빨강·파랑·하늘색 스트라이프는",
            "그 자체로 한 시대의 상징이 됐다.",
        ],
    },
    {
        "num": 8, "type": "body",
        "photo": "photo-004.jpg",
        "label": "DETAIL",
        "subtitle_lines": ["르망 최다 우승, 19회.", "포르쉐가 곧 르망이다."],
        "text_lines": [
            "눈앞에 있던 935는 70년대 르망과 IMSA를",
            "휩쓸었던 차. 24시간을 달릴 수 있는 내구성,",
            "그리고 끝까지 포기하지 않는 엔지니어링이",
            "이 차에 담겨 있다.",
        ],
    },
    {
        "num": 9, "type": "body",
        "photo": "photo-011.jpg",
        "label": "F1",
        "subtitle_lines": ["포르쉐의 엔진은,", "F1까지 갔다."],
        "text_lines": [
            "1983–1987년, 맥라렌 F1은 'TAG-Porsche'",
            "엔진을 얹고 달렸다. 4년 동안 25승, 드라이버",
            "챔피언 3회. 포르쉐의 심장이 F1 그리드에서",
            "가장 빨랐던 시절이다.",
        ],
    },
    {
        "num": 10, "type": "body",
        "photo": "photo-009.jpg",
        "label": "RALLY",
        "subtitle_lines": ["사막에서도,", "포르쉐였다."],
        "text_lines": [
            "파리-다카르 랠리, WRC, IMSA, 르망.",
            "포장도로든 사막이든, 포르쉐는 어디든 갔다.",
            "959는 1984년 파리-다카르를 제패했다.",
        ],
    },
    {
        "num": 11, "type": "body",
        "photo": "photo-020.jpg",
        "label": "NOW",
        "subtitle_lines": ["그리고 포르쉐는,", "다시 전기로 돌아왔다."],
        "text_lines": [
            "1900년 전기로 시작했던 포르쉐는, 2019년",
            "'Taycan'으로 다시 전기로 돌아왔다. 125년의",
            "원을 그리며, 그 사이에 쌓인 레이스 DNA를",
            "그대로 안고서.",
        ],
    },
    {
        "num": 12, "type": "closing",
        "photo": "photo-003.jpg",
        "head": "포르쉐의 진짜 이야기,",
        "big": "이제 알겠지?",
        "cta_lines": [
            "도움이 됐다면 저장 · 공유",
            "다음 매거진도 놓치지 마세요",
        ],
        "handle": "@yunkiride",
    },
]


def img_to_data_uri(filename):
    path = os.path.join(PHOTOS, filename)
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:image/jpeg;base64,{data}"


GRADIENTS = """  <defs>
    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.15"/>
      <stop offset="30%" stop-color="#000000" stop-opacity="0.05"/>
      <stop offset="65%" stop-color="#000000" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="coverGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.55"/>
      <stop offset="35%" stop-color="#000000" stop-opacity="0.15"/>
      <stop offset="70%" stop-color="#000000" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.85"/>
    </linearGradient>
    <linearGradient id="closingGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.7"/>
    </linearGradient>
  </defs>"""


def wm(x, y, anchor="end"):
    return f"""  <text x="{x}" y="{y}" font-family="Noto Sans KR, sans-serif" font-size="26" font-weight="700" text-anchor="{anchor}" letter-spacing="1">
    <tspan fill="#ffffff">YUNKI</tspan><tspan fill="#D5001C">RIDE</tspan>
  </text>"""


def build_cover(card):
    img = img_to_data_uri(card["photo"])
    title1, title2 = card["title"]
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1080" height="1350" viewBox="0 0 1080 1350">
{GRADIENTS}
  <image href="{img}" x="0" y="0" width="1080" height="1350" preserveAspectRatio="xMidYMid slice"/>
  <rect width="1080" height="1350" fill="url(#coverGrad)"/>
  <text x="540" y="620" font-family="Noto Sans KR, sans-serif" font-size="124" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="-2">{title1}</text>
  <text x="540" y="760" font-family="Noto Sans KR, sans-serif" font-size="124" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="-2">{title2}</text>
  <text x="540" y="830" font-family="Noto Sans KR, sans-serif" font-size="32" font-weight="400" fill="#ffffff" fill-opacity="0.85" text-anchor="middle" letter-spacing="-0.5">{card['subtitle']}</text>
{wm(540, 1300, anchor="middle")}
</svg>
"""


def build_body(card, is_intro=False):
    img = img_to_data_uri(card["photo"])
    label = card["label"]
    sub_lines = card["subtitle_lines"]
    text_lines = card["text_lines"]

    subtitle_size = 68 if is_intro else 58
    label_y = 920
    sub_y_start = 990
    sub_line_height = int(subtitle_size * 1.2)
    text_y_start = sub_y_start + sub_line_height * len(sub_lines) + 24
    text_line_height = 48

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1080" height="1350" viewBox="0 0 1080 1350">',
        GRADIENTS,
        f'  <image href="{img}" x="0" y="0" width="1080" height="1350" preserveAspectRatio="xMidYMid slice"/>',
        '  <rect width="1080" height="1350" fill="url(#bodyGrad)"/>',
        wm(1020, 78, anchor="end"),
        f'  <text x="70" y="{label_y}" font-family="Noto Sans KR, sans-serif" font-size="22" font-weight="500" fill="#D5001C" letter-spacing="5">{label}</text>',
    ]
    for i, line in enumerate(sub_lines):
        y = sub_y_start + i * sub_line_height
        parts.append(f'  <text x="70" y="{y}" font-family="Noto Sans KR, sans-serif" font-size="{subtitle_size}" font-weight="900" fill="#ffffff" letter-spacing="-1.5">{line}</text>')
    for i, line in enumerate(text_lines):
        y = text_y_start + i * text_line_height
        parts.append(f'  <text x="70" y="{y}" font-family="Noto Sans KR, sans-serif" font-size="30" font-weight="400" fill="#ffffff" fill-opacity="0.92" letter-spacing="-0.3">{line}</text>')
    parts.append(f'  <text x="1010" y="1325" font-family="Noto Sans KR, sans-serif" font-size="18" font-weight="400" fill="#ffffff" fill-opacity="0.55" text-anchor="end" letter-spacing="2">{card["num"]:02d} / 12</text>')
    parts.append('</svg>\n')
    return "\n".join(parts)


def build_closing(card):
    img = img_to_data_uri(card["photo"])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1080" height="1350" viewBox="0 0 1080 1350">
{GRADIENTS}
  <image href="{img}" x="0" y="0" width="1080" height="1350" preserveAspectRatio="xMidYMid slice"/>
  <rect width="1080" height="1350" fill="url(#closingGrad)"/>
{wm(540, 78, anchor="middle")}
  <text x="540" y="560" font-family="Noto Sans KR, sans-serif" font-size="32" font-weight="500" fill="#ffffff" fill-opacity="0.9" text-anchor="middle" letter-spacing="-0.5">{card['head']}</text>
  <text x="540" y="680" font-family="Noto Sans KR, sans-serif" font-size="96" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="-2">{card['big']}</text>
  <text x="540" y="820" font-family="Noto Sans KR, sans-serif" font-size="26" font-weight="400" fill="#ffffff" fill-opacity="0.85" text-anchor="middle" letter-spacing="-0.3">{card['cta_lines'][0]}</text>
  <text x="540" y="870" font-family="Noto Sans KR, sans-serif" font-size="26" font-weight="400" fill="#ffffff" fill-opacity="0.85" text-anchor="middle" letter-spacing="-0.3">{card['cta_lines'][1]}</text>
  <text x="540" y="965" font-family="Noto Sans KR, sans-serif" font-size="28" font-weight="700" fill="#D5001C" text-anchor="middle" letter-spacing="1">{card['handle']}</text>
</svg>
"""


def main():
    os.makedirs(SVG_OUT, exist_ok=True)
    for card in cards:
        t = card["type"]
        if t == "cover":
            svg = build_cover(card)
        elif t == "intro":
            svg = build_body(card, is_intro=True)
        elif t == "body":
            svg = build_body(card, is_intro=False)
        elif t == "closing":
            svg = build_closing(card)
        path = os.path.join(SVG_OUT, f"card-{card['num']:02d}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        size_kb = os.path.getsize(path) // 1024
        print(f"✓ card-{card['num']:02d}.svg ({size_kb} KB)")


if __name__ == "__main__":
    main()
