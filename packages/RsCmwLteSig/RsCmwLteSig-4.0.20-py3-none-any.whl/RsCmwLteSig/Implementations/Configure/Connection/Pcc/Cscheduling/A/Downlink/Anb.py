from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AnbCls:
	"""Anb commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Anb, default value after init: Anb.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("anb", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_anb_get', 'repcap_anb_set', repcap.Anb.Nr1)

	def repcap_anb_set(self, anb: repcap.Anb) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Anb.Default
		Default value after init: Anb.Nr1"""
		self._cmd_group.set_repcap_enum_value(anb)

	def repcap_anb_get(self) -> repcap.Anb:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, additional_nb: bool, anb=repcap.Anb.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:A:DL:ANB<Number> \n
		Snippet: driver.configure.connection.pcc.cscheduling.a.downlink.anb.set(additional_nb = False, anb = repcap.Anb.Default) \n
		Enables or disables additional narrowbands for compact scheduling downlink, for a maximum eMTC bandwidth of 5 MHz. \n
			:param additional_nb: OFF | ON ON: Use the additional narrowband. OFF: Do not use the additional narrowband.
			:param anb: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Anb')
		"""
		param = Conversions.bool_to_str(additional_nb)
		anb_cmd_val = self._cmd_group.get_repcap_cmd_value(anb, repcap.Anb)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:A:DL:ANB{anb_cmd_val} {param}')

	def get(self, anb=repcap.Anb.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:A:DL:ANB<Number> \n
		Snippet: value: bool = driver.configure.connection.pcc.cscheduling.a.downlink.anb.get(anb = repcap.Anb.Default) \n
		Enables or disables additional narrowbands for compact scheduling downlink, for a maximum eMTC bandwidth of 5 MHz. \n
			:param anb: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Anb')
			:return: additional_nb: OFF | ON ON: Use the additional narrowband. OFF: Do not use the additional narrowband."""
		anb_cmd_val = self._cmd_group.get_repcap_cmd_value(anb, repcap.Anb)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:A:DL:ANB{anb_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'AnbCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AnbCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
