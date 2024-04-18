from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RouteCls:
	"""Route commands group definition. 113 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("route", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 105 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenario'):
			from .Scenario import ScenarioCls
			self._scenario = ScenarioCls(self._core, self._cmd_group)
		return self._scenario

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: NAV | SCEL | TRO | AD | SCF | TROF | ADF | CATR | CAFR | BF | BFSM4 | BH | CATF | CAFF | BFF | BHF | CC | CCMP | CCMS1 | CF | CH | CHSM4 | CJ | CJSM4 | CL | CFF | CHF | CJF | CJFS4 | DD | DH | DJ | DJSM4 | DL | DLSM4 | DN | DNSM4 | DP | DHF | DPF | EE | EJ | EL | ELSM4 | EN | ENSM4 | EP | EPSM4 | ER | ERSM4 | ET | EJF | EPF | EPFS4 | FF | FL | FN | FNSM4 | FP | FPSM4 | FR | FRSM4 | FT | FTSM4 | FV | FVSM4 | FX | FLF | FPF | FPFS4 | GG | GN | GP | GPSM4 | GR | GRSM4 | GT | GTSM4 | GV | GVSM4 | GX | GXSM4 | GYA | GYAS4 | GYC | GNF | GPF | GPFS4 | HH | HP | HR | HRSM4 | HT | HTSM4 | HV | HVSM4 | HX | HXSM4 | HYA | HYAS4 | HYC | HYCS4 | HYE | HYES4 | HYG | HPF Active scenario For mapping of the values to scenario names, see [CMDLINKRESOLVED Route.Scenario#Value CMDLINKRESOLVED].
			- Controller: str: string For future use - returned value not relevant
			- Rx_Connector: enums.RxConnector: RF connector for the PCC input path
			- Rx_Converter: enums.RxConverter: RX module for the PCC input path
			- Tx_Connector_1: enums.TxConnector: RF connector for output path 1
			- Tx_Converter_1: enums.TxConverter: TX module for output path 1
			- Tx_Connector_2: enums.TxConnector: RF connector for output path 2
			- Tx_Converter_2: enums.TxConverter: TX module for output path 2
			- Tx_Connector_3: enums.TxConnector: RF connector for output path 3
			- Tx_Converter_3: enums.TxConverter: TX module for output path 3
			- Tx_Connector_4: enums.TxConnector: RF connector for output path 4
			- Tx_Converter_4: enums.TxConverter: TX module for output path 4
			- Tx_Connector_5: enums.TxConnector: RF connector for output path 5
			- Tx_Converter_5: enums.TxConverter: TX module for output path 5
			- Tx_Connector_6: enums.TxConnector: RF connector for output path 6
			- Tx_Converter_6: enums.TxConverter: TX module for output path 6
			- Tx_Connector_7: enums.TxConnector: RF connector for output path 7
			- Tx_Converter_7: enums.TxConverter: TX module for output path 7
			- Tx_Connector_8: enums.TxConnector: RF connector for output path 8
			- Tx_Converter_8: enums.TxConverter: TX module for output path 8
			- Tx_Connector_9: enums.TxConnector: RF connector for output path 9
			- Tx_Converter_9: enums.TxConverter: TX module for output path 9
			- Tx_Connector_10: enums.TxConnector: RF connector for output path 10
			- Tx_Converter_10: enums.TxConverter: TX module for output path 10
			- Tx_Connector_11: enums.TxConnector: RF connector for output path 11
			- Tx_Converter_11: enums.TxConverter: TX module for output path 11
			- Tx_Connector_12: enums.TxConnector: RF connector for output path 12
			- Tx_Converter_12: enums.TxConverter: TX module for output path 12
			- Tx_Connector_13: enums.TxConnector: RF connector for output path 13
			- Tx_Converter_13: enums.TxConverter: TX module for output path 13
			- Tx_Connector_14: enums.TxConnector: RF connector for output path 14
			- Tx_Converter_14: enums.TxConverter: TX module for output path 14
			- Tx_Connector_15: enums.TxConnector: RF connector for output path 15
			- Tx_Converter_15: enums.TxConverter: TX module for output path 15
			- Tx_Connector_16: enums.TxConnector: RF connector for output path 16
			- Tx_Converter_16: enums.TxConverter: TX module for output path 16
			- Iq_Connector_1: enums.TxConnector: No longer relevant
			- Iq_Connector_2: enums.TxConnector: No longer relevant
			- Iq_Connector_3: enums.TxConnector: No longer relevant
			- Iq_Connector_4: enums.TxConnector: No longer relevant
			- Iq_Connector_5: enums.TxConnector: No longer relevant
			- Iq_Connector_6: enums.TxConnector: No longer relevant
			- Iq_Connector_7: enums.TxConnector: No longer relevant
			- Iq_Connector_8: enums.TxConnector: No longer relevant"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_str('Controller'),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector_1', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_1', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_2', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_2', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_3', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_3', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_4', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_4', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_5', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_5', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_6', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_6', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_7', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_7', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_8', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_8', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_9', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_9', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_10', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_10', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_11', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_11', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_12', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_12', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_13', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_13', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_14', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_14', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_15', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_15', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_16', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_16', enums.TxConverter),
			ArgStruct.scalar_enum('Iq_Connector_1', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_Connector_2', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_Connector_3', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_Connector_4', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_Connector_5', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_Connector_6', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_Connector_7', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_Connector_8', enums.TxConnector)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Controller: str = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector_1: enums.TxConnector = None
			self.Tx_Converter_1: enums.TxConverter = None
			self.Tx_Connector_2: enums.TxConnector = None
			self.Tx_Converter_2: enums.TxConverter = None
			self.Tx_Connector_3: enums.TxConnector = None
			self.Tx_Converter_3: enums.TxConverter = None
			self.Tx_Connector_4: enums.TxConnector = None
			self.Tx_Converter_4: enums.TxConverter = None
			self.Tx_Connector_5: enums.TxConnector = None
			self.Tx_Converter_5: enums.TxConverter = None
			self.Tx_Connector_6: enums.TxConnector = None
			self.Tx_Converter_6: enums.TxConverter = None
			self.Tx_Connector_7: enums.TxConnector = None
			self.Tx_Converter_7: enums.TxConverter = None
			self.Tx_Connector_8: enums.TxConnector = None
			self.Tx_Converter_8: enums.TxConverter = None
			self.Tx_Connector_9: enums.TxConnector = None
			self.Tx_Converter_9: enums.TxConverter = None
			self.Tx_Connector_10: enums.TxConnector = None
			self.Tx_Converter_10: enums.TxConverter = None
			self.Tx_Connector_11: enums.TxConnector = None
			self.Tx_Converter_11: enums.TxConverter = None
			self.Tx_Connector_12: enums.TxConnector = None
			self.Tx_Converter_12: enums.TxConverter = None
			self.Tx_Connector_13: enums.TxConnector = None
			self.Tx_Converter_13: enums.TxConverter = None
			self.Tx_Connector_14: enums.TxConnector = None
			self.Tx_Converter_14: enums.TxConverter = None
			self.Tx_Connector_15: enums.TxConnector = None
			self.Tx_Converter_15: enums.TxConverter = None
			self.Tx_Connector_16: enums.TxConnector = None
			self.Tx_Converter_16: enums.TxConverter = None
			self.Iq_Connector_1: enums.TxConnector = None
			self.Iq_Connector_2: enums.TxConnector = None
			self.Iq_Connector_3: enums.TxConnector = None
			self.Iq_Connector_4: enums.TxConnector = None
			self.Iq_Connector_5: enums.TxConnector = None
			self.Iq_Connector_6: enums.TxConnector = None
			self.Iq_Connector_7: enums.TxConnector = None
			self.Iq_Connector_8: enums.TxConnector = None

	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance> \n
		Snippet: value: ValueStruct = driver.route.get_value() \n
		Returns the configured routing settings. The parameters <Scenario> and <Controller> are always returned. From the other
		parameters, only the subset relevant for the active scenario is returned. For possible connector and converter values,
		see 'Values for signal path selection'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'RouteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RouteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
