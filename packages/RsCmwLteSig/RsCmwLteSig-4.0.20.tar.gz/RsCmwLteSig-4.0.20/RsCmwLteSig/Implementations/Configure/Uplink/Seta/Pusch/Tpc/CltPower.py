from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CltPowerCls:
	"""CltPower commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cltPower", core, parent)

	def get_offset(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETA:PUSCh:TPC:CLTPower:OFFSet \n
		Snippet: value: float = driver.configure.uplink.seta.pusch.tpc.cltPower.get_offset() \n
		Defines a target power offset relative to the power primary carrier, for power control with the TPC setup CLOop.
		The setting is irrelevant for carriers with independent UL power control. \n
			:return: offset: numeric Target power = primary carrier target power + Offset Range: -7 dB to 7 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETA:PUSCh:TPC:CLTPower:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETA:PUSCh:TPC:CLTPower:OFFSet \n
		Snippet: driver.configure.uplink.seta.pusch.tpc.cltPower.set_offset(offset = 1.0) \n
		Defines a target power offset relative to the power primary carrier, for power control with the TPC setup CLOop.
		The setting is irrelevant for carriers with independent UL power control. \n
			:param offset: numeric Target power = primary carrier target power + Offset Range: -7 dB to 7 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETA:PUSCh:TPC:CLTPower:OFFSet {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETA:PUSCh:TPC:CLTPower \n
		Snippet: value: float = driver.configure.uplink.seta.pusch.tpc.cltPower.get_value() \n
		Defines the target power for power control with the TPC setup CLOop. \n
			:return: power: numeric Range: -50 dBm to 33 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETA:PUSCh:TPC:CLTPower?')
		return Conversions.str_to_float(response)

	def set_value(self, power: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETA:PUSCh:TPC:CLTPower \n
		Snippet: driver.configure.uplink.seta.pusch.tpc.cltPower.set_value(power = 1.0) \n
		Defines the target power for power control with the TPC setup CLOop. \n
			:param power: numeric Range: -50 dBm to 33 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETA:PUSCh:TPC:CLTPower {param}')
