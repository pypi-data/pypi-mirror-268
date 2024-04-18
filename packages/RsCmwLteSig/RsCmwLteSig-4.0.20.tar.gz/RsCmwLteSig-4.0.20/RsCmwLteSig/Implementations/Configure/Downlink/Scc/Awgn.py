from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AwgnCls:
	"""Awgn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("awgn", core, parent)

	def set(self, awgn: float or bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:AWGN \n
		Snippet: driver.configure.downlink.scc.awgn.set(awgn = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the total level of the additive white Gaussian noise (AWGN) interferer. The unit dBm/15 kHz indicates the
		spectral density integrated across one subcarrier. The range depends on several parameters. It either equals the range of
		the RS EPRE or is a part of this range. \n
			:param awgn: (float or boolean) numeric | ON | OFF Range: depends on many parameters , Unit: dBm/15kHz ON | OFF enables or disables the AWGN interferer.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_or_bool_value_to_str(awgn)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:AWGN {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:AWGN \n
		Snippet: value: float or bool = driver.configure.downlink.scc.awgn.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the total level of the additive white Gaussian noise (AWGN) interferer. The unit dBm/15 kHz indicates the
		spectral density integrated across one subcarrier. The range depends on several parameters. It either equals the range of
		the RS EPRE or is a part of this range. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: awgn: (float or boolean) numeric | ON | OFF Range: depends on many parameters , Unit: dBm/15kHz ON | OFF enables or disables the AWGN interferer."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:AWGN?')
		return Conversions.str_to_float_or_bool(response)
