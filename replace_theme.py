import os
import glob

replacements = {
    "#190019": "#0B1121",
    "#FBE4D8": "#F8FAFC",
    "#854F6C": "#2563EB",
    "#522B5B": "#1E40AF",
    "#DFB6B2": "#93C5FD",
    "#2B124C": "#1E293B",
    "82,43,91": "30,64,175",
    "133,79,108": "37,99,235",
    "223,182,178": "147,197,253",
    "25,0,25": "11,17,33",
    "text-slate-950": "text-slate-900" # Minor fix if any
}

src_dir = "c:/Users/acer/Documents/kanchana-ai-portfolio/src"

for filepath in glob.glob(src_dir + "/**/*.jsx", recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old_val, new_val in replacements.items():
        new_content = new_content.replace(old_val, new_val)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

# Also check index.css and App.jsx which is at src root
for filepath in glob.glob(src_dir + "/*.jsx"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old_val, new_val in replacements.items():
        new_content = new_content.replace(old_val, new_val)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
