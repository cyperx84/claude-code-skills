#!/usr/bin/env python3
"""
Generate model-index.json by scanning all mental model files
"""

import json
import os
import re
from pathlib import Path

def extract_model_metadata(file_path):
    """Extract metadata from a mental model file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract model name (first line after "## Mental Model = ")
    name_match = re.search(r'## Mental Model = (.+)', content)
    name = name_match.group(1).strip() if name_match else ""

    # Extract category
    category_match = re.search(r'\*\*Category = (.+)\*\*', content)
    category = category_match.group(1).strip() if category_match else ""

    # Extract description (text between **Description:** and next **section)
    desc_match = re.search(r'\*\*Description:\*\*\s+(.+?)(?=\n\n\*\*)', content, re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else ""
    # Limit to first 200 chars for summary
    summary = (description[:200] + '...') if len(description) > 200 else description

    # Extract keywords
    keywords_match = re.search(r'\*\*Keywords for Situations:\*\*\s+(.+?)(?=\n\n|\n\*\*)', content, re.DOTALL)
    keywords_text = keywords_match.group(1).strip() if keywords_match else ""
    keywords = [k.strip() for k in keywords_text.split(',')]

    # Extract ID from filename (m##)
    filename = os.path.basename(file_path)
    id_match = re.match(r'm(\d+)_', filename)
    model_id = f"m{id_match.group(1)}" if id_match else ""

    # Extract snake_case title from filename
    title_match = re.match(r'm\d+_(.+)\.md', filename)
    slug = title_match.group(1) if title_match else ""

    return {
        "id": model_id,
        "name": name,
        "slug": slug,
        "category": category,
        "path": file_path,
        "keywords": keywords,
        "summary": summary
    }

def main():
    # Find all mental model files
    mental_models_dir = Path("Mental_Models")
    model_files = sorted(mental_models_dir.glob("*/m*.md"))

    models = []
    categories = {}

    for file_path in model_files:
        try:
            metadata = extract_model_metadata(str(file_path))
            models.append(metadata)

            # Track categories
            cat = metadata['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(metadata['id'])

            print(f"✓ Processed: {metadata['id']} - {metadata['name']}")
        except Exception as e:
            print(f"✗ Error processing {file_path}: {e}")

    # Create index structure
    index = {
        "version": "1.0.0",
        "generated": "2025-10-31",
        "total_models": len(models),
        "categories": categories,
        "models": models
    }

    # Write to .skill/resources/model-index.json
    output_dir = Path(".skill/resources")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "model-index.json"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Generated index with {len(models)} models")
    print(f"✓ Saved to: {output_file}")
    print(f"\nCategories: {', '.join(sorted(categories.keys()))}")

if __name__ == "__main__":
    main()
