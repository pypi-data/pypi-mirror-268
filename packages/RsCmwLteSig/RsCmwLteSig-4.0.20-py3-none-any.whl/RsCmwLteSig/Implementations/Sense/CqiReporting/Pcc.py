from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	def get_rperiod(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CQIReporting[:PCC]:RPERiod \n
		Snippet: value: int = driver.sense.cqiReporting.pcc.get_rperiod() \n
		Queries the reporting period Np in subframes, resulting from the configured 'cqi-pmi-ConfigIndex'. \n
			:return: period: decimal Range: 1 to 160
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CQIReporting:PCC:RPERiod?')
		return Conversions.str_to_int(response)

	def get_roffset(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CQIReporting[:PCC]:ROFFset \n
		Snippet: value: int = driver.sense.cqiReporting.pcc.get_roffset() \n
		Queries the reporting offset NOFFSET,CQI in subframes, resulting from the configured 'cqi-pmi-ConfigIndex'. \n
			:return: offset: decimal Range: 0 to 159
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CQIReporting:PCC:ROFFset?')
		return Conversions.str_to_int(response)
