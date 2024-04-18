from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AtableCls:
	"""Atable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atable", core, parent)

	# noinspection PyTypeChecker
	def get_list_py(self) -> List[enums.Table]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:FCPRi:DL:MCS:ATABle:LIST \n
		Snippet: value: List[enums.Table] = driver.sense.connection.pcc.fcpri.downlink.mcs.atable.get_list_py() \n
		Returns a list of all mapping tables available for the scheduling type 'Follow WB CQI-PMI-RI' in the table mode
		DETermined. \n
			:return: tables: ANY | CW1 | CW2 | OTLC1 | OTLC2 | TFLC1 | TFLC2 Comma-separated list of table identifiers that can be used in the mapping table commands SENSe:LTE:SIGNi:CONNection:...:FCPRi:DL:MCSTable[:...]:DETermined.
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:FCPRi:DL:MCS:ATABle:LIST?')
		return Conversions.str_to_list_enum(response, enums.Table)
