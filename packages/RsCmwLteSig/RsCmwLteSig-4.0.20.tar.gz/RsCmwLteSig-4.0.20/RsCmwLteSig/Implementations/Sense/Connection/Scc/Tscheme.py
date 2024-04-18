from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TschemeCls:
	"""Tscheme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tscheme", core, parent)

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.TransmScheme:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:TSCHeme \n
		Snippet: value: enums.TransmScheme = driver.sense.connection.scc.tscheme.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the transmission scheme. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: scheme: SISO | SIMO | TXDiversity | OLSMultiplex | CLSMultiplex | CLSingle | SBF5 | SBF8 | DBF78 | FBF710 SISO: single input single output SIMO: single input multiple outputs (receive diversity) TXDiversity: transmit diversity OLSMultiplex: open loop spatial multiplexing CLSMultiplex: closed loop spatial multiplexing CLSingle: closed loop spatial multiplexing, single layer SBF5: single-layer beamforming (port 5) SBF8: single-layer beamforming (port 8) DBF78: dual-layer beamforming (ports 7, 8) FBF710: four-layer beamforming (ports 7 to 10)"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TSCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.TransmScheme)
