from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImodeCls:
	"""Imode commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("imode", core, parent)

	# noinspection PyTypeChecker
	def get_clength(self) -> enums.IdleDrxLength:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:IMODe:CLENgth \n
		Snippet: value: enums.IdleDrxLength = driver.configure.connection.cdrx.imode.get_clength() \n
		Configures the duration of one eDRX cycle in idle mode. \n
			:return: length: L512 | L1024 | L2048 | L4096 | L6144 | L8192 | L10240 | L12288 | L14336 | L16384 | L32768 | L65536 | L131072 | L262144 Ln means n radio frames
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:IMODe:CLENgth?')
		return Conversions.str_to_scalar_enum(response, enums.IdleDrxLength)

	def set_clength(self, length: enums.IdleDrxLength) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:IMODe:CLENgth \n
		Snippet: driver.configure.connection.cdrx.imode.set_clength(length = enums.IdleDrxLength.L1024) \n
		Configures the duration of one eDRX cycle in idle mode. \n
			:param length: L512 | L1024 | L2048 | L4096 | L6144 | L8192 | L10240 | L12288 | L14336 | L16384 | L32768 | L65536 | L131072 | L262144 Ln means n radio frames
		"""
		param = Conversions.enum_scalar_to_str(length, enums.IdleDrxLength)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:IMODe:CLENgth {param}')

	# noinspection PyTypeChecker
	def get_pt_window(self) -> enums.Window:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:IMODe:PTWindow \n
		Snippet: value: enums.Window = driver.configure.connection.cdrx.imode.get_pt_window() \n
		Configures the duration of one paging time window in idle mode. \n
			:return: window: W1280 | W2560 | W3840 | W5120 | W6400 | W7680 | W8960 | W10240 | W11520 | W12800 | W14080 | W15360 | W16640 | W17920 | W19200 | W20480 Wn means n subframes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:IMODe:PTWindow?')
		return Conversions.str_to_scalar_enum(response, enums.Window)

	def set_pt_window(self, window: enums.Window) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:IMODe:PTWindow \n
		Snippet: driver.configure.connection.cdrx.imode.set_pt_window(window = enums.Window.W10240) \n
		Configures the duration of one paging time window in idle mode. \n
			:param window: W1280 | W2560 | W3840 | W5120 | W6400 | W7680 | W8960 | W10240 | W11520 | W12800 | W14080 | W15360 | W16640 | W17920 | W19200 | W20480 Wn means n subframes
		"""
		param = Conversions.enum_scalar_to_str(window, enums.Window)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:IMODe:PTWindow {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:IMODe:ENABle \n
		Snippet: value: bool = driver.configure.connection.cdrx.imode.get_enable() \n
		Enables or disables eDRX. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:IMODe:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:IMODe:ENABle \n
		Snippet: driver.configure.connection.cdrx.imode.set_enable(enable = False) \n
		Enables or disables eDRX. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:IMODe:ENABle {param}')
