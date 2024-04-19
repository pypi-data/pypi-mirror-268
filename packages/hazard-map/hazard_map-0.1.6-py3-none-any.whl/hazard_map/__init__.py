import argparse


def main():
    from hazard_map.hazard_map import HazardMap, Sheet, Kind

    arguments = parse_arguments()

    print('Welcome to hazard-map!')

    print()

    print(f'The outputs of this script will be saved in the following directory:')
    print(f'\"{arguments.output_directory}\"')

    print()

    hazard_log = HazardMap(arguments.input_workbook)

    graph = hazard_log.extract_sheet_mappings(
        [
            Sheet('HazardCause Mapping', (0, 0), (1, 1), (2, 2), False),
            Sheet('CauseControl Mapping', (0, 0), (1, 1), (2, 2), False),
        ],
        arguments.mapping_regex,
    )
    print(f'Mappings were successfully extracted from the workbook "{arguments.input_workbook}"!')
    print(hazard_log.report_kind_counts())

    print()

    hazard_log_output_file = hazard_log.write_to_file(
        arguments.output_directory,
        arguments.output_json,
    )

    hazard_log.draw_graph()
    plot_output_file = hazard_log.save_graph(arguments.output_directory, arguments.plot_dpi)


def parse_arguments():
    '''Uses the argparse library to create a command-line interface for the script.'''
    parser = argparse.ArgumentParser(
        prog='hazard-map',
        description='Build and analyze a network model of hazards, causes, and controls',
    )

    parser.add_argument(
        'input_workbook',
        help='The hazard mapping excel file to evaluate',
    )

    parser.add_argument(
        '-o',
        '--output-directory',
        help='Set a directory for the script to save its outputs to',
        default='hazard-log',
        type=str,
    )

    parser.add_argument(
        '-j',
        '--output-json',
        help='Save a json description of the mappings alongside the hazard log',
        default=False,
        type=bool,
        action=argparse.BooleanOptionalAction,
    )

    parser.add_argument(
        '-m',
        '--mapping-regex',
        help='Set a custom regex for identifying mapping pairs',
        default='',
        type=str,
    )

    parser.add_argument(
        '-d',
        '--plot-dpi',
        help='Set a custom DPI (quality) for the plot output',
        default=None,
        type=int,
    )

    return parser.parse_args()


if __name__ == '__main__':
    main()
