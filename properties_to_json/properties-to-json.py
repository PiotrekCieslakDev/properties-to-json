import json
import sys
import os

def properties_to_json(input_file):
    data = {}

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # pomiń komentarze i puste linie
            if not line or line.startswith("#"):
                continue

            # rozdziel klucz i wartość
            if "=" in line:
                key, value = line.split("=", 1)
                data[key.strip()] = value.strip()

    # nazwa wyjściowa
    output_file = input_file + ".json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Zapisano JSON do: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python properties_to_json.py <plik.properties>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print(f"Plik '{input_file}' nie istnieje.")
        sys.exit(1)

    properties_to_json(input_file)
