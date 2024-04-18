from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPyCls:
	"""InputPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	def set(self, ext_rf_in_att: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:EATTenuation:INPut \n
		Snippet: driver.configure.rfSettings.scc.eattenuation.inputPy.set(ext_rf_in_att = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:param ext_rf_in_att: numeric Range: -50 dB to 90 dB, Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(ext_rf_in_att)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:EATTenuation:INPut {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:EATTenuation:INPut \n
		Snippet: value: float = driver.configure.rfSettings.scc.eattenuation.inputPy.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: ext_rf_in_att: numeric Range: -50 dB to 90 dB, Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:EATTenuation:INPut?')
		return Conversions.str_to_float(response)
