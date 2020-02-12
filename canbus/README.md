## When charging

- Connect charger to EMS (3 pins cable)
- Set power supply to 120V/1-3A and connect it to the charger (PV input)
- Connect Modbus between EMS and charger
- Connect CAN-USB adapter between computer and backplane (PLC-CAN input)
- Flip the big switch where batteries are connected to
- Connect computer with Solar Bora's Modbus Control application to backplane via Modbus
- Open Solar Bora's Modbus Control
  - Enable EMS and then enable contactor 6
  - Enable Charger, State AUTO, Charge current between 1000-3000 mA
  - If no current is drawn from the power supply, set Charger's State to STOP, Charge current to 0 mA and then repeat previous step

## When discharging

- Connect inverter to EMS (3 pins cable)
- Connect loads (induction stoves or kettles) to inverter
- Fill stoves/kettle with water
- Connect Modbus between EMS and inverter
- Connect computer with Solar Bora's Modbus Control application to backplane via Modbus
- Open Solar Bora's Modbus Control
  - Enable EMS and then enable contactor 7
  - Enable Inverter
- Start the loads
- For 120 V batteries, one induction stove @ 2 kW will draw around 4 A and will work until the voltage goes under ##

## Collect data and plot

- Give permissions to serial port ACM0: `sudo chmod 666 /dev/ttyACM0`
- **If you don't want over-wright the previous measurement, give # in log#.csv a new value in the following python-files**
- Run `python3 024-init-csv.py`. This will create the csv-file's keys in a log#.csv file
- Run `python3 026-save-new-data-to-csv-timer.py`. This will read the LMU and save new data to log#.csv. Don't close it
- Run `python3 029-plot-data-live.py`. Will will read from log#.csv and plot voltage, temperature, current and pressure for node of id=1

<!-- - Activate the virtual environment created by PyCharm by running one random script in PyCharm
  - TODO: activate virtual environment in the terminal -->

## Virtual environment and requirements

- Compiled in a virtual environment using Python 3.5 as interpreter in PyCharm
- Requirements:
  - `canopen`
  - `pyserial`
  - `pandas`
  - `matplotlib`

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
