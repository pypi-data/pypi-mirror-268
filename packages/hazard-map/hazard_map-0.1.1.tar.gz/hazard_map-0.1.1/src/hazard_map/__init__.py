import argparse
from hazard_map import HazardMap, Sheet
# from hazard_map.hazard_map import HazardMap, Sheet

def main():
    arguments = parse_arguments()

    hazard_log = HazardMap(arguments.input_workbook)

    graph = hazard_log.extract_sheet_mappings([
        Sheet('HazardCause Mapping', (0, 0), (1, 1), (2, 2), False),
        Sheet('CauseControl Mapping', (0, 0), (1, 1), (2, 2), False),
    ])
    print('Mappings extracted from the workbook')

    hazard_log_output_file = hazard_log.write_to_file(arguments.output_directory)
    print('\nWrote the mappings in the hazard log format to the following file:')
    print(hazard_log_output_file)

    hazard_log.draw_graph()
    plot_output_file = hazard_log.save_graph(arguments.output_directory)
    print('\nSaved a plot of the network to the following file:')
    print(plot_output_file)

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

    return parser.parse_args()

if __name__ == '__main__':
    main()
