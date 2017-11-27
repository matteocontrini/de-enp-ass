# De-enp-ass

Converts an exported .txt file from Enpass to .csv compatible with 1Password.

## Pre-usage
You must have python installed on your computer. If you have a mac it's already installed. If you run linux you already know everything ;)
If you run Windows, Google is your friend.

## Note
The exported txt file from enpass may require some love before conversion. Please make sure there are at least **two empty lines** between each item in the file.

It's somewhat of a hit or miss, for me it works great but you'll need to quickly check the enpass txt file to see that the password chunks are not looking funky.

## Usage
Download de-enp-ass.py, open up the terminal, cd to that folder and run:

```python de-enp-ass.py /path/to/exported-from-enpass.txt```

This will generate one file in the same folder as the exported enpass file:

`exported-from-enpass-logins.csv`

For importing in 1password (mac), choose file->import, use button "options" in the lower left corner. 
Choose .csv file and then "import credit cards", open the credit card file.
Do it again for secure notes and logins and choose correct import in the dialog.

## Eh
If it works for you, great!
I made this mainly for myself because I had a sh#t ton of passwords and would have been a pain to manually migrate, but I really wanted to migrate. I figured others might benefit of it too.
I may update the script to be better in the future... Feel free to contribute.

## Yup
I don't take any responsibilities for stuff that might be missed during conversion. This is for anyones convenience.
