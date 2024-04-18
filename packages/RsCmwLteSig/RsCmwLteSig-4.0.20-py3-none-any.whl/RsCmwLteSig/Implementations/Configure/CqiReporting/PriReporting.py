from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PriReportingCls:
	"""PriReporting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("priReporting", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:PRIReporting:ENABle \n
		Snippet: value: bool = driver.configure.cqiReporting.priReporting.get_enable() \n
		Enables/disables PMI/RI reporting for transmission mode 8 and 9. As a prerequisite for PMI and RI reporting, CQI
		reporting must also be enabled. \n
			:return: enable: OFF | ON OFF: only CQI reporting ON: CQI, PMI and RI reporting
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CQIReporting:PRIReporting:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting:PRIReporting:ENABle \n
		Snippet: driver.configure.cqiReporting.priReporting.set_enable(enable = False) \n
		Enables/disables PMI/RI reporting for transmission mode 8 and 9. As a prerequisite for PMI and RI reporting, CQI
		reporting must also be enabled. \n
			:param enable: OFF | ON OFF: only CQI reporting ON: CQI, PMI and RI reporting
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CQIReporting:PRIReporting:ENABle {param}')
