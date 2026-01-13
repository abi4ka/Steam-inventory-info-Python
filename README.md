# Steam Inventory Parser

A simple Python program to retrieve a Steam user's inventory items using their SteamID64.  
By default, the program fetches items from **CS2 (app_id = 730)**, but you can change `APP_ID` to target a different game.

> **Note:** This program works **without a Steam API Key**.

## Features

- Fetches inventory items for a given SteamID64.
- Displays item name, type, and marketable status.
- No API key required.

---

## Example Output

```
## Inventory Items:
Name: Music Kit | Daniel Sadowski, The 8-Bit Kit
Type: High Grade Music Kit
Marketable: Yes
---------------
Name: M4A4 | Dark Blossom
Type: Industrial Grade Rifle
Marketable: Yes
---------------
````

---

## Dependencies

- Python 3.8+
- `requests`

Install dependencies:

```bash
pip install requests
````

---

## Configuration

* `app_id`: Steam application ID (default: `730` — CS2 / CS:GO)
* `context_id`: Inventory context ID (default: `2`)

You can change these values in the script if needed.

---

## Usage

```bash
python main.py
```

Enter a valid **SteamID64** when prompted.

---

## Author

Created by [abik](https://github.com/abi4ka)
