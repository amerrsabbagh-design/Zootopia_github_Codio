import json
from pathlib import Path


DATA_FILE = Path("animals_data.json")
TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")


def load_animals():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def generate_animal_card(animal: dict) -> str:
    """Return HTML for a single animal card."""
    name = animal.get("name", "Unknown")
    taxonomy = animal.get("taxonomy", {})
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    scientific_name = taxonomy.get("scientific_name", "")
    diet = characteristics.get("diet", "")
    lifespan = characteristics.get("lifespan", "")
    location_str = ", ".join(locations)

    # Keep it small and readable for now
    return f"""
    <li class="cards__item">
        <h2 class="card__title">{name}</h2>
        <div class="card__text">
            <p><strong>Scientific name:</strong> {scientific_name}</p>
            <p><strong>Diet:</strong> {diet}</p>
            <p><strong>Lifespan:</strong> {lifespan}</p>
            <p><strong>Locations:</strong> {location_str}</p>
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
