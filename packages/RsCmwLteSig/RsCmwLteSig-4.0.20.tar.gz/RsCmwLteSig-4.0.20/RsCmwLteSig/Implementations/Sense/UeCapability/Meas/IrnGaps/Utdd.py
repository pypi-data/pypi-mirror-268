from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UtddCls:
	"""Utdd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utdd", core, parent)

	def get(self, index: enums.OperatingBandD = None) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:MEAS:IRNGaps:UTDD<n> \n
		Snippet: value: List[bool] = driver.sense.ueCapability.meas.irnGaps.utdd.get(index = enums.OperatingBandD.OB1) \n
		Returns a list of values indicating the need for downlink measurement gaps when operating on a specific E-UTRA band and
		measuring on a specific UTRA TDD band. The full list contains 32 times 256 values. Each block of 32 values corresponds to
		the UTRA TDD bands. The 256 repetitions correspond to the E-UTRA bands: {measured band: 1, 2, ...
		, 32}used band: user-defined, {measured band: 1, 2, ..., 32}used band: 1, ..., {measured band: 1, 2, ..., 32}used band:
		255 Via the optional parameter <Index>, you can alternatively query the list for a single UTRA TDD band: {used band:
		user-defined, 1, 2, ..., 255}measured band <Index> \n
			:param index: OB1 | OB2 | ... | OB32 Selects the measured UTRA TDD band, for which the list is returned.
			:return: value: OFF | ON Without Index: 32 x 256 = 8192 values With Index: 256 values"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Enum, enums.OperatingBandD, is_optional=True))
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:MEAS:IRNGaps:UTDD128? {param}'.rstrip())
		return Conversions.str_to_bool_list(response)
