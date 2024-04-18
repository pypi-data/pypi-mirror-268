from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.FadingMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:DSHift:MODE \n
		Snippet: driver.configure.fading.scc.fadingSimulator.dshift.mode.set(mode = enums.FadingMode.NORMal, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the Doppler shift mode. \n
			:param mode: NORMal | USER NORMal: The maximum Doppler frequency is determined by the fading profile. USER: The maximum Doppler frequency is configurable.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FadingMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:DSHift:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.FadingMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:DSHift:MODE \n
		Snippet: value: enums.FadingMode = driver.configure.fading.scc.fadingSimulator.dshift.mode.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the Doppler shift mode. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mode: NORMal | USER NORMal: The maximum Doppler frequency is determined by the fading profile. USER: The maximum Doppler frequency is configurable."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:DSHift:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadingMode)
