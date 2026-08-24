#!/usr/bin/env python3
"""_os, _network, _database, _datastructure, _algorithm 폴더를 스캔해
README.md의 TIL-INDEX 마커 사이 내용을 카테고리별 목록으로 갱신한다."""
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"
START_MARKER = "<!-- TIL-INDEX:START -->"
END_MARKER = "<!-- TIL-INDEX:END -->"

CATEGORY_DIRS = {
    "_os": "OS",
    "_network": "Network",
    "_database": "Database",
    "_datastructure": "DataStructure",
    "_algorithm": "Algorithm",
}

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_front_matter(text):
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"')
    return fields


def collect_entries():
    entries = []
    for dir_name, category in CATEGORY_DIRS.items():
        folder = REPO_ROOT / dir_name
        if not folder.is_dir():
            continue
        for md_file in folder.glob("*.md"):
            fields = parse_front_matter(md_file.read_text(encoding="utf-8"))
            title = fields.get("title", md_file.stem)
            date = fields.get("date", "")
            entries.append(
                {
                    "category": category,
                    "title": title,
                    "date": date,
                    "path": md_file.relative_to(REPO_ROOT).as_posix(),
                }
            )
    return entries


def render_index(entries):
    by_category = {}
    for entry in entries:
        by_category.setdefault(entry["category"], []).append(entry)

    lines = []
    for category in CATEGORY_DIRS.values():
        items = by_category.get(category, [])
        if not items:
            continue
        items.sort(key=lambda e: e["date"], reverse=True)
        lines.append(f"### {category}")
        for item in items:
            date_part = f" ({item['date']})" if item["date"] else ""
            lines.append(f"- [{item['title']}]({item['path']}){date_part}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def update_readme(index_body):
    content = README_PATH.read_text(encoding="utf-8")
    if START_MARKER not in content or END_MARKER not in content:
        raise SystemExit("README.md에 TIL-INDEX 마커가 없습니다.")
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    replacement = f"{START_MARKER}\n{index_body}\n{END_MARKER}"
    new_content = pattern.sub(replacement, content)
    if new_content != content:
        README_PATH.write_text(new_content, encoding="utf-8")
        print("README.md updated.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    update_readme(render_index(collect_entries()))
