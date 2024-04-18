from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrateCls:
	"""Crate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crate", core, parent)

	def get(self, symbols: enums.Symbols, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDCHannels:LAA:RBURst:DL<Stream>:PEPSubframes:CRATe \n
		Snippet: value: float = driver.sense.connection.scc.udChannels.laa.rburst.downlink.pepSubFrames.crate.get(symbols = enums.Symbols.S0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Queries the code rate for ending subframes with a certain partial allocation, for LAA, random bursts, scheduling type
		'User-defined Channels'. \n
			:param symbols: S6 | S9 | S10 | S11 | S12 Number of OFDM symbols allocated in the ending subframe
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
			:return: coderate: float Range: 0 to 10"""
		param = Conversions.enum_scalar_to_str(symbols, enums.Symbols)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDCHannels:LAA:RBURst:DL{stream_cmd_val}:PEPSubframes:CRATe? {param}')
		return Conversions.str_to_float(response)
