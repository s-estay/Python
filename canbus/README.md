## Getting started

- Flip the big switch where batteries are connected to
- Give permissions to serial port ACM0: `sudo chmod 666 /dev/ttyACM0`
- Activate the virtual environment created by PyCharm by running one random script in PyCharm
  - TODO: activate virtual environment in the terminal
- Run individual scripts in the terminal: `python3 015-scan-nodes.py`


## Virtual environment and requirements

- Compiled in a virtual environment using Python 3.5 as interpreter in PyCharm
- Requirements: `canopen` and `pyserial`

<!--
- Load `requirements.txt` when creating a new virtual environment:
```
virtualenv -p python3.5 project/venv
source project/venv/bin/activate
python --version
pip install -r project/requirements.txt
pip list
```
-->

## References

- [CANopen for Python](https://canopen.readthedocs.io/en/latest/)
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
