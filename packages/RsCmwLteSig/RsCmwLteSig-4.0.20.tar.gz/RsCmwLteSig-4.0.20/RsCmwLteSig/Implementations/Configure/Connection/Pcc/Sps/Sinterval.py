from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SintervalCls:
	"""Sinterval commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinterval", core, parent)

	# noinspection PyTypeChecker
	def get_downlink(self) -> enums.IntervalC:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:SINTerval[:DL] \n
		Snippet: value: enums.IntervalC = driver.configure.connection.pcc.sps.sinterval.get_downlink() \n
		Configures the DL subframe periodicity n for the scheduling type SPS. The UE is granted the configured RB allocation in
		every nth subframe. For TDD, the selected value is internally rounded down to a multiple of 10. Example: S128 means every
		120th subframe. \n
			:return: interval: S10 | S20 | S32 | S40 | S64 | S80 | S128 | S160 | S320 | S640 Every 10th subframe to every 640th subframe
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:SINTerval:DL?')
		return Conversions.str_to_scalar_enum(response, enums.IntervalC)

	def set_downlink(self, interval: enums.IntervalC) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:SINTerval[:DL] \n
		Snippet: driver.configure.connection.pcc.sps.sinterval.set_downlink(interval = enums.IntervalC.S10) \n
		Configures the DL subframe periodicity n for the scheduling type SPS. The UE is granted the configured RB allocation in
		every nth subframe. For TDD, the selected value is internally rounded down to a multiple of 10. Example: S128 means every
		120th subframe. \n
			:param interval: S10 | S20 | S32 | S40 | S64 | S80 | S128 | S160 | S320 | S640 Every 10th subframe to every 640th subframe
		"""
		param = Conversions.enum_scalar_to_str(interval, enums.IntervalC)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:SINTerval:DL {param}')

	# noinspection PyTypeChecker
	def get_uplink(self) -> enums.SpsInteval:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:SINTerval:UL \n
		Snippet: value: enums.SpsInteval = driver.configure.connection.pcc.sps.sinterval.get_uplink() \n
		Configures the UL subframe periodicity n for the scheduling type SPS. The UE is granted the configured RB allocation in
		every nth subframe. For TDD, the selected value is internally rounded down to a multiple of 10. Example: S128 means every
		120th subframe. \n
			:return: interval: SADL | S1 | S2 | S3 | S4 | S5 | S10 | S20 | S32 | S40 | S64 | S80 | S128 | S160 | S320 | S640 SADL: same as downlink S1, S2 to S640: Every subframe, every 2nd subframe to every 640th subframe
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:SINTerval:UL?')
		return Conversions.str_to_scalar_enum(response, enums.SpsInteval)

	def set_uplink(self, interval: enums.SpsInteval) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:SINTerval:UL \n
		Snippet: driver.configure.connection.pcc.sps.sinterval.set_uplink(interval = enums.SpsInteval.S1) \n
		Configures the UL subframe periodicity n for the scheduling type SPS. The UE is granted the configured RB allocation in
		every nth subframe. For TDD, the selected value is internally rounded down to a multiple of 10. Example: S128 means every
		120th subframe. \n
			:param interval: SADL | S1 | S2 | S3 | S4 | S5 | S10 | S20 | S32 | S40 | S64 | S80 | S128 | S160 | S320 | S640 SADL: same as downlink S1, S2 to S640: Every subframe, every 2nd subframe to every 640th subframe
		"""
		param = Conversions.enum_scalar_to_str(interval, enums.SpsInteval)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:SINTerval:UL {param}')
