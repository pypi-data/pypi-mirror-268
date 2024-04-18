from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_ports(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:POWer:PORTs \n
		Snippet: value: int = driver.configure.downlink.pcc.power.get_ports() \n
		Defines the power offset for the antenna ports 7 to 10. \n
			:return: power: numeric Range: -12 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:POWer:PORTs?')
		return Conversions.str_to_int(response)

	def set_ports(self, power: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:POWer:PORTs \n
		Snippet: driver.configure.downlink.pcc.power.set_ports(power = 1) \n
		Defines the power offset for the antenna ports 7 to 10. \n
			:param power: numeric Range: -12 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:POWer:PORTs {param}')
