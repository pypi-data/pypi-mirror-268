from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VCls:
	"""V commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("v", core, parent)

	def get(self, index: enums.OperatingBandC = None) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:IFNGaps:V<number> \n
		Snippet: value: List[bool] = driver.sense.ueCapability.meas.interFreqNgaps.v.get(index = enums.OperatingBandC.OB1) \n
		Returns a list of values indicating the need for downlink measurement gaps when operating on a specific E-UTRA band
		combination and measuring on a specific E-UTRA band. The full list contains 256 times n+1 values. Each block of 256
		values corresponds to the measured E-UTRA bands. Each repetition corresponds to a supported band combination. The list is
		ordered as follows: {measured band: user-defined, 1, 2, ..., 255}used band combination 0, {measured band: user-defined, 1,
		2, ..., 255}used band combination 1, ..., {measured band: user-defined, 1, 2, ..., 255}used band combination n Via the
		optional parameter <Index>, you can alternatively query the list for a single measured E-UTRA band: {used combination: 0,
		1, ..., n}measured band <Index> \n
			:param index: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255 Selects the measured E-UTRA band, for which the list is returned.
			:return: value: OFF | ON Without Index: 256 x (n+1) values With Index: n+1 values"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Enum, enums.OperatingBandC, is_optional=True))
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:IFNGaps:V1020? {param}'.rstrip())
		return Conversions.str_to_bool_list(response)
