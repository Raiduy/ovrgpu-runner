# OVRprofiler metrics collector

This is a simple tool to collect metrics from the OVRprofiler tool and store them in a CSV file.

* OS: Windows 10
* VR: Oculus Quest 2

## Requirements
OVRMetricsTool: https://developer.oculus.com/documentation/native/android/ts-ovrmetricstool/
ADB: https://developer.android.com/tools/adb

## Usage
1. Run `metrics_collector.ps1` in PowerShell. Output will be stored in `./raw_data/<timestamp>.txt`.
2. Run `csvconverter.py` to convert the raw data to a CSV file. Output will be stored in `./data/<timestamp>.csv`.