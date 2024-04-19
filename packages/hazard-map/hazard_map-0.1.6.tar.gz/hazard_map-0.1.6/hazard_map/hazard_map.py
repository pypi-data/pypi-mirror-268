import io
import os
import re
from enum import Enum
from dataclasses import dataclass
from typing import Tuple, Dict, Optional
import functools
import json

import numpy as np
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt


@dataclass(frozen=True)
class Sheet:
    '''Represents a sheet within an Excel workbook. Each should contain one mapping table.'''

    name: str
    id_list_locations: tuple[int, int]
    name_list_locations: tuple[int, int]
    mapping_table_location: tuple[int, int]
    transpose: bool


class Kind(Enum):
    '''Describes the kind of a node in the network and how it should be labelled as a string.'''

    HAZARD = 'H'
    CAUSE = 'CA'
    CONTROL = 'CO'


@dataclass(frozen=True)
@functools.total_ordering
class Node:
    '''Represents a node in the network.'''

    kind: Kind
    number: int

    def to_str(self) -> str:
        '''Returns a string repsentation of a node.'''
        return f'{self.kind.value}-{str(self.number).zfill(ZERO_PADDING_DIGITS)}'

    @classmethod
    def from_str(cls, string: str):
        '''Tries to create a new node from a string representation of one.'''
        match = re.match(NODE_MATCHER, string)
        if not match:
            raise Exception(f'{string} couldn\'t be parsed as a node')

        return cls(
            KIND_STR_DICT[match['kind']],
            int(match['number']),
        )

    def __lt__(self, other) -> bool:
        '''Allows some basic sorting of nodes by the number they are labelled with.'''
        return self.number < other.number


ZERO_PADDING_DIGITS = 2
DEFAULT_RENDERING_DPI = 480

NODE_MATCHER = re.compile(r'^(?P<kind>H|CA|CO)-?(?P<number>\d+)$')
MAPPING_MATCHER = re.compile(r'^\s*[Y]\s*$', re.I)

KIND_STR_DICT = {
    'H': Kind.HAZARD,
    'CA': Kind.CAUSE,
    'CO': Kind.CONTROL,
}

KIND_COLOURS = {
    Kind.HAZARD: '#d2476b',
    Kind.CAUSE: '#7d5594',
    Kind.CONTROL: '#2762bc',
}


