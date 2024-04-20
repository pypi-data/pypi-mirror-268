from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SecurityCls:
	"""Security commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("security", core, parent)

	# noinspection PyTypeChecker
	def get_integrity(self) -> enums.SecurityAlgorithm:
		"""SCPI: [CONFigure]:SIGNaling:EPS:AS:SECurity:INTegrity \n
		Snippet: value: enums.SecurityAlgorithm = driver.configure.signaling.eps.asPy.security.get_integrity() \n
		Selects an algorithm for AS integrity protection in EPS tracking areas. \n
			:return: algorithm: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:AS:SECurity:INTegrity?')
		return Conversions.str_to_scalar_enum(response, enums.SecurityAlgorithm)

	def set_integrity(self, algorithm: enums.SecurityAlgorithm) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:AS:SECurity:INTegrity \n
		Snippet: driver.configure.signaling.eps.asPy.security.set_integrity(algorithm = enums.SecurityAlgorithm.AES) \n
		Selects an algorithm for AS integrity protection in EPS tracking areas. \n
			:param algorithm: No help available
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.SecurityAlgorithm)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:AS:SECurity:INTegrity {param}')

	# noinspection PyTypeChecker
	def get_ciphering(self) -> enums.SecurityAlgorithm:
		"""SCPI: [CONFigure]:SIGNaling:EPS:AS:SECurity:CIPHering \n
		Snippet: value: enums.SecurityAlgorithm = driver.configure.signaling.eps.asPy.security.get_ciphering() \n
		Selects an algorithm for AS ciphering in EPS tracking areas. \n
			:return: algorithm: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:AS:SECurity:CIPHering?')
		return Conversions.str_to_scalar_enum(response, enums.SecurityAlgorithm)

	def set_ciphering(self, algorithm: enums.SecurityAlgorithm) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:AS:SECurity:CIPHering \n
		Snippet: driver.configure.signaling.eps.asPy.security.set_ciphering(algorithm = enums.SecurityAlgorithm.AES) \n
		Selects an algorithm for AS ciphering in EPS tracking areas. \n
			:param algorithm: No help available
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.SecurityAlgorithm)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:AS:SECurity:CIPHering {param}')
