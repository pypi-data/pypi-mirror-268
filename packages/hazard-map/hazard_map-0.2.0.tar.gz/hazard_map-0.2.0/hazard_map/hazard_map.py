import functools
import json
import os
import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import networkx as nx
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from termcolor import colored


@dataclass(frozen=True)
class Sheet:
    """Represents a sheet within an Excel workbook. Each should contain one mapping table."""

    name: str
    id_list_locations: tuple[int, int]
    name_list_locations: tuple[int, int]
    mapping_table_location: tuple[int, int]
    transpose: bool


class Kind(Enum):
    """Describes the kind of a node in the network and how it should be labelled as a string."""

    HAZARD = 'H'
    CAUSE = 'CA'
    CONTROL = 'CO'


@dataclass(frozen=True)
@functools.total_ordering
class Node:
    """Represents a node in the network."""

    kind: Kind
    number: int

    def to_str(self) -> str:
        """Returns a string repsentation of a node."""
        return f'{self.kind.value}-{str(self.number).zfill(ZERO_PADDING_DIGITS)}'

    @classmethod
    def from_str(cls, string: str):
        """Tries to create a new node from a string representation of one."""
        match = re.match(NODE_MATCHER, string.strip())
        if not match:
            raise Exception(f"{string} couldn't be parsed as a node")

        return cls(
            KIND_STR_DICT[match['kind']],
            int(match['number']),
        )

    def __gt__(self, other) -> bool:
        """Allows nodes to be sorted according to their kind and number."""
        if list(Kind).index(self.kind) > list(Kind).index(other.kind):
            return True
        else:
            return self.number > other.number


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
    Kind.HAZARD: {'name': 'red', 'hex': '#d2476b'},
    Kind.CAUSE: {'name': 'magenta', 'hex': '#7d5594'},
    Kind.CONTROL: {'name': 'blue', 'hex': '#2762bc'},
}


