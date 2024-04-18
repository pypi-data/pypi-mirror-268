from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OutputCls:
	"""Output commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Output, default value after init: Output.Out1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_output_get', 'repcap_output_set', repcap.Output.Out1)

	def repcap_output_set(self, output: repcap.Output) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Output.Default
		Default value after init: Output.Out1"""
		self._cmd_group.set_repcap_enum_value(output)

	def repcap_output_get(self) -> repcap.Output:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, ext_rf_out_att: float, output=repcap.Output.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:EATTenuation:OUTPut<n> \n
		Snippet: driver.configure.rfSettings.pcc.eattenuation.output.set(ext_rf_out_att = 1.0, output = repcap.Output.Default) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF output path number <n>.
		Depending on the transmission scheme, several output paths are used for each carrier and the attenuation can be
		configured per output path. \n
			:param ext_rf_out_att: numeric Range: -50 dB to 90 dB, Unit: dB
			:param output: optional repeated capability selector. Default value: Out1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(ext_rf_out_att)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:EATTenuation:OUTPut{output_cmd_val} {param}')

	def get(self, output=repcap.Output.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:EATTenuation:OUTPut<n> \n
		Snippet: value: float = driver.configure.rfSettings.pcc.eattenuation.output.get(output = repcap.Output.Default) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the RF output path number <n>.
		Depending on the transmission scheme, several output paths are used for each carrier and the attenuation can be
		configured per output path. \n
			:param output: optional repeated capability selector. Default value: Out1 (settable in the interface 'Output')
			:return: ext_rf_out_att: numeric Range: -50 dB to 90 dB, Unit: dB"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:EATTenuation:OUTPut{output_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'OutputCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OutputCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
