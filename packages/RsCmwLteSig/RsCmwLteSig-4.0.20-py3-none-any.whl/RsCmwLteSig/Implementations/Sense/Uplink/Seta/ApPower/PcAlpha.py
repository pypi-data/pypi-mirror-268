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
	def get_basic(self) -> enums.PathCompAlpha:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETA:APPower:PCALpha:BASic \n
		Snippet: value: enums.PathCompAlpha = driver.sense.uplink.seta.apPower.pcAlpha.get_basic() \n
		Queries the value of parameter 'alpha', signaled to the UE if basic UL power configuration applies. \n
			:return: path_comp_alpha: ZERO | DOT4 | DOT5 | DOT6 | DOT7 | DOT8 | DOT9 | ONE ZERO: 0 DOT4 ... DOT9: 0.4 ... 0.9 ONE: 1.0
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETA:APPower:PCALpha:BASic?')
		return Conversions.str_to_scalar_enum(response, enums.PathCompAlpha)
