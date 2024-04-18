from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[enums.Table]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FCPRi:DL:MCS:ATABle:LIST \n
		Snippet: value: List[enums.Table] = driver.sense.connection.scc.fcpri.downlink.mcs.atable.listPy.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns a list of all mapping tables available for the scheduling type 'Follow WB CQI-PMI-RI' in the table mode
		DETermined. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: tables: ANY | CW1 | CW2 | OTLC1 | OTLC2 | TFLC1 | TFLC2 Comma-separated list of table identifiers that can be used in the mapping table commands SENSe:LTE:SIGNi:CONNection:...:FCPRi:DL:MCSTable[:...]:DETermined."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FCPRi:DL:MCS:ATABle:LIST?')
		return Conversions.str_to_list_enum(response, enums.Table)
