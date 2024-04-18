from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UbnpMeasCls:
	"""UbnpMeas commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ubnpMeas", core, parent)

	def get_lmidle(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:UBNPmeas:LMIDle \n
		Snippet: value: bool = driver.sense.ueCapability.ubnpMeas.get_lmidle() \n
		Returns whether the UE supports logged measurements in idle mode or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:UBNPmeas:LMIDle?')
		return Conversions.str_to_bool(response)

	def get_sg_location(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:UBNPmeas:SGLocation \n
		Snippet: value: bool = driver.sense.ueCapability.ubnpMeas.get_sg_location() \n
		Returns whether the UE is equipped with a GNSS receiver or not. \n
			:return: supported: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:UBNPmeas:SGLocation?')
		return Conversions.str_to_bool(response)
