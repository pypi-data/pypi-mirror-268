from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandCls:
	"""Band commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("band", core, parent)

	def set(self, band: enums.OperatingBandC, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:BAND \n
		Snippet: driver.configure.scc.band.set(band = enums.OperatingBandC.OB1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the operating band (OB) . The allowed input range depends on the duplex mode (FDD or TDD) . \n
			:param band: FDD: UDEFined | OB1 | ... | OB32 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB252 | OB255 (OB29/32/67/69/75/76/252/255 only for SCC DL) TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 (OB46/49 only for SCC DL)
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(band, enums.OperatingBandC)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:BAND {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.OperatingBandC:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:SCC<Carrier>:BAND \n
		Snippet: value: enums.OperatingBandC = driver.configure.scc.band.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the operating band (OB) . The allowed input range depends on the duplex mode (FDD or TDD) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: band: FDD: UDEFined | OB1 | ... | OB32 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB252 | OB255 (OB29/32/67/69/75/76/252/255 only for SCC DL) TDD: UDEFined | OB33 | ... | OB46 | OB48 | ... | OB53 | OB250 (OB46/49 only for SCC DL)"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.OperatingBandC)
