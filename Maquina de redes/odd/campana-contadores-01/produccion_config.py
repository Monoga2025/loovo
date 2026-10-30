"""
Preconfiguración de producción para Video #1: Nicho Contadores Colombia
Campaña: D1 / D2 / D3 — Crisis Contable 2030
"""

PRODUCCION_CONFIG = {
    "campana_id": "campana-contadores-01",
    "titulo": "Crisis Contable 2030 — Los 3 Sistemas IA",
    "duracion_segundos": 45,
    "formato": "9:16",
    "resolucion": (1080, 1920),
    "fps": 30,
    "audio": {
        "lufs_target": -17.6,
        "lra_target": 4.5,
        "true_peak": -2.0,
        "ducking_db": -18.0
    },
    "cortes": [
        {
            "tramo": "00:00 - 00:04",
            "tipo": "hook_ia_higgsfield",
            "fuente": "crudo/01_reportera_ia.mp4",
            "sfx": "sfx/alerta_noticiero.wav",
            "lower_third": "URGENTE: CRISIS CONTABLE 2030"
        },
        {
            "tramo": "00:04 - 00:05",
            "tipo": "rompe_patron",
            "efecto": "glitch_invert_flash",
            "sfx": "sfx/crunch_glass_break.wav"
        },
        {
            "tramo": "00:05 - 00:10",
            "tipo": "camara_real_puente",
            "fuente": "crudo/02_camara_real_hablado.mp4",
            "texto_pantalla": "CALMA. ESTAMOS EN 2026."
        },
        {
            "tramo": "00:10 - 00:20",
            "tipo": "sistema_1_dian",
            "b_roll": "broll/sistema_1_agente_dian.mp4",
            "overlay": "AGENTE TRIBUTARIO IA (2.4s)",
            "sfx": "sfx/whoosh_ding.wav"
        },
        {
            "tramo": "00:20 - 00:30",
            "tipo": "sistema_2_extractor",
            "b_roll": "broll/sistema_2_ocr_excel.mp4",
            "overlay": "EXTRACTOR INTELIGENTE OCR -> XLS / SIIGO",
            "sfx": "sfx/laser_scan_pop.wav"
        },
        {
            "tramo": "00:30 - 00:38",
            "tipo": "sistema_3_conciliador",
            "b_roll": "broll/sistema_3_conciliacion.mp4",
            "overlay": "CONCILIADOR BANCOLOMBIA / DAVIVIENDA",
            "sfx": "sfx/alert_error_beep.wav"
        },
        {
            "tramo": "00:38 - 00:45",
            "tipo": "cta_d1_d2_d3",
            "fuente": "crudo/02_camara_real_hablado.mp4",
            "triggers": [
                {"id": "D1", "sticker": "logo_tiendas_d1.png", "sfx": "sfx/kaching_caja.wav"},
                {"id": "D2", "sticker": "meme_dedos_d2.png", "sfx": "sfx/pop_cartoon.wav"},
                {"id": "D3", "sticker": "pack_completo_d3.png", "sfx": "sfx/whoosh_shine.wav"}
            ]
        }
    ]
}

if __name__ == "__main__":
    import json
    print(json.dumps(PRODUCCION_CONFIG, indent=2, ensure_ascii=False))
