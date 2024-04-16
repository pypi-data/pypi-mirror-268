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

Pass an Excel workbook (xlsx) file with hazard-cause and cause-control mappings in worksheets named "HazardCause Mapping" and "CauseControl Mapping":

``` fish
hazard-map our_mappings.xlsx
```

A custom location to save the outputs of the script to can be defined too:

``` fish
hazard-map our_mappings.xlsx -o ~/documents/our_hazard_log
```
