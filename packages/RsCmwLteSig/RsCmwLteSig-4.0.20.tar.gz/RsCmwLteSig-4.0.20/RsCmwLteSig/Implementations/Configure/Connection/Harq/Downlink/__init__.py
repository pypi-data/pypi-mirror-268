from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 5 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def udSequence(self):
		"""udSequence commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_udSequence'):
			from .UdSequence import UdSequenceCls
			self._udSequence = UdSequenceCls(self._core, self._cmd_group)
		return self._udSequence

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:ENABle \n
		Snippet: value: bool = driver.configure.connection.harq.downlink.get_enable() \n
		Enables or disables HARQ for downlink transmissions. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:ENABle \n
		Snippet: driver.configure.connection.harq.downlink.set_enable(enable = False) \n
		Enables or disables HARQ for downlink transmissions. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:ENABle {param}')

	def get_nht(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:NHT \n
		Snippet: value: int = driver.configure.connection.harq.downlink.get_nht() \n
		Specifies the maximum number of downlink transmissions, including initial transmissions and retransmissions. \n
			:return: number: numeric Range: 2 to 4
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:NHT?')
		return Conversions.str_to_int(response)

	def set_nht(self, number: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:NHT \n
		Snippet: driver.configure.connection.harq.downlink.set_nht(number = 1) \n
		Specifies the maximum number of downlink transmissions, including initial transmissions and retransmissions. \n
			:param number: numeric Range: 2 to 4
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:NHT {param}')

	# noinspection PyTypeChecker
	def get_rvc_sequence(self) -> enums.RedundancyVerSequence:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:RVCSequence \n
		Snippet: value: enums.RedundancyVerSequence = driver.configure.connection.harq.downlink.get_rvc_sequence() \n
		Selects the redundancy version sequence for DL HARQ. \n
			:return: sequence: TS1 | TS4 | UDEFined TS1: according to 3GPP TS 36.101 TS4: according to 3GPP TS 36.104 UDEFined: user-defined sequence, see method RsCmwLteSig.Configure.Connection.Harq.Downlink.UdSequence.set
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:RVCSequence?')
		return Conversions.str_to_scalar_enum(response, enums.RedundancyVerSequence)

	def set_rvc_sequence(self, sequence: enums.RedundancyVerSequence) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:HARQ:DL:RVCSequence \n
		Snippet: driver.configure.connection.harq.downlink.set_rvc_sequence(sequence = enums.RedundancyVerSequence.TS1) \n
		Selects the redundancy version sequence for DL HARQ. \n
			:param sequence: TS1 | TS4 | UDEFined TS1: according to 3GPP TS 36.101 TS4: according to 3GPP TS 36.104 UDEFined: user-defined sequence, see method RsCmwLteSig.Configure.Connection.Harq.Downlink.UdSequence.set
		"""
		param = Conversions.enum_scalar_to_str(sequence, enums.RedundancyVerSequence)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:HARQ:DL:RVCSequence {param}')

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
