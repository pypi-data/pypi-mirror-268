from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NbPositionCls:
	"""NbPosition commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nbPosition", core, parent)

	# noinspection PyTypeChecker
	def get_downlink(self) -> enums.DownlinkNarrowBandPosition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:NBPosition:DL \n
		Snippet: value: enums.DownlinkNarrowBandPosition = driver.configure.connection.pcc.udChannels.emtc.nbPosition.get_downlink() \n
		Selects the narrowband position for a user-defined downlink channel for eMTC. The allowed values have dependencies
		described in the background information, see 'User-defined channels for eMTC'. \n
			:return: position: LOW | MID | HIGH | GPP3
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:NBPosition:DL?')
		return Conversions.str_to_scalar_enum(response, enums.DownlinkNarrowBandPosition)

	def set_downlink(self, position: enums.DownlinkNarrowBandPosition) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:NBPosition:DL \n
		Snippet: driver.configure.connection.pcc.udChannels.emtc.nbPosition.set_downlink(position = enums.DownlinkNarrowBandPosition.GPP3) \n
		Selects the narrowband position for a user-defined downlink channel for eMTC. The allowed values have dependencies
		described in the background information, see 'User-defined channels for eMTC'. \n
			:param position: LOW | MID | HIGH | GPP3
		"""
		param = Conversions.enum_scalar_to_str(position, enums.DownlinkNarrowBandPosition)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:NBPosition:DL {param}')

	# noinspection PyTypeChecker
	def get_uplink(self) -> enums.UplinkNarrowBandPosition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:NBPosition:UL \n
		Snippet: value: enums.UplinkNarrowBandPosition = driver.configure.connection.pcc.udChannels.emtc.nbPosition.get_uplink() \n
		Selects the lowest narrowband for a user-defined uplink channel for eMTC. The allowed values have dependencies described
		in the background information, see 'User-defined channels for eMTC'. \n
			:return: position: LOW | HIGH | NB1 | NB2 | NB3 | NB4 | NB5 | NB6 | NB7 | NB8 | NB9 | NB10 | NB11 | NB12 | NB13 | NB14
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:NBPosition:UL?')
		return Conversions.str_to_scalar_enum(response, enums.UplinkNarrowBandPosition)

	def set_uplink(self, position: enums.UplinkNarrowBandPosition) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:NBPosition:UL \n
		Snippet: driver.configure.connection.pcc.udChannels.emtc.nbPosition.set_uplink(position = enums.UplinkNarrowBandPosition.HIGH) \n
		Selects the lowest narrowband for a user-defined uplink channel for eMTC. The allowed values have dependencies described
		in the background information, see 'User-defined channels for eMTC'. \n
			:param position: LOW | HIGH | NB1 | NB2 | NB3 | NB4 | NB5 | NB6 | NB7 | NB8 | NB9 | NB10 | NB11 | NB12 | NB13 | NB14
		"""
		param = Conversions.enum_scalar_to_str(position, enums.UplinkNarrowBandPosition)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:NBPosition:UL {param}')
