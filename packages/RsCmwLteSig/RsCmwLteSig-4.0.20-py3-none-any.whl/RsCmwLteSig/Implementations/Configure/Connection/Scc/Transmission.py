from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TransmissionCls:
	"""Transmission commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transmission", core, parent)

	def set(self, mode: enums.TransmissionMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:TRANsmission \n
		Snippet: driver.configure.connection.scc.transmission.set(mode = enums.TransmissionMode.TM1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the LTE transmission mode. The value must be compatible to the active scenario, see Table 'Transmission scheme
		overview'. \n
			:param mode: TM1 | TM2 | TM3 | TM4 | TM6 | TM7 | TM8 | TM9 Transmission mode 1, 2, 3, 4, 6, 7, 8, 9
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TransmissionMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TRANsmission {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.TransmissionMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:TRANsmission \n
		Snippet: value: enums.TransmissionMode = driver.configure.connection.scc.transmission.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the LTE transmission mode. The value must be compatible to the active scenario, see Table 'Transmission scheme
		overview'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mode: TM1 | TM2 | TM3 | TM4 | TM6 | TM7 | TM8 | TM9 Transmission mode 1, 2, 3, 4, 6, 7, 8, 9"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TRANsmission?')
		return Conversions.str_to_scalar_enum(response, enums.TransmissionMode)
