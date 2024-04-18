from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DcSupportCls:
	"""DcSupport commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcSupport", core, parent)

	def get_asynchronous(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:DCSupport:ASYNchronous \n
		Snippet: value: int = driver.sense.ueCapability.rf.dcSupport.get_asynchronous() \n
		Returns whether the UE supports asynchronous DC and power control mode 2. \n
			:return: support: 0 | 1 Comma-separated list of values, one value per band combination (combination 0 to n)
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:DCSupport:ASYNchronous?')
		return Conversions.str_to_int(response)

	def get_scgrouping(self) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:DCSupport:SCGRouping \n
		Snippet: value: int = driver.sense.ueCapability.rf.dcSupport.get_scgrouping() \n
		Returns the value received as 'supportedCellGrouping'. It indicates for which mapping of serving cells to the first and
		second cell groups the UE supports asynchronous DC. \n
			:return: support: decimal Comma-separated list of values, one value per band combination (combination 0 to n)
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:RF:DCSupport:SCGRouping?')
		return Conversions.str_to_int(response)
