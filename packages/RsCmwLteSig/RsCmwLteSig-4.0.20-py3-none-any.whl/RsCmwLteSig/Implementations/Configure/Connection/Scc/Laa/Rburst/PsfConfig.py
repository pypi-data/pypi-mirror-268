from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsfConfigCls:
	"""PsfConfig commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psfConfig", core, parent)

	def set(self, configuration: enums.PallocConfig, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:PSFConfig \n
		Snippet: driver.configure.connection.scc.laa.rburst.psfConfig.set(configuration = enums.PallocConfig.BOTH, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures in which subframes partial allocation is allowed, for LAA with random bursts. \n
			:param configuration: NO | INIT | END | BOTH NO: only full allocation INIT: partial allocation allowed for initial subframes END: partial allocation allowed for ending subframes BOTH: partial allocation allowed for initial and ending subframes
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(configuration, enums.PallocConfig)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:PSFConfig {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.PallocConfig:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:RBURst:PSFConfig \n
		Snippet: value: enums.PallocConfig = driver.configure.connection.scc.laa.rburst.psfConfig.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures in which subframes partial allocation is allowed, for LAA with random bursts. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: configuration: NO | INIT | END | BOTH NO: only full allocation INIT: partial allocation allowed for initial subframes END: partial allocation allowed for ending subframes BOTH: partial allocation allowed for initial and ending subframes"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:RBURst:PSFConfig?')
		return Conversions.str_to_scalar_enum(response, enums.PallocConfig)
