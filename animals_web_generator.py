import json
from pathlib import Path

DATA_FILE = Path("animals_data.json")
TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")


def load_animals():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_animals_text(animals: list[dict]) -> str:
    """Build the plain text block exactly like the example."""
    lines = []
    for animal in animals:
        name = animal.get("name", "Unknown")
        characteristics = animal.get("characteristics", {})
        locations = animal.get("locations", [])

        diet = characteristics.get("diet", "Unknown")
        animal_type = characteristics.get("type")  # may be missing
        location = locations[0] if locations else "Unknown"

        lines.append(f"Name: {name}")
        lines.append(f"Diet: {diet}")
        lines.append(f"Location: {location}")
        if animal_type is not None:
            lines.append(f"Type: {animal_type}")
        # empty line between animals
        lines.append("")

    return "\n".join(lines)


def main():
    animals = load_animals()

    # 1. Read template
    with TEMPLATE_FILE.open("r", encoding="utf-8") as f:
        template = f.read()

    # 2. Generate string with animals’ data
    animals_text = build_animals_text(animals)

    # 3. Replace placeholder
    output_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_text)

    # 4. Write to animals.html
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        f.write(output_html)

    print(f"Generated {OUTPUT_FILE} with {len(animals)} animals.")


if __name__ == "__main__":
    main()
