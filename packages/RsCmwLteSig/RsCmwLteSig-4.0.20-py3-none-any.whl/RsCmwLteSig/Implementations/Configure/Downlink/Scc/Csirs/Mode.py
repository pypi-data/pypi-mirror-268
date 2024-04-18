from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.CsirsMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:CSIRs:MODE \n
		Snippet: driver.configure.downlink.scc.csirs.mode.set(mode = enums.CsirsMode.ACSirs, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a configuration mode for the used CSI-RS power offset. \n
			:param mode: ACSirs | MANual ACSirs The used power offset matches the signaled value. For configuration of the signaled value, see method RsCmwLteSig.Configure.Connection.Scc.Tm.Csirs.Power.set. MANual The used power offset is independent from the signaled value. For configuration of the used power offset, see method RsCmwLteSig.Configure.Downlink.Scc.Csirs.Poffset.set.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CsirsMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:CSIRs:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.CsirsMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:CSIRs:MODE \n
		Snippet: value: enums.CsirsMode = driver.configure.downlink.scc.csirs.mode.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a configuration mode for the used CSI-RS power offset. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mode: ACSirs | MANual ACSirs The used power offset matches the signaled value. For configuration of the signaled value, see method RsCmwLteSig.Configure.Connection.Scc.Tm.Csirs.Power.set. MANual The used power offset is independent from the signaled value. For configuration of the used power offset, see method RsCmwLteSig.Configure.Downlink.Scc.Csirs.Poffset.set."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:CSIRs:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CsirsMode)