class HazardMap:
    """Represents a set of hazard, cause, and control mappings."""

    def __init__(self, workbook_path: str):
        self.WORKBOOK_PATH = workbook_path
        self.WORKBOOK_NAME = self.parse_workbook_filename(self.WORKBOOK_PATH)

        self.graph = nx.Graph()
        self.all_nodes: set[Node] = set()
        self.disconnected_nodes: dict[Kind, set] = {kind: set() for kind in list(Kind)}

    def parse_workbook_filename(self, workbook_path: str) -> str:
        """Check that the file being used is an Excel workbook and parse out its name."""
        workbook_filename = os.path.basename(workbook_path)
        workbook_name, workbook_filetype = os.path.splitext(workbook_filename)
        if workbook_filetype == '.xlsx':
            return workbook_name
        else:
            raise Exception('Please upload an xlsx file')

    def extract_sheet_mappings(
        self, sheets: list[Sheet], custom_mapping_regex: Optional[str] = None
    ):
        """Extract hazard-cause and cause-control mappings from the matrices in the workbook."""
        for sheet in sheets:
            df = pd.read_excel(self.WORKBOOK_PATH, sheet.name, header=None, index_col=None)

            # transform the sheet as appropriate
            if sheet.transpose:
                df = df.T
            df = self._extract_mapping_matrix(df, sheet)
            df = self._clean_up_mappings(df, custom_mapping_regex)

            # record all nodes that appear in the table
            self.all_nodes.update(df.index.to_list() + df.columns.to_list())

            df.apply(self._add_mappings_to_graph, axis=1)

    def _extract_mapping_matrix(self, df: pd.DataFrame, sheet: Sheet) -> pd.DataFrame:
        """Extract a the table of mappings from the raw worksheet."""
        table_dimensions = tuple(
            [
                self._find_table_dimension(name_list)
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

    def _clean_up_mappings(
        self, df: pd.DataFrame, custom_mapping_regex: Optional[str] = None
    ) -> pd.DataFrame:
        """Clean up the mapping table by converting axes to meaninful types and assessing whether
        nodes map together or not."""
        # convert the axes of the table from strings to nodes
        df.index = df.index.map(Node.from_str)
        df.columns = df.columns.map(Node.from_str)

        # determine whether nodes map together or not
        df = df.apply(
            lambda s: s.str.match(
                MAPPING_MATCHER if not custom_mapping_regex else re.compile(custom_mapping_regex)
            )
        )

        return df

    def _find_table_dimension(self, s: pd.Series) -> int:
        """Find out what size the mapping table is (i.e. how many pairs are in the table)."""
        for i, item in enumerate(s):
            if item in [0, np.nan, '']:
                break
        return i

    def _add_mappings_to_graph(self, row: pd.Series):
        """Add mappings from the clean table discerned from the worksheet to the graph."""
        map_from = row.name
        row = row.dropna()
        mapped_to = row[row].index.to_list()
        for map_to in mapped_to:
            self.graph.add_edge(map_from, map_to)

    def report_kind_counts(self) -> str:
        """Count how many nodes of each kind are present in the network and create a string
        describing the result."""
        kind_count_report = 'The network consists of:'
        all_kinds = list(Kind)

        for i, kind in enumerate(all_kinds):
            kind_count = len(self.filter_node_set_for_kind(self.graph, kind))
            kind_str = colored(
                f"{kind.name.title()}{'s' if kind_count > 1 else ''}",
                KIND_COLOURS.get(kind, {'name': 'white'})['name'],  # type: ignore [arg-type]
            )
            kind_count_report += f"\n{' '*4}• {kind_count} {kind_str}"

        return kind_count_report

    def report_disconnected_nodes(self) -> Optional[str]:
        """Find nodes which aren't connected to others as they should be and create a string
        describing the result"""
        self.disconnected_nodes = self._find_disconnected_nodes()

        kinds_with_disconnections = [
            kind for kind, disconnected_set in self.disconnected_nodes.items() if disconnected_set
        ]
        if not kinds_with_disconnections:
            return None

        disconnected_nodes_report = 'Some nodes are missing connections:'
        for kind in list(Kind):
            if kind in kinds_with_disconnections:
                disconnected_nodes_of_kind = sorted(list(self.disconnected_nodes[kind]))
                disconnected_nodes_str = ', '.join(
                    [node.to_str() for node in disconnected_nodes_of_kind]
                )
                kind_str = colored(
                    f"{kind.name.title()}{'s' if len(disconnected_nodes_of_kind) > 1 else ''}",
                    KIND_COLOURS.get(kind, {'name': 'white'})['name'],  # type: ignore [arg-type]
                )
                disconnected_nodes_report += f"\n{' '*4}• {kind_str}: {disconnected_nodes_str}"

        return disconnected_nodes_report

    def _find_disconnected_nodes(self) -> dict[Kind, set[Node]]:
        """Find nodes in the graph which don't connect to the rest as they should."""
        intended_connections = {
            Kind.HAZARD: set([Kind.CAUSE]),
            Kind.CAUSE: set([Kind.HAZARD, Kind.CONTROL]),
            Kind.CONTROL: set([Kind.CAUSE]),
        }

        # search for nodes which don't connect to all of the kinds that they should
        for kind, connected_kinds in intended_connections.items():
            for node in self.filter_node_set_for_kind(self.graph, kind):
                for connected_kind in connected_kinds:
                    if not self.filter_node_set_for_kind(
                        self.graph.neighbors(node), connected_kind
                    ):
                        self.disconnected_nodes[kind].add(node)

        # find nodes that appeared in the mapping table axes but don't map to anything
        for node in self.all_nodes:
            if node not in self.graph:
                self.disconnected_nodes[node.kind].add(node)

        return self.disconnected_nodes

    def filter_node_set_for_kind(self, node_set: set[Node], kind: Kind) -> list[Node]:
        """Return all nodes of a given kind from a set."""
        return sorted([node for node in node_set if node.kind == kind])

    def write_to_file(self, output_directory: str, output_json: bool = False):
        """Save the extracted mappings as a reformatted Excel workbook (and json if requested)."""
        if nx.is_empty(self.graph):
            print("The graph is empty - there's no hazard log to save.")
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
                f"\"{colored(os.path.basename(output_file), 'cyan')}\"."
            )

        if output_json:
            json_file = os.path.join(output_directory, f'{self.WORKBOOK_NAME}-mappings.json')
            json_mappings = self._create_json_description()
            with open(json_file, 'w') as f:
                f.write(json_mappings)
            print(
                'Created a json description of the mappings in '
                f"\"{colored(os.path.basename(json_file), 'cyan')}\"."
            )

    def _create_json_description(self) -> str:
        """Traverse the network, storing connections in a dictionary which is converted to json."""
        mapping_dict: dict[str, dict] = {}

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

    def draw_graph(
        self, custom_dpi: Optional[int] = None
    ) -> Optional[tuple[plt.Figure, plt.Axes]]:
        """Draw a colourful graph of network."""
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
            node_color=[
                KIND_COLOURS.get(node.kind, {'hex': '#53676c'})['hex'] for node in self.graph.nodes
            ],
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
        """Determine the size of each node on the graph based on how many connections it has."""
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

    def save_drawing(self, output_directory: str, custom_dpi: Optional[int] = None):
        """Save a graph of the network to a file."""
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

        print(
            f"Saved a plot of the network to \"{colored(os.path.basename(output_file), 'cyan')}\"."
        )

    def get_kind_connection_counts(self, kind: Kind) -> pd.DataFrame:
        """Determine how many nodes of each kind a given kind of node is connected to."""
        comparison_kinds = list(Kind)

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
