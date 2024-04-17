# Amit HVAC Control

Library for controlling Amit HVAC solution using the web server as an interface. It works by scraping the HMI web pages and sending POST requests for save operations.

Only works with the specifically developed machine logic runtime application for the following hardware:

* AMiNi4W2 PLC
* AMR-OP70RHC/04 Wall-mounted controller

## Run

Run the main file with arguments to test the connection nd retrieve all data.
```bash
python ./src/amit_hvac_control/__main__.py --host=<internal_network_address> --username=<username> --password=<password>
```

## Build

```bash
python -m build
```
