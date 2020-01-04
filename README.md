# FTC Log Analyzer

FTC Log Analyzer is a Python Web Application built with Plot.ly and Dash to help FTC Teams visualize CSV Data from the robot controller. The App is loosely based off the "Dash Financial Report" example app.

The App in its current state can only view the Current Draw, and the Position of two motors, though I hope to quickly add more functionality


## Installation

Pull or Clone our Repository. Then run:

```bash
$user python3 init.py
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
Tedious? Yes we know. It's a small price to pay while we work on a better solution.

### Step 2:

The .CSV file you write too will have to be extracted from the Phone's storage, and loaded onto a computer with WiFi connection. This file will then have to be posted to GitHub, PasteBin, Google Drive, or any kind of Internet Connected File Storage Service which will let you link the raw CSV Data (We recommend GitHub).

### Step 3:

By Default, the FTC Log Analyzer will link to .csv file under "main.py". The default link is some sample data, and if you do not change it, you will run into some issues (like not having the correct data set for starters). You will have to change this link to the link of the raw CSV data you made earlier.

### Step 4:
Install REQUIREMENTS.txt using pip (python package manager). This will stop runtime errors on your code
```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
