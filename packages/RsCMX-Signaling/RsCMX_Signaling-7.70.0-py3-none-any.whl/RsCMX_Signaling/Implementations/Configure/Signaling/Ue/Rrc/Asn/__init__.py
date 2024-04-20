from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AsnCls:
	"""Asn commands group definition. 5 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("asn", core, parent)

	@property
	def lte(self):
		"""lte commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	def set_setup(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UE:RRC:ASN:SETup \n
		Snippet: driver.configure.signaling.ue.rrc.asn.set_setup(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:UE:RRC:ASN:SETup {param}')

	def set_re_config(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UE:RRC:ASN:REConfig \n
		Snippet: driver.configure.signaling.ue.rrc.asn.set_re_config(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:UE:RRC:ASN:REConfig {param}')

	def set_release(self, message: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UE:RRC:ASN:RELease \n
		Snippet: driver.configure.signaling.ue.rrc.asn.set_release(message = 'abc') \n
		No command help available \n
			:param message: No help available
		"""
		param = Conversions.value_to_quoted_str(message)
		self._core.io.write(f'CONFigure:SIGNaling:UE:RRC:ASN:RELease {param}')

	def clone(self) -> 'AsnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AsnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
