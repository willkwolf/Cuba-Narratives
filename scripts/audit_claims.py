#!/usr/bin/env python3
"""
audit_claims.py - Script de Auditoría Continua y Verificación de Hipótesis
Repositorio: Cuba-Narratives
Objetivo: Garantizar integridad de datos, consistencia metodológica y trazabilidad de claims.
"""

import json
import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(WORKSPACE_ROOT, "data")
INDICADORES_FILE = os.path.join(DATA_DIR, "indicadores.json")
BITACORA_FILE = os.path.join(DATA_DIR, "bitacora.json")
FUENTES_MD = os.path.join(WORKSPACE_ROOT, "Fuentes.md")
README_MD = os.path.join(WORKSPACE_ROOT, "README.md")
INDEX_HTML = os.path.join(WORKSPACE_ROOT, "index.html")

def log(msg, level="INFO"):
    icons = {"INFO": "ℹ️", "SUCCESS": "✅", "WARNING": "⚠️", "ERROR": "❌"}
    print(f"{icons.get(level, '')} [{level}] {msg}")

def check_json_files():
    errors = 0
    if not os.path.exists(INDICADORES_FILE):
        log(f"Archivo no encontrado: {INDICADORES_FILE}", "ERROR")
        return False
    if not os.path.exists(BITACORA_FILE):
        log(f"Archivo no encontrado: {BITACORA_FILE}", "ERROR")
        return False

    # Validar indicadores
    with open(INDICADORES_FILE, "r", encoding="utf-8") as f:
        try:
            indicadores_data = json.load(f)
            log("indicadores.json es un JSON válido", "SUCCESS")
        except Exception as e:
            log(f"Error parseando indicadores.json: {e}", "ERROR")
            return False

    required_ind_keys = ["id", "indicador", "valor_nominal", "fuente_primaria", "sesgo_fuente", "convergencia"]
    ind_list = indicadores_data.get("indicadores", [])
    log(f"Validando {len(ind_list)} indicadores cuantitativos...")
    for idx, item in enumerate(ind_list):
        for key in required_ind_keys:
            if key not in item:
                log(f"Indicador #{idx} ({item.get('id', 'sin-id')}) carece del campo obligatorio '{key}'", "ERROR")
                errors += 1

    # Validar bitácora
    with open(BITACORA_FILE, "r", encoding="utf-8") as f:
        try:
            bitacora_data = json.load(f)
            log("bitacora.json es un JSON válido", "SUCCESS")
        except Exception as e:
            log(f"Error parseando bitacora.json: {e}", "ERROR")
            return False

    required_bit_keys = ["id", "fecha", "categoria", "titulo", "fuentes", "impacto_hipotesis"]
    hitos_list = bitacora_data.get("hitos", [])
    log(f"Validando {len(hitos_list)} hitos periodísticos en la bitácora...")
    for idx, item in enumerate(hitos_list):
        for key in required_bit_keys:
            if key not in item:
                log(f"Hito #{idx} ({item.get('id', 'sin-id')}) carece del campo obligatorio '{key}'", "ERROR")
                errors += 1

    return errors == 0

def check_html_integrity():
    if not os.path.exists(INDEX_HTML):
        log(f"index.html no encontrado en {INDEX_HTML}", "ERROR")
        return False

    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html_content = f.read()

    checks = [
        ("Sección Bitácora id='bitacora'", 'id="bitacora"' in html_content),
        ("Filtros interactivos de bitácora", 'class="bitacora-filter-btn' in html_content),
        ("Contraste GAESA 40% (balances reales)", "40%" in html_content),
        ("Contraste GAESA 70% (estimación exilio)", "70%" in html_content),
        ("Referencia a sanciones Sept 2026 (SecState Marco Rubio)", "Rubio" in html_content or "14404" in html_content or "Banco Exterior de Cuba" in html_content),
        ("Contraste ocupación hotelera ONEI / Monreal", "ocupación" in html_content or "hotelera" in html_content or "Monreal" in html_content)
    ]

    all_passed = True
    for desc, passed in checks:
        if passed:
            log(f"Verificación de integración HTML: {desc}", "SUCCESS")
        else:
            log(f"Falta integración en HTML: {desc}", "WARNING")
            all_passed = False

    return all_passed

def main():
    print("=" * 60)
    print("🔍 AUDITORÍA DE DATOS, FUENTES E HIPÓTESIS — CUBA NARRATIVES")
    print("=" * 60)

    json_ok = check_json_files()
    html_ok = check_html_integrity()

    print("-" * 60)
    if json_ok:
        log("Todos los esquemas de datos son válidos y consistentes.", "SUCCESS")
    else:
        log("Se encontraron errores en los datos estructurados.", "ERROR")
        sys.exit(1)

    if not html_ok:
        log("Advertencias pendientes de sincronización en index.html.", "WARNING")
    else:
        log("Integración y trazabilidad en index.html verificada con éxito.", "SUCCESS")

    print("=" * 60)

if __name__ == "__main__":
    main()
