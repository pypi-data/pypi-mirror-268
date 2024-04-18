from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScprocCls:
	"""Scproc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scproc", core, parent)

	# noinspection PyTypeChecker
	def get(self, eutraBand=repcap.EutraBand.Default) -> enums.UeProcessesCount:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:BCOMbination:V<Number>:EUTRa<BandNr>:SCPRoc \n
		Snippet: value: enums.UeProcessesCount = driver.sense.ueCapability.rf.bcombination.v.eutra.scproc.get(eutraBand = repcap.EutraBand.Default) \n
		Returns the maximum number of CSI processes supported by the UE. The information is returned for a selected band of all
		supported carrier aggregation band combinations. \n
			:param eutraBand: optional repeated capability selector. Default value: Band1 (settable in the interface 'Eutra')
			:return: proc: N1 | N3 | N4 Comma-separated list of values, one value per band combination (combination 0 to n)"""
		eutraBand_cmd_val = self._cmd_group.get_repcap_cmd_value(eutraBand, repcap.EutraBand)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:RF:BCOMbination:V1020:EUTRa{eutraBand_cmd_val}:SCPRoc?')
		return Conversions.str_to_scalar_enum(response, enums.UeProcessesCount)
