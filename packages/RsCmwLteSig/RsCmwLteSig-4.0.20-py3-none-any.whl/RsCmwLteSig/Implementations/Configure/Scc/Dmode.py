from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmodeCls:
	"""Dmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmode", core, parent)

	def set(self, mode: enums.DuplexMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:DMODe \n
		Snippet: driver.configure.scc.dmode.set(mode = enums.DuplexMode.FDD, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the duplex mode of the LTE signal: FDD or TDD. See also method RsCmwLteSig.Configure.Pcc.Dmode.ucSpecific. \n
			:param mode: FDD | TDD
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DuplexMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:DMODe {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.DuplexMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:DMODe \n
		Snippet: value: enums.DuplexMode = driver.configure.scc.dmode.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the duplex mode of the LTE signal: FDD or TDD. See also method RsCmwLteSig.Configure.Pcc.Dmode.ucSpecific. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mode: FDD | TDD"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:DMODe?')
		return Conversions.str_to_scalar_enum(response, enums.DuplexMode)
