import re
import sys
from pathlib import Path
import difflib
from datetime import datetime, timedelta

def update_versions(old_version, new_version, file_paths):
    try:
        from zoneinfo import ZoneInfo
        current_date = datetime.now(ZoneInfo("Australia/Sydney")).strftime("%d/%m/%Y")
    except Exception:
        # fallback if tzdata isn't available
        current_date = (datetime.utcnow() + timedelta(hours=10)).strftime("%d/%m/%Y")

    # Patterns for GitHub release links and MOTD
    patterns = [
        # GitHub release download URLs (mod-specific)
        (rf"(https://github\.com/[^/]+/[^/]+/releases/download/){re.escape(old_version)}(/comMC-[^\"\)]+)", rf"\g<1>{new_version}\g<2>"),

        # Simplified links for other files
        (rf"(https://github\.com/[^/]+/[^/]+/releases/download/){re.escape(old_version)}(/[^\"\)]+)", rf"\g<1>{new_version}\g<2>"),

        # MOTD: full match with date (preferred — needs to come first)
        (rf"(motd=.*?§bv){re.escape(old_version)}( §r\| .*?\\n§8Updated )\d{{4}}/\d{{2}}/\d{{2}}", rf"\g<1>{new_version}\g<2>{current_date}"),

        # MOTD: version number only (backup — must come after)
        (rf"(motd=.*?§bv){re.escape(old_version)}(\b)", rf"\g<1>{new_version}\g<2>"),
    ]

    for file_path in file_paths:
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            continue

        content = file_path.read_text(encoding="utf-8")
        updated = content

        for pattern, replacement in patterns:
            updated = re.sub(pattern, replacement, updated)

        if content != updated:
            print(f"\n🔧 Changes in {file_path.relative_to(repo_root)}:")
            diff = difflib.unified_diff(
                content.splitlines(),
                updated.splitlines(),
                fromfile="before",
                tofile="after",
                lineterm=""
            )
            print("\n".join(diff))

            confirm = input("Apply these changes? (y/n): ").strip().lower()
            if confirm == 'y':
                file_path.write_text(updated, encoding="utf-8")
                print("✅ Changes applied.")
            else:
                print("❎ Changes discarded.")
        else:
            print(f"✅ No changes needed in {file_path.relative_to(repo_root)}.")

# --- CLI Arguments ---
if len(sys.argv) != 3:
    print("Usage: python script.py <old_version> <new_version>")
    sys.exit(1)

old_version = sys.argv[1]
new_version = sys.argv[2]

# --- Path Setup ---
script_dir = Path(__file__).resolve().parent
repo_root = script_dir.parent

files_to_update = [
    repo_root / "README.md",
    repo_root / "server" / "server.properties",
    # Add more paths if needed
]

update_versions(old_version, new_version, files_to_update)
