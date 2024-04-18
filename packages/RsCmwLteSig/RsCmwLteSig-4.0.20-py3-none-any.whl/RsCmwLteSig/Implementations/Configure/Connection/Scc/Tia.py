from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TiaCls:
	"""Tia commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: TbsIndexAlt, default value after init: TbsIndexAlt.Nr2"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tia", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_tbsIndexAlt_get', 'repcap_tbsIndexAlt_set', repcap.TbsIndexAlt.Nr2)

	def repcap_tbsIndexAlt_set(self, tbsIndexAlt: repcap.TbsIndexAlt) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TbsIndexAlt.Default
		Default value after init: TbsIndexAlt.Nr2"""
		self._cmd_group.set_repcap_enum_value(tbsIndexAlt)

	def repcap_tbsIndexAlt_get(self) -> repcap.TbsIndexAlt:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, enable: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, tbsIndexAlt=repcap.TbsIndexAlt.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:TIA<Nr> \n
		Snippet: driver.configure.connection.scc.tia.set(enable = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, tbsIndexAlt = repcap.TbsIndexAlt.Default) \n
		Enables or disables sending the 'tbsIndexAlt<no>...' parameter to the UE. \n
			:param enable: OFF | ON
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param tbsIndexAlt: optional repeated capability selector. Default value: Nr2 (settable in the interface 'Tia')
		"""
		param = Conversions.bool_to_str(enable)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		tbsIndexAlt_cmd_val = self._cmd_group.get_repcap_cmd_value(tbsIndexAlt, repcap.TbsIndexAlt)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TIA{tbsIndexAlt_cmd_val} {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, tbsIndexAlt=repcap.TbsIndexAlt.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:TIA<Nr> \n
		Snippet: value: bool = driver.configure.connection.scc.tia.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, tbsIndexAlt = repcap.TbsIndexAlt.Default) \n
		Enables or disables sending the 'tbsIndexAlt<no>...' parameter to the UE. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param tbsIndexAlt: optional repeated capability selector. Default value: Nr2 (settable in the interface 'Tia')
			:return: enable: OFF | ON"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		tbsIndexAlt_cmd_val = self._cmd_group.get_repcap_cmd_value(tbsIndexAlt, repcap.TbsIndexAlt)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TIA{tbsIndexAlt_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'TiaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TiaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
