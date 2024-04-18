from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsirsCls:
	"""Csirs commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csirs", core, parent)

	# noinspection PyTypeChecker
	def get_aports(self) -> enums.AntennaPorts:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CSIRs:APORts \n
		Snippet: value: enums.AntennaPorts = driver.configure.connection.pcc.tm.csirs.get_aports() \n
		Selects the antenna ports used for the CSI-RS for TM 9. \n
			:return: ports: NONE | P15 | P1516 | P1518 | P1522 NONE: no CSI-RS P15: port 15 P1516: port 15 and 16 P1518: port 15 to 18 P1522: port 15 to 22
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CSIRs:APORts?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaPorts)

	def set_aports(self, ports: enums.AntennaPorts) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CSIRs:APORts \n
		Snippet: driver.configure.connection.pcc.tm.csirs.set_aports(ports = enums.AntennaPorts.NONE) \n
		Selects the antenna ports used for the CSI-RS for TM 9. \n
			:param ports: NONE | P15 | P1516 | P1518 | P1522 NONE: no CSI-RS P15: port 15 P1516: port 15 and 16 P1518: port 15 to 18 P1522: port 15 to 22
		"""
		param = Conversions.enum_scalar_to_str(ports, enums.AntennaPorts)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CSIRs:APORts {param}')

	def get_subframe(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CSIRs:SUBFrame \n
		Snippet: value: int = driver.configure.connection.pcc.tm.csirs.get_subframe() \n
		Selects the CSI-RS subframe configuration. \n
			:return: config: numeric Range: 0 to 154
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CSIRs:SUBFrame?')
		return Conversions.str_to_int(response)

	def set_subframe(self, config: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CSIRs:SUBFrame \n
		Snippet: driver.configure.connection.pcc.tm.csirs.set_subframe(config = 1) \n
		Selects the CSI-RS subframe configuration. \n
			:param config: numeric Range: 0 to 154
		"""
		param = Conversions.decimal_value_to_str(config)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CSIRs:SUBFrame {param}')

	def get_resource(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CSIRs:RESource \n
		Snippet: value: int = driver.configure.connection.pcc.tm.csirs.get_resource() \n
		Selects the CSI reference signal configuration. \n
			:return: resource: numeric Range: 0 to 31
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CSIRs:RESource?')
		return Conversions.str_to_int(response)

	def set_resource(self, resource: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CSIRs:RESource \n
		Snippet: driver.configure.connection.pcc.tm.csirs.set_resource(resource = 1) \n
		Selects the CSI reference signal configuration. \n
			:param resource: numeric Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(resource)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CSIRs:RESource {param}')

	def get_power(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CSIRs:POWer \n
		Snippet: value: int = driver.configure.connection.pcc.tm.csirs.get_power() \n
		Sets the value Pc to be signaled to the UE. Pc is the assumed ratio of the RS EPRE to the CSI-RS EPRE. \n
			:return: power: integer Range: -8 dB to 15 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CSIRs:POWer?')
		return Conversions.str_to_int(response)

	def set_power(self, power: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CSIRs:POWer \n
		Snippet: driver.configure.connection.pcc.tm.csirs.set_power(power = 1) \n
		Sets the value Pc to be signaled to the UE. Pc is the assumed ratio of the RS EPRE to the CSI-RS EPRE. \n
			:param power: integer Range: -8 dB to 15 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CSIRs:POWer {param}')
