from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OnsDurationCls:
	"""OnsDuration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("onsDuration", core, parent)

	def set(self, duration: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:SCMuting:ONSDuration \n
		Snippet: driver.configure.cell.scc.scMuting.onsDuration.set(duration = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the ON state duration for SCell muting (SCC DL muting) . \n
			:param duration: numeric Range: 1 ms to 1000 ms, Unit: ms
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(duration)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SCMuting:ONSDuration {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:SCMuting:ONSDuration \n
		Snippet: value: int = driver.configure.cell.scc.scMuting.onsDuration.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the ON state duration for SCell muting (SCC DL muting) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: duration: numeric Range: 1 ms to 1000 ms, Unit: ms"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:SCMuting:ONSDuration?')
		return Conversions.str_to_int(response)
