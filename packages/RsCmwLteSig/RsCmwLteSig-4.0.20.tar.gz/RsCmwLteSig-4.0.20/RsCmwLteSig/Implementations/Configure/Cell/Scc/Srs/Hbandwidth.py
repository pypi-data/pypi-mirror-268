from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HbandwidthCls:
	"""Hbandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hbandwidth", core, parent)

	def set(self, hopping_bw: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SRS:HBANdwidth \n
		Snippet: driver.configure.cell.scc.srs.hbandwidth.set(hopping_bw = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'srs-HoppingBandwidth' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param hopping_bw: numeric Range: 0 to 3
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(hopping_bw)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SRS:HBANdwidth {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<carrier>:SRS:HBANdwidth \n
		Snippet: value: int = driver.configure.cell.scc.srs.hbandwidth.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the 'srs-HoppingBandwidth' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: hopping_bw: numeric Range: 0 to 3"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SRS:HBANdwidth?')
		return Conversions.str_to_int(response)
