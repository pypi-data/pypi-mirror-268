from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def get_a(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:CEParameters:MODE:A \n
		Snippet: value: bool = driver.sense.ueCapability.ceParameters.mode.get_a() \n
		Returns whether the UE supports operation in CE mode A. \n
			:return: parameter: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:CEParameters:MODE:A?')
		return Conversions.str_to_bool(response)

	def get_b(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:CEParameters:MODE:B \n
		Snippet: value: bool = driver.sense.ueCapability.ceParameters.mode.get_b() \n
		Returns whether the UE supports operation in CE mode B. \n
			:return: parameter: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:CEParameters:MODE:B?')
		return Conversions.str_to_bool(response)
