import os
import json
import re
from datetime import datetime

# Config
CONTENT_ROOT = "../../../"  # Go up 3 levels to 'algorithms' root
OUTPUT_DIR = "../../../"    # Output to 'algorithms' root (Matches index.html src="../../data.js")
DATA_FILE = os.path.join(OUTPUT_DIR, "data.js")

# Filtering Logic
IGNORE_DIRS = {".git", ".gemini", "web_viewer", "__pycache__", ".vscode", "tmp", "app", "public", "scripts", "src", "assets"}
IGNORE_FILES = {".DS_Store", "LICENSE", "README.md", "STRUCTURE.md", "task.md", "implementation_plan.md", "walkthrough.md", "data.js"}

def normalize_path(path):
    """Ensure consistent forward slashes and no leading/trailing slashes."""
    return path.replace("\\", "/").strip("/")

def scan_repository(root_path):
    simple_tree = {}
    flat_index = []
    stats = {
        "files": 0,
        "topics": 0,
        "lines_of_code": 0,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    def process_dir(current_path, rel_path):
        """Recursively scan directories to build tree and index."""
        node = {}
        has_content = False
        
        try:
            # Sort: Directories first, then files
            entries = sorted(os.scandir(current_path), key=lambda e: (not e.is_dir(), e.name))
        except FileNotFoundError:
            return None

        for entry in entries:
            # Skip hidden or ignored
            if entry.name.startswith(".") or entry.name in IGNORE_DIRS:
                continue
            
            entry_rel_path = normalize_path(os.path.join(rel_path, entry.name))
            
            if entry.is_dir():
                sub_node = process_dir(entry.path, entry_rel_path)
                if sub_node:
                    node[entry.name] = sub_node
                    has_content = True
                    stats["topics"] += 1
            
            elif entry.is_file():
                if entry.name in IGNORE_FILES:
                    continue
                
                ext = os.path.splitext(entry.name)[1].lower()
                if ext not in [".md", ".py"]:
                    continue

                try:
                    with open(entry.path, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    print(f"Error reading {entry.path}: {e}")
                    continue

                stats["files"] += 1
                if ext == ".py":
                    stats["lines_of_code"] += len(content.splitlines())

                # Add to Tree
                node[entry.name] = {
                    "type": "file", 
                    "ext": ext, 
                    "path": entry_rel_path
                }
                has_content = True

                # Add to Search Index
                flat_index.append({
                    "id": entry_rel_path,
                    "title": entry.name.replace(ext, "").replace("_", " "),
                    "type": "Code" if ext == ".py" else "Topic",
                    "path": entry_rel_path,
                    "breadcrumbs": [b.replace("_", " ") for b in entry_rel_path.split("/")[:-1]],
                    "content": content
                })
        
        return node if has_content else None

    print(f"Scanning {os.path.abspath(root_path)}...")
    simple_tree = process_dir(root_path, "")
    return simple_tree, flat_index, stats

if __name__ == "__main__":
    tree, index, statistics = scan_repository(CONTENT_ROOT)
    
    if tree:
        js_content = f"""
window.KB_DATA = {{
    tree: {json.dumps(tree)},
    index: {json.dumps(index)},
    stats: {json.dumps(statistics)}
}};
console.log("KB Data Loaded", window.KB_DATA.stats);
"""
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(js_content)
        
        print(f"Authentication Successful: Data generated at {DATA_FILE}")
        print(f"Statistics: {statistics}")
    else:
        print("Scan failed: No content found.")
