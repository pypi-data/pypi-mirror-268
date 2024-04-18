from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcAlphaCls:
	"""PcAlpha commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcAlpha", core, parent)

	# noinspection PyTypeChecker
	def get_advanced(self) -> enums.PathCompAlpha:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:APPower:PCALpha:ADVanced \n
		Snippet: value: enums.PathCompAlpha = driver.configure.uplink.setb.apPower.pcAlpha.get_advanced() \n
		Specifies the value of parameter 'alpha', signaled to the UE if advanced UL power configuration applies. \n
			:return: path_comp_alpha: ZERO | DOT4 | DOT5 | DOT6 | DOT7 | DOT8 | DOT9 | ONE ZERO: 0 DOT4 ... DOT9: 0.4 ... 0.9 ONE: 1.0
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETB:APPower:PCALpha:ADVanced?')
		return Conversions.str_to_scalar_enum(response, enums.PathCompAlpha)

	def set_advanced(self, path_comp_alpha: enums.PathCompAlpha) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:APPower:PCALpha:ADVanced \n
		Snippet: driver.configure.uplink.setb.apPower.pcAlpha.set_advanced(path_comp_alpha = enums.PathCompAlpha.DOT4) \n
		Specifies the value of parameter 'alpha', signaled to the UE if advanced UL power configuration applies. \n
			:param path_comp_alpha: ZERO | DOT4 | DOT5 | DOT6 | DOT7 | DOT8 | DOT9 | ONE ZERO: 0 DOT4 ... DOT9: 0.4 ... 0.9 ONE: 1.0
		"""
		param = Conversions.enum_scalar_to_str(path_comp_alpha, enums.PathCompAlpha)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETB:APPower:PCALpha:ADVanced {param}')
