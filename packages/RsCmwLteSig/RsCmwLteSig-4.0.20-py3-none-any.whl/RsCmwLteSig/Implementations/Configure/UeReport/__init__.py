from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeReportCls:
	"""UeReport commands group definition. 16 total commands, 2 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueReport", core, parent)

	@property
	def fcoefficient(self):
		"""fcoefficient commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fcoefficient'):
			from .Fcoefficient import FcoefficientCls
			self._fcoefficient = FcoefficientCls(self._core, self._cmd_group)
		return self._fcoefficient

	@property
	def scc(self):
		"""scc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Scc import SccCls
			self._scc = SccCls(self._core, self._cmd_group)
		return self._scc

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:ENABle \n
		Snippet: value: bool = driver.configure.ueReport.get_enable() \n
		Enables or disables UE measurement reports. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:ENABle \n
		Snippet: driver.configure.ueReport.set_enable(enable = False) \n
		Enables or disables UE measurement reports. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:ENABle {param}')

	# noinspection PyTypeChecker
	def get_wm_quantity(self) -> enums.WmQuantity:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:WMQuantity \n
		Snippet: value: enums.WmQuantity = driver.configure.ueReport.get_wm_quantity() \n
		Selects whether the UE must determine the RSCP or the Ec/No during WCDMA neighbor cell measurements. \n
			:return: quantity: RSCP | ECNO
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:WMQuantity?')
		return Conversions.str_to_scalar_enum(response, enums.WmQuantity)

	def set_wm_quantity(self, quantity: enums.WmQuantity) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:WMQuantity \n
		Snippet: driver.configure.ueReport.set_wm_quantity(quantity = enums.WmQuantity.ECNO) \n
		Selects whether the UE must determine the RSCP or the Ec/No during WCDMA neighbor cell measurements. \n
			:param quantity: RSCP | ECNO
		"""
		param = Conversions.enum_scalar_to_str(quantity, enums.WmQuantity)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:WMQuantity {param}')

	def get_mg_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:MGENable \n
		Snippet: value: bool = driver.configure.ueReport.get_mg_enable() \n
		Enables or disables transmission gaps for neighbor cell measurements. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:MGENable?')
		return Conversions.str_to_bool(response)

	def set_mg_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:MGENable \n
		Snippet: driver.configure.ueReport.set_mg_enable(enable = False) \n
		Enables or disables transmission gaps for neighbor cell measurements. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:MGENable {param}')

	# noinspection PyTypeChecker
	def get_mg_period(self) -> enums.TransGap:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:MGPeriod \n
		Snippet: value: enums.TransGap = driver.configure.ueReport.get_mg_period() \n
		Specifies the periodicity of transmission gaps for neighbor cell measurements. \n
			:return: gap: G040 | G080 G040: one gap per 40 ms G080: one gap per 80 ms
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:MGPeriod?')
		return Conversions.str_to_scalar_enum(response, enums.TransGap)

	def set_mg_period(self, gap: enums.TransGap) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:MGPeriod \n
		Snippet: driver.configure.ueReport.set_mg_period(gap = enums.TransGap.G040) \n
		Specifies the periodicity of transmission gaps for neighbor cell measurements. \n
			:param gap: G040 | G080 G040: one gap per 40 ms G080: one gap per 80 ms
		"""
		param = Conversions.enum_scalar_to_str(gap, enums.TransGap)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:MGPeriod {param}')

	# noinspection PyTypeChecker
	def get_rinterval(self) -> enums.ReportInterval:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:RINTerval \n
		Snippet: value: enums.ReportInterval = driver.configure.ueReport.get_rinterval() \n
		Sets the interval between two consecutive measurement reports. \n
			:return: interval: I120 | I240 | I480 | I640 | I1024 | I2048 | I5120 | I10240 Interval in ms, e.g. I240 = 240 ms
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:RINTerval?')
		return Conversions.str_to_scalar_enum(response, enums.ReportInterval)

	def set_rinterval(self, interval: enums.ReportInterval) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:RINTerval \n
		Snippet: driver.configure.ueReport.set_rinterval(interval = enums.ReportInterval.I1024) \n
		Sets the interval between two consecutive measurement reports. \n
			:param interval: I120 | I240 | I480 | I640 | I1024 | I2048 | I5120 | I10240 Interval in ms, e.g. I240 = 240 ms
		"""
		param = Conversions.enum_scalar_to_str(interval, enums.ReportInterval)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:RINTerval {param}')

	# noinspection PyTypeChecker
	def get_mcs_cell(self) -> enums.MeasCellCycle:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:MCSCell \n
		Snippet: value: enums.MeasCellCycle = driver.configure.ueReport.get_mcs_cell() \n
		Specifies the signaling parameter 'measCycleSCell'. \n
			:return: cycle: OFF | SF160 | SF256 | SF320 | SF512 | SF640 | SF1024 | SF1280 OFF: Do not signal 'measCycleSCell' SFn: n subframes
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:MCSCell?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCellCycle)

	def set_mcs_cell(self, cycle: enums.MeasCellCycle) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:MCSCell \n
		Snippet: driver.configure.ueReport.set_mcs_cell(cycle = enums.MeasCellCycle.OFF) \n
		Specifies the signaling parameter 'measCycleSCell'. \n
			:param cycle: OFF | SF160 | SF256 | SF320 | SF512 | SF640 | SF1024 | SF1280 OFF: Do not signal 'measCycleSCell' SFn: n subframes
		"""
		param = Conversions.enum_scalar_to_str(cycle, enums.MeasCellCycle)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:MCSCell {param}')

	def get_ainterrupt(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:AINTerrupt \n
		Snippet: value: bool = driver.configure.ueReport.get_ainterrupt() \n
		Specifies the signaling parameter 'allowInterruptions'. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UEReport:AINTerrupt?')
		return Conversions.str_to_bool(response)

	def set_ainterrupt(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:AINTerrupt \n
		Snippet: driver.configure.ueReport.set_ainterrupt(enable = False) \n
		Specifies the signaling parameter 'allowInterruptions'. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:AINTerrupt {param}')

	def clone(self) -> 'UeReportCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeReportCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
