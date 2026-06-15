"""
Agent de veille des taux de change – CFO Chine
Version enrichie avec données officielles (akshare)
==================================================
Sources :
- Taux de marché : Frankfurter (API gratuite, base ECB)
- Taux officiels Chine : Banque Populaire de Chine (PBOC) via akshare
- Analyse d'impact : DeepSeek (fluctuations > seuils)

Fréquence : quotidienne (lundi-vendredi, 8h Shanghai)
Variables : DEEPSEEK_API_KEY (optionnelle)
Dépendance : pip install akshare
"""

import os
import json
import logging
import requests
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

# Pour l'analyse LLM (optionnelle mais recommandée)
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

# Pour les données officielles chinoises
try:
    import akshare as ak
    HAS_AKSHARE = True
except ImportError:
    HAS_AKSHARE = False
    print("⚠️ akshare non installé. Exécutez 'pip install akshare' pour activer les données PBOC.")

load_dotenv()

# Configuration des logs
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

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------
CURRENCIES = ["CNY", "USD", "EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "HKD"]
BASE_CURRENCY = "EUR"  # L'API Frankfurter utilise EUR comme base

# Seuils de fluctuation jugés significatifs (en pourcentage)
THRESHOLD_1D = 0.8      # >0.8% en une journée
THRESHOLD_7D = 2.0      # >2% sur 7 jours
THRESHOLD_30D = 4.0     # >4% sur 30 jours

# API gratuite (Frankfurter - données de la BCE, sans clé)
API_URL = "https://api.frankfurter.app/latest"

# ------------------------------------------------------------
# 1. Données de marché (Frankfurter)
# ------------------------------------------------------------
def get_current_rates(base=BASE_CURRENCY):
    """Récupère les taux actuels depuis l'API Frankfurter."""
    try:
        params = {"from": base, "to": ",".join(CURRENCIES)}
        resp = requests.get(API_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        rates = data.get("rates", {})
        date = data.get("date")
        log.info(f"Taux de marché récupérés pour le {date}")
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
# 2. Données officielles PBOC (via akshare)
# ------------------------------------------------------------
def get_pboc_mid_rate(currency_cn="美元", date_str=None):
    """
    Récupère le taux de référence central PBOC pour une devise donnée.
    currency_cn : nom de la devise en chinois (ex: "美元" pour USD, "欧元" pour EUR)
    date_str : format "YYYYMMDD"
    """
    if not HAS_AKSHARE:
        log.warning("akshare non installé. Impossible de récupérer les données PBOC.")
        return None
    
    if date_str is None:
        date_str = datetime.now().strftime("%Y%m%d")
    
    try:
        # Interface akshare pour les taux historiques de la Banque de Chine
        df = ak.currency_boc_sina(symbol=currency_cn, date=date_str)
        if df is not None and len(df) > 0:
            # La colonne '央行中间价' contient le taux de référence central
            mid_rate = df.iloc[0]['央行中间价']
            log.info(f"PBOC {currency_cn} mid-rate le {date_str}: {mid_rate}")
            return float(mid_rate)
    except Exception as e:
        log.warning(f"Erreur récupération PBOC pour {currency_cn}: {e}")
    return None

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
    """
    Récupère les taux PBOC pour les devises majeures (USD, EUR, JPY, GBP, HKD)
    et les stocke dans l'historique.
    """
    pboc_history = load_pboc_history()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Mapping devise anglaise -> nom chinois pour l'API
    currency_map = {
        "USD": "美元",
        "EUR": "欧元",
        "JPY": "日元",
        "GBP": "英镑",
        "HKD": "港币",
    }
    
    pboc_rates = {}
    for ccy, ccy_cn in currency_map.items():
        rate = get_pboc_mid_rate(ccy_cn)
        if rate:
            pboc_rates[ccy] = rate
    
    if pboc_rates:
        pboc_history[today] = pboc_rates
        # Garder 60 jours
        if len(pboc_history) > 60:
            oldest = sorted(pboc_history.keys())[0]
            del pboc_history[oldest]
        save_pboc_history(pboc_history)
        log.info(f"Historique PBOC mis à jour : {len(pboc_rates)} devise(s)")
    
    return pboc_rates

def compare_with_pboc(current_rates, pboc_rates):
    """
    Compare les taux de marché Frankfurter avec les taux officiels PBOC.
    Retourne les écarts significatifs.
    """
    deviations = []
    for ccy in pboc_rates:
        if ccy in current_rates:
            market_rate = current_rates[ccy]
            pboc_rate = pboc_rates[ccy]
            deviation_pct = (market_rate - pboc_rate) / pboc_rate * 100
            if abs(deviation_pct) > 0.5:  # Écart > 0.5% considéré comme significatif
                deviations.append({
                    "currency": ccy,
                    "market_rate": market_rate,
                    "pboc_rate": pboc_rate,
                    "deviation_pct": deviation_pct
                })
    return deviations

# ------------------------------------------------------------
# 3. Détection des fluctuations
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
            alerts.append({
                "currency": currency,
                "type": "daily",
                "variation": var_day,
                "current": current,
                "previous": prev_day,
                "period": "1 jour"
            })
        if var_week is not None and abs(var_week) >= THRESHOLD_7D:
            alerts.append({
                "currency": currency,
                "type": "weekly",
                "variation": var_week,
                "current": current,
                "previous": prev_week,
                "period": "7 jours"
            })
        if var_month is not None and abs(var_month) >= THRESHOLD_30D:
            alerts.append({
                "currency": currency,
                "type": "monthly",
                "variation": var_month,
                "current": current,
                "previous": prev_month,
                "period": "30 jours"
            })
    return alerts

# ------------------------------------------------------------
# 4. Analyse d'impact via DeepSeek
# ------------------------------------------------------------
def analyze_impact_with_llm(alerts, pboc_deviations):
    if not HAS_ANTHROPIC:
        log.warning("Module anthropic non installé. Pas d'analyse LLM.")
        return None
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        log.warning("DEEPSEEK_API_KEY non définie. Analyse LLM ignorée.")
        return None

    client = anthropic.Anthropic(base_url="https://api.deepseek.com/anthropic", api_key=api_key)

    alert_text = ""
    for a in alerts:
        direction = "hausse" if a["variation"] > 0 else "baisse"
        alert_text += f"- {a['currency']} : {direction} de {abs(a['variation']):.2f}% sur {a['period']} (taux actuel {a['current']:.4f})\n"
    
    deviation_text = ""
    for d in pboc_deviations:
        direction = "au-dessus" if d["deviation_pct"] > 0 else "en dessous"
        deviation_text += f"- {d['currency']} : écart de {abs(d['deviation_pct']):.2f}% {direction} du taux PBOC (marché {d['market_rate']:.4f} vs PBOC {d['pboc_rate']:.4f})\n"

    if not alert_text and not deviation_text:
        return "Aucune fluctuation significative ni écart anormal par rapport au taux PBOC à signaler."

    prompt = f"""Tu es un expert en finance internationale et trésorerie, conseillant un CFO d'une multinationale ayant des opérations en Chine.

Voici les fluctuations de change significatives détectées aujourd'hui :

{alert_text}
{deviation_text}

Analyse pour chaque devise et écart :
1. Causes possibles (macroéconomiques, politiques, interventions PBOC, saisonnières)
2. Impact concret sur la trésorerie, le besoin en fonds de roulement, les coûts d'approvisionnement ou les revenus à l'export pour une entreprise opérant en Chine
3. Actions recommandées pour le CFO : couverture (hedging), avancement ou retard de paiements, renégociation de contrats, réallocation de trésorerie

Termine par une synthèse exécutive de 5 lignes pour le brief matinal du CFO, en mettant en évidence les risques change liés à la Chine.

Réponse en français, professionnelle et concise.
"""
    try:
        msg = client.messages.create(
            model="deepseek-v4-pro",
            max_tokens=2048,
            system="Tu es un conseiller senior en gestion des risques de change, spécialiste des marchés émergents et de la Chine.",
            messages=[{"role": "user", "content": prompt}]
        )
        response_text = ""
        for block in msg.content:
            if hasattr(block, 'type') and block.type == "text":
                response_text += block.text
            elif hasattr(block, 'text'):
                response_text += block.text
        return response_text if response_text else "Analyse non disponible."
    except Exception as e:
        log.error(f"Erreur lors de l'appel DeepSeek : {e}")
        return None

# ------------------------------------------------------------
# 5. Génération du rapport
# ------------------------------------------------------------
def generate_report(alerts, current_rates, date, pboc_rates, pboc_deviations, llm_analysis):
    lines = []
    lines.append("=" * 70)
    lines.append(f"  VEILLE TAUX DE CHANGE – {date}")
    lines.append("  Pour : CFO – Opérations Chine & International")
    lines.append("=" * 70)
    lines.append("")
    lines.append("  📊 TAUX DE MARCHÉ ACTUELS (base EUR) :")
    for ccy in CURRENCIES:
        if ccy in current_rates:
            lines.append(f"    {ccy} : {current_rates[ccy]:.4f}")
    lines.append("")
    
    if pboc_rates:
        lines.append("  🏦 TAUX OFFICIELS PBOC (taux de référence central) :")
        for ccy, rate in pboc_rates.items():
            lines.append(f"    {ccy}/CNY : {rate:.4f}")
        lines.append("")
    
    lines.append("-" * 70)
    lines.append("  📈 FLUCTUATIONS SIGNIFICATIVES DÉTECTÉES")
    lines.append("-" * 70)
    if alerts:
        for a in alerts:
            sign = "+" if a["variation"] > 0 else "-"
            lines.append(f"  • {a['currency']} : {sign}{abs(a['variation']):.2f}% sur {a['period']} (→ {a['current']:.4f})")
    else:
        lines.append("  Aucune fluctuation dépassant les seuils définis.")
    lines.append("")
    
    if pboc_deviations:
        lines.append("-" * 70)
        lines.append("  🏦 ÉCARTS MARCHÉ vs PBOC (significatifs)")
        lines.append("-" * 70)
        for d in pboc_deviations:
            direction = "au-dessus du" if d["deviation_pct"] > 0 else "en dessous du"
            lines.append(f"  • {d['currency']} : écart de {abs(d['deviation_pct']):.2f}% {direction} taux officiel PBOC")
        lines.append("")
    
    if llm_analysis:
        lines.append("-" * 70)
        lines.append("  💡 ANALYSE D'IMPACT & RECOMMANDATIONS (DeepSeek)")
        lines.append("-" * 70)
        lines.append(llm_analysis)
    else:
        lines.append("-" * 70)
        lines.append("  ℹ️ Analyse LLM non disponible – clé API manquante ou module absent")
        if pboc_rates:
            lines.append("  Les données PBOC sont néanmoins disponibles pour information.")
    
    lines.append("")
    lines.append("=" * 70)
    return "\n".join(lines)

def save_report(report):
    filename = REPORT_FILE.parent / f"forex_chine_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    log.info(f"Rapport sauvegardé : {filename}")
    return filename

# ------------------------------------------------------------
# 6. Exécution principale
# ------------------------------------------------------------
def run_forex_agent():
    log.info("Démarrage de l'agent de veille des taux de change (version enrichie PBOC)")
    
    # Étape 1 : Données de marché Frankfurter
    rates, date = get_current_rates()
    if not rates:
        log.error("Impossible de récupérer les taux de marché. Arrêt.")
        return
    
    history = load_history()
    update_history(rates, date)
    
    # Étape 2 : Données officielles PBOC
    pboc_rates = {}
    pboc_deviations = []
    if HAS_AKSHARE:
        pboc_rates = update_pboc_history()
        if pboc_rates:
            pboc_deviations = compare_with_pboc(rates, pboc_rates)
    
    # Étape 3 : Détection des fluctuations
    alerts = detect_significant_movements(rates, date, history)
    
    # Étape 4 : Analyse LLM (si des alertes ou écarts existent)
    llm_analysis = None
    if alerts or pboc_deviations:
        log.info(f"{len(alerts)} fluctuation(s) détectée(s), {len(pboc_deviations)} écart(s) PBOC. Appel DeepSeek.")
        llm_analysis = analyze_impact_with_llm(alerts, pboc_deviations)
    else:
        log.info("Aucune fluctuation ou écart significatif détecté.")
    
    # Étape 5 : Rapport
    report = generate_report(alerts, rates, date, pboc_rates, pboc_deviations, llm_analysis)
    print(report)
    save_report(report)
    log.info("Agent terminé.")

if __name__ == "__main__":
    run_forex_agent()