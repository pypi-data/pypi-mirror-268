from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MrdcCls:
	"""Mrdc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mrdc", core, parent)

	def get_enr_only(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:MRDC:ENRonly \n
		Snippet: value: bool = driver.configure.signaling.eps.ueCapability.mrdc.get_enr_only() \n
		Adds the field 'eutra-nr-only-r15' to the message 'UeCapabilityEnquiry', for EPS tracking areas, container type
		'UE-MRDC-Capability'. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:UECapability:MRDC:ENRonly?')
		return Conversions.str_to_bool(response)

	def set_enr_only(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:MRDC:ENRonly \n
		Snippet: driver.configure.signaling.eps.ueCapability.mrdc.set_enr_only(enable = False) \n
		Adds the field 'eutra-nr-only-r15' to the message 'UeCapabilityEnquiry', for EPS tracking areas, container type
		'UE-MRDC-Capability'. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:UECapability:MRDC:ENRonly {param}')
