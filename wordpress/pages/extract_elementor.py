#!/usr/bin/env python3
"""Ringkas _elementor_data (output wp_get_post_meta) jadi daftar widget + teks + gambar.
    python3 extract_elementor.py <meta.json> <out-dir>   → simpan elementor-source.json + cetak ringkasan
"""
import html, json, re, sys
from pathlib import Path

SKIP = ("tooltip", "typography", "color", "align", "size", "tag", "gradient", "transition", "animation", "_id")
strip = lambda s: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def summarize(val):
    """Ambil teks, url gambar/tautan dari nilai setting (string, dict media/link, atau repeater)."""
    if isinstance(val, str):
        return strip(val)[:400] or None
    if isinstance(val, dict):
        return (f"{val.get('id')}|{val['url']}" if val.get("id") else val["url"]) if val.get("url") else None
    if isinstance(val, list) and val and isinstance(val[0], dict):
        items = [{k: summarize(v) for k, v in it.items() if not k.startswith("_") and summarize(v)} for it in val]
        return [i for i in items if i] or None


def walk(nodes):
    for e in nodes:
        w = e.get("widgetType")
        s = e.get("settings", {})
        if w or s.get("background_overlay_image") or s.get("background_image"):
            out = {k: summarize(v) for k, v in s.items()
                   if not k.startswith(("_", "premium", "element_pack", "eael_vto", "pa_")) and not any(x in k for x in SKIP)
                   and summarize(v)}
            print(e["id"], w or e["elType"], json.dumps(out, ensure_ascii=False))
        walk(e.get("elements", []))


v = json.load(open(sys.argv[1]))["value"]
data = json.loads(v) if isinstance(v, str) else v
Path(sys.argv[2], "elementor-source.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
walk(data)
