from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeranCls:
	"""Geran commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("geran", core, parent)

	def get(self, index: enums.GeranBband = None) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:IRNGaps:GERan \n
		Snippet: value: List[bool] = driver.sense.ueCapability.meas.irnGaps.geran.get(index = enums.GeranBband.G045) \n
		Returns a list of values indicating the need for downlink measurement gaps when operating on a specific E-UTRA band and
		measuring on a specific GERAN band. The full list contains 11 times 256 values. Each block of 11 values corresponds to
		the following GERAN bands: GSM 450, GSM 480, GSM 710, GSM 750, GSM 810, GSM 850, P-GSM 900, E-GSM 900, R-GSM 900, GSM
		1800, GSM 1900. The 256 repetitions correspond to the E-UTRA bands: {measured band: GSM 450, GSM 480, ..., GSM 1900}used
		band: user-defined, {measured band: GSM 450, GSM 480, ..., GSM 1900}used band: 1, ..., {measured band: GSM 450, GSM 480, .
		.., GSM 1900}used band: 256 Via the optional parameter <Index>, you can alternatively query the list for a single GERAN
		band: {used band: user-defined, 1, 2, ..., 255}measured band <Index> \n
			:param index: G045 | G048 | G071 | G075 | G081 | G085 | G09P | G09E | G09R | G18 | G19 Selects the measured GERAN band, for which the list is returned.
			:return: value: OFF | ON Without Index: 11 x 256 = 2816 values With Index: 256 values"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Enum, enums.GeranBband, is_optional=True))
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:IRNGaps:GERan? {param}'.rstrip())
		return Conversions.str_to_bool_list(response)
