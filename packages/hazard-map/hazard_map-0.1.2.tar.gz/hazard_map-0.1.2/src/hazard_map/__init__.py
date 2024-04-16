import argparse
# from hazard_map import HazardMap, Sheet
from hazard_map.hazard_map import HazardMap, Sheet

DEFAULT_OUTPUT_DIR = './hazard-log'

def main():
    print('Welcome to hazard-map!')

    print()
    
    arguments = parse_arguments()

    if arguments.output_directory:
        if arguments.output_directory[-1] == '/': 
            arguments.output_directory = arguments.output_directory[:-1]
        output_directory = arguments.output_directory
    else:
        output_directory = DEFAULT_OUTPUT_DIR
    print(f'The ourputs of this script will be saved in the following directory:')
    print(output_directory)

    print()

    hazard_log = HazardMap(arguments.input_workbook)

    graph = hazard_log.extract_sheet_mappings([
        Sheet('HazardCause Mapping', (0, 0), (1, 1), (2, 2), False),
        Sheet('CauseControl Mapping', (0, 0), (1, 1), (2, 2), False),
    ])
    print('Mappings were successfully extracted from the workbook!')

    print()

    hazard_log_output_file = hazard_log.write_to_file(output_directory)
    print(f'Wrote the mappings in the hazard log format to "{hazard_log_output_file}"')

    hazard_log.draw_graph()
    plot_output_file = hazard_log.save_graph(output_directory, arguments.plot_dpi)
    print(f'Saved a plot of the network to "{plot_output_file}"')

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='hazard-map',
        description='Build and analyze a network model of hazards, causes, and controls',
    )

    parser.add_argument(
        'input_workbook',
        help='The hazard mapping excel file to evaluate',
    )

    parser.add_argument(
        '-o', '--output-directory',
        help='Set a custom directory for the script to save its outputs to',
        default=None,
        type=str,
    )

    parser.add_argument(
        '-d', '--plot-dpi',
        help='Set a custom DPI (quality) for the plot output',
        default=None,
        type=int,
    )

    return parser.parse_args()

if __name__ == '__main__':
    main()
