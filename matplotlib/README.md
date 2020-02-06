## Shit doesn't work?

- [Create a new virtual environment](https://github.com/s-estay/Python/tree/master/matplotlib#create-new-virtual-environment)
- [Install requirements](https://github.com/s-estay/Python/tree/master/matplotlib#virtual-environment-requirements)
- Activate virtual environment: `source project/venv/bin/activate`
- Run script: `python 05-build-in-styles.py`
- We don't need to specify `python3 05-build-in-styles.py` because Python 3 is only version of Python installed in this virtual environment. Don't take my word, see it for yourself: `python --version`
- Do stuff and when done, deactivate the virtual environment: `deactivate`

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

## References

- [Matplotlib Tutorials: Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)
- [Matplotlib Tutorials: Resources](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Matplotlib)
- [Virtual Python Environment builder](https://pypi.org/project/virtualenv/)
- [How to Use Virtual Environments with the Built-In venv Module](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
- [Workflow: Python and Virtualenv](https://www.youtube.com/watch?v=nnhjvHYRsmM)
- [Using .gitignore the Right Way](https://labs.consol.de/development/git/2017/02/22/gitignore.html)
