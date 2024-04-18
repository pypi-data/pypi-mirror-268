from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LossCls:
	"""Loss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loss", core, parent)

	def set(self, insertion_loss: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:ILOSs:LOSS \n
		Snippet: driver.configure.fading.scc.fadingSimulator.iloss.loss.set(insertion_loss = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the insertion loss for the fading simulator. A setting is only allowed in USER mode (see CONFigure:...
		:FSIMulator:ILOSs:MODE) . \n
			:param insertion_loss: numeric Range: 0 dB to 30 dB, Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(insertion_loss)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:ILOSs:LOSS {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:ILOSs:LOSS \n
		Snippet: value: float = driver.configure.fading.scc.fadingSimulator.iloss.loss.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the insertion loss for the fading simulator. A setting is only allowed in USER mode (see CONFigure:...
		:FSIMulator:ILOSs:MODE) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: insertion_loss: numeric Range: 0 dB to 30 dB, Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:ILOSs:LOSS?')
		return Conversions.str_to_float(response)
