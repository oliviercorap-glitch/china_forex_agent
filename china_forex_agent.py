"""
Agent de veille des taux de change – CFO Chine
Version corrigée (taux PBOC en unité de base + filtrage date)
==================================================
Sources :
- Taux de marché : Frankfurter
- Taux officiels Chine : PBOC via akshare (converti en base 1)
Seuil d'ancienneté : 7 jours max pour les données PBOC
Variables : DEEPSEEK_API_KEY (optionnelle)
"""

import os
import json
import logging
import requests
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import akshare as ak
    HAS_AKSHARE = True
except ImportError:
    HAS_AKSHARE = False

load_dotenv()

LOG_FILE = Path("logs/agent_forex.log")
HISTORY_FILE = Path("forex_history.json")
PBOC_HISTORY_FILE = Path("pboc_history.json")
REPORT_FILE = Path("rapports/forex_chine_latest.txt")
Path("logs").mkdir(exist_ok=True)
Path("rapports").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(LOG_FILE, encoding="utf-8")],
)
log = logging.getLogger(__name__)

CURRENCIES = ["CNY", "USD", "EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "HKD"]
BASE_CURRENCY = "EUR"
THRESHOLD_1D = 0.8
THRESHOLD_7D = 2.0
THRESHOLD_30D = 4.0
API_URL = "https://api.frankfurter.app/latest"

# ------------------------------------------------------------
# 1. Données de marché (Frankfurter)
# ------------------------------------------------------------
def get_current_rates(base=BASE_CURRENCY):
    try:
        params = {"from": base, "to": ",".join(CURRENCIES)}
        resp = requests.get(API_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        rates = data.get("rates", {})
        date = data.get("date")
        log.info(f"Taux de marché récupérés pour {date}")
        return rates, date
    except Exception as e:
        log.error(f"Erreur API Frankfurter : {e}")
        return None, None

def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def update_history(current_rates, date):
    history = load_history()
    history[date] = current_rates
    if len(history) > 60:
        oldest = sorted(history.keys())[0]
        del history[oldest]
    save_history(history)
    return history

def get_rate_at_date(history, currency, target_date):
    dates = sorted(history.keys())
    for d in reversed(dates):
        if d <= target_date and currency in history[d]:
            return history[d][currency]
    return None

def calculate_variation(current, previous):
    if previous is None or previous == 0:
        return None
    return (current - previous) / previous * 100

# ------------------------------------------------------------
# 2. Données PBOC (correction : conversion en base 1)
# ------------------------------------------------------------
def get_latest_pboc_rate(currency_cn="美元"):
    """Retourne (taux_pour_1_unite, date_string) ou (None, None)"""
    if not HAS_AKSHARE:
        return None, None
    try:
        df = ak.currency_boc_sina(symbol=currency_cn)
        if df is not None and len(df) > 0:
            latest = df.iloc[0]
            date_val = latest['日期']
            if hasattr(date_val, 'strftime'):
                date_str = date_val.strftime("%Y-%m-%d")
            else:
                date_str = str(date_val)
            # Le taux est pour 100 unités de devise étrangère
            rate_per_100 = float(latest['央行中间价'])
            rate_per_1 = rate_per_100 / 100.0
            log.info(f"PBOC {currency_cn} : {rate_per_100} / 100 = {rate_per_1} ({date_str})")
            return rate_per_1, date_str
    except Exception as e:
        log.warning(f"Erreur PBOC pour {currency_cn}: {e}")
    return None, None

def load_pboc_history():
    if PBOC_HISTORY_FILE.exists():
        with open(PBOC_HISTORY_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def save_pboc_history(history):
    with open(PBOC_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def update_pboc_history():
    pboc_history = load_pboc_history()
    today = datetime.now().strftime("%Y-%m-%d")
    currency_map = {"USD": "美元", "EUR": "欧元", "JPY": "日元", "GBP": "英镑", "HKD": "港币"}
    pboc_rates = {}
    for ccy, ccy_cn in currency_map.items():
        rate, date_str = get_latest_pboc_rate(ccy_cn)
        if rate:
            pboc_rates[ccy] = {"rate": rate, "date": date_str}
    if pboc_rates:
        pboc_history[today] = pboc_rates
        if len(pboc_history) > 60:
            oldest = sorted(pboc_history.keys())[0]
            del pboc_history[oldest]
        save_pboc_history(pboc_history)
        log.info(f"Historique PBOC mis à jour : {len(pboc_rates)} devise(s)")
    return pboc_rates

def get_current_pboc_rates():
    """Renvoie les taux PBOC les plus récents (moins de 7 jours)"""
    pboc_history = load_pboc_history()
    if not pboc_history:
        return {}
    # Trier par date décroissante
    dates = sorted(pboc_history.keys(), reverse=True)
    today = datetime.now()
    for d in dates:
        try:
            d_obj = datetime.strptime(d, "%Y-%m-%d")
            if (today - d_obj).days <= 7:
                return pboc_history[d]
        except:
            continue
    # Si tous sont trop vieux, prendre le plus récent
    return pboc_history[dates[0]] if dates else {}

def compare_with_pboc(current_rates, pboc_rates):
    """Compare les taux de marché aux taux PBOC (déjà convertis en base 1)"""
    deviations = []
    # Pour chaque devise présente dans pboc_rates
    for ccy, pboc_data in pboc_rates.items():
        pboc_rate = pboc_data.get("rate")
        if not pboc_rate:
            continue
        # On cherche le taux de marché correspondant (USD/CNY ou EUR/CNY)
        if ccy == "USD" and "CNY" in current_rates and "USD" in current_rates:
            market_usd_cny = current_rates["CNY"] / current_rates["USD"]
            deviation = (market_usd_cny - pboc_rate) / pboc_rate * 100
            if abs(deviation) > 0.5:
                deviations.append({
                    "pair": "USD/CNY",
                    "market_rate": market_usd_cny,
                    "pboc_rate": pboc_rate,
                    "deviation_pct": deviation
                })
        if ccy == "EUR" and "CNY" in current_rates:
            market_eur_cny = current_rates["CNY"]
            deviation = (market_eur_cny - pboc_rate) / pboc_rate * 100
            if abs(deviation) > 0.5:
                deviations.append({
                    "pair": "EUR/CNY",
                    "market_rate": market_eur_cny,
                    "pboc_rate": pboc_rate,
                    "deviation_pct": deviation
                })
    return deviations

# ------------------------------------------------------------
# 3. Fluctuations (inchangé)
# ------------------------------------------------------------
def detect_significant_movements(current_rates, date, history):
    alerts = []
    yesterday = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    week_ago = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=7)).strftime("%Y-%m-%d")
    month_ago = (datetime.strptime(date, "%Y-%m-%d") - timedelta(days=30)).strftime("%Y-%m-%d")
    for currency in CURRENCIES:
        if currency == BASE_CURRENCY:
            continue
        current = current_rates.get(currency)
        if current is None:
            continue
        prev_day = get_rate_at_date(history, currency, yesterday)
        var_day = calculate_variation(current, prev_day) if prev_day else None
        prev_week = get_rate_at_date(history, currency, week_ago)
        var_week = calculate_variation(current, prev_week) if prev_week else None
        prev_month = get_rate_at_date(history, currency, month_ago)
        var_month = calculate_variation(current, prev_month) if prev_month else None
        if var_day is not None and abs(var_day) >= THRESHOLD_1D:
            alerts.append({"currency": currency, "variation": var_day, "period": "1 jour", "current": current})
        if var_week is not None and abs(var_week) >= THRESHOLD_7D:
            alerts.append({"currency": currency, "variation": var_week, "period": "7 jours", "current": current})
        if var_month is not None and abs(var_month) >= THRESHOLD_30D:
            alerts.append({"currency": currency, "variation": var_month, "period": "30 jours", "current": current})
    return alerts

# ------------------------------------------------------------
# 4. Analyse LLM (identique)
# ------------------------------------------------------------
def analyze_impact_with_llm(alerts, pboc_deviations):
    if not HAS_ANTHROPIC:
        return None
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        return None
    client = anthropic.Anthropic(base_url="https://api.deepseek.com/anthropic", api_key=api_key)
    alert_text = ""
    for a in alerts:
        direction = "hausse" if a["variation"] > 0 else "baisse"
        alert_text += f"- {a['currency']} : {direction} de {abs(a['variation']):.2f}% sur {a['period']} (→ {a['current']:.4f})\n"
    deviation_text = ""
    for d in pboc_deviations:
        direction = "au-dessus" if d["deviation_pct"] > 0 else "en dessous"
        deviation_text += f"- {d['pair']} : écart de {abs(d['deviation_pct']):.2f}% {direction} du fixing PBOC (marché {d['market_rate']:.4f} vs PBOC {d['pboc_rate']:.4f})\n"
    if not alert_text and not deviation_text:
        return "Aucune fluctuation ni écart significatif."
    prompt = f"""Tu es un expert en finance internationale, conseillant un CFO en Chine.

Fluctuations :\n{alert_text}
Écarts PBOC :\n{deviation_text}

Analyse les impacts trésorerie, change, couverture. Termine par 5 lignes de synthèse pour le CFO.

En français, concis."""
    try:
        msg = client.messages.create(
            model="deepseek-v4-pro",
            max_tokens=2048,
            system="Expert risques de change.",
            messages=[{"role": "user", "content": prompt}]
        )
        response_text = ""
        for block in msg.content:
            if hasattr(block, 'type') and block.type == "text":
                response_text += block.text
            elif hasattr(block, 'text'):
                response_text += block.text
        return response_text or "Analyse non disponible."
    except Exception as e:
        log.error(f"Erreur LLM: {e}")
        return None

# ------------------------------------------------------------
# 5. Rapport
# ------------------------------------------------------------
def generate_report(alerts, current_rates, date, pboc_rates, pboc_deviations, llm_analysis):
    lines = []
    lines.append("=" * 70)
    lines.append(f"  VEILLE TAUX DE CHANGE – {date}")
    lines.append("  Pour : CFO – Opérations Chine & International")
    lines.append("=" * 70)
    lines.append("\n  📊 TAUX DE MARCHÉ ACTUELS (base EUR) :")
    for ccy in CURRENCIES:
        if ccy in current_rates:
            lines.append(f"    {ccy} : {current_rates[ccy]:.4f}")
    lines.append("")
    if pboc_rates:
        lines.append("  🏦 TAUX OFFICIELS PBOC (dernier fixing, exprimé en unité de base) :")
        for ccy, data in pboc_rates.items():
            rate = data.get("rate", "N/A")
            date_str = data.get("date", "inconnue")
            lines.append(f"    {ccy}/CNY : {rate:.4f} (fixing du {date_str})")
        lines.append("")
    lines.append("-" * 70)
    lines.append("  📈 FLUCTUATIONS SIGNIFICATIVES")
    lines.append("-" * 70)
    if alerts:
        for a in alerts:
            sign = "+" if a["variation"] > 0 else "-"
            lines.append(f"  • {a['currency']} : {sign}{abs(a['variation']):.2f}% sur {a['period']} (→ {a['current']:.4f})")
    else:
        lines.append("  Aucune fluctuation notable.")
    lines.append("")
    if pboc_deviations:
        lines.append("-" * 70)
        lines.append("  🏦 ÉCARTS MARCHÉ vs FIXING PBOC")
        lines.append("-" * 70)
        for d in pboc_deviations:
            direction = "au-dessus" if d["deviation_pct"] > 0 else "en dessous"
            lines.append(f"  • {d['pair']} : écart de {abs(d['deviation_pct']):.2f}% {direction} du fixing")
        lines.append("")
    if llm_analysis:
        lines.append("-" * 70)
        lines.append("  💡 ANALYSE & RECOMMANDATIONS")
        lines.append("-" * 70)
        lines.append(llm_analysis)
    else:
        lines.append("-" * 70)
        lines.append("  ℹ️ Analyse approfondie non disponible")
    lines.append("\n" + "=" * 70)
    return "\n".join(lines)

def save_report(report):
    filename = REPORT_FILE.parent / f"forex_chine_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    log.info(f"Rapport sauvegardé : {filename}")

# ------------------------------------------------------------
# 6. Exécution
# ------------------------------------------------------------
def run_forex_agent():
    log.info("Démarrage agent change (version corrigée)")
    rates, date = get_current_rates()
    if not rates:
        log.error("Impossible de récupérer les taux de marché.")
        return
    history = load_history()
    update_history(rates, date)
    alerts = detect_significant_movements(rates, date, history)
    pboc_rates = get_current_pboc_rates()  # utilise les dernières données (<7 jours)
    pboc_deviations = compare_with_pboc(rates, pboc_rates) if pboc_rates else []
    llm_analysis = None
    if alerts or pboc_deviations:
        llm_analysis = analyze_impact_with_llm(alerts, pboc_deviations)
    report = generate_report(alerts, rates, date, pboc_rates, pboc_deviations, llm_analysis)
    print(report)
    save_report(report)
    log.info("Agent terminé.")

if __name__ == "__main__":
    run_forex_agent()
