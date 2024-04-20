from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PuschCls:
	"""Pusch commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def tpRecoding(self):
		"""tpRecoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpRecoding'):
			from .TpRecoding import TpRecodingCls
			self._tpRecoding = TpRecodingCls(self._core, self._cmd_group)
		return self._tpRecoding

	@property
	def dtfs(self):
		"""dtfs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dtfs'):
			from .Dtfs import DtfsCls
			self._dtfs = DtfsCls(self._core, self._cmd_group)
		return self._dtfs

	@property
	def tschema(self):
		"""tschema commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tschema'):
			from .Tschema import TschemaCls
			self._tschema = TschemaCls(self._core, self._cmd_group)
		return self._tschema

	def clone(self) -> 'PuschCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PuschCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
