from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def set(self, enable: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, qAMmodulationOrderB=repcap.QAMmodulationOrderB.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:QAM<ModOrder>:DL \n
		Snippet: driver.configure.connection.scc.qam.downlink.set(enable = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, qAMmodulationOrderB = repcap.QAMmodulationOrderB.Default) \n
		Selects which 3GPP tables are used for CQI scheduling: tables up to 64-QAM, tables up to 256-QAM or tables up to 1024-QAM. \n
			:param enable: OFF | ON ON, QAM256: use tables with 256-QAM OFF, QAM256: use tables without 256-QAM ON, QAM1024: use tables with 1024-QAM OFF, QAM1024: use tables without 1024-QAM
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param qAMmodulationOrderB: optional repeated capability selector. Default value: QAM256 (settable in the interface 'Qam')
		"""
		param = Conversions.bool_to_str(enable)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		qAMmodulationOrderB_cmd_val = self._cmd_group.get_repcap_cmd_value(qAMmodulationOrderB, repcap.QAMmodulationOrderB)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:QAM{qAMmodulationOrderB_cmd_val}:DL {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, qAMmodulationOrderB=repcap.QAMmodulationOrderB.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:QAM<ModOrder>:DL \n
		Snippet: value: bool = driver.configure.connection.scc.qam.downlink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, qAMmodulationOrderB = repcap.QAMmodulationOrderB.Default) \n
		Selects which 3GPP tables are used for CQI scheduling: tables up to 64-QAM, tables up to 256-QAM or tables up to 1024-QAM. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param qAMmodulationOrderB: optional repeated capability selector. Default value: QAM256 (settable in the interface 'Qam')
			:return: enable: OFF | ON ON, QAM256: use tables with 256-QAM OFF, QAM256: use tables without 256-QAM ON, QAM1024: use tables with 1024-QAM OFF, QAM1024: use tables without 1024-QAM"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		qAMmodulationOrderB_cmd_val = self._cmd_group.get_repcap_cmd_value(qAMmodulationOrderB, repcap.QAMmodulationOrderB)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:QAM{qAMmodulationOrderB_cmd_val}:DL?')
		return Conversions.str_to_bool(response)
