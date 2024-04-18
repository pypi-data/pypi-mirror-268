from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdrxCls:
	"""Cdrx commands group definition. 12 total commands, 1 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdrx", core, parent)

	@property
	def imode(self):
		"""imode commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_imode'):
			from .Imode import ImodeCls
			self._imode = ImodeCls(self._core, self._cmd_group)
		return self._imode

	# noinspection PyTypeChecker
	def get_enable(self) -> enums.EnableDrx:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:ENABle \n
		Snippet: value: enums.EnableDrx = driver.configure.connection.cdrx.get_enable() \n
		Enables or disables DRX and selects a set of DRX settings. \n
			:return: enable: DRXS | DRXL | UDEFined | ON | OFF DRXS: DRX_S, 3GPP TS 36.521-3, table H.3.6-1 DRXL: DRX_L, 3GPP TS 36.521-3, table H.3.6-2 UDEFined: user-defined DRX settings ON: enables DRX with previously selected set OFF: disables DRX
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:ENABle?')
		return Conversions.str_to_scalar_enum(response, enums.EnableDrx)

	def set_enable(self, enable: enums.EnableDrx) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:ENABle \n
		Snippet: driver.configure.connection.cdrx.set_enable(enable = enums.EnableDrx.DRXL) \n
		Enables or disables DRX and selects a set of DRX settings. \n
			:param enable: DRXS | DRXL | UDEFined | ON | OFF DRXS: DRX_S, 3GPP TS 36.521-3, table H.3.6-1 DRXL: DRX_L, 3GPP TS 36.521-3, table H.3.6-2 UDEFined: user-defined DRX settings ON: enables DRX with previously selected set OFF: disables DRX
		"""
		param = Conversions.enum_scalar_to_str(enable, enums.EnableDrx)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:ENABle {param}')

	# noinspection PyTypeChecker
	def get_od_timer(self) -> enums.OnDurationTimer:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:ODTimer \n
		Snippet: value: enums.OnDurationTimer = driver.configure.connection.cdrx.get_od_timer() \n
		Configures the onDurationTimer. The value must be smaller than or equal to the long DRX cycle duration. \n
			:return: timer: PSF1 | PSF2 | PSF3 | PSF4 | PSF5 | PSF6 | PSF8 | PSF10 | PSF20 | PSF30 | PSF40 | PSF50 | PSF60 | PSF80 | PSF100 | PSF200 | PSF300 | PSF400 | PSF500 | PSF600 | PSF800 | PSF1000 | PSF1200 | PSF1600 PSFn means n PDCCH subframes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:ODTimer?')
		return Conversions.str_to_scalar_enum(response, enums.OnDurationTimer)

	def set_od_timer(self, timer: enums.OnDurationTimer) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:ODTimer \n
		Snippet: driver.configure.connection.cdrx.set_od_timer(timer = enums.OnDurationTimer.PSF1) \n
		Configures the onDurationTimer. The value must be smaller than or equal to the long DRX cycle duration. \n
			:param timer: PSF1 | PSF2 | PSF3 | PSF4 | PSF5 | PSF6 | PSF8 | PSF10 | PSF20 | PSF30 | PSF40 | PSF50 | PSF60 | PSF80 | PSF100 | PSF200 | PSF300 | PSF400 | PSF500 | PSF600 | PSF800 | PSF1000 | PSF1200 | PSF1600 PSFn means n PDCCH subframes
		"""
		param = Conversions.enum_scalar_to_str(timer, enums.OnDurationTimer)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:ODTimer {param}')

	# noinspection PyTypeChecker
	def get_itimer(self) -> enums.InactivityTimer:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:ITIMer \n
		Snippet: value: enums.InactivityTimer = driver.configure.connection.cdrx.get_itimer() \n
		Configures the 'drx-InactivityTimer'. \n
			:return: timer: PSF1 | PSF2 | PSF3 | PSF4 | PSF5 | PSF6 | PSF8 | PSF10 | PSF20 | PSF30 | PSF40 | PSF50 | PSF60 | PSF80 | PSF100 | PSF200 | PSF300 | PSF500 | PSF750 | PSF1280 | PSF1920 | PSF2560 PSFn means n PDCCH subframes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:ITIMer?')
		return Conversions.str_to_scalar_enum(response, enums.InactivityTimer)

	def set_itimer(self, timer: enums.InactivityTimer) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:ITIMer \n
		Snippet: driver.configure.connection.cdrx.set_itimer(timer = enums.InactivityTimer.PSF1) \n
		Configures the 'drx-InactivityTimer'. \n
			:param timer: PSF1 | PSF2 | PSF3 | PSF4 | PSF5 | PSF6 | PSF8 | PSF10 | PSF20 | PSF30 | PSF40 | PSF50 | PSF60 | PSF80 | PSF100 | PSF200 | PSF300 | PSF500 | PSF750 | PSF1280 | PSF1920 | PSF2560 PSFn means n PDCCH subframes
		"""
		param = Conversions.enum_scalar_to_str(timer, enums.InactivityTimer)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:ITIMer {param}')

	# noinspection PyTypeChecker
	def get_rtimer(self) -> enums.RetransmissionTimer:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:RTIMer \n
		Snippet: value: enums.RetransmissionTimer = driver.configure.connection.cdrx.get_rtimer() \n
		Configures the 'drx-RetransmissionTimer'. \n
			:return: timer: PSF0 | PSF1 | PSF2 | PSF4 | PSF6 | PSF8 | PSF16 | PSF24 | PSF33 | PSF40 | PSF64 | PSF80 | PSF96 | PSF112 | PSF128 | PSF160 | PSF320 PSFn means n PDCCH subframes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:RTIMer?')
		return Conversions.str_to_scalar_enum(response, enums.RetransmissionTimer)

	def set_rtimer(self, timer: enums.RetransmissionTimer) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:RTIMer \n
		Snippet: driver.configure.connection.cdrx.set_rtimer(timer = enums.RetransmissionTimer.PSF0) \n
		Configures the 'drx-RetransmissionTimer'. \n
			:param timer: PSF0 | PSF1 | PSF2 | PSF4 | PSF6 | PSF8 | PSF16 | PSF24 | PSF33 | PSF40 | PSF64 | PSF80 | PSF96 | PSF112 | PSF128 | PSF160 | PSF320 PSFn means n PDCCH subframes
		"""
		param = Conversions.enum_scalar_to_str(timer, enums.RetransmissionTimer)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:RTIMer {param}')

	# noinspection PyTypeChecker
	def get_ld_cycle(self) -> enums.LdCycle:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:LDCYcle \n
		Snippet: value: enums.LdCycle = driver.configure.connection.cdrx.get_ld_cycle() \n
		Configures the duration of one long DRX cycle. If short DRX cycles are enabled, the long DRX cycle duration must be
		divisible by the short DRX cycle duration. \n
			:return: cycle: SF10 | SF20 | SF32 | SF40 | SF60 | SF64 | SF70 | SF80 | SF128 | SF160 | SF256 | SF320 | SF512 | SF640 | SF1024 | SF1280 | SF2048 | SF2560 | SF5120 | SF10240 SFn means n subframes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:LDCYcle?')
		return Conversions.str_to_scalar_enum(response, enums.LdCycle)

	def set_ld_cycle(self, cycle: enums.LdCycle) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:LDCYcle \n
		Snippet: driver.configure.connection.cdrx.set_ld_cycle(cycle = enums.LdCycle.SF10) \n
		Configures the duration of one long DRX cycle. If short DRX cycles are enabled, the long DRX cycle duration must be
		divisible by the short DRX cycle duration. \n
			:param cycle: SF10 | SF20 | SF32 | SF40 | SF60 | SF64 | SF70 | SF80 | SF128 | SF160 | SF256 | SF320 | SF512 | SF640 | SF1024 | SF1280 | SF2048 | SF2560 | SF5120 | SF10240 SFn means n subframes
		"""
		param = Conversions.enum_scalar_to_str(cycle, enums.LdCycle)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:LDCYcle {param}')

	def get_soffset(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:SOFFset \n
		Snippet: value: int = driver.configure.connection.cdrx.get_soffset() \n
		Configures the 'drxStartOffset', shifting all DRX cycles. \n
			:return: offset: numeric Range: 0 to length of long DRX cycle - 1
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:SOFFset?')
		return Conversions.str_to_int(response)

	def set_soffset(self, offset: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:SOFFset \n
		Snippet: driver.configure.connection.cdrx.set_soffset(offset = 1) \n
		Configures the 'drxStartOffset', shifting all DRX cycles. \n
			:param offset: numeric Range: 0 to length of long DRX cycle - 1
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:SOFFset {param}')

	def get_sc_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:SCENable \n
		Snippet: value: bool = driver.configure.connection.cdrx.get_sc_enable() \n
		Enables or disables short DRX cycles. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:SCENable?')
		return Conversions.str_to_bool(response)

	def set_sc_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:SCENable \n
		Snippet: driver.configure.connection.cdrx.set_sc_enable(enable = False) \n
		Enables or disables short DRX cycles. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:SCENable {param}')

	# noinspection PyTypeChecker
	def get_sd_cycle(self) -> enums.SdCycle:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:SDCYcle \n
		Snippet: value: enums.SdCycle = driver.configure.connection.cdrx.get_sd_cycle() \n
		Configures the duration of one short DRX cycle. The long DRX cycle duration must be divisible by the short DRX cycle
		duration. \n
			:return: cycle: SF2 | SF4 | SF5 | SF8 | SF10 | SF16 | SF20 | SF32 | SF40 | SF64 | SF80 | SF128 | SF160 | SF256 | SF320 | SF512 | SF640 SFn means n subframes If a query returns NAV, short cycles are disabled.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:SDCYcle?')
		return Conversions.str_to_scalar_enum(response, enums.SdCycle)

	def set_sd_cycle(self, cycle: enums.SdCycle) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:SDCYcle \n
		Snippet: driver.configure.connection.cdrx.set_sd_cycle(cycle = enums.SdCycle.SF10) \n
		Configures the duration of one short DRX cycle. The long DRX cycle duration must be divisible by the short DRX cycle
		duration. \n
			:param cycle: SF2 | SF4 | SF5 | SF8 | SF10 | SF16 | SF20 | SF32 | SF40 | SF64 | SF80 | SF128 | SF160 | SF256 | SF320 | SF512 | SF640 SFn means n subframes If a query returns NAV, short cycles are disabled.
		"""
		param = Conversions.enum_scalar_to_str(cycle, enums.SdCycle)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:SDCYcle {param}')

	def get_sc_timer(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:SCTimer \n
		Snippet: value: int = driver.configure.connection.cdrx.get_sc_timer() \n
		Configures the short cycle timer. \n
			:return: timer: numeric Number of short DRX cycles Range: 1 to 16
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:SCTimer?')
		return Conversions.str_to_int(response)

	def set_sc_timer(self, timer: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:CDRX:SCTimer \n
		Snippet: driver.configure.connection.cdrx.set_sc_timer(timer = 1) \n
		Configures the short cycle timer. \n
			:param timer: numeric Number of short DRX cycles Range: 1 to 16
		"""
		param = Conversions.decimal_value_to_str(timer)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:CDRX:SCTimer {param}')

	def clone(self) -> 'CdrxCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CdrxCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
