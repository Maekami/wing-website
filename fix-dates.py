from pathlib import Path
import re

count = 0

for root in ["content/authors", "content/publication"]:
    for path in Path(root).rglob("*.md"):
        original = path.read_text()
        updated = original

        # Replace invalid month 00 with January.
        updated = re.sub(
            r"^(\s*date:\s*['\"]?\d{4})-00-(\d{2})(['\"]?)$",
            r"\1-01-\2\3",
            updated,
            flags=re.MULTILINE
        )

        # Add day 01 to incomplete publication dates.
        updated = re.sub(
            r"^(\s*publishDate:\s*['\"]?\d{4}-\d{2})(['\"]?)$",
            r"\1-01\2",
            updated,
            flags=re.MULTILINE
        )

        if updated != original:
            path.write_text(updated)
            print("Fixed:", path)
            count += 1

print(f"Updated {count} files")
