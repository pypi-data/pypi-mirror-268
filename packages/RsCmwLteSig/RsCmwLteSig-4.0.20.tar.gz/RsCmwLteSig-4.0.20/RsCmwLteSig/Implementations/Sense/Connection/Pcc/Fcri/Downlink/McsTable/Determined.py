from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeterminedCls:
	"""Determined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("determined", core, parent)

	def get(self, table_name: enums.Table = None) -> List[int]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:FCRI:DL:MCSTable:DETermined \n
		Snippet: value: List[int] = driver.sense.connection.pcc.fcri.downlink.mcsTable.determined.get(table_name = enums.Table.ANY) \n
		Queries an automatically determined mapping table for normal subframes. For the scheduling type 'Follow WB CQI-RI' in the
		table mode DETermined. \n
			:param table_name: ANY | CW1 | CW2 | OTLC1 | OTLC2 | TFLC1 | TFLC2 Selects which mapping table is queried. To check which tables are available, use method RsCmwLteSig.Sense.Connection.Scc.Fcri.Downlink.Mcs.Atable.ListPy.get_. ANY: table used for all code word / layer constellations CW1: codeword mapped to 1 layer CW2: codeword mapped to 2 layers OTLC1: codeword mapped to 1 layer / 1 or 2 layers in total OTLC2: codeword mapped to 2 layers / 2 layers in total TFLC1: codeword mapped to 1 layer / 3 or 4 layers in total TFLC2: codeword mapped to 2 layers / 3 or 4 layers in total If the Tablename is omitted, CW1 is used.
			:return: mcs: decimal Comma-separated list of 15 MCS values, for reported CQI index value 1 to 15 Range: 0 to 31"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('table_name', table_name, DataType.Enum, enums.Table, is_optional=True))
		response = self._core.io.query_bin_or_ascii_int_list(f'SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:FCRI:DL:MCSTable:DETermined? {param}'.rstrip())
		return response
