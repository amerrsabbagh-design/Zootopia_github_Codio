import json
from pathlib import Path

DATA_FILE = Path("animals_data.json")
TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")


def load_animals():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def generate_animal_card(animal: dict) -> str:
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type")  # may be missing
    location = locations[0] if locations else "Unknown"

    # build lines inside the card
    lines = [
        f"<p><strong>Name:</strong> {name}</p>",
        f"<p><strong>Diet:</strong> {diet}</p>",
        f"<p><strong>Location:</strong> {location}</p>",
    ]
    if animal_type is not None:
        lines.append(f"<p><strong>Type:</strong> {animal_type}</p>")

    inner_html = "\n            ".join(lines)

    return f"""
    <li class="cards__item">
        <div class="card__text">
            {inner_html}
        </div>
    </li>
    """.strip()


def generate_animals_html(animals: list[dict]) -> str:
    cards = [generate_animal_card(animal) for animal in animals]
    return "\n".join(cards)


def main():
    animals = load_animals()

    with TEMPLATE_FILE.open("r", encoding="utf-8") as f:
        template = f.read()

    animals_html = generate_animals_html(animals)
    output = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        f.write(output)

    print(f"Generated {OUTPUT_FILE} with {len(animals)} animals.")


if __name__ == "__main__":
    main()
