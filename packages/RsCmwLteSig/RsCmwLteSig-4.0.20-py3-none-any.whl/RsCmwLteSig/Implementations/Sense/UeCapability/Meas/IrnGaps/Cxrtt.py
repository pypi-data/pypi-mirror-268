from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CxrttCls:
	"""Cxrtt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cxrtt", core, parent)

	def get(self, index: enums.Cdma2kBand = None) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:IRNGaps:CXRTt \n
		Snippet: value: List[bool] = driver.sense.ueCapability.meas.irnGaps.cxrtt.get(index = enums.Cdma2kBand.BC0) \n
		Returns a list of values indicating the need for downlink measurement gaps when operating on a specific E-UTRA band and
		measuring on a specific CDMA2000 1xRTT band class. The full list contains 18 times 256 values. Each block of 18 values
		corresponds to the CDMA2000 band classes. The 256 repetitions correspond to the E-UTRA bands: {measured band: 0, 1, ...
		, 17}used band: user-defined, {measured band: 0, 1, ..., 17}used band: 1, ..., {measured band: 0, 1, ..., 17}used band:
		256 Via the optional parameter <Index>, you can alternatively query the list for a single CDMA2000 band class: {used
		band: user-defined, 1, 2, ..., 255}measured band <Index> \n
			:param index: BC0 | BC1 | ... | BC17 Selects the measured CDMA2000 band class, for which the list is returned.
			:return: value: OFF | ON Without Index: 18 x 256 = 4608 values With Index: 256 values"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Enum, enums.Cdma2kBand, is_optional=True))
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:IRNGaps:CXRTt? {param}'.rstrip())
		return Conversions.str_to_bool_list(response)
