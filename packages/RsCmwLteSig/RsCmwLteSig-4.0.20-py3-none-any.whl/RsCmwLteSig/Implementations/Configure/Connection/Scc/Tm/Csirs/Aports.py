from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AportsCls:
	"""Aports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aports", core, parent)

	def set(self, ports: enums.AntennaPorts, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CSIRs:APORts \n
		Snippet: driver.configure.connection.scc.tm.csirs.aports.set(ports = enums.AntennaPorts.NONE, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the antenna ports used for the CSI-RS for TM 9. \n
			:param ports: NONE | P15 | P1516 | P1518 | P1522 NONE: no CSI-RS P15: port 15 P1516: port 15 and 16 P1518: port 15 to 18 P1522: port 15 to 22
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(ports, enums.AntennaPorts)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CSIRs:APORts {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.AntennaPorts:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CSIRs:APORts \n
		Snippet: value: enums.AntennaPorts = driver.configure.connection.scc.tm.csirs.aports.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the antenna ports used for the CSI-RS for TM 9. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: ports: NONE | P15 | P1516 | P1518 | P1522 NONE: no CSI-RS P15: port 15 P1516: port 15 and 16 P1518: port 15 to 18 P1522: port 15 to 22"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CSIRs:APORts?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaPorts)
