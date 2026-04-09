#!/usr/bin/env python3
"""
generate_report.py — Génère un rapport PDF d'analyse financière.

Récupère les données et news d'une action via Yahoo Finance, analyse le sentiment
et les thèmes, et compose un rapport PDF professionnel.

Usage:
    python3 generate_report.py NVDA
    python3 generate_report.py AAPL
    python3 generate_report.py TSLA

Output:
    .tmp/finance_report_{TICKER}.pdf (à la racine du starter kit)
"""

import os
import sys
import subprocess
from datetime import datetime
from collections import Counter

try:
    import yfinance as yf
except ImportError:
    print("Erreur: la librairie 'yfinance' n'est pas installée.")
    print("Installation : pip3 install yfinance --break-system-packages")
    sys.exit(1)

try:
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
except ImportError:
    print("Erreur: la librairie 'reportlab' n'est pas installée.")
    print("Installation : pip3 install reportlab --break-system-packages")
    sys.exit(1)


# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STARTER_KIT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", ".."))
TMP_DIR = os.path.join(STARTER_KIT_ROOT, ".tmp")


# ── Palette ──────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
BG = HexColor("#0B1120")
CARD = HexColor("#1E293B")
CARD_BLUE = HexColor("#1E3A8A")
CARD_GREEN = HexColor("#0F2A1F")
CARD_RED = HexColor("#3B0F12")
BORDER = HexColor("#334155")
ACCENT = HexColor("#3B82F6")
ACCENT2 = HexColor("#10B981")
WARN = HexColor("#F59E0B")
DANGER = HexColor("#EF4444")
TEXT = HexColor("#F1F5F9")
MUTED = HexColor("#94A3B8")

FONT = "Helvetica"
FONT_B = "Helvetica-Bold"
MARGIN = 50


# ── Sentiment analysis (keyword-based, basic) ────────────────────────────────

POSITIVE_KEYWORDS = {
    "beat", "beats", "exceed", "exceeds", "exceeded", "growth", "soar", "surge",
    "rally", "gain", "gains", "rise", "rises", "rising", "boost", "boosted",
    "strong", "record", "high", "highs", "buy", "bullish", "outperform",
    "upgrade", "upgraded", "positive", "profit", "profits", "win", "wins",
    "winning", "success", "successful", "momentum", "breakthrough", "best",
    "improve", "improved", "improvement", "advance", "advances", "expand",
    "expanding", "innovation", "innovative", "leader", "leading",
}

NEGATIVE_KEYWORDS = {
    "miss", "misses", "missed", "fall", "falls", "fell", "drop", "drops",
    "dropped", "decline", "declines", "declined", "loss", "losses", "lost",
    "weak", "weakness", "low", "lows", "sell", "bearish", "underperform",
    "downgrade", "downgraded", "negative", "concern", "concerns", "worry",
    "worried", "warn", "warning", "warned", "risk", "risks", "risky",
    "fail", "fails", "failed", "failure", "crash", "crashes", "crashed",
    "plunge", "plunges", "plunged", "tumble", "tumbles", "tumbled",
    "lawsuit", "investigation", "fine", "penalty",
}

THEME_KEYWORDS = {
    "AI / IA": {"ai", "artificial", "intelligence", "ia", "agi", "llm", "model",
                "models", "chatgpt", "claude", "gemini", "neural", "machine learning"},
    "Earnings / Résultats": {"earnings", "revenue", "profit", "quarter", "quarterly",
                             "q1", "q2", "q3", "q4", "annual", "fiscal", "report", "reports"},
    "Produits": {"product", "products", "launch", "launches", "launched", "release",
                 "releases", "released", "iphone", "android", "device", "devices"},
    "Régulation / Légal": {"sec", "regulation", "regulatory", "lawsuit", "court",
                           "legal", "ftc", "doj", "antitrust", "investigation"},
    "Direction": {"ceo", "cfo", "executive", "founder", "leadership", "management",
                  "board", "appointed", "resigned", "hired", "fired"},
    "Marché / Stock": {"stock", "shares", "share", "market", "investor", "investors",
                       "price", "valuation", "trading", "trade"},
    "Concurrence": {"competitor", "competitors", "rival", "rivals", "competition",
                    "compete", "competing", "vs"},
    "Innovation / R&D": {"innovation", "innovative", "research", "development", "patent",
                         "breakthrough", "discovery", "technology", "tech"},
}


