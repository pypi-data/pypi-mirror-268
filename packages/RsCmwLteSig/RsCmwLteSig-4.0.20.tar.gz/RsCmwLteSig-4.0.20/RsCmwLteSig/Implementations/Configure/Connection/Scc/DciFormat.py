from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DciFormatCls:
	"""DciFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dciFormat", core, parent)

	def set(self, dci: enums.DciFormat, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:DCIFormat \n
		Snippet: driver.configure.connection.scc.dciFormat.set(dci = enums.DciFormat.D1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the DCI format. The value must be compatible to the transmission mode, see Table 'Transmission scheme overview'. \n
			:param dci: D1 | D1A | D1B | D2 | D2A | D2B | D2C | D61 Format 1, 1A, 1B, 2, 2A, 2B, 2C, 6-1A/B
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(dci, enums.DciFormat)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:DCIFormat {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.DciFormat:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:DCIFormat \n
		Snippet: value: enums.DciFormat = driver.configure.connection.scc.dciFormat.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the DCI format. The value must be compatible to the transmission mode, see Table 'Transmission scheme overview'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: dci: D1 | D1A | D1B | D2 | D2A | D2B | D2C | D61 Format 1, 1A, 1B, 2, 2A, 2B, 2C, 6-1A/B"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:DCIFormat?')
		return Conversions.str_to_scalar_enum(response, enums.DciFormat)
