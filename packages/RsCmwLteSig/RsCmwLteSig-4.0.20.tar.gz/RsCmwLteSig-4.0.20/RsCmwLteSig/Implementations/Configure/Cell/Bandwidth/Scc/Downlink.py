from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def set(self, bandwidth: enums.Bandwidth, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:BANDwidth:SCC<Carrier>:DL \n
		Snippet: driver.configure.cell.bandwidth.scc.downlink.set(bandwidth = enums.Bandwidth.B014, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the DL cell bandwidth. The PCC DL bandwidth is also used for the UL. \n
			:param bandwidth: B014 | B030 | B050 | B100 | B150 | B200 B014: 1.4 MHz B030: 3 MHz B050: 5 MHz B100: 10 MHz B150: 15 MHz B200: 20 MHz
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.Bandwidth)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:BANDwidth:SCC{secondaryCompCarrier_cmd_val}:DL {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.Bandwidth:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:BANDwidth:SCC<Carrier>:DL \n
		Snippet: value: enums.Bandwidth = driver.configure.cell.bandwidth.scc.downlink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the DL cell bandwidth. The PCC DL bandwidth is also used for the UL. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: bandwidth: B014 | B030 | B050 | B100 | B150 | B200 B014: 1.4 MHz B030: 3 MHz B050: 5 MHz B100: 10 MHz B150: 15 MHz B200: 20 MHz"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:BANDwidth:SCC{secondaryCompCarrier_cmd_val}:DL?')
		return Conversions.str_to_scalar_enum(response, enums.Bandwidth)
