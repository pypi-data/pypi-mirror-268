from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmacCls:
	"""Pmac commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmac", core, parent)

	def set(self, activation: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:SCMuting:PMAC \n
		Snippet: driver.configure.cell.scc.scMuting.pmac.set(activation = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables periodic MAC activation. \n
			:param activation: OFF | ON
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(activation)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SCMuting:PMAC {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:SCMuting:PMAC \n
		Snippet: value: bool = driver.configure.cell.scc.scMuting.pmac.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables periodic MAC activation. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: activation: OFF | ON"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SCMuting:PMAC?')
		return Conversions.str_to_bool(response)
