## INF601 - Advanced Programming in Python
 James Kobell |
 Mini Project 2

### Project
 Mini Project 2 is a Python project for reading a ticker dataset (csv file format) and plotting the moving average price of each month in a year. A dataset spanning multiple years will produce multiple charts. Includes error logging when reading from a dataset csv file. Includes error logging when saving png charts to charts folder.

### Interpreter
Python 3.10.6

### Installation
- Create a directory for the project.
- Install Python 3.10.6 if not already installed.
- Refer to requirements.txt and pip install the listed packages.
- Update each package.
- Copy main.py into the directory.

### System Environment
- Within the directory of the project:
    - Create a directory with the name 'charts'.
    - Create a directory with the name 'app_data'.
    - Create a file with the name 'app_log.txt'.     
- Place targeted ticker dataset csv file(s) into app_data directory. 

### Running Project
- In main.py, replace the ticker symbol, 'TSLA' with the ticker symbol of a targeted dataset at `ticker = 'TSLA'`.
- In app_data directory, verify name/rename dataset csv file to '[ticker symbol].csv
- From command line in the project directory or a suitable Python IDE, run main.py.
- Open the newly created 'charts' folder. Refer to the System Environment section within this readme document.
- View each .png file with an application suitable for viewing .png files.
- To create Moving Average charts for a different ticker symbol, repeat steps 1-2 of this section - Running Project.
- View error log entries, if any, in app_log.txt.

### Options
- To view each chart as they are created during the running of the project, uncomment `plt.show()` by removing the first '#' on the line.

### Alternate dataset file types
- In main.py, replace 'read_csv' at `df = pd.read_csv(data_filename)` with a suitable method name for reading the targeted dataset filetype. 
- Example: In main.py, replace 'read_csv' at `df = pd.read_csv(data_filename)` with 'read_json' for reading a targeted dataset with a name format as '[ticker symbol].json.
- Result: `df = pd.read_json(data_filename)`

### Contributing
- Please open an issue to initiate a change process.