from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, ca_mode: enums.CarrAggregationMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SCC<Carrier>:CAGGregation:MODE \n
		Snippet: driver.configure.scc.caggregation.mode.set(ca_mode = enums.CarrAggregationMode.INTRaband, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		No command help available \n
			:param ca_mode: No help available
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(ca_mode, enums.CarrAggregationMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:CAGGregation:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.CarrAggregationMode:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SCC<Carrier>:CAGGregation:MODE \n
		Snippet: value: enums.CarrAggregationMode = driver.configure.scc.caggregation.mode.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		No command help available \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: ca_mode: No help available"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:CAGGregation:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CarrAggregationMode)
