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

	def set(self, mode: enums.BeamformingMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:BEAMforming:MODE \n
		Snippet: driver.configure.connection.scc.beamforming.mode.set(mode = enums.BeamformingMode.OFF, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the beamforming mode for TM 7 and 8.
			INTRO_CMD_HELP: Depending on other settings, only a subset of the values is allowed, see: \n
			- TM 7: 'Beamforming Mode'
			- TM 8: 'Beamforming Mode' \n
			:param mode: OFF | ON | TSBF | PMAT OFF: Beamforming is disabled ON: Beamforming is enabled. The configured beamforming matrix is used. TSBF: Beamforming is enabled. The beamforming matrix is selected randomly as defined in 3GPP TS 36.521, annex B.4.1 and B.4.2. PMAT: Beamforming is enabled. A precoding matrix is used as beamforming matrix, see method RsCmwLteSig.Configure.Connection.Pcc.pmatrix.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.BeamformingMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:BEAMforming:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.BeamformingMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:BEAMforming:MODE \n
		Snippet: value: enums.BeamformingMode = driver.configure.connection.scc.beamforming.mode.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the beamforming mode for TM 7 and 8.
			INTRO_CMD_HELP: Depending on other settings, only a subset of the values is allowed, see: \n
			- TM 7: 'Beamforming Mode'
			- TM 8: 'Beamforming Mode' \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mode: OFF | ON | TSBF | PMAT OFF: Beamforming is disabled ON: Beamforming is enabled. The configured beamforming matrix is used. TSBF: Beamforming is enabled. The beamforming matrix is selected randomly as defined in 3GPP TS 36.521, annex B.4.1 and B.4.2. PMAT: Beamforming is enabled. A precoding matrix is used as beamforming matrix, see method RsCmwLteSig.Configure.Connection.Pcc.pmatrix."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:BEAMforming:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BeamformingMode)
