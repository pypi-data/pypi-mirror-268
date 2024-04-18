from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FgIndicatorsCls:
	"""FgIndicators commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fgIndicators", core, parent)

	def get_rnadd(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:FGINdicators:RNADd \n
		Snippet: value: str = driver.sense.ueCapability.fgIndicators.get_rnadd() \n
		Returns the 'featureGroupIndRel9Add-r9' contained in the UE capability information. The 32-bit value contains one bit per
		feature group (1 = supported, 0 = not supported) . \n
			:return: feature_group_ind: binary Range: #B0 to #B11111111111111111111111111111111
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:FGINdicators:RNADd?')
		return trim_str_response(response)

	def get_rten(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:FGINdicators:RTEN \n
		Snippet: value: str = driver.sense.ueCapability.fgIndicators.get_rten() \n
		Returns the 'featureGroupIndRel10-r10' contained in the UE capability information. The 32-bit value contains one bit per
		feature group (1 = supported, 0 = not supported) . \n
			:return: feature_group_ind: binary Range: #B0 to #B11111111111111111111111111111111
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:FGINdicators:RTEN?')
		return trim_str_response(response)

	def get_value(self) -> str:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:FGINdicators \n
		Snippet: value: str = driver.sense.ueCapability.fgIndicators.get_value() \n
		Returns the 'featureGroupIndicators' contained in the UE capability information. The 32-bit value contains one bit per
		feature group (1 = supported, 0 = not supported) . \n
			:return: feature_group_ind: binary Range: #B0 to #B11111111111111111111111111111111
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:FGINdicators?')
		return trim_str_response(response)
