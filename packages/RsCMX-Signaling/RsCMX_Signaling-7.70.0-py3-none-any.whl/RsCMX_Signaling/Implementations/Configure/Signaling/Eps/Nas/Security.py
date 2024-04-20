from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SecurityCls:
	"""Security commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("security", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:SECurity:ENABle \n
		Snippet: value: bool = driver.configure.signaling.eps.nas.security.get_enable() \n
		Enables security procedures (ciphering, integrity protection) for EPS tracking areas. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:NAS:SECurity:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:SECurity:ENABle \n
		Snippet: driver.configure.signaling.eps.nas.security.set_enable(enable = False) \n
		Enables security procedures (ciphering, integrity protection) for EPS tracking areas. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:NAS:SECurity:ENABle {param}')

	# noinspection PyTypeChecker
	def get_integrity(self) -> enums.SecurityAlgorithmC:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:SECurity:INTegrity \n
		Snippet: value: enums.SecurityAlgorithmC = driver.configure.signaling.eps.nas.security.get_integrity() \n
		Selects an algorithm for NAS integrity protection in EPS tracking areas. \n
			:return: algorithm: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:NAS:SECurity:INTegrity?')
		return Conversions.str_to_scalar_enum(response, enums.SecurityAlgorithmC)

	def set_integrity(self, algorithm: enums.SecurityAlgorithmC) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:SECurity:INTegrity \n
		Snippet: driver.configure.signaling.eps.nas.security.set_integrity(algorithm = enums.SecurityAlgorithmC.EIA0) \n
		Selects an algorithm for NAS integrity protection in EPS tracking areas. \n
			:param algorithm: No help available
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.SecurityAlgorithmC)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:NAS:SECurity:INTegrity {param}')

	# noinspection PyTypeChecker
	def get_ciphering(self) -> enums.SecurityAlgorithmB:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:SECurity:CIPHering \n
		Snippet: value: enums.SecurityAlgorithmB = driver.configure.signaling.eps.nas.security.get_ciphering() \n
		Selects an algorithm for NAS ciphering in EPS tracking areas. \n
			:return: algorithm: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:NAS:SECurity:CIPHering?')
		return Conversions.str_to_scalar_enum(response, enums.SecurityAlgorithmB)

	def set_ciphering(self, algorithm: enums.SecurityAlgorithmB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:SECurity:CIPHering \n
		Snippet: driver.configure.signaling.eps.nas.security.set_ciphering(algorithm = enums.SecurityAlgorithmB.EEA0) \n
		Selects an algorithm for NAS ciphering in EPS tracking areas. \n
			:param algorithm: No help available
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.SecurityAlgorithmB)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:NAS:SECurity:CIPHering {param}')