def analyze_sentiment(text):
    """Return (sentiment_label, score) where score is in [-1, 1]."""
    if not text:
        return "neutre", 0.0
    words = text.lower().split()
    pos = sum(1 for w in words if w.strip(".,!?;:()") in POSITIVE_KEYWORDS)
    neg = sum(1 for w in words if w.strip(".,!?;:()") in NEGATIVE_KEYWORDS)
    total = pos + neg
    if total == 0:
        return "neutre", 0.0
    score = (pos - neg) / total
    if score > 0.2:
        return "positif", score
    elif score < -0.2:
        return "négatif", score
    return "neutre", score


def extract_themes(news_items, top_n=5):
    """Return list of (theme, count) sorted by count desc."""
    counter = Counter()
    for item in news_items:
        text = (item.get("title", "") + " " + item.get("summary", "")).lower()
        for theme, keywords in THEME_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                counter[theme] += 1
    return counter.most_common(top_n)


# ── Yahoo Finance fetching ──────────────────────────────────────────────────

def fetch_company_data(ticker_symbol):
    """Fetch company info, price data, and news from Yahoo Finance."""
    print(f"Récupération des données pour {ticker_symbol}...")
    ticker = yf.Ticker(ticker_symbol)

    info = {}
    try:
        info = ticker.info or {}
    except Exception as e:
        print(f"  Avertissement (info): {e}")

    # Price history (last 30 days)
    hist = None
    try:
        hist = ticker.history(period="1mo")
    except Exception as e:
        print(f"  Avertissement (history): {e}")

    # News (last 10 articles)
    news = []
    try:
        raw_news = ticker.news or []
        for item in raw_news[:10]:
            content = item.get("content", item)
            news.append({
                "title": content.get("title", ""),
                "summary": content.get("summary", "") or content.get("description", ""),
                "publisher": content.get("provider", {}).get("displayName", "") if isinstance(content.get("provider"), dict) else (content.get("publisher", "") or ""),
                "link": content.get("canonicalUrl", {}).get("url", "") if isinstance(content.get("canonicalUrl"), dict) else content.get("link", ""),
            })
    except Exception as e:
        print(f"  Avertissement (news): {e}")

    return {
        "ticker": ticker_symbol.upper(),
        "name": info.get("longName") or info.get("shortName") or ticker_symbol.upper(),
        "sector": info.get("sector", "Inconnu"),
        "industry": info.get("industry", "Inconnue"),
        "current_price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "previous_close": info.get("previousClose"),
        "market_cap": info.get("marketCap"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
        "currency": info.get("currency", "USD"),
        "history": hist,
        "news": news,
    }


def format_market_cap(value):
    """Format market cap as $X.YT / $X.YB / $X.YM."""
    if not value:
        return "N/A"
    if value >= 1e12:
        return f"${value / 1e12:.2f}T"
    if value >= 1e9:
        return f"${value / 1e9:.2f}B"
    if value >= 1e6:
        return f"${value / 1e6:.2f}M"
    return f"${value:.0f}"


def format_price_change(current, previous):
    """Return (change_str, percent_str, color)."""
    if not current or not previous:
        return "N/A", "N/A", MUTED
    change = current - previous
    percent = (change / previous) * 100
    color = ACCENT2 if change >= 0 else DANGER
    sign = "+" if change >= 0 else ""
    return f"{sign}{change:.2f}", f"{sign}{percent:.2f}%", color


# ── PDF rendering ────────────────────────────────────────────────────────────

def draw_card(c, x, y, w, h, fill=CARD, border=BORDER, radius=8):
    c.setFillColor(fill)
    c.setStrokeColor(border)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def wrap_text(c, text, max_width, font, size):
    """Split text into lines that fit within max_width."""
    words = text.split()
    if not words:
        return [""]
    lines = []
    line = words[0]
    for w in words[1:]:
        test = line + " " + w
        if c.stringWidth(test, font, size) > max_width:
            lines.append(line)
            line = w
        else:
            line = test
    lines.append(line)
    return lines


def draw_page_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def draw_footer(c, page_num, total_pages, ticker):
    c.setFillColor(MUTED)
    c.setFont(FONT, 8)
    c.drawString(MARGIN, 25, f"Rapport d'analyse {ticker} — généré par Claude Code Starter Kit")
    c.drawRightString(PAGE_W - MARGIN, 25, f"{page_num} / {total_pages}")


def render_report(data, output_path):
    """Render the full PDF report."""
    print("Génération du PDF...")
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setTitle(f"{data['ticker']} — Analyse financière")
    c.setAuthor("Claude Code Starter Kit")

    total_pages = 3

    # ── Page 1 : COVER + KEY METRICS ───────────────────────────────────────
    draw_page_bg(c)

    # Top accent bar
    c.setFillColor(ACCENT)
    c.rect(MARGIN, PAGE_H - 80, 6, 50, fill=1, stroke=0)

    # Eyebrow
    c.setFillColor(ACCENT)
    c.setFont(FONT_B, 10)
    c.drawString(MARGIN + 16, PAGE_H - 50, "RAPPORT D'ANALYSE FINANCIÈRE")

    # Ticker (huge)
    c.setFillColor(TEXT)
    c.setFont(FONT_B, 64)
    c.drawString(MARGIN + 16, PAGE_H - 130, data["ticker"])

    # Company name
    c.setFillColor(TEXT)
    c.setFont(FONT_B, 18)
    company_name = data["name"]
    if len(company_name) > 50:
        company_name = company_name[:47] + "..."
    c.drawString(MARGIN + 16, PAGE_H - 160, company_name)

    # Sector / Industry
    c.setFillColor(MUTED)
    c.setFont(FONT, 11)
    c.drawString(MARGIN + 16, PAGE_H - 180, f"{data['sector']}  •  {data['industry']}")

    # Generation date
    c.setFillColor(MUTED)
    c.setFont(FONT, 9)
    date_str = datetime.now().strftime("%d %B %Y à %Hh%M")
    c.drawString(MARGIN + 16, PAGE_H - 195, f"Généré le {date_str}")

    # ── Key metrics cards ──────────────────────────────────────────────────
    cards_y = PAGE_H - 320
    card_w = (PAGE_W - 2 * MARGIN - 30) / 2
    card_h = 100

    # Current price card
    change_str, percent_str, change_color = format_price_change(
        data["current_price"], data["previous_close"]
    )
    draw_card(c, MARGIN, cards_y, card_w, card_h, fill=CARD_BLUE, border=ACCENT)
    c.setFillColor(MUTED)
    c.setFont(FONT_B, 9)
    c.drawString(MARGIN + 16, cards_y + card_h - 18, "PRIX ACTUEL")
    c.setFillColor(TEXT)
    c.setFont(FONT_B, 32)
    price_str = f"${data['current_price']:.2f}" if data['current_price'] else "N/A"
    c.drawString(MARGIN + 16, cards_y + card_h - 55, price_str)
    c.setFillColor(change_color)
    c.setFont(FONT_B, 12)
    c.drawString(MARGIN + 16, cards_y + 18, f"{change_str}  ({percent_str})")
    c.setFillColor(MUTED)
    c.setFont(FONT, 9)
    c.drawString(MARGIN + 16, cards_y + 6, "vs clôture précédente")

    # Market cap card
    mcap_x = MARGIN + card_w + 30
    draw_card(c, mcap_x, cards_y, card_w, card_h, fill=CARD_GREEN, border=ACCENT2)
    c.setFillColor(MUTED)
    c.setFont(FONT_B, 9)
    c.drawString(mcap_x + 16, cards_y + card_h - 18, "CAPITALISATION")
    c.setFillColor(TEXT)
    c.setFont(FONT_B, 32)
    c.drawString(mcap_x + 16, cards_y + card_h - 55, format_market_cap(data["market_cap"]))
    c.setFillColor(MUTED)
    c.setFont(FONT, 9)
    c.drawString(mcap_x + 16, cards_y + 18, f"Devise : {data['currency']}")

    # 52-week range
    range_y = cards_y - 120
    draw_card(c, MARGIN, range_y, PAGE_W - 2 * MARGIN, 90, fill=CARD, border=BORDER)
    c.setFillColor(ACCENT)
    c.setFont(FONT_B, 9)
    c.drawString(MARGIN + 16, range_y + 70, "FOURCHETTE 52 SEMAINES")
    c.setFillColor(MUTED)
    c.setFont(FONT, 10)
    c.drawString(MARGIN + 16, range_y + 50, "Plus bas")
    c.drawRightString(PAGE_W - MARGIN - 16, range_y + 50, "Plus haut")

    low = data["fifty_two_week_low"]
    high = data["fifty_two_week_high"]
    c.setFillColor(TEXT)
    c.setFont(FONT_B, 16)
    c.drawString(MARGIN + 16, range_y + 28, f"${low:.2f}" if low else "N/A")
    c.drawRightString(PAGE_W - MARGIN - 16, range_y + 28, f"${high:.2f}" if high else "N/A")

    # Range bar visual
    bar_x = MARGIN + 16
    bar_y = range_y + 14
    bar_w = PAGE_W - 2 * MARGIN - 32
    bar_h = 4
    c.setFillColor(BORDER)
    c.roundRect(bar_x, bar_y, bar_w, bar_h, 2, fill=1, stroke=0)
    if low and high and data["current_price"]:
        position = (data["current_price"] - low) / max(high - low, 1)
        position = max(0, min(1, position))
        marker_x = bar_x + position * bar_w
        c.setFillColor(ACCENT)
        c.circle(marker_x, bar_y + bar_h / 2, 5, fill=1, stroke=0)

    # Page 1 footer
    draw_footer(c, 1, total_pages, data["ticker"])
    c.showPage()

    # ── Page 2 : NEWS RÉCENTES ─────────────────────────────────────────────
    draw_page_bg(c)

    c.setFillColor(ACCENT)
    c.rect(MARGIN, PAGE_H - 60, 6, 30, fill=1, stroke=0)
    c.setFillColor(TEXT)
    c.setFont(FONT_B, 22)
    c.drawString(MARGIN + 16, PAGE_H - 50, "News récentes")
    c.setFillColor(MUTED)
    c.setFont(FONT, 11)
    c.drawString(MARGIN + 16, PAGE_H - 68, f"Les dernières nouvelles sur {data['ticker']}")

    y = PAGE_H - 100

    if not data["news"]:
        c.setFillColor(MUTED)
        c.setFont(FONT, 11)
        c.drawString(MARGIN + 16, y - 20, "Aucune news récente disponible pour ce ticker.")
    else:
        for i, item in enumerate(data["news"][:8], 1):
            if y < 100:
                break

            title = item["title"]
            publisher = item["publisher"] or "Source inconnue"
            sentiment, score = analyze_sentiment(title + " " + item.get("summary", ""))

            sentiment_color = {
                "positif": ACCENT2,
                "négatif": DANGER,
                "neutre": MUTED,
            }[sentiment]

            # News card
            card_h = 70
            draw_card(c, MARGIN, y - card_h, PAGE_W - 2 * MARGIN, card_h, fill=CARD, border=BORDER)

            # Sentiment marker
            c.setFillColor(sentiment_color)
            c.circle(MARGIN + 14, y - 14, 4, fill=1, stroke=0)

            # Title (wrapped)
            c.setFillColor(TEXT)
            c.setFont(FONT_B, 11)
            title_lines = wrap_text(c, title, PAGE_W - 2 * MARGIN - 50, FONT_B, 11)
            for j, line in enumerate(title_lines[:2]):
                c.drawString(MARGIN + 24, y - 14 - j * 13, line)

            # Publisher + sentiment
            c.setFillColor(MUTED)
            c.setFont(FONT, 9)
            c.drawString(MARGIN + 24, y - 50, publisher)
            c.setFillColor(sentiment_color)
            c.setFont(FONT_B, 9)
            c.drawRightString(PAGE_W - MARGIN - 14, y - 50, f"Sentiment : {sentiment}")

            y -= card_h + 8

    draw_footer(c, 2, total_pages, data["ticker"])
    c.showPage()

    # ── Page 3 : ANALYSE & RECOMMANDATION ──────────────────────────────────
    draw_page_bg(c)

    c.setFillColor(ACCENT)
    c.rect(MARGIN, PAGE_H - 60, 6, 30, fill=1, stroke=0)
    c.setFillColor(TEXT)
    c.setFont(FONT_B, 22)
    c.drawString(MARGIN + 16, PAGE_H - 50, "Analyse")
    c.setFillColor(MUTED)
    c.setFont(FONT, 11)
    c.drawString(MARGIN + 16, PAGE_H - 68, "Sentiment global et thèmes principaux")

    # Compute global sentiment from all news
    if data["news"]:
        scores = [analyze_sentiment(n["title"] + " " + n.get("summary", ""))[1]
                  for n in data["news"]]
        avg_score = sum(scores) / len(scores)
    else:
        avg_score = 0.0

    if avg_score > 0.15:
        global_sentiment = "POSITIF"
        sent_color = ACCENT2
        sent_bg = CARD_GREEN
        sent_explanation = "Les news récentes sont majoritairement positives. Le marché semble optimiste sur cette compagnie à court terme."
    elif avg_score < -0.15:
        global_sentiment = "NÉGATIF"
        sent_color = DANGER
        sent_bg = CARD_RED
        sent_explanation = "Les news récentes sont majoritairement négatives. Plusieurs signaux préoccupants ressortent dans les publications récentes."
    else:
        global_sentiment = "NEUTRE"
        sent_color = MUTED
        sent_bg = CARD
        sent_explanation = "Les news récentes sont mitigées. Pas de tendance claire à court terme."

    # Sentiment card
    sent_y = PAGE_H - 220
    sent_h = 110
    draw_card(c, MARGIN, sent_y, PAGE_W - 2 * MARGIN, sent_h, fill=sent_bg, border=sent_color)
    c.setFillColor(MUTED)
    c.setFont(FONT_B, 9)
    c.drawString(MARGIN + 16, sent_y + sent_h - 18, "SENTIMENT GLOBAL")
    c.setFillColor(sent_color)
    c.setFont(FONT_B, 36)
    c.drawString(MARGIN + 16, sent_y + sent_h - 60, global_sentiment)
    c.setFillColor(TEXT)
    c.setFont(FONT, 10)
    explanation_lines = wrap_text(c, sent_explanation, PAGE_W - 2 * MARGIN - 32, FONT, 10)
    explain_y = sent_y + 28
    for line in explanation_lines[:2]:
        c.drawString(MARGIN + 16, explain_y, line)
        explain_y -= 13

    # Themes section
    themes = extract_themes(data["news"])
    themes_y = sent_y - 30

    c.setFillColor(ACCENT)
    c.setFont(FONT_B, 11)
    c.drawString(MARGIN, themes_y, "THÈMES PRINCIPAUX")
    themes_y -= 18

    if themes:
        for theme, count in themes:
            c.setFillColor(ACCENT)
            c.circle(MARGIN + 4, themes_y + 3, 3, fill=1, stroke=0)
            c.setFillColor(TEXT)
            c.setFont(FONT_B, 11)
            c.drawString(MARGIN + 14, themes_y, theme)
            c.setFillColor(MUTED)
            c.setFont(FONT, 10)
            c.drawString(MARGIN + 200, themes_y, f"{count} mentions")
            themes_y -= 18
    else:
        c.setFillColor(MUTED)
        c.setFont(FONT, 10)
        c.drawString(MARGIN, themes_y, "Aucun thème majeur identifié dans les news disponibles.")
        themes_y -= 18

    # Disclaimer
    disclaimer_h = 80
    disclaimer_y = MARGIN + 60
    draw_card(c, MARGIN, disclaimer_y, PAGE_W - 2 * MARGIN, disclaimer_h,
              fill=CARD, border=WARN)
    c.setFillColor(WARN)
    c.setFont(FONT_B, 9)
    c.drawString(MARGIN + 16, disclaimer_y + disclaimer_h - 18, "AVERTISSEMENT IMPORTANT")
    c.setFillColor(TEXT)
    c.setFont(FONT, 9)
    disclaimer_text = (
        "Ce rapport est généré automatiquement à des fins éducatives uniquement. "
        "Il ne constitue PAS un conseil d'investissement. Les décisions financières "
        "ne doivent jamais être prises sur la seule base d'un outil automatisé. "
        "Consulte un conseiller financier qualifié avant d'investir."
    )
    disclaimer_lines = wrap_text(c, disclaimer_text, PAGE_W - 2 * MARGIN - 32, FONT, 9)
    dy = disclaimer_y + disclaimer_h - 36
    for line in disclaimer_lines:
        c.drawString(MARGIN + 16, dy, line)
        dy -= 12

    draw_footer(c, 3, total_pages, data["ticker"])
    c.showPage()

    c.save()
    print(f"  PDF généré : {output_path}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_report.py TICKER")
        print("Exemples : python3 generate_report.py NVDA")
        print("           python3 generate_report.py AAPL")
        sys.exit(1)

    ticker = sys.argv[1].upper().strip()

    print()
    print("=" * 60)
    print(f"  Rapport financier — {ticker}")
    print("=" * 60)
    print()

    # Ensure .tmp/ exists
    os.makedirs(TMP_DIR, exist_ok=True)

    # Fetch
    data = fetch_company_data(ticker)

    if not data["current_price"] and not data["news"]:
        print(f"\nErreur : aucune donnée trouvée pour le ticker '{ticker}'.")
        print("Vérifie que le ticker est correct (NVDA, AAPL, TSLA, MSFT...).")
        sys.exit(1)

    print(f"  Compagnie : {data['name']}")
    print(f"  Secteur : {data['sector']}")
    print(f"  News récupérées : {len(data['news'])}")
    print()

    # Render
    output_path = os.path.join(TMP_DIR, f"finance_report_{ticker}.pdf")
    render_report(data, output_path)

    print()
    print("=" * 60)
    print("  TERMINÉ")
    print("=" * 60)
    print(f"\nLe rapport est dans : {output_path}")

    # Open the PDF on macOS
    if sys.platform == "darwin":
        try:
            subprocess.run(["open", output_path], check=False)
            print("Ouverture du PDF...")
        except Exception:
            pass


if __name__ == "__main__":
    main()
