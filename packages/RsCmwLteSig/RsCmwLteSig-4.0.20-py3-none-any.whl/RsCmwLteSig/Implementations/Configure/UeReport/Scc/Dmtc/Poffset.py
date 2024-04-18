from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoffsetCls:
	"""Poffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, offset: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:DMTC:POFFset \n
		Snippet: driver.configure.ueReport.scc.dmtc.poffset.set(offset = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the offset of the DRS for LAA. The offset must be at least 5 ms smaller than the configured periodicity, see
		method RsCmwLteSig.Configure.UeReport.Scc.Dmtc.Period.set. \n
			:param offset: numeric Range: 0 ms to 155 ms, Unit: ms
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:DMTC:POFFset {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:DMTC:POFFset \n
		Snippet: value: int = driver.configure.ueReport.scc.dmtc.poffset.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the offset of the DRS for LAA. The offset must be at least 5 ms smaller than the configured periodicity, see
		method RsCmwLteSig.Configure.UeReport.Scc.Dmtc.Period.set. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: offset: numeric Range: 0 ms to 155 ms, Unit: ms"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:DMTC:POFFset?')
		return Conversions.str_to_int(response)
