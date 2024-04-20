from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCapabilityCls:
	"""UeCapability commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueCapability", core, parent)

	@property
	def eutra(self):
		"""eutra commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eutra'):
			from .Eutra import EutraCls
			self._eutra = EutraCls(self._core, self._cmd_group)
		return self._eutra

	@property
	def mrdc(self):
		"""mrdc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mrdc'):
			from .Mrdc import MrdcCls
			self._mrdc = MrdcCls(self._core, self._cmd_group)
		return self._mrdc

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ModeUeCapability:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:MODE \n
		Snippet: value: enums.ModeUeCapability = driver.configure.signaling.eps.ueCapability.get_mode() \n
		Selects the configuration mode for 'UeCapabilityEnquiry' messages in EPS tracking areas. \n
			:return: mode: SKIP: no 'UeCapabilityEnquiry' messages AUTO: automatic message configuration UDEFined: configuration via the other commands in this chapter
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:UECapability:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ModeUeCapability)

	def set_mode(self, mode: enums.ModeUeCapability) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:MODE \n
		Snippet: driver.configure.signaling.eps.ueCapability.set_mode(mode = enums.ModeUeCapability.AUTO) \n
		Selects the configuration mode for 'UeCapabilityEnquiry' messages in EPS tracking areas. \n
			:param mode: SKIP: no 'UeCapabilityEnquiry' messages AUTO: automatic message configuration UDEFined: configuration via the other commands in this chapter
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ModeUeCapability)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:UECapability:MODE {param}')

	def get_segmentation(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:SEGMentation \n
		Snippet: value: bool = driver.configure.signaling.eps.ueCapability.get_segmentation() \n
		Selects whether the UE is allowed to use segmentation for capability information in EPS tracking areas. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:UECapability:SEGMentation?')
		return Conversions.str_to_bool(response)

	def set_segmentation(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:UECapability:SEGMentation \n
		Snippet: driver.configure.signaling.eps.ueCapability.set_segmentation(enable = False) \n
		Selects whether the UE is allowed to use segmentation for capability information in EPS tracking areas. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:UECapability:SEGMentation {param}')

	def clone(self) -> 'UeCapabilityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCapabilityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
