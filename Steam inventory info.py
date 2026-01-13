import requests

app_id = 730

def get_inventory_items(steam_id, context_id=2):
    """
    Retrieves a list of items from a Steam inventory using SteamID64.
    """
    url = f'http://steamcommunity.com/inventory/{steam_id}/{app_id}/{context_id}'
    try:
        response = requests.get(url).json()
        if 'descriptions' in response:
            return response['assets'], response['descriptions']
        else:
            print(f"Error retrieving items: {response.get('message', 'Unknown error')}")
            return None
    except requests.RequestException as e:
        print(f"HTTP request error: {e}")
        return None

def main():
    steam_id = input("Enter the Steam profile SteamID64: ")
    assets, descriptions = get_inventory_items(steam_id)

    if assets:
        print("Inventory Items:")
        print('---')
        for asset in assets:
            classid = asset['classid']
            for description in descriptions:
                if description['classid'] == classid:
                    print(f"Name: {description['name']}")
                    print(f"Type: {description['type']}")
                    print(f"Marketable: {'Yes' if description['marketable'] else 'No'}")
                    print('---')
    else:
        print("Failed to retrieve inventory items.")


if __name__ == '__main__':
    main()