from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "references/data-policy.md",
    "references/report-policy.md",
    "assets/report-skeleton.html",
)
REQUIRED_SKILL_MARKERS = (
    "disable-model-invocation: true",
    "First-use introduction",
    "100 条正式报告 Gate",
    "Report Questions",
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    skills_root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else repo_root / "skills"
    skill_dirs = sorted(
        path for path in skills_root.iterdir() if path.is_dir() and re.fullmatch(r"voc-\d{2}-.+", path.name)
    )
    errors: list[str] = []
    canonical_hash: str | None = None

    if len(skill_dirs) != 25:
        errors.append(f"expected 25 VOC skills, got {len(skill_dirs)}")

    expected_numbers = list(range(1, 26))
    actual_numbers = [int(path.name[4:6]) for path in skill_dirs]
    if actual_numbers != expected_numbers:
        errors.append(f"expected skill numbers 01-25, got {actual_numbers}")

    for skill_dir in skill_dirs:
        files = [skill_dir / relative_path for relative_path in REQUIRED_FILES]
        for file_path in files:
            if not file_path.is_file():
                errors.append(f"{skill_dir.name}: missing {file_path.relative_to(skill_dir)}")
        if any(not file_path.is_file() for file_path in files):
            continue

        skill_text = files[0].read_text(encoding="utf-8-sig")
        runtime_text = "\n".join(
            file_path.read_text(encoding="utf-8-sig", errors="ignore") for file_path in files
        )

        name_match = re.search(r"(?m)^name:\s*([^\s]+)\s*$", skill_text)
        if not name_match or name_match.group(1) != skill_dir.name:
            found = name_match.group(1) if name_match else "<missing>"
            errors.append(f"{skill_dir.name}: frontmatter name is {found}")

        report_hash = hashlib.sha256(files[3].read_bytes()).hexdigest()
        canonical_hash = canonical_hash or report_hash
        if report_hash != canonical_hash:
            errors.append(f"{skill_dir.name}: report template hash mismatch")

        for marker in REQUIRED_SKILL_MARKERS:
            if marker not in skill_text:
                errors.append(f"{skill_dir.name}: missing {marker}")

        if re.search(r"https?://|www\.", runtime_text, flags=re.IGNORECASE):
            errors.append(f"{skill_dir.name}: external link in runtime files")
        if re.search(r"op_sk_[A-Za-z0-9_-]+", runtime_text):
            errors.append(f"{skill_dir.name}: API key leak")

    result = {
        "skill_count": len(skill_dirs),
        "canonical_hash": canonical_hash,
        "errors": errors,
        "status": "PASS" if not errors else "FAIL",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
