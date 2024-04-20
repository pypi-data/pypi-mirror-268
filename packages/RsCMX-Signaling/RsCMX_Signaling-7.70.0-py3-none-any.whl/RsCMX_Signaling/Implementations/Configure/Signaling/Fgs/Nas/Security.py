from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SecurityCls:
	"""Security commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("security", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:ENABle \n
		Snippet: value: bool = driver.configure.signaling.fgs.nas.security.get_enable() \n
		Enables security procedures (ciphering, integrity protection) for 5GS tracking areas. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:SECurity:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:ENABle \n
		Snippet: driver.configure.signaling.fgs.nas.security.set_enable(enable = False) \n
		Enables security procedures (ciphering, integrity protection) for 5GS tracking areas. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:SECurity:ENABle {param}')

	# noinspection PyTypeChecker
	def get_integrity(self) -> enums.IntegrityAlgorithm:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:INTegrity \n
		Snippet: value: enums.IntegrityAlgorithm = driver.configure.signaling.fgs.nas.security.get_integrity() \n
		Selects an algorithm for NAS integrity protection in 5GS tracking areas. \n
			:return: algorithm: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:SECurity:INTegrity?')
		return Conversions.str_to_scalar_enum(response, enums.IntegrityAlgorithm)

	def set_integrity(self, algorithm: enums.IntegrityAlgorithm) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:INTegrity \n
		Snippet: driver.configure.signaling.fgs.nas.security.set_integrity(algorithm = enums.IntegrityAlgorithm.HIGHest) \n
		Selects an algorithm for NAS integrity protection in 5GS tracking areas. \n
			:param algorithm: No help available
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.IntegrityAlgorithm)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:SECurity:INTegrity {param}')

	# noinspection PyTypeChecker
	def get_ciphering(self) -> enums.CipherAlgorithm:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:CIPHering \n
		Snippet: value: enums.CipherAlgorithm = driver.configure.signaling.fgs.nas.security.get_ciphering() \n
		Selects an algorithm for NAS ciphering in 5GS tracking areas. \n
			:return: algorithm: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:SECurity:CIPHering?')
		return Conversions.str_to_scalar_enum(response, enums.CipherAlgorithm)

	def set_ciphering(self, algorithm: enums.CipherAlgorithm) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:CIPHering \n
		Snippet: driver.configure.signaling.fgs.nas.security.set_ciphering(algorithm = enums.CipherAlgorithm.EA0) \n
		Selects an algorithm for NAS ciphering in 5GS tracking areas. \n
			:param algorithm: No help available
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.CipherAlgorithm)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:SECurity:CIPHering {param}')

	# noinspection PyTypeChecker
	def get_pauth(self) -> enums.AuthProcedure:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:PAUTh \n
		Snippet: value: enums.AuthProcedure = driver.configure.signaling.fgs.nas.security.get_pauth() \n
		Selects a primary authentication and key agreement procedure for 5GS tracking areas. \n
			:return: procedure: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:SECurity:PAUTh?')
		return Conversions.str_to_scalar_enum(response, enums.AuthProcedure)

	def set_pauth(self, procedure: enums.AuthProcedure) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:PAUTh \n
		Snippet: driver.configure.signaling.fgs.nas.security.set_pauth(procedure = enums.AuthProcedure.EAKA) \n
		Selects a primary authentication and key agreement procedure for 5GS tracking areas. \n
			:param procedure: No help available
		"""
		param = Conversions.enum_scalar_to_str(procedure, enums.AuthProcedure)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:SECurity:PAUTh {param}')

	def get_ps_auth(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:PSAuth \n
		Snippet: value: bool = driver.configure.signaling.fgs.nas.security.get_ps_auth() \n
		Enables authentication for PDU session establishment. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:SECurity:PSAuth?')
		return Conversions.str_to_bool(response)

	def set_ps_auth(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:SECurity:PSAuth \n
		Snippet: driver.configure.signaling.fgs.nas.security.set_ps_auth(enable = False) \n
		Enables authentication for PDU session establishment. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:SECurity:PSAuth {param}')
