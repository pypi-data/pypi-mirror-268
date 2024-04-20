from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TlvCls:
	"""Tlv commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tlv", core, parent)

	def set_att_accept(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:TLV:ATTaccept \n
		Snippet: driver.configure.signaling.eps.nas.tlv.set_att_accept(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:NAS:TLV:ATTaccept {param}')

	def set_dbearer(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:TLV:DBEarer \n
		Snippet: driver.configure.signaling.eps.nas.tlv.set_dbearer(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:NAS:TLV:DBEarer {param}')

	def set_bearer(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:NAS:TLV:BEARer \n
		Snippet: driver.configure.signaling.eps.nas.tlv.set_bearer(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:NAS:TLV:BEARer {param}')
