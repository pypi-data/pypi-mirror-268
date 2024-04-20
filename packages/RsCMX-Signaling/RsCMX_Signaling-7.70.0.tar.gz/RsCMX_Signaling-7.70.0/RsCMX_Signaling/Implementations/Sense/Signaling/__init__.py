from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalingCls:
	"""Signaling commands group definition. 41 total commands, 9 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signaling", core, parent)

	@property
	def topology(self):
		"""topology commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_topology'):
			from .Topology import TopologyCls
			self._topology = TopologyCls(self._core, self._cmd_group)
		return self._topology

	@property
	def ue(self):
		"""ue commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Ue import UeCls
			self._ue = UeCls(self._core, self._cmd_group)
		return self._ue

	@property
	def tmode(self):
		"""tmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmode'):
			from .Tmode import TmodeCls
			self._tmode = TmodeCls(self._core, self._cmd_group)
		return self._tmode

	@property
	def cell(self):
		"""cell commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import CellCls
			self._cell = CellCls(self._core, self._cmd_group)
		return self._cell

	@property
	def ccopy(self):
		"""ccopy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccopy'):
			from .Ccopy import CcopyCls
			self._ccopy = CcopyCls(self._core, self._cmd_group)
		return self._ccopy

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def nradio(self):
		"""nradio commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	@property
	def fading(self):
		"""fading commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Fading import FadingCls
			self._fading = FadingCls(self._core, self._cmd_group)
		return self._fading

	@property
	def awgn(self):
		"""awgn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import AwgnCls
			self._awgn = AwgnCls(self._core, self._cmd_group)
		return self._awgn

	# noinspection PyTypeChecker
	class SmsStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Core_Network: List[enums.CoreNetwork]: Type of network delivering the message, EPS or 5G
			- Address: List[str]: Address of the originator of the message
			- State: List[enums.StateTest]: States whether an error occurred.
			- Message: List[str]: For successful transmission, the short message contents. For erroneous transmission, information about the error."""
		__meta_args_list = [
			ArgStruct('Core_Network', DataType.EnumList, enums.CoreNetwork, False, True, 1),
			ArgStruct('Address', DataType.StringList, None, False, True, 1),
			ArgStruct('State', DataType.EnumList, enums.StateTest, False, True, 1),
			ArgStruct('Message', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Core_Network: List[enums.CoreNetwork] = None
			self.Address: List[str] = None
			self.State: List[enums.StateTest] = None
			self.Message: List[str] = None

	def get_sms(self) -> SmsStruct:
		"""SCPI: SENSe:SIGNaling:SMS \n
		Snippet: value: SmsStruct = driver.sense.signaling.get_sms() \n
		Queries information about the last received mobile-originated short message. \n
			:return: structure: for return value, see the help for SmsStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:SIGNaling:SMS?', self.__class__.SmsStruct())

	def clone(self) -> 'SignalingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
