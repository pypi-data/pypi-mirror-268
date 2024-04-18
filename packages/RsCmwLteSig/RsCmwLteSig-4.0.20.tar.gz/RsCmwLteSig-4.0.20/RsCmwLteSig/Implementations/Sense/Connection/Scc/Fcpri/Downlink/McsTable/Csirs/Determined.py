from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeterminedCls:
	"""Determined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("determined", core, parent)

	def get(self, table_name: enums.Table = None, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[int]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FCPRi:DL:MCSTable:CSIRs:DETermined \n
		Snippet: value: List[int] = driver.sense.connection.scc.fcpri.downlink.mcsTable.csirs.determined.get(table_name = enums.Table.ANY, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries an automatically determined mapping table for subframes with CSI-RS. For the scheduling type 'Follow WB
		CQI-PMI-RI' in the table mode DETermined. \n
			:param table_name: ANY | CW1 | CW2 | OTLC1 | OTLC2 | TFLC1 | TFLC2 Selects which mapping table is queried. To check which tables are available, use method RsCmwLteSig.Sense.Connection.Scc.Fcpri.Downlink.Mcs.Atable.ListPy.get_. ANY: table used for all code word / layer constellations CW1: codeword mapped to 1 layer CW2: codeword mapped to 2 layers OTLC1: codeword mapped to 1 layer / 1 or 2 layers in total OTLC2: codeword mapped to 2 layers / 2 layers in total TFLC1: codeword mapped to 1 layer / 3 or 4 layers in total TFLC2: codeword mapped to 2 layers / 3 or 4 layers in total If the Tablename is omitted, OTLC1 is used.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mcs: decimal Comma-separated list of 15 MCS values, for reported CQI index value 1 to 15 Range: 0 to 31"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('table_name', table_name, DataType.Enum, enums.Table, is_optional=True))
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_bin_or_ascii_int_list(f'SENSe:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FCPRi:DL:MCSTable:CSIRs:DETermined? {param}'.rstrip())
		return response
