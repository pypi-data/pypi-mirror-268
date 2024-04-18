from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BCls:
	"""B commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	# noinspection PyTypeChecker
	def get_interval(self) -> enums.IntervalB:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:HOPPing:DL:B:INTerval \n
		Snippet: value: enums.IntervalB = driver.configure.pcc.emtc.hopping.downlink.b.get_interval() \n
		Specifies the time interval between two hops for CE mode B, DL or UL. \n
			:return: interval: I2 | I4 | I8 | I16 Time interval in subframes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:HOPPing:DL:B:INTerval?')
		return Conversions.str_to_scalar_enum(response, enums.IntervalB)

	def set_interval(self, interval: enums.IntervalB) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:HOPPing:DL:B:INTerval \n
		Snippet: driver.configure.pcc.emtc.hopping.downlink.b.set_interval(interval = enums.IntervalB.I16) \n
		Specifies the time interval between two hops for CE mode B, DL or UL. \n
			:param interval: I2 | I4 | I8 | I16 Time interval in subframes
		"""
		param = Conversions.enum_scalar_to_str(interval, enums.IntervalB)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:HOPPing:DL:B:INTerval {param}')
