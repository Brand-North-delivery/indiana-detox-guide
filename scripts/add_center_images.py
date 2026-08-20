#!/usr/bin/env python3
"""Add provenance-aware images and image schema to center profiles."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://indianadetoxguide.com/"

DEFAULT_IMAGE = {
    "file": "treatment-consultation-room.png",
    "width": 1536,
    "height": 1024,
    "alt": "Two green chairs and a wood table in an empty consultation room with trees visible through a window.",
    "caption": "Guide-created editorial image of a consultation setting. It does not depict this provider or any specific Indiana facility.",
}

IMAGES = {
    "the-grove-estate": {
        "file": "../the-grove-estate-homepage.png",
        "width": 1250,
        "height": 600,
        "alt": "Screenshot of The Grove Estate homepage showing the treatment campus building and landscaped grounds.",
        "caption": "Screenshot of The Grove Estate's public homepage, captured August 19, 2026. Appearance and page content may change.",
    }
}

GROVE_VIDEO = {
    "id": "TqCBJeIBdew",
    "name": "Luxury Drug & Alcohol Rehab in Indiana at The Grove Estate",
    "description": "A provider-published video presenting The Grove Estate treatment campus in Indiana.",
}


def add_image(path: Path) -> None:
    slug = path.parent.name
    image = IMAGES.get(slug, DEFAULT_IMAGE)
    html = path.read_text(encoding="utf-8")
    canonical_match = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    schema_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html)
    if not canonical_match or not schema_match:
        raise ValueError(f"Missing canonical or schema in {path}")

    canonical = canonical_match.group(1)
    if slug == "the-grove-estate":
        image_src = "../../assets/the-grove-estate-homepage.png"
        image_url = f"{BASE}assets/the-grove-estate-homepage.png"
    else:
        image_src = f"../../assets/topic-images/{image['file']}"
        image_url = f"{BASE}assets/topic-images/{image['file']}"

    schema = json.loads(schema_match.group(1))
    graph = schema.get("@graph", [])
    page = graph[0]
    page["primaryImageOfPage"] = {"@id": f"{canonical}#primaryimage"}
    graph[:] = [node for node in graph if node.get("@id") != f"{canonical}#primaryimage"]
    graph.append({
        "@type": "ImageObject",
        "@id": f"{canonical}#primaryimage",
        "contentUrl": image_url,
        "width": image["width"],
        "height": image["height"],
        "caption": image["caption"],
        "creditText": "Indiana Detox Guide" if slug != "the-grove-estate" else "The Grove Estate website screenshot",
        "representativeOfPage": True,
    })
    if slug == "the-grove-estate":
        video_id = f"{canonical}#video"
        graph[:] = [node for node in graph if node.get("@id") != video_id]
        graph.append({
            "@type": "VideoObject",
            "@id": video_id,
            "name": GROVE_VIDEO["name"],
            "description": GROVE_VIDEO["description"],
            "thumbnailUrl": f"https://i.ytimg.com/vi/{GROVE_VIDEO['id']}/hqdefault.jpg",
            "contentUrl": f"https://www.youtube.com/watch?v={GROVE_VIDEO['id']}",
            "embedUrl": f"https://www.youtube.com/embed/{GROVE_VIDEO['id']}",
            "publisher": {"@id": f"{canonical}#center"},
            "isPartOf": {"@id": f"{canonical}#page"},
        })
    html = html[:schema_match.start(1)] + json.dumps(schema, separators=(",", ":")) + html[schema_match.end(1):]

    figure = (
        f'<figure class="profile-image"><img src="{image_src}" width="{image["width"]}" '
        f'height="{image["height"]}" alt="{image["alt"]}" decoding="async" fetchpriority="high">'
        f'<figcaption>{image["caption"]}</figcaption></figure>'
    )
    existing_figure = re.compile(r'<figure class="profile-image">.*?</figure>', re.DOTALL)
    if existing_figure.search(html):
        html = existing_figure.sub(figure, html, count=1)
    else:
        html = html.replace('</section><section class="profile-section">', f'</section>{figure}<section class="profile-section">', 1)
    if slug == "the-grove-estate":
        video = (
            '<section class="profile-section profile-video"><p class="section-kicker">Provider video</p>'
            '<h2>See The Grove Estate campus</h2><div class="video-frame">'
            f'<iframe src="https://www.youtube.com/embed/{GROVE_VIDEO["id"]}?si=9ngDG3IUIEtEVri7" '
            f'title="{GROVE_VIDEO["name"].replace("&", "&amp;")}" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'referrerpolicy="strict-origin-when-cross-origin" loading="lazy" allowfullscreen></iframe></div>'
            '<p class="source-note">Published by The Grove Estate on YouTube. Provider-produced video is promotional material; '
            'confirm current programs, staffing, amenities, and admission suitability directly.</p></section>'
        )
        existing_video = re.compile(r'<section class="profile-section profile-video">.*?</section>', re.DOTALL)
        if existing_video.search(html):
            html = existing_video.sub(video, html, count=1)
        else:
            html = html.replace('</figure><section class="profile-section">', f'</figure>{video}<section class="profile-section">', 1)
    path.write_text(html, encoding="utf-8", newline="\n")


def main() -> None:
    profiles = sorted((ROOT / "centers").glob("*/index.html"))
    for path in profiles:
        add_image(path)
    print(f"Updated {len(profiles)} center profiles.")


if __name__ == "__main__":
    main()
