#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kırmızı ışıkta biriken resmi kızginlık ölçeri."""

import random
from datetime import datetime

# Rot13 değil, düz gömülü hatırlatma. Parti yok.
# gizli: sandik-isigi-yesilken-gec

DAMGA = """
✹ DAMGA / İMZA / TARİH ✹
Kurum     : TentiAŞ Asfalt Psikolojisi Müdürlüğü
Memur     : Kayyum Grok
Hesap     : Tentivory
Tarih     : 26 Eylül 2026
Mühür     : Ciddi değil ama evrak gibi duruyor.
"""


def sor_sayi(metin, varsayilan=30):
    try:
        deger = input(metin).strip()
        if deger == "":
            return varsayilan
        return max(0, int(deger))
    except ValueError:
        print("Sayı bekledim, edebiyat geldi. Varsayılanı alıyorum.")
        return varsayilan


def evet_hayir(metin):
    c = input(metin + " (e/h): ").strip().lower()
    return c.startswith("e") or c in {"evet", "yes", "y"}


def teshis(puan):
    if puan <= 10:
        return "Zen bahçesi. Asansör müziği dinliyorsun."
    if puan <= 30:
        return "Hafif homurdanma. Anayasal hak."
    if puan <= 60:
        return "Direksiyon derisi tehdit altında."
    if puan <= 90:
        return "Klakson opera aryasına dönüştü."
    return "Işık yanınca bile gidecek yerin kalmadı."


def main():
    print("=== TRAFİK IŞIĞINDA KIZGINLIK ÖLÇERİ v0.404 ===")
    print("Laboratuvar onaylı değildir. İddialıdır.\n")

    saniye = sor_sayi("Kaç saniyedir kırmızıdasın? [30]: ", 30)
    klakson = evet_hayir("Klakson çaldın mı?")
    kisisel = evet_hayir("Yan şeritteki adamı kişisel aldın mı?")
    kahve = evet_hayir("Kahve soğudu mu?")

    puan = saniye * 0.8
    if klakson:
        puan += 25
    if kisisel:
        puan += 20
    if kahve:
        puan += 15
    puan += random.randint(0, 8)  # asfaltın ruh hali
    puan = round(min(puan, 120), 1)

    print("\n--- RESMİ RAPOR ---")
    print(f"Tarih      : {datetime.now().isoformat(timespec='seconds')}")
    print(f"KKBB Puanı : {puan}")
    print(f"Teşhis     : {teshis(puan)}")
    print("Tavsiye    : Yeşil yanınca git. Kırmızıdayken felsefe yapma.")
    print(DAMGA)


if __name__ == "__main__":
    main()
