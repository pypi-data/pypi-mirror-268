from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LteCls:
	"""Lte commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	def set_re_config(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UE:RRC:ASN:LTE:REConfig \n
		Snippet: driver.configure.signaling.ue.rrc.asn.lte.set_re_config(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:UE:RRC:ASN:LTE:REConfig {param}')

	def set_release(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UE:RRC:ASN:LTE:RELease \n
		Snippet: driver.configure.signaling.ue.rrc.asn.lte.set_release(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:UE:RRC:ASN:LTE:RELease {param}')
