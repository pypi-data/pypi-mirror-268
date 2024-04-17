<div align="center">
    <h1>
        hazard-map
    </h1>
</div>

![screenshot](https://gitlab.com/thom-cameron/hazard-map/-/raw/main/repo_assets/example_map.png)

Build a network model from spreadsheets of hazard, cause, and control mappings and carry out useful analyses. 

Overview
--------

This is a simple command-line tool that takes an Excel workbook with tables of mappings and creates a network model to use for analyses and visualization. 

Installation
------------

Install the command-line application from [PyPI](https://pypi.org) with [pip](https://pip.pypa.io/en/stable/installation/):

``` fish
pip install hazard-map
```

Usage
-----

Use the `-h` flag to see the available options:

``` fish
hazard-map -h
```

```
usage: hazard-map [-h] [-o OUTPUT_DIRECTORY] [-d PLOT_DPI] [-j | --output-json | --no-output-json] input_workbook

Build and analyze a network model of hazards, causes, and controls

positional arguments:
  input_workbook        The hazard mapping excel file to evaluate

options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        Set a directory for the script to save its outputs to
  -d PLOT_DPI, --plot-dpi PLOT_DPI
                        Set a custom DPI (quality) for the plot output
  -j, --output-json, --no-output-json
                        Save a json description of the mappings alongside the hazard log
```

Pass an Excel workbook (xlsx) file with hazard-cause and cause-control mappings in worksheets named "HazardCause Mapping" and "CauseControl Mapping" respectively:

``` fish
hazard-map our_mappings.xlsx
```
