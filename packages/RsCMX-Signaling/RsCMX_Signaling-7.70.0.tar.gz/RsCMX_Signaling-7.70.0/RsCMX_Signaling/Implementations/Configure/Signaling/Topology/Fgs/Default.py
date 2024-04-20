from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DefaultCls:
	"""Default commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("default", core, parent)

	# noinspection PyTypeChecker
	def get_voice(self) -> enums.VoiceHandling:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:DEFault:VOICe \n
		Snippet: value: enums.VoiceHandling = driver.configure.signaling.topology.fgs.default.get_voice() \n
		Defines the handling of voice calls for UE registered in a 5GS tracking area. \n
			:return: voice_handling: UECap: The fallback decision is based on UE capabilities. VONR: Always voice over NR. EFRedirect: Always EPS fallback with redirection. EFHandover: Always EPS fallback with handover.
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TOPology:FGS:DEFault:VOICe?')
		return Conversions.str_to_scalar_enum(response, enums.VoiceHandling)

	def set_voice(self, voice_handling: enums.VoiceHandling) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:DEFault:VOICe \n
		Snippet: driver.configure.signaling.topology.fgs.default.set_voice(voice_handling = enums.VoiceHandling.EFHandover) \n
		Defines the handling of voice calls for UE registered in a 5GS tracking area. \n
			:param voice_handling: UECap: The fallback decision is based on UE capabilities. VONR: Always voice over NR. EFRedirect: Always EPS fallback with redirection. EFHandover: Always EPS fallback with handover.
		"""
		param = Conversions.enum_scalar_to_str(voice_handling, enums.VoiceHandling)
		self._core.io.write(f'CONFigure:SIGNaling:TOPology:FGS:DEFault:VOICe {param}')
