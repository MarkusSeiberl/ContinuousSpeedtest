# ContinuousSpeedtest

This python script runs the [Tarife.at](https://www.tarife.at/speedtest) speed test every hour. The results will be written to a csv file.

It is intended to run on an [Raspberry Pi](https://www.raspberrypi.org/).

## Prerequisites

### Python packages

**Selenium WebDriver:**
> pip install selenium

**Job Scheduler:**
> pip install schedule

### Chrome Driver

Download and install the WebDriver driver for the Chromium Browser from [here](https://launchpad.net/ubuntu/trusty/+package/chromium-chromedriver)

> wget http://launchpadlibrarian.net/361669488/chromium-chromedriver_65.0.3325.181-0ubuntu0.14.04.1_armhf.deb

> dpkg -i chromium-chromedriver_65.0.3325.181-0ubuntu0.14.04.1_armhf.deb

## Usage

**Run:**

> python scheduler.py

## Result File

The results are saved the the file `speedtest_results.csv`.
Every new line represents a new measurement.

```csv
<UNIX timestamp>,<Ping in ms>,<Download Speed in Mbit/s>,<Upload Speed in Mbit/s>
```
