#!/usr/bin/env python3
"""Static consistency check for the repository harness.

Checks roles and their tool registrations, skills and their discovery links,
the workflow and decision indexes, relative Markdown links and anchors, and
unfilled placeholders. Reads AGENTS.md and CLAUDE.md files, docs/, .agents/,
.claude/ and .codex/. Uses only the Python standard library (3.8 or later).

Run from the repository root:
    python3 .agents/skills/change-harness/scripts/check_harness.py
Options:
    --root PATH            harness root (default: found from the working directory)
    --allow-placeholders   do not report {{NAME}} placeholders (unadopted template only)
Exit status is 1 when any check fails.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

DESCRIPTION_LIMIT = 1024
THIN_REGISTRATION_LIMIT = 1500  # characters of registration body
HARNESS_DIRS = ("docs/", ".agents/", ".claude/", ".codex/")
HARNESS_FILES = ("AGENTS.md", "CLAUDE.md")
LINK_EXEMPT_PREFIXES = ("docs/templates/",)  # formats whose links are written for their destination
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}


class Report:
    def __init__(self):
        self.errors = []
        self.counts = {}

    def error(self, area, message):
        self.errors.append((area, message))

    def count(self, area, n):
        self.counts[area] = n


def find_root(start):
    here = Path(start).resolve()
    for candidate in [here] + list(here.parents):
        if (candidate / "AGENTS.md").is_file() and (candidate / "docs" / "README.md").is_file():
            return candidate
    try:
        top = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=str(here), capture_output=True, text=True, check=True,
        ).stdout.strip()
        if top:
            return Path(top)
    except (OSError, subprocess.CalledProcessError):
        pass
    return here


def rel(root, path):
    try:
        return Path(path).relative_to(root).as_posix()
    except ValueError:
        return Path(path).as_posix()


def read(path):
    return Path(path).read_text(encoding="utf-8")


def harness_files(root, suffixes):
    """Harness files with the given suffixes: tracked and untracked, minus ignored."""
    paths = None
    try:
        out = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=str(root), capture_output=True, text=True, check=True,
        ).stdout
        paths = [p for p in out.split("\0") if p]
    except (OSError, subprocess.CalledProcessError):
        paths = None
    if paths is None:  # not a Git checkout
        paths = [name for name in HARNESS_FILES if (root / name).is_file()]
        for top in HARNESS_DIRS:
            for dirpath, dirnames, filenames in os.walk(root / top):
                dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
                paths.extend(rel(root, Path(dirpath) / name) for name in filenames)
    for p in sorted(set(paths)):
        in_scope = p.startswith(HARNESS_DIRS) or p.rsplit("/", 1)[-1] in HARNESS_FILES
        if in_scope and p.endswith(suffixes) and (root / p).is_file():
            yield root / p


# ---------- frontmatter and registration parsing ----------

def parse_frontmatter(text):
    """Return a dict of simple `key: value` frontmatter fields, or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields = {}
    key = None
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            key, value = match.group(1), match.group(2).strip()
            if value in (">", "|", ">-", "|-"):
                value = ""
            fields[key] = unquote_value(value)
        elif key and line.startswith((" ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return None  # no closing delimiter


def unquote_value(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def body_after_frontmatter(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                return "\n".join(lines[i + 1:])
    return text


def parse_toml(text):
    """Parse a registration. Raises ValueError when it cannot be read."""
    try:
        import tomllib  # Python 3.11+
    except ImportError:
        tomllib = None
    if tomllib is not None:
        return tomllib.loads(text)
    data = {}
    for match in re.finditer(r"^(\w+)\s*=\s*(\"\"\"|''')(.*?)\2", text, re.S | re.M):
        data[match.group(1)] = match.group(3)
    for match in re.finditer(r'^(\w+)\s*=\s*"((?:[^"\\]|\\.)*)"\s*$', text, re.M):
        data.setdefault(match.group(1), match.group(2).replace('\\"', '"'))
    for match in re.finditer(r"^(\w+)\s*=\s*'([^']*)'\s*$", text, re.M):
        data.setdefault(match.group(1), match.group(2))
    if "name" not in data:
        raise ValueError("no name field could be read")
    return data


# ---------- checks ----------

def check_roles(root, report):
    agents_dir = root / "docs" / "agents"
    if not agents_dir.is_dir():
        report.error("roles", "docs/agents/ is missing")
        return
    briefs = sorted(p.stem for p in agents_dir.glob("*.md") if p.name not in ("README.md", "common.md"))
    report.count("roles", len(briefs))
    index_path = agents_dir / "README.md"
    index = read(index_path) if index_path.is_file() else ""
    if not index:
        report.error("roles", "docs/agents/README.md (role index) is missing")

    tools = []
    if (root / ".claude" / "agents").is_dir():
        tools.append(("Claude Code", root / ".claude" / "agents", ".md"))
    if (root / ".codex" / "agents").is_dir():
        tools.append(("Codex", root / ".codex" / "agents", ".toml"))

    for role in briefs:
        if index and "({}.md)".format(role) not in index:
            report.error("roles", "{}: no row in docs/agents/README.md".format(role))

    descriptions = {}
    for tool, directory, suffix in tools:
        registered = sorted(p.stem for p in directory.glob("*" + suffix))
        for role in briefs:
            if role not in registered:
                report.error("roles", "{}: no {} registration at {}".format(role, tool, rel(root, directory / (role + suffix))))
        for role in registered:
            path = directory / (role + suffix)
            where = rel(root, path)
            if role not in briefs:
                report.error("roles", "{}: registration with no brief at docs/agents/{}.md".format(where, role))
            text = read(path)
            if suffix == ".md":
                fields = parse_frontmatter(text)
                if fields is None:
                    report.error("roles", "{}: frontmatter missing or not closed".format(where))
                    continue
                body = body_after_frontmatter(text)
            else:
                try:
                    fields = parse_toml(text)
                except ValueError as exc:  # includes tomllib.TOMLDecodeError
                    report.error("roles", "{}: does not parse ({})".format(where, exc))
                    continue
                body = str(fields.get("developer_instructions", ""))
            name = str(fields.get("name", ""))
            description = str(fields.get("description", "")).strip()
            if name != role:
                report.error("roles", "{}: name '{}' does not match the file name '{}'".format(where, name, role))
            if not description:
                report.error("roles", "{}: description is empty".format(where))
            descriptions.setdefault(role, {})[tool] = description
            if "docs/agents/{}.md".format(role) not in body:
                report.error("roles", "{}: does not point to docs/agents/{}.md".format(where, role))
            if len(body.strip()) > THIN_REGISTRATION_LIMIT:
                report.error("roles", "{}: body is {} characters; a registration only points to the brief".format(where, len(body.strip())))

    for role, by_tool in sorted(descriptions.items()):
        if len(set(by_tool.values())) > 1:
            report.error("roles", "{}: descriptions differ between {}".format(role, ", ".join(sorted(by_tool))))


def check_skills(root, report):
    skills_dir = root / ".agents" / "skills"
    canonical = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
    report.count("skills", len(canonical))
    claude_skills = root / ".claude" / "skills"
    uses_claude = (root / ".claude").is_dir()

    for skill in canonical:
        skill_md = skill / "SKILL.md"
        if not skill_md.is_file():
            report.error("skills", "{}: SKILL.md is missing".format(rel(root, skill)))
            continue
        fields = parse_frontmatter(read(skill_md))
        where = rel(root, skill_md)
        if fields is None:
            report.error("skills", "{}: frontmatter missing or not closed".format(where))
            continue
        if fields.get("name") != skill.name:
            report.error("skills", "{}: name '{}' does not match folder '{}'".format(where, fields.get("name"), skill.name))
        description = fields.get("description", "")
        if not description:
            report.error("skills", "{}: description is empty".format(where))
        elif len(description) > DESCRIPTION_LIMIT:
            report.error("skills", "{}: description is {} characters (limit {})".format(where, len(description), DESCRIPTION_LIMIT))
        if uses_claude:
            link = claude_skills / skill.name
            if not os.path.lexists(str(link)):
                report.error("skills", "{}: no Claude Code link at {}".format(skill.name, rel(root, link)))
            elif not link.is_symlink():
                report.error("skills", "{}: is a copy, not a symlink to {}".format(rel(root, link), rel(root, skill)))
            else:
                target = os.readlink(str(link))
                if os.path.isabs(target):
                    report.error("skills", "{}: symlink target is absolute ({}); use ../../.agents/skills/{}".format(rel(root, link), target, skill.name))
                elif link.resolve() != skill.resolve():
                    report.error("skills", "{}: resolves to {}, not {}".format(rel(root, link), target, rel(root, skill)))

    if claude_skills.is_dir():
        names = {s.name for s in canonical}
        for entry in sorted(claude_skills.iterdir()):
            if not entry.name.startswith(".") and entry.name not in names:
                report.error("skills", "{}: no canonical skill at .agents/skills/{} (retired or copied?)".format(rel(root, entry), entry.name))


def check_workflows(root, report):
    workflows_dir = root / "docs" / "workflows"
    index_path = workflows_dir / "README.md"
    if not index_path.is_file():
        report.error("workflows", "docs/workflows/README.md (workflow index) is missing")
        return
    index = read(index_path)
    files = sorted(p for p in workflows_dir.glob("*.md") if p.name != "README.md")
    report.count("workflows", len(files))
    table_links = set()
    for line in index.splitlines():
        if line.lstrip().startswith("|"):
            table_links.update(re.findall(r"\]\(([\w.-]+\.md)(?:#[^)]*)?\)", line))
    for path in files:
        if "({}".format(path.name) not in index:
            report.error("workflows", "{}: not linked from docs/workflows/README.md".format(rel(root, path)))
        if path.name in table_links:
            head = "\n".join(read(path).splitlines()[:12])
            if "Stages:" not in head:
                report.error("workflows", "{}: no 'Stages:' line near the top".format(rel(root, path)))


def check_decisions(root, report):
    decisions_dir = root / "docs" / "decisions"
    if not decisions_dir.is_dir():
        return
    files = sorted(decisions_dir.glob("DEC-*.md"))
    report.count("decisions", len(files))
    index_path = decisions_dir / "README.md"
    if files and not index_path.is_file():
        report.error("decisions", "docs/decisions/README.md (decision index) is missing")
        return
    index = read(index_path) if index_path.is_file() else ""
    seen = {}
    for path in files:
        match = re.match(r"DEC-(\d+)", path.name)
        if not match:
            report.error("decisions", "{}: file name does not start with DEC-NNN".format(rel(root, path)))
            continue
        number = int(match.group(1))
        if number in seen:
            report.error("decisions", "DEC-{:03d} is used by both {} and {}".format(number, seen[number], path.name))
        seen[number] = path.name
        status_match = re.search(r"^Status:\s*(\w+)", read(path), re.M)
        if not status_match:
            report.error("decisions", "{}: no 'Status:' line".format(rel(root, path)))
            continue
        row = next((line for line in index.splitlines() if "({})".format(path.name) in line), None)
        if row is None:
            report.error("decisions", "{}: no row in docs/decisions/README.md".format(path.name))
            continue
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        index_status = cells[-1].split()[0] if cells and cells[-1] else ""
        if index_status.lower() != status_match.group(1).lower():
            report.error("decisions", "{}: status '{}' but the index says '{}'".format(path.name, status_match.group(1), cells[-1]))


# ---------- links ----------

FENCE = re.compile(r"^(```|~~~)")
LINK = re.compile(r"!?\[(?:[^\[\]]|\[[^\]]*\])*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_ID = re.compile(r"""\b(?:id|name)\s*=\s*["']([^"']+)["']""")
PLACEHOLDER = re.compile(r"\{\{\s*[A-Za-z_][A-Za-z0-9_]*\s*\}\}")


def lines_outside_fences(text):
    in_fence = False
    for line in text.splitlines():
        if FENCE.match(line.strip()):
            in_fence = not in_fence
            yield ""
        else:
            yield "" if in_fence else line


def slugify(heading):
    """GitHub-style anchor for a heading's source text."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # links keep their text
    text = re.sub(r"<[^>]+>", "", text).replace("`", "")
    text = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"\1", text)  # _emphasis_
    text = re.sub(r"[^\w\- ]", "", text.lower().strip())
    return text.replace(" ", "-")


_anchor_cache = {}


def anchors(path):
    if path not in _anchor_cache:
        found, counts = set(), {}
        for line in lines_outside_fences(read(path)):
            match = HEADING.match(line)
            if match:
                slug = slugify(match.group(2))
                n = counts.get(slug, 0)
                found.add(slug if n == 0 else "{}-{}".format(slug, n))
                counts[slug] = n + 1
            found.update(HTML_ID.findall(line))
        _anchor_cache[path] = found
    return _anchor_cache[path]


def check_links(root, report, allow_placeholders):
    checked = 0
    for path in harness_files(root, (".md",)):
        relative = rel(root, path)
        if relative.startswith(LINK_EXEMPT_PREFIXES):
            continue
        for number, line in enumerate(lines_outside_fences(read(path)), 1):
            for target in LINK.findall(re.sub(r"`[^`]*`", "", line)):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue  # external URL or mailto
                if "{{" in target and allow_placeholders:
                    continue
                checked += 1
                file_part, _, anchor = target.partition("#")
                destination = path if not file_part else (path.parent / unquote(file_part))
                if not os.path.exists(str(destination)):
                    report.error("links", "{}:{}: '{}' does not exist".format(relative, number, target))
                    continue
                if anchor and destination.suffix == ".md" and anchor not in anchors(destination.resolve()):
                    report.error("links", "{}:{}: '{}' has no heading '#{}'".format(relative, number, target, anchor))
    report.count("links", checked)


def check_placeholders(root, report):
    for path in harness_files(root, (".md", ".toml")):
        for number, line in enumerate(read(path).splitlines(), 1):
            if PLACEHOLDER.search(line):
                report.error("placeholders", "{}:{}: {}".format(rel(root, path), number, line.strip()[:80]))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", help="harness root (default: found from the working directory)")
    parser.add_argument("--allow-placeholders", action="store_true", help="skip {{NAME}} placeholders (unadopted template only)")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else find_root(os.getcwd())

    report = Report()
    check_roles(root, report)
    check_skills(root, report)
    check_workflows(root, report)
    check_decisions(root, report)
    check_links(root, report, args.allow_placeholders)
    if not args.allow_placeholders:
        check_placeholders(root, report)

    print("Harness check: {}".format(root))
    print("Checked: " + ", ".join("{} {}".format(n, area) for area, n in report.counts.items()))
    if not report.errors:
        print("No problems found.")
        return 0
    print("{} problem(s):".format(len(report.errors)))
    for area, message in report.errors:
        print("  [{}] {}".format(area, message))
    return 1


if __name__ == "__main__":
    sys.exit(main())
