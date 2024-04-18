from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TdBearerCls:
	"""TdBearer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdBearer", core, parent)

	# noinspection PyTypeChecker
	def get_rlc_mode(self) -> enums.RlcMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:TDBearer:RLCMode \n
		Snippet: value: enums.RlcMode = driver.configure.connection.tdBearer.get_rlc_mode() \n
		Selects the RLC mode for downlink transmissions (dedicated bearer in test mode) . \n
			:return: mode: UM | AM UM: unacknowledged mode AM: acknowledged mode
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:TDBearer:RLCMode?')
		return Conversions.str_to_scalar_enum(response, enums.RlcMode)

	def set_rlc_mode(self, mode: enums.RlcMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:TDBearer:RLCMode \n
		Snippet: driver.configure.connection.tdBearer.set_rlc_mode(mode = enums.RlcMode.AM) \n
		Selects the RLC mode for downlink transmissions (dedicated bearer in test mode) . \n
			:param mode: UM | AM UM: unacknowledged mode AM: acknowledged mode
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RlcMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:TDBearer:RLCMode {param}')
