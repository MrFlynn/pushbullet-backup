# pushbullet-backup
### Description:

Downloads all pushes from Pushbullet account and write them to JSON file.

### Pre-Requisites:

You must have Python 3.0+ and pip installed in order to run this application. On Mac, install [Homebrew](brew.sh) and then run this command:

`$ brew install python3`

On Ubuntu run this command:

`$ sudo apt-get install python3 python3-pip`

### Download and Setup:

Clone the repository and cd into it:

`$ git clone https://github.com/MrFlynn/pushbullet-backup.git`

`$ cd pushbullet-backup/`

Next, install the proper requirements:

`$ [sudo] pip3 install -r requirements.txt`

Rename `config.ini.stub` to `config.ini` and open the file with your favorite text edit. Replace `<YOUR-TOKEN-HERE>` with your Pushbullet access token. To get your access token, visit [this page](https://www.pushbullet.com/#settings) and click *Create Access Token*.

### Running the Application:

Just run `python3 backup.py` to start the application. 

This might take some time based on your internet speed or if Pushbullet decides to rate limit you (**NOTE:** I do *not* to take responsibility if this happens and you get an email from Pushbullet telling you to stop—it was your choice to run this application in the first place.)

A json file with the name `pushbullet-backup-<day>-<month>-<year>.json` will be written to the directory where the application was run.