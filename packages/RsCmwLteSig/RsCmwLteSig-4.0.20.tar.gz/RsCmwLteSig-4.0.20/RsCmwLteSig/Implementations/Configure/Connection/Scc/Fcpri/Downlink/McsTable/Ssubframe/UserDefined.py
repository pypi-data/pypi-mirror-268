from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefinedCls:
	"""UserDefined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("userDefined", core, parent)

	def set(self, mcs: List[int], secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FCPRi:DL:MCSTable:SSUBframe:UDEFined \n
		Snippet: driver.configure.connection.scc.fcpri.downlink.mcsTable.ssubframe.userDefined.set(mcs = [1, 2, 3], secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures a user-defined mapping table for special subframes that assigns an MCS index value to each possible reported
		wideband CQI index value. The table is used for the scheduling type 'Follow WB CQI-PMI-RI' if the table mode is set to
		UDEFined. \n
			:param mcs: numeric Comma-separated list of 15 MCS values, for reported CQI index value 1 to 15 The range is restricted by the highest allowed modulation scheme: max 27 with 256-QAM, max 26 with 1024-QAM. Range: 0 to 28
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.list_to_csv_str(mcs)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FCPRi:DL:MCSTable:SSUBframe:UDEFined {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[int]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FCPRi:DL:MCSTable:SSUBframe:UDEFined \n
		Snippet: value: List[int] = driver.configure.connection.scc.fcpri.downlink.mcsTable.ssubframe.userDefined.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures a user-defined mapping table for special subframes that assigns an MCS index value to each possible reported
		wideband CQI index value. The table is used for the scheduling type 'Follow WB CQI-PMI-RI' if the table mode is set to
		UDEFined. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mcs: numeric Comma-separated list of 15 MCS values, for reported CQI index value 1 to 15 The range is restricted by the highest allowed modulation scheme: max 27 with 256-QAM, max 26 with 1024-QAM. Range: 0 to 28"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_bin_or_ascii_int_list(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FCPRi:DL:MCSTable:SSUBframe:UDEFined?')
		return response
