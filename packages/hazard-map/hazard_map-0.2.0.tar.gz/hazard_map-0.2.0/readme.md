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
usage: hazard-map [-h] [-o OUTPUT_DIRECTORY] [-j | --output-json | --no-output-json] [-m MAPPING_REGEX] [-d PLOT_DPI] input_workbook

Build and analyze a network model of hazards, causes, and controls

positional arguments:
  input_workbook        The hazard mapping excel file to evaluate

options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
                        Set a directory for the script to save its outputs to
  -j, --output-json, --no-output-json
                        Save a json description of the mappings alongside the hazard log
  -m MAPPING_REGEX, --mapping-regex MAPPING_REGEX
                        Set a custom regex for identifying mapping pairs
  -d PLOT_DPI, --plot-dpi PLOT_DPI
                        Set a custom DPI (quality) for the plot output
```

Pass an Excel workbook (xlsx) file with hazard-cause and cause-control mappings (indicated by a "Y" at the intersection of row/column pair that map onto one-another) in worksheets named "HazardCause Mapping" and "CauseControl Mapping" respectively:

``` fish
hazard-map our_mappings.xlsx
```

See the [test mappings](https://gitlab.com/thom-cameron/hazard-map/-/blob/main/tests/test_mappings.xlsx) for an example of a compatible document.

Development
-----------

If you want to develop this project further or just set it up so you can modify the source code (to work with a different matrix format, for example), clone this repo:

``` fish
git clone https://gitlab.com/thom-cameron/hazard-map
cd hazard-map
```

Packaging and dependency management for this project are handled by [poetry](https://python-poetry.org/). Install poetry, or, if you use [nix](https://nixos.org/), start up a shell with everything you need:

``` fish
nix-shell
```

Then, get the code running:

``` fish
# install dependencies
poetry install

# run the test suite
poetry run pytest

# run the application
poetry run hazard-map

# or enter an interactive shell in a properly configured virtual environment
poetry run python
```
