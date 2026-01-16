import json
from pathlib import Path

DATA_FILE = Path("animals_data.json")
TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")


def load_animals():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def serialize_animal(animal: dict) -> str:
    """Return HTML for a single animal card."""
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type")
    location = locations[0] if locations else "Unknown"

    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    output += f'      <strong>Location:</strong> {location}<br/>\n'
    if animal_type is not None:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n\n'
    return output


def build_animals_html(animals: list[dict]) -> str:
    output = ""
    for animal in animals:
        output += serialize_animal(animal)
    return output


def main():
    animals = load_animals()

    with TEMPLATE_FILE.open("r", encoding="utf-8") as f:
        template = f.read()

    animals_html = build_animals_html(animals)
    output_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        f.write(output_html)

    print(f"Generated {OUTPUT_FILE} with {len(animals)} animals.")


if __name__ == "__main__":
    main()
