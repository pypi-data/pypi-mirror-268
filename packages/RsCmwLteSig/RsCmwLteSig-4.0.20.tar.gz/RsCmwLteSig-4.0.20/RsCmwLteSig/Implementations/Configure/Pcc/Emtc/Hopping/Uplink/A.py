from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ACls:
	"""A commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)

	# noinspection PyTypeChecker
	def get_interval(self) -> enums.IntervalA:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:HOPPing:UL:A:INTerval \n
		Snippet: value: enums.IntervalA = driver.configure.pcc.emtc.hopping.uplink.a.get_interval() \n
		Specifies the time interval between two hops for CE mode A, DL or UL. \n
			:return: interval: I1 | I2 | I4 | I8 Time interval in subframes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:HOPPing:UL:A:INTerval?')
		return Conversions.str_to_scalar_enum(response, enums.IntervalA)

	def set_interval(self, interval: enums.IntervalA) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:HOPPing:UL:A:INTerval \n
		Snippet: driver.configure.pcc.emtc.hopping.uplink.a.set_interval(interval = enums.IntervalA.I1) \n
		Specifies the time interval between two hops for CE mode A, DL or UL. \n
			:param interval: I1 | I2 | I4 | I8 Time interval in subframes
		"""
		param = Conversions.enum_scalar_to_str(interval, enums.IntervalA)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:HOPPing:UL:A:INTerval {param}')
