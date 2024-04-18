from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NtxAntennasCls:
	"""NtxAntennas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntxAntennas", core, parent)

	def set(self, antennas: enums.AntennasTxB, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:NTXantennas \n
		Snippet: driver.configure.connection.scc.tm.ntxAntennas.set(antennas = enums.AntennasTxB.EIGHt, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of downlink TX antennas for TM 9. \n
			:param antennas: TWO | FOUR | EIGHt
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(antennas, enums.AntennasTxB)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:NTXantennas {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.AntennasTxB:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:NTXantennas \n
		Snippet: value: enums.AntennasTxB = driver.configure.connection.scc.tm.ntxAntennas.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of downlink TX antennas for TM 9. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: antennas: TWO | FOUR | EIGHt"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:NTXantennas?')
		return Conversions.str_to_scalar_enum(response, enums.AntennasTxB)
