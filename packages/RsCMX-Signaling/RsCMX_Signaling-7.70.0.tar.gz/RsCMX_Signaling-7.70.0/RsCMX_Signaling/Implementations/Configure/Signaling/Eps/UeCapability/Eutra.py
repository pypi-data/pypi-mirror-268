from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EutraCls:
	"""Eutra commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eutra", core, parent)

	def get_rformat(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:EUTRa:RFORmat \n
		Snippet: value: bool = driver.configure.signaling.eps.ueCapability.eutra.get_rformat() \n
		Adds the field 'requestReducedFormat-r13' to the message 'UeCapabilityEnquiry', for EPS tracking areas, container type
		'UE-EUTRA-Capability'. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:UECapability:EUTRa:RFORmat?')
		return Conversions.str_to_bool(response)

	def set_rformat(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:EUTRa:RFORmat \n
		Snippet: driver.configure.signaling.eps.ueCapability.eutra.set_rformat(enable = False) \n
		Adds the field 'requestReducedFormat-r13' to the message 'UeCapabilityEnquiry', for EPS tracking areas, container type
		'UE-EUTRA-Capability'. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:UECapability:EUTRa:RFORmat {param}')

	def get_sfc(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:EUTRa:SFC \n
		Snippet: value: bool = driver.configure.signaling.eps.ueCapability.eutra.get_sfc() \n
		Adds the field 'requestSkipFallbackComb-r13' to the message 'UeCapabilityEnquiry', for EPS tracking areas, container type
		'UE-EUTRA-Capability'. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:UECapability:EUTRa:SFC?')
		return Conversions.str_to_bool(response)

	def set_sfc(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:EUTRa:SFC \n
		Snippet: driver.configure.signaling.eps.ueCapability.eutra.set_sfc(enable = False) \n
		Adds the field 'requestSkipFallbackComb-r13' to the message 'UeCapabilityEnquiry', for EPS tracking areas, container type
		'UE-EUTRA-Capability'. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:UECapability:EUTRa:SFC {param}')
