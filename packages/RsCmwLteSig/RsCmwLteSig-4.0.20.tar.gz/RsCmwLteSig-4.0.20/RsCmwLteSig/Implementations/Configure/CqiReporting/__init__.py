from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CqiReportingCls:
	"""CqiReporting commands group definition. 9 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqiReporting", core, parent)

	@property
	def scc(self):
		"""scc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scc'):
			from .Scc import SccCls
			self._scc = SccCls(self._core, self._cmd_group)
		return self._scc

	@property
	def priReporting(self):
		"""priReporting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_priReporting'):
			from .PriReporting import PriReportingCls
			self._priReporting = PriReportingCls(self._core, self._cmd_group)
		return self._priReporting

	@property
	def pcc(self):
		"""pcc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcc'):
			from .Pcc import PccCls
			self._pcc = PccCls(self._core, self._cmd_group)
		return self._pcc

	# noinspection PyTypeChecker
	def get_enable(self) -> enums.EnableCqiReport:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:ENABle \n
		Snippet: value: enums.EnableCqiReport = driver.configure.cqiReporting.get_enable() \n
		Enables/disables periodic CQI reporting. \n
			:return: enable: OFF | PERiodic OFF: no CQI reporting PERiodic: periodic CQI reporting
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CQIReporting:ENABle?')
		return Conversions.str_to_scalar_enum(response, enums.EnableCqiReport)

	def set_enable(self, enable: enums.EnableCqiReport) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:ENABle \n
		Snippet: driver.configure.cqiReporting.set_enable(enable = enums.EnableCqiReport.OFF) \n
		Enables/disables periodic CQI reporting. \n
			:param enable: OFF | PERiodic OFF: no CQI reporting PERiodic: periodic CQI reporting
		"""
		param = Conversions.enum_scalar_to_str(enable, enums.EnableCqiReport)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CQIReporting:ENABle {param}')

	# noinspection PyTypeChecker
	def get_csir_mode(self) -> enums.CsiReportingMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:CSIRmode \n
		Snippet: value: enums.CsiReportingMode = driver.configure.cqiReporting.get_csir_mode() \n
		Configures the CSI reporting mode. \n
			:return: mode: S1 | S2 S1: submode 1 S2: submode 2
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CQIReporting:CSIRmode?')
		return Conversions.str_to_scalar_enum(response, enums.CsiReportingMode)

	def set_csir_mode(self, mode: enums.CsiReportingMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:CSIRmode \n
		Snippet: driver.configure.cqiReporting.set_csir_mode(mode = enums.CsiReportingMode.S1) \n
		Configures the CSI reporting mode. \n
			:param mode: S1 | S2 S1: submode 1 S2: submode 2
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CsiReportingMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CQIReporting:CSIRmode {param}')

	def get_sancqi(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:SANCqi \n
		Snippet: value: bool = driver.configure.cqiReporting.get_sancqi() \n
		Configures whether the simultaneous transmission of ACK/NACK and CQI is allowed. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CQIReporting:SANCqi?')
		return Conversions.str_to_bool(response)

	def set_sancqi(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:SANCqi \n
		Snippet: driver.configure.cqiReporting.set_sancqi(enable = False) \n
		Configures whether the simultaneous transmission of ACK/NACK and CQI is allowed. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CQIReporting:SANCqi {param}')

	def clone(self) -> 'CqiReportingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CqiReportingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
