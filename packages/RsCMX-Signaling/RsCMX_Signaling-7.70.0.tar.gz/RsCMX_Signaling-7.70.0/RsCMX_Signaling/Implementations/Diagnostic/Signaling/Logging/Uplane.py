from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplaneCls:
	"""Uplane commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplane", core, parent)

	# noinspection PyTypeChecker
	def get_uplink(self) -> enums.LogLevel:
		"""SCPI: DIAGnostic:SIGNaling:LOGGing:UPLane:UL \n
		Snippet: value: enums.LogLevel = driver.diagnostic.signaling.logging.uplane.get_uplink() \n
		No command help available \n
			:return: log_level: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:SIGNaling:LOGGing:UPLane:UL?')
		return Conversions.str_to_scalar_enum(response, enums.LogLevel)

	def set_uplink(self, log_level: enums.LogLevel) -> None:
		"""SCPI: DIAGnostic:SIGNaling:LOGGing:UPLane:UL \n
		Snippet: driver.diagnostic.signaling.logging.uplane.set_uplink(log_level = enums.LogLevel.BRIef) \n
		No command help available \n
			:param log_level: No help available
		"""
		param = Conversions.enum_scalar_to_str(log_level, enums.LogLevel)
		self._core.io.write(f'DIAGnostic:SIGNaling:LOGGing:UPLane:UL {param}')

	# noinspection PyTypeChecker
	def get_downlink(self) -> enums.LogLevel:
		"""SCPI: DIAGnostic:SIGNaling:LOGGing:UPLane:DL \n
		Snippet: value: enums.LogLevel = driver.diagnostic.signaling.logging.uplane.get_downlink() \n
		No command help available \n
			:return: log_level: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:SIGNaling:LOGGing:UPLane:DL?')
		return Conversions.str_to_scalar_enum(response, enums.LogLevel)

	def set_downlink(self, log_level: enums.LogLevel) -> None:
		"""SCPI: DIAGnostic:SIGNaling:LOGGing:UPLane:DL \n
		Snippet: driver.diagnostic.signaling.logging.uplane.set_downlink(log_level = enums.LogLevel.BRIef) \n
		No command help available \n
			:param log_level: No help available
		"""
		param = Conversions.enum_scalar_to_str(log_level, enums.LogLevel)
		self._core.io.write(f'DIAGnostic:SIGNaling:LOGGing:UPLane:DL {param}')