class HazardMap:
    '''Represents a set of hazard, cause, and control mappings.'''

    def __init__(self, workbook_path: str):
        self.WORKBOOK_PATH = workbook_path
        self.WORKBOOK_NAME = self.parse_workbook_filename(self.WORKBOOK_PATH)

        self.graph = nx.Graph()

    def parse_workbook_filename(self, workbook_path: str) -> str:
        '''Check that the file being used is an Excel workbook and parse out its name.'''
        workbook_filename = os.path.basename(workbook_path)
        workbook_name, workbook_filetype = os.path.splitext(workbook_filename)
        if workbook_filetype == '.xlsx':
            return workbook_name
        else:
            raise Exception('Please upload an xlsx file')

    def extract_sheet_mappings(
        self, sheets: list[Sheet], custom_mapping_regex: Optional[str] = None
    ):
        '''Extract hazard-cause and cause-control mappings from the matrices in the workbook.'''
        for sheet in sheets:
            df = pd.read_excel(self.WORKBOOK_PATH, sheet.name, header=None, index_col=None)

            # transform the sheet as appropriate
            if sheet.transpose:
                df = df.T
            df = self._extract_clean_mappings(df, sheet)

            df.apply(self._extract_individual_mappings, axis=1, args=[custom_mapping_regex])

    def _extract_clean_mappings(self, df: pd.DataFrame, sheet: Sheet) -> pd.DataFrame:
        '''Extract a clean table of mappings from the raw worksheet.'''

        # find out what size the mapping table is (i.e. how many pairs are in the table)
        def find_list_length(s: pd.Series) -> int:
            for i, item in enumerate(s):
                if item in [0, np.nan, '']:
                    break
            return i

        table_dimensions = tuple(
            [
                find_list_length(name_list)
                for name_list, axis in zip(
                    (
                        df.iloc[sheet.name_list_locations[1], sheet.mapping_table_location[0] :],
                        df.iloc[sheet.mapping_table_location[1] :, sheet.name_list_locations[0]],
                    ),
                    ('horizontal', 'vertical'),
                )
            ]
        )
        # name the entries according to their labelling in the sheet
        df = df.set_index(df.iloc[:, sheet.id_list_locations[1]])
        df.columns = pd.Index(df.iloc[sheet.id_list_locations[0], :])
        # reduce the dataframe to only the mappings on the sheet
        df = df.iloc[
            sheet.mapping_table_location[1] : sheet.mapping_table_location[1]
            + table_dimensions[1],
            sheet.mapping_table_location[0] : sheet.mapping_table_location[0]
            + table_dimensions[0],
        ]
        return df

    def _extract_individual_mappings(
        self, row: pd.Series, custom_mapping_regex: Optional[str] = None
    ):
        '''Extract meaningful mappings from the clean table discerned from the worksheet.'''
        map_from = Node.from_str(str(row.name))

        matcher = MAPPING_MATCHER if not custom_mapping_regex else re.compile(custom_mapping_regex)

        row = row.dropna()
        mapped = row[row.str.match(matcher.pattern)].index.str.strip().to_list()
        mapped_typed = [Node.from_str(node_str) for node_str in mapped]

        for map_to in mapped_typed:
            self.graph.add_edge(map_from, map_to)

    def write_to_file(self, output_directory: str, output_json: bool = False):
        '''Save the extracted mappings as a reformatted Excel workbook (and json if requested).'''
        if nx.is_empty(self.graph):
            print('The graph is empty - there\'s no hazard log to save.')
            return

        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
        output_file = os.path.join(output_directory, f'{self.WORKBOOK_NAME}-hazard_log.xlsx')

        with pd.ExcelWriter(output_file) as writer:
            for hazard in self.filter_node_set_for_kind(
                self.graph.nodes,
                Kind.HAZARD,
            ):
                cause_control_mappings = []

                for cause in self.filter_node_set_for_kind(
                    self.graph[hazard],
                    Kind.CAUSE,
                ):
                    for control in self.filter_node_set_for_kind(
                        self.graph[cause],
                        Kind.CONTROL,
                    ):
                        cause_control_mappings.append((cause.to_str(), control.to_str()))

                df = (
                    pd.DataFrame(
                        data=cause_control_mappings,
                        columns=['cause', 'control'],
                    )
                    .set_index('cause', append=True)
                    .reorder_levels([1, 0])
                )
                df.to_excel(writer, sheet_name=hazard.to_str())
            print(
                'Wrote the mappings in the hazard log format to '
                f'\"{os.path.basename(output_file)}\".'
            )

        if output_json:
            json_file = os.path.join(output_directory, f'{self.WORKBOOK_NAME}-mappings.json')
            json_mappings = self._create_json_description()
            with open(json_file, 'w') as f:
                f.write(json_mappings)
            print(
                'Created a json description of the mappings in '
                f'\"{os.path.basename(json_file)}\".'
            )

    def _create_json_description(self) -> str:
        '''Traverse the network, storing connections in a dictionary which is converted to json.'''
        mapping_dict: Dict[str, dict] = {}

        for hazard in self.filter_node_set_for_kind(
            self.graph.nodes,
            Kind.HAZARD,
        ):
            mapping_dict[hazard.to_str()] = {}

            for cause in self.filter_node_set_for_kind(
                self.graph[hazard],
                Kind.CAUSE,
            ):
                mapping_dict[hazard.to_str()][cause.to_str()] = []

                for control in self.filter_node_set_for_kind(
                    self.graph[cause],
                    Kind.CONTROL,
                ):
                    mapping_dict[hazard.to_str()][cause.to_str()].append(control.to_str())

        return json.dumps(mapping_dict, indent=2)

    def filter_node_set_for_kind(self, node_set: set, kind: Kind) -> list[Node]:
        '''Return all nodes of a given kind from a set.'''
        return sorted([node for node in node_set if node.kind == kind])

    def draw_graph(
        self, custom_dpi: Optional[int] = None
    ) -> Optional[Tuple[plt.Figure, plt.Axes]]:
        '''Draw a colourful graph of network.'''
        self.fig, self.ax = plt.subplots(
            frameon=False,
            figsize=(9, 7),
            dpi=DEFAULT_RENDERING_DPI if not custom_dpi else custom_dpi,
        )
        self.ax.axis('off')

        if nx.is_empty(self.graph):
            return None

        nx.draw_networkx(
            self.graph,
            pos=nx.kamada_kawai_layout(self.graph),
            node_color=[KIND_COLOURS.get(node.kind, '#53676c') for node in self.graph.nodes],
            labels={node: node.to_str() for node in self.graph.nodes},
            node_size=self._define_node_sizes((100, 250)),
            font_size=3,
            alpha=0.9,
            edge_color=(0.5, 0.5, 0.5, 0.9),
            width=0.5,
            ax=self.ax,
        )

        return self.fig, self.ax

    def _define_node_sizes(
        self,
        size_limits: tuple[float, float],
    ) -> list[float]:
        '''Determine the size of each node on the graph based on how many connections it has.'''
        degrees = self.graph.degree()
        large_connect = np.percentile([n_connections for node, n_connections in degrees], 97)
        add_size_per_connect = (size_limits[1] - size_limits[0]) / large_connect

        return [
            min(
                [
                    size_limits[0] + add_size_per_connect * n_connections,
                    size_limits[1],
                ]
            )
            for node, n_connections in degrees
        ]

    def save_graph(self, output_directory: str, custom_dpi: Optional[int] = None):
        '''Save a graph of the network to a file.'''
        if not hasattr(self, 'fig'):
            self.draw_graph()

        if nx.is_empty(self.graph):
            return

        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
        output_file = os.path.join(output_directory, f'{self.WORKBOOK_NAME}-graph_rendering.png')

        plt.savefig(
            output_file,
            transparent=True,
            dpi=DEFAULT_RENDERING_DPI if not custom_dpi else custom_dpi,
        )

        print(f'Saved a plot of the network to "{os.path.basename(output_file)}".')

    def report_kind_counts(self) -> str:
        kind_count_report = 'The network consists of '
        all_kinds = [Kind.HAZARD, Kind.CAUSE, Kind.CONTROL]

        for i, kind in enumerate(all_kinds):
            if i < len(all_kinds) - 2:
                terminator = ', '
            elif i == len(all_kinds) - 2:
                terminator = ', and '
            else:
                terminator = '.'
            kind_count = len(self.filter_node_set_for_kind(self.graph, kind))
            kind_count_report += (
                f'{kind_count} '
                f"{kind.name.lower()}{'s' if kind_count > 1 else ''}"
                f'{terminator}'
            )

        return kind_count_report

    def get_kind_connection_counts(self, kind: Kind) -> pd.DataFrame:
        '''Determine how many nodes of each kind a given kind of node is connected to.'''
        comparison_kinds = [Kind.HAZARD, Kind.CAUSE, Kind.CONTROL]

        counts = [
            tuple(
                [node.to_str()]
                + [
                    len(
                        self.filter_node_set_for_kind(
                            self.graph.neighbors(node),
                            comp_kind,
                        )
                    )
                    for comp_kind in comparison_kinds
                ]
            )
            for node in self.filter_node_set_for_kind(self.graph.nodes, kind)
        ]

        df = pd.DataFrame(
            data=counts, columns=['node'] + [kind.name.lower() for kind in comparison_kinds]
        ).set_index('node')
        df = df.drop(columns=[column for column in df.columns if df[column].sum() == 0])
        df.index = df.index.rename(kind.name.lower())

        if len(df.columns) > 1:
            df['total'] = df.apply(np.sum, axis=1)
            df = df.sort_values('total', ascending=False)
        else:
            df = df.sort_values(df.columns[0], ascending=False)

        return df
