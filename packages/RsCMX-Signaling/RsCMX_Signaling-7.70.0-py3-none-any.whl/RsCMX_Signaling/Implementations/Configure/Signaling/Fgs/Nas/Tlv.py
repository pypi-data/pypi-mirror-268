from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TlvCls:
	"""Tlv commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tlv", core, parent)

	def set_reg_accept(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:TLV:REGaccept \n
		Snippet: driver.configure.signaling.fgs.nas.tlv.set_reg_accept(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:TLV:REGaccept {param}')

	def set_pdu_accept(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:TLV:PDUaccept \n
		Snippet: driver.configure.signaling.fgs.nas.tlv.set_pdu_accept(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:TLV:PDUaccept {param}')
