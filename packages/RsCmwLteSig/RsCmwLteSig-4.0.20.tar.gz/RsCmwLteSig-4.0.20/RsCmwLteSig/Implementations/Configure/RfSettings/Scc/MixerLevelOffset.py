from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MixerLevelOffsetCls:
	"""MixerLevelOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mixerLevelOffset", core, parent)

	def set(self, mix_lev_offset: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:MLOFfset \n
		Snippet: driver.configure.rfSettings.scc.mixerLevelOffset.set(mix_lev_offset = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Varies the input level of the mixer in the analyzer path. \n
			:param mix_lev_offset: numeric Range: -10 dB to 10 dB, Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(mix_lev_offset)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:MLOFfset {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:MLOFfset \n
		Snippet: value: int = driver.configure.rfSettings.scc.mixerLevelOffset.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Varies the input level of the mixer in the analyzer path. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mix_lev_offset: numeric Range: -10 dB to 10 dB, Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:MLOFfset?')
		return Conversions.str_to_int(response)
