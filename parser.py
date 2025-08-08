import os
import json
import re
import html
import unicodedata
from typing import List, Dict


def clean_html(raw: str) -> str:
    if raw is None:
        return ""
    text = html.unescape(str(raw))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def slugify(value: str, maxlen: int = 120) -> str:
    if not value:
        return "job"
    value = unicodedata.normalize("NFKD", str(value))
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return value[:maxlen] or "job"


def build_job_text(job: Dict) -> str:
    title = job.get("title", "").strip()
    industry = job.get("industry", "").strip()
    category = job.get("category", "").strip()
    experience = job.get("experience", "").strip()
    skills = job.get("skills") or job.get("skill") or []
    if not isinstance(skills, list):
        # If skills is a comma separated string, convert to list
        if isinstance(skills, str):
            skills = [s.strip() for s in skills.split(",") if s.strip()]
        else:
            skills = []

    client = job.get("client_name", "").strip()
    job_id = job.get("job_id", "").strip()
    display_job_id = job.get("display_job_id", "").strip()
    location_type = job.get("location_type", "").strip()
    wfa = job.get("work_from_anywhere_in_world", None)

    summary = clean_html(job.get("summary"))
    responsibilities = clean_html(job.get("responsibilities"))
    requirements = clean_html(job.get("requirements"))

    lines = [
        f"Title: {title}",
        f"Job ID: {job_id}" if job_id else "",
        f"Display Job ID: {display_job_id}" if display_job_id else "",
        f"Client: {client}",
        f"Industry: {industry}",
        f"Category: {category}",
        f"Experience Level: {experience}",
        f"Location Type: {location_type}",
    ]

    if wfa is not None:
        lines.append(f"Work From Anywhere: {'Yes' if bool(wfa) else 'No'}")

    lines.append("")  # blank line

    lines.append("SUMMARY:")
    lines.append(summary or "N/A")
    lines.append("")

    lines.append("RESPONSIBILITIES:")
    lines.append(responsibilities or "N/A")
    lines.append("")

    lines.append("REQUIREMENTS:")
    lines.append(requirements or "N/A")
    lines.append("")

    lines.append("SKILLS:")
    if skills:
        for skill in skills:
            lines.append(f"- {skill}")
    else:
        lines.append("None listed")

    # filter out any empty strings before joining
    lines = [line for line in lines if line.strip() != ""]

    return "\n".join(lines)


def save_jobs_from_json(input_json: str, output_dir: str) -> List[str]:
    os.makedirs(output_dir, exist_ok=True)

    with open(input_json, "r", encoding="utf-8") as f:
        jobs = json.load(f)  # expects JSON array

    written_files = []

    for idx, job in enumerate(jobs, start=1):
        try:
            title = job.get("title") or job.get("job_id") or f"job_{idx}"
            filename = f"{slugify(title, 60)}.txt"
            filepath = os.path.join(output_dir, filename)
            content = build_job_text(job)

            with open(filepath, "w", encoding="utf-8") as out_f:
                out_f.write(content)

            written_files.append(filepath)
            print(f"[{idx}/{len(jobs)}] Saved: {filepath}")

        except Exception as e:
            print(f"[{idx}] Error writing file: {e}")

    return written_files


if __name__ == "__main__":
    input_file = "jd.json"  # path to your JSON file
    output_folder = "job_texts"
    save_jobs_from_json(input_file, output_folder)
    print("All jobs processed.")
