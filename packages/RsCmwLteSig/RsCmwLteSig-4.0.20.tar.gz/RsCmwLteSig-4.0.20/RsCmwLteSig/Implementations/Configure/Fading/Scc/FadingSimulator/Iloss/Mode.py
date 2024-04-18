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

	def set(self, insert_loss_mode: enums.InsertLossMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:ILOSs:MODE \n
		Snippet: driver.configure.fading.scc.fadingSimulator.iloss.mode.set(insert_loss_mode = enums.InsertLossMode.LACP, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the insertion loss mode. \n
			:param insert_loss_mode: NORMal | USER NORMal: The insertion loss is determined by the fading profile. USER: The insertion loss is configurable.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(insert_loss_mode, enums.InsertLossMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:ILOSs:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.InsertLossMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:ILOSs:MODE \n
		Snippet: value: enums.InsertLossMode = driver.configure.fading.scc.fadingSimulator.iloss.mode.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the insertion loss mode. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: insert_loss_mode: NORMal | USER NORMal: The insertion loss is determined by the fading profile. USER: The insertion loss is configurable."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:ILOSs:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.InsertLossMode)
