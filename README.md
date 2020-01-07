# FTC Log Analyzer

FTC Log Analyzer is a Python Web Application built with Plot.ly and Dash to help FTC Teams visualize CSV Data from the robot controller. The App is loosely based off the "Dash Financial Report" example app.

The App in its current state can only view the Current Draw, and the Position of two motors, though I hope to quickly add more functionality


## Modifying and Running the App Locally - Precautions and Notice
Guess what! There's a special branch for you guys to push your own versions of the app! Use that to push significant app changes!

Feel free to modify the app as much as possible! However there are a couple of precautions that you might wanna take, including:

- Have at the very least, a basic understanding of Python. You don't need to be a Python Guru, just a simple understanding should be enough.
- **Read the Plot.ly and Dash** documentation **BEFORE** you make changes
      - The folks at Plot.ly have done a really excellent job with documentation. They have a LOT of source code available, and the do a really good job explaining the structure of the application code. Python is not a very syntax heavy and you should be able to pick it up easily if you don't have a lot of experience.
- Make sure you follow our Installation and Usage instructions! If something doesn't work, chances are Plot.ly documentation covers why! If there's an error with my code, please let me know!

Just a notice. When adding extra graphs, please make sure you follow the layout structure. Copy and Paste-ing random source code in random places is just going to cause frustration (I speak from experience). 

### Installation

Pull or Clone our Repository. Then run:

```bash
$user python3 app.py
```
This will open the app on 127.0.0.1:8050


## Usage
### Step 1:

The FTC Log Analyzer is by no means a "fully packaged" solution. The App is literally in Pre-Alpha. You will have to use PrintWriter and FileWriter in your TeleOp or Autonomous program to write data to a file in your phone. This file will need to be formatted properly as follows:
```
Time, Motor1 Current Draw, Motor2 Current Draw, Motor1 Position, Motor2 Position
Data, Data, Data, Data, Data
Data, Data, Data, Data, Data
Data, Data, Data, Data, Data
//blah blah blah u get the idea :)
```
Tedious? Yes I know. It's a small price to pay while I work on a better solution.

### Step 2:

The .CSV file you write too will have to be extracted from the Phone's storage, and loaded onto a computer with WiFi connection. This file will then have to be posted to GitHub, PasteBin, Google Drive, or any kind of Internet Connected File Storage Service which will let you link the raw CSV Data (I recommend GitHub).

### Step 3:

By Default, the FTC Log Analyzer will link to some .csv files under "overview.py" in the pages directory. The default link is some sample data, and if you do not change it, you will run into some issues (like not having the correct data set for starters). You will have to change this link to the link of the raw CSV data you made earlier. You will also have to edit the "team_facts.csv" file so it has your team info instead of ours :)

### Step 4:
Install REQUIREMENTS.txt using pip (python package manager). This will stop runtime errors on your code
```bash
$ sudo apt-get install pip -y
$ pip install -r requirements.txt
```
## Using the App online
Expect to see this feature available soon! Including a "upload .csv" so you won't be changing the source code every time!

After I scrape enough cash to buy a domain name!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Also please hey if you modify and republish it please give me, or FTC Team 14607 some credit :)

Happy Coding! - Dev

## License
[MIT](https://choosealicense.com/licenses/mit/)
