# Properties → JSON Converter

A single-file web tool that converts Java `.properties` content into JSON.

Just open the HTML file in your browser, paste your `.properties`, and instantly get JSON on the right side.  
No backend, no build step, no dependencies.

---

## Features

- 🔁 **Live preview** – JSON updates automatically as you type or paste.
- 🌓 **Light / Dark theme** – toggle with a switch; preference is stored in `localStorage`.
- 📋 **Copy JSON** – one click to copy the result to your clipboard.
- 💾 **Download JSON** – download the generated JSON as `output.json`.
- 🧠 **Simple algorithm, predictable behavior**:
  - Skips empty lines.
  - Skips lines starting with `#` (comments).
  - Skips lines starting with `spring.profiles.active`.
  - Supports both `key=value` and `key: value`.
  - Trims whitespace around keys and values.
  - Removes surrounding single or double quotes from values.
  - Outputs nicely formatted JSON with 2-space indentation.

---

## Getting Started

1. Clone or download this repository.
2. Open the HTML file (e.g. `index.html` or `props_to_json.html`) in any modern browser:
   - Double-click the file **or**
   - Right-click → “Open with” → your browser.

No server is required – everything runs locally in your browser.

---

## Usage

1. **Paste `.properties`** content into the **left** textarea.
   ```properties
   spring.profiles.active=prod
   # comment
   jwt-access-expiration-ms=900000
   jwt-refresh-expiration-ms=604800000
