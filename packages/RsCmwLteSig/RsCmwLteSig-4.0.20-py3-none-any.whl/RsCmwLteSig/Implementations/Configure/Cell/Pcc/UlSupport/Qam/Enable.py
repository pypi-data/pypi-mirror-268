from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, qAMmodulationOrder=repcap.QAMmodulationOrder.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:ULSupport:QAM<ModOrder>:ENABle \n
		Snippet: driver.configure.cell.pcc.ulSupport.qam.enable.set(enable = False, qAMmodulationOrder = repcap.QAMmodulationOrder.Default) \n
		Selects whether 64-QAM and 256-QAM are allowed in the uplink or not. \n
			:param enable: OFF | ON ON: 64-QAM and 256-QAM allowed OFF: 64-QAM and 256-QAM not allowed
			:param qAMmodulationOrder: optional repeated capability selector. Default value: QAM64 (settable in the interface 'Qam')
		"""
		param = Conversions.bool_to_str(enable)
		qAMmodulationOrder_cmd_val = self._cmd_group.get_repcap_cmd_value(qAMmodulationOrder, repcap.QAMmodulationOrder)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:ULSupport:QAM{qAMmodulationOrder_cmd_val}:ENABle {param}')

	def get(self, qAMmodulationOrder=repcap.QAMmodulationOrder.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:ULSupport:QAM<ModOrder>:ENABle \n
		Snippet: value: bool = driver.configure.cell.pcc.ulSupport.qam.enable.get(qAMmodulationOrder = repcap.QAMmodulationOrder.Default) \n
		Selects whether 64-QAM and 256-QAM are allowed in the uplink or not. \n
			:param qAMmodulationOrder: optional repeated capability selector. Default value: QAM64 (settable in the interface 'Qam')
			:return: enable: OFF | ON ON: 64-QAM and 256-QAM allowed OFF: 64-QAM and 256-QAM not allowed"""
		qAMmodulationOrder_cmd_val = self._cmd_group.get_repcap_cmd_value(qAMmodulationOrder, repcap.QAMmodulationOrder)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:ULSupport:QAM{qAMmodulationOrder_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
