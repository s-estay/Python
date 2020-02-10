## Shit doesn't work?

- [Create a new virtual environment](https://github.com/s-estay/Python/tree/master/matplotlib#create-new-virtual-environment)
- [Install requirements](https://github.com/s-estay/Python/tree/master/matplotlib#virtual-environment-requirements)
- Activate virtual environment: `source project/venv/bin/activate`
- Run script: `python 05-build-in-styles.py`
- We don't need to specify `python3 05-build-in-styles.py` because Python 3 is the only version of Python installed in this virtual environment. Don't take my word, see it for yourself: `python --version`
- Do stuff and when done, deactivate the virtual environment: `deactivate`

<p align="center">
  <img src="https://github.com/s-estay/Python/blob/master/matplotlib/plot.png">
</p>

## Create new virtual environment

- Check if you have the Virtual Python Environment builder: `pip list`
- You should have something like `virtualenv (16.7.9)`
- If not, do `pip install virtualenv`
- Create a virtual environment inside the project folder called **venv**: `virtualenv project/venv`
- Activate the environment: `source project/venv/bin/activate`
- The version of Python created inside the virtual environment is going to be the same as the version used to create the environment. In this case Python 2.7.17
- To check the Python version: `python --version`
- To create a virtual environment with an specific version of Python: `virtualenv -p python3 project/venv`. Python 3 has to be installed in order for this to work
- Check the installed packages in the virtual environment: `pip list` or `pip3 list`
- To deactivate the virtual environment: `deactivate`
- To delete the virtual environment, just delete the **venv** folder or do `rm -rf project/venv/`
- Create a `gitignore` file and add the **venv** folder: `venv/`
- Observe, the actual py-files has to be located in the **project** folder

## Virtual environment requirements

- Install something inside the virtual environment: `pip install matplotlib`
- Check the currently installed packages: `pip list`
- Run `pip freeze > project/requirements.txt` to save the requirements in a txt-file
- To check the txt-file: `cat requirements.txt`
- Now, let's say we have deleted our environment and we want to create a new one with the correct requirements: `pip install -r project/requirements.txt`

## How to run `27-live-plot-csv-file.py`

The idea here is to plot data from a source that is generating live data. Python file `data6-gen.py` will generate that live data and save it to a csv-file `data6.csv`. To plot that live data:

- Delete `data6.csv`
- Open terminal and activate the virtual environment
- Run `python data6-gen.py` to generate new live data to `data6.csv`
- Open a second terminal and activate the virtual environment
- Run `python 27-live-plot-csv-file.py`
- Do the same to run `28-live-plot-csv-file-ii.py`

<p align="center">
  <img src="https://github.com/s-estay/Python/blob/master/matplotlib/live-plot.png">
</p>

## CSV files

- CSV stands for *Comma-separated values*
- Allow us to put into a plain text file some data and use some type of delimiter (usually a comma) to separate the different fields - [Corey Schafer: CSV Module](https://youtu.be/q5uM4VKywbA)
- In the sample csv-file below, the fields (keys) are *first_name*, *last_name* and *email*, separated by a comma.
```
first_name,last_name,email
John,Doe,john-doe@bogusemail.com
Mary,Smith-Robinson,maryjacobs@bogusemail.com
Dave,Smith,davesmith@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Tom,Wright,tomwright@bogusemail.com
Steve,Robinson,steverobinson@bogusemail.com
```

## References

- [Matplotlib Tutorials: Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)
- [Matplotlib Tutorials: Resources](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Matplotlib)
- [Virtual Python Environment builder](https://pypi.org/project/virtualenv/)
- [How to Use Virtual Environments with the Built-In venv Module](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
- [Workflow: Python and Virtualenv](https://www.youtube.com/watch?v=nnhjvHYRsmM)
- [Using .gitignore the Right Way](https://labs.consol.de/development/git/2017/02/22/gitignore.html)
- [Time format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
- [Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values)
