from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MbmsCls:
	"""Mbms commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mbms", core, parent)

	def get_nscell(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MBMS:NSCell \n
		Snippet: value: bool = driver.sense.ueCapability.mbms.get_nscell() \n
		Returns whether the UE supports MBMS reception via a serving cell to be added. \n
			:return: cell: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:MBMS:NSCell?')
		return Conversions.str_to_bool(response)

	def get_scell(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MBMS:SCELl \n
		Snippet: value: bool = driver.sense.ueCapability.mbms.get_scell() \n
		Returns whether the UE supports MBMS reception via an SCell. \n
			:return: scell: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:MBMS:SCELl?')
		return Conversions.str_to_bool(response)
