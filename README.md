# Scraping data using Discord's API is against their TOS, use this at your own risk.

# Discord Emoji Scraper
A set of simple Python scripts to scrape emojis and stickers from Discord servers.

I took inspiration from [Tiemen's Discord Emoji Downloader](https://github.com/ThaTiemsz/Discord-Emoji-Downloader).

## Running
- Edit `emoji_scraper.py` and add your Discord token there (Invalid tokens usually cause error code 401).
- You can also change your output directory in the scripts.
- Run `python emoji_scraper.py {arg1}` where `{arg1}` can either be:
  - A server ID: the script will call Discord's API to request that server's info, emojis and stickers using your authentication token.
  - "fromjson": the script will parse the data from an already existing file in the same directory, named `jsondata.json`.

## fromjson
Every time you download using a server ID, the script will call the API and save the respond data to `jsondata.json`, so if you need to redownload from the same server multiple times in a row without calling the API again, just use `fromjson` instead of the ID and it will read from the file instead (provided the file exists).

The reason behind this is because Discord don't want you to use the API for these things, and sending too many requests in a short period of time will raise suspicion (You probably won't get banned for downloading emojis if you don't do anything stupid).

## File formats
I believe these are the file formats coming directly from Discord without any conversion
|          	| Static 	| Animated      	|
|----------	|--------	|---------------	|
| Emojis   	| .webp  	| .gif          	|
| Stickers 	| .png   	| animated .png 	|

## Browsing downloaded assets
Downloaded assets are stored inside folders with their corresponding server ID, since server names can contain characters that I was too lazy to deal with, I decided to write them in text files, placed in the same folder. You can use the `list_output.py` script to list the downloaded directories with their names along side. If you have changed the output directory in the main `emoji_scraper.py` script, you might want to change it in `list_output.py` too so it can find the correct location.

If you have GNU find, xargs and [bat](https://github.com/sharkdp/bat), this one liner should also do the job (replace {OUTPUT DIRECTORY} with your output directory, E.g. `output`).
```sh
find {OUTPUT DIRECTORY}/*/name.txt | xargs -I x bat x --style header-filename
```

Example
```console
> find output/*/name.txt | xargs -I x bat x --style header-filename
File: output/1063291660496293928/name.txt
ralsei's sillies
File: output/256926147827335170/name.txt
OneShot ("Why are 10 Alulas Stored in this Room?")
File: output/283467363729408000/name.txt
Hollow Knight
File: output/409719543984947201/name.txt
Finji
File: output/89798994816946176/name.txt
Home of Emotional Pandas
File: output/950256523869839400/name.txt
Cupcord
```
