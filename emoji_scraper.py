import requests
import json
import sys
import shutil
import os

# Change your token here
header = {"Authorization": ""}
# You can change the output directory here
output_path = "./output"

serer_url = "https://discordapp.com/api/v6/guilds"
emoji_url= "https://cdn.discordapp.com/emojis"
sticker_url = "https://media.discordapp.net/stickers"
forbidden_characters = "\/:*?<>|"

# Get json data and set up variables
server_id = ""
server_name = ""
if (sys.argv[1] == "fromjson"):
    if not os.path.isfile("./jsondata.json"):
        sys.exit("jsondata.json not found, you will need to populate it yourself or run again with a server ID.")       
    data = json.load(open("jsondata.json", "r"))
    server_id = data["id"]
    server_name = data["name"]
else:
    server_id = sys.argv[1]
    response = requests.get(f'{serer_url}/{server_id}', headers=header)
    if not response.status_code == 200:
        sys.exit(f'[API REQUEST ERROR]: {response.status_code}')
    data = json.loads(response.text)
    server_name = data["name"]
    with open("jsondata.json", "w") as f:
        f.writelines(response.text)
output_path += f"/{server_id}"
if not os.path.exists(output_path):
    os.makedirs(output_path)

print("You are scraping from:")
print(f"  id: {server_id}")
print(f"  name: {server_name}")
print(f"  description: {data['description']}")
print()

# Write server name to a text file inside
# its output directory so its easier for you to find.
with open(f"{output_path}/name.txt", "w") as f:
    f.write(server_name)

# download emojis
if not os.path.exists(f"{output_path}/emojis"):
    os.makedirs(f"{output_path}/emojis")
print("Scraping emojis")
for x in range(len(data["emojis"])):
    if (data["emojis"][x]["animated"] == True):
        download_url = f"{emoji_url}/{data['emojis'][x]['id']}.gif?size=4096"
        filename = f"{data['emojis'][x]['name']}.gif"
    else:
        download_url = f"{emoji_url}/{data['emojis'][x]['id']}.webp?size=4096"
        filename = f"{data['emojis'][x]['name']}.webp"
    
    # make sure file name is valid
    filename = "".join([x for x in filename if x not in forbidden_characters])

    image_response = requests.get(download_url, stream=True)
    if not image_response.status_code == 200:
        sys.exit(f'[EMOJI DOWNLOAD ERROR]: {image_response.status_code}')
    
    with open(f"{output_path}/emojis/{filename}",'wb') as f:
        shutil.copyfileobj(image_response.raw, f)
    #print(f"[{x+1}/{len(data['emojis'])}] Downloaded: {filename}, {data['emojis'][x]['id']}, {download_url}")
    print(f"[{x+1}/{len(data['emojis'])}] Downloaded: {data['emojis'][x]['id']}, {filename}, {download_url}")

# download stickers
if not os.path.exists(f"{output_path}/stickers"):
    os.makedirs(f"{output_path}/stickers")
print("Scraping stickers")
for x in range(len(data["stickers"])):
    download_url = f"{sticker_url}/{data['stickers'][x]['id']}.png?size=4096"
    filename = f"{data['stickers'][x]['name']}.png"
    
    # make sure file name is valid
    filename = "".join([x for x in filename if x not in forbidden_characters])
    
    image_response = requests.get(download_url, stream=True)
    if not image_response.status_code == 200:
        sys.exit(f'[STICKER DOWNLOAD ERROR]: {image_response.status_code}')
        
    with open(f"{output_path}/stickers/{filename}",'wb') as f:
        shutil.copyfileobj(image_response.raw, f)
    #print(f"[{x+1}/{len(data['stickers'])}] Downloaded: {filename}, {data['stickers'][x]['id']}, {download_url}")
    print(f"[{x+1}/{len(data['stickers'])}] Downloaded: {data['stickers'][x]['id']}, {filename}, {download_url}")

print(f"Found and downloaded {len(data['emojis'])} emojis and {len(data['stickers'])} stickers from {server_id} ({server_name}).")
