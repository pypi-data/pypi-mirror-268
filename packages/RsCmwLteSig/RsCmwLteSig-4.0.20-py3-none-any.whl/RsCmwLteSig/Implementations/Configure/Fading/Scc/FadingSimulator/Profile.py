from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProfileCls:
	"""Profile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("profile", core, parent)

	def set(self, profile: enums.FadingProfile, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:PROFile \n
		Snippet: driver.configure.fading.scc.fadingSimulator.profile.set(profile = enums.FadingProfile.CTESt, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a propagation condition profile for fading. \n
			:param profile: EP5Low | EP5Medium | EP5High | EV5Low | EV5Medium | EV5High | EV7Low | EV7Medium | EV7High | ET7Low | ET7Medium | ET7High | ET3Low | ET3Medium | ET3High | HSTRain | HST | CTESt | ETL30 | ETM30 | ETH30 | EVL200 | EVM200 | EVH200 | UMI3 | UMI30 | UMA3 | UMA30 EP5Low | EP5Medium | EP5High EPA, 5-Hz Doppler, low/medium/high correlation ETL30 | ETM30 | ETH30 ETU, 30-Hz Doppler, low/medium/high correlation ET7Low | ET7Medium | ET7High ETU, 70-Hz Doppler, low/medium/high correlation ET3Low | ET3Medium | ET3High ETU, 300-Hz Doppler, low/medium/high correlation EV5Low | EV5Medium | EV5High EVA, 5-Hz Doppler, low/medium/high correlation EV7Low | EV7Medium | EV7High EVA, 70-Hz Doppler, low/medium/high correlation EVL200 | EVM200 | EVH200 EVA, 200-Hz Doppler, low/medium/high correlation HSTRain | HST High-speed train scenario (both values have the same effect) CTESt Multi-path profile for CQI tests UMI3 | UMI30 SCME UMi, 3 km/h or 30 km/h UMA3 | UMA30 SCME UMa, 3 km/h or 30 km/h
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(profile, enums.FadingProfile)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:PROFile {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.FadingProfile:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:PROFile \n
		Snippet: value: enums.FadingProfile = driver.configure.fading.scc.fadingSimulator.profile.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a propagation condition profile for fading. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: profile: EP5Low | EP5Medium | EP5High | EV5Low | EV5Medium | EV5High | EV7Low | EV7Medium | EV7High | ET7Low | ET7Medium | ET7High | ET3Low | ET3Medium | ET3High | HSTRain | HST | CTESt | ETL30 | ETM30 | ETH30 | EVL200 | EVM200 | EVH200 | UMI3 | UMI30 | UMA3 | UMA30 EP5Low | EP5Medium | EP5High EPA, 5-Hz Doppler, low/medium/high correlation ETL30 | ETM30 | ETH30 ETU, 30-Hz Doppler, low/medium/high correlation ET7Low | ET7Medium | ET7High ETU, 70-Hz Doppler, low/medium/high correlation ET3Low | ET3Medium | ET3High ETU, 300-Hz Doppler, low/medium/high correlation EV5Low | EV5Medium | EV5High EVA, 5-Hz Doppler, low/medium/high correlation EV7Low | EV7Medium | EV7High EVA, 70-Hz Doppler, low/medium/high correlation EVL200 | EVM200 | EVH200 EVA, 200-Hz Doppler, low/medium/high correlation HSTRain | HST High-speed train scenario (both values have the same effect) CTESt Multi-path profile for CQI tests UMI3 | UMI30 SCME UMi, 3 km/h or 30 km/h UMA3 | UMA30 SCME UMa, 3 km/h or 30 km/h"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:PROFile?')
		return Conversions.str_to_scalar_enum(response, enums.FadingProfile)
