from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UfddCls:
	"""Ufdd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ufdd", core, parent)

	def get(self, index: enums.OperatingBandD = None) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:IRNGaps:V<number>:UFDD \n
		Snippet: value: List[bool] = driver.sense.ueCapability.meas.irnGaps.v.ufdd.get(index = enums.OperatingBandD.OB1) \n
		Returns a list of values indicating the need for downlink measurement gaps when operating on a specific E-UTRA band
		combination and measuring on a specific UTRA FDD band. The full list contains 32 times n+1 values. Each block of 32
		values corresponds to the UTRA FDD bands. Each repetition corresponds to a supported band combination: {measured band: 1,
		2, ..., 32}used band combination 0, {measured band: 1, 2, ..., 32}used band combination 1, ..., {measured band: 1, 2, ...,
		32}used band combination n Via the optional parameter <Index>, you can alternatively query the list for a single UTRA FDD
		band: {used combination: 0, 1, ..., n}measured band <Index> \n
			:param index: OB1 | OB2 | ... | OB32 Selects the measured UTRA FDD band, for which the list is returned.
			:return: value: OFF | ON Without Index: 32 x (n+1) values With Index: n+1 values"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Enum, enums.OperatingBandD, is_optional=True))
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:IRNGaps:V1020:UFDD? {param}'.rstrip())
		return Conversions.str_to_bool_list(response)
