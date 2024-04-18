from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsirsCls:
	"""Csirs commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csirs", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.CsirsMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:CSIRs:MODE \n
		Snippet: value: enums.CsirsMode = driver.configure.downlink.pcc.csirs.get_mode() \n
		Selects a configuration mode for the used CSI-RS power offset. \n
			:return: mode: ACSirs | MANual ACSirs The used power offset matches the signaled value. For configuration of the signaled value, see method RsCmwLteSig.Configure.Connection.Scc.Tm.Csirs.Power.set. MANual The used power offset is independent from the signaled value. For configuration of the used power offset, see method RsCmwLteSig.Configure.Downlink.Scc.Csirs.Poffset.set.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:CSIRs:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CsirsMode)

	def set_mode(self, mode: enums.CsirsMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:CSIRs:MODE \n
		Snippet: driver.configure.downlink.pcc.csirs.set_mode(mode = enums.CsirsMode.ACSirs) \n
		Selects a configuration mode for the used CSI-RS power offset. \n
			:param mode: ACSirs | MANual ACSirs The used power offset matches the signaled value. For configuration of the signaled value, see method RsCmwLteSig.Configure.Connection.Scc.Tm.Csirs.Power.set. MANual The used power offset is independent from the signaled value. For configuration of the used power offset, see method RsCmwLteSig.Configure.Downlink.Scc.Csirs.Poffset.set.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CsirsMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:CSIRs:MODE {param}')

	def get_poffset(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:CSIRs:POFFset \n
		Snippet: value: float = driver.configure.downlink.pcc.csirs.get_poffset() \n
		Sets the EPRE of the PDSCH relative to the EPRE of the CSI reference signal. The value is only used for method
		RsCmwLteSig.Configure.Downlink.Scc.Csirs.Mode.set = ACSirs. \n
			:return: offset: numeric Range: -30 dB to 8 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:CSIRs:POFFset?')
		return Conversions.str_to_float(response)

	def set_poffset(self, offset: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:CSIRs:POFFset \n
		Snippet: driver.configure.downlink.pcc.csirs.set_poffset(offset = 1.0) \n
		Sets the EPRE of the PDSCH relative to the EPRE of the CSI reference signal. The value is only used for method
		RsCmwLteSig.Configure.Downlink.Scc.Csirs.Mode.set = ACSirs. \n
			:param offset: numeric Range: -30 dB to 8 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:CSIRs:POFFset {param}')
