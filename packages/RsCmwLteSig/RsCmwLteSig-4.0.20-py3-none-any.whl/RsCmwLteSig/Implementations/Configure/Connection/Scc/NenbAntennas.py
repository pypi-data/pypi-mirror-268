from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NenbAntennasCls:
	"""NenbAntennas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nenbAntennas", core, parent)

	def set(self, antennas: enums.AntennasTxA, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:NENBantennas \n
		Snippet: driver.configure.connection.scc.nenbAntennas.set(antennas = enums.AntennasTxA.FOUR, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of downlink TX antennas for transmission mode 1 to 6. The value must be compatible to the active
		scenario and transmission mode, see Table 'Transmission scheme overview'. \n
			:param antennas: ONE | TWO | FOUR
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(antennas, enums.AntennasTxA)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:NENBantennas {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.AntennasTxA:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:NENBantennas \n
		Snippet: value: enums.AntennasTxA = driver.configure.connection.scc.nenbAntennas.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of downlink TX antennas for transmission mode 1 to 6. The value must be compatible to the active
		scenario and transmission mode, see Table 'Transmission scheme overview'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: antennas: ONE | TWO | FOUR"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:NENBantennas?')
		return Conversions.str_to_scalar_enum(response, enums.AntennasTxA)
