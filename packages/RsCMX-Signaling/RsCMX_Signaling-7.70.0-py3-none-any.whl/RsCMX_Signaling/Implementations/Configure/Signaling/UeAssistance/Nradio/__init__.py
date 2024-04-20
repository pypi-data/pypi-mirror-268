from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NradioCls:
	"""Nradio commands group definition. 9 total commands, 8 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nradio", core, parent)

	@property
	def dbReport(self):
		"""dbReport commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbReport'):
			from .DbReport import DbReportCls
			self._dbReport = DbReportCls(self._core, self._cmd_group)
		return self._dbReport

	@property
	def oassistance(self):
		"""oassistance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oassistance'):
			from .Oassistance import OassistanceCls
			self._oassistance = OassistanceCls(self._core, self._cmd_group)
		return self._oassistance

	@property
	def drxPref(self):
		"""drxPref commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_drxPref'):
			from .DrxPref import DrxPrefCls
			self._drxPref = DrxPrefCls(self._core, self._cmd_group)
		return self._drxPref

	@property
	def mbwPref(self):
		"""mbwPref commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mbwPref'):
			from .MbwPref import MbwPrefCls
			self._mbwPref = MbwPrefCls(self._core, self._cmd_group)
		return self._mbwPref

	@property
	def mccPref(self):
		"""mccPref commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mccPref'):
			from .MccPref import MccPrefCls
			self._mccPref = MccPrefCls(self._core, self._cmd_group)
		return self._mccPref

	@property
	def mmLayer(self):
		"""mmLayer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmLayer'):
			from .MmLayer import MmLayerCls
			self._mmLayer = MmLayerCls(self._core, self._cmd_group)
		return self._mmLayer

	@property
	def msOffset(self):
		"""msOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_msOffset'):
			from .MsOffset import MsOffsetCls
			self._msOffset = MsOffsetCls(self._core, self._cmd_group)
		return self._msOffset

	@property
	def relPref(self):
		"""relPref commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relPref'):
			from .RelPref import RelPrefCls
			self._relPref = RelPrefCls(self._core, self._cmd_group)
		return self._relPref

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Dbr_Enable: bool: Enables/disables transmitting the parameter 'delayBudgetReportingConfig' in the IE 'OtherConfig'.
			- Dbr_Prohibit_Timer: enums.ProhibitTimer: Optional setting parameter. Signaled 'delayBudgetReportingProhibitTimer'. Sn: n ms SnDm: n.m ms
			- Oass_Enable: bool: Optional setting parameter. Enables/disables transmitting the parameter 'OverheatingAssistanceConfig' in the IE 'OtherConfig'.
			- Oass_Prohibit_Timer: enums.ProhibitTimer: Optional setting parameter. Signaled 'overheatingIndicationProhibitTimer'. Sn: n ms SnDm: n.m ms
			- Drxp_Enable: bool: Optional setting parameter. Enables/disables transmitting the parameter 'DRX-PreferenceConfig-r16' in the IE 'OtherConfig'.
			- Drxp_Prohibit_Timer: enums.ProhibitTimer: Optional setting parameter. Signaled 'drx-PreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms
			- Mbwp_Enable: bool: Optional setting parameter. Enables/disables transmitting the parameter 'MaxBW-PreferenceConfig-r16' in the IE 'OtherConfig'.
			- Mbwp_Prohibit_Timer: enums.ProhibitTimer: Optional setting parameter. Signaled 'maxBW-PreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms
			- Mccp_Enable: bool: Optional setting parameter. Enables/disables transmitting the parameter 'MaxCC-PreferenceConfig-r16' in the IE 'OtherConfig'.
			- Mccp_Prohibit_Timer: enums.ProhibitTimer: Optional setting parameter. Signaled 'maxCC-PreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms
			- Mml_Enable: bool: Optional setting parameter. Enables/disables transmitting the parameter 'MaxMIMO-LayerPreferenceConfig-r16' in the IE 'OtherConfig'.
			- Mml_Prohibit_Timer: enums.ProhibitTimer: Optional setting parameter. Signaled 'maxMIMO-LayerPreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms
			- Msof_Enable: bool: Optional setting parameter. Enables/disables transmitting the parameter 'MinSchedulingOffsetPreferenceConfig-r16' in the IE 'OtherConfig'.
			- Msof_Prohibit_Timer: enums.ProhibitTimer: Optional setting parameter. Signaled 'minSchedulingOffsetPreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms
			- Relp_Enable: bool: Optional setting parameter. Enables/disables transmitting the parameter 'ReleasePreferenceConfig-r16' in the IE 'OtherConfig'.
			- Relp_Prohibit_Timer: enums.ProhibitTimer: Optional setting parameter. Signaled 'releasePreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Dbr_Enable'),
			ArgStruct.scalar_enum_optional('Dbr_Prohibit_Timer', enums.ProhibitTimer),
			ArgStruct.scalar_bool_optional('Oass_Enable'),
			ArgStruct.scalar_enum_optional('Oass_Prohibit_Timer', enums.ProhibitTimer),
			ArgStruct.scalar_bool_optional('Drxp_Enable'),
			ArgStruct.scalar_enum_optional('Drxp_Prohibit_Timer', enums.ProhibitTimer),
			ArgStruct.scalar_bool_optional('Mbwp_Enable'),
			ArgStruct.scalar_enum_optional('Mbwp_Prohibit_Timer', enums.ProhibitTimer),
			ArgStruct.scalar_bool_optional('Mccp_Enable'),
			ArgStruct.scalar_enum_optional('Mccp_Prohibit_Timer', enums.ProhibitTimer),
			ArgStruct.scalar_bool_optional('Mml_Enable'),
			ArgStruct.scalar_enum_optional('Mml_Prohibit_Timer', enums.ProhibitTimer),
			ArgStruct.scalar_bool_optional('Msof_Enable'),
			ArgStruct.scalar_enum_optional('Msof_Prohibit_Timer', enums.ProhibitTimer),
			ArgStruct.scalar_bool_optional('Relp_Enable'),
			ArgStruct.scalar_enum_optional('Relp_Prohibit_Timer', enums.ProhibitTimer)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dbr_Enable: bool = None
			self.Dbr_Prohibit_Timer: enums.ProhibitTimer = None
			self.Oass_Enable: bool = None
			self.Oass_Prohibit_Timer: enums.ProhibitTimer = None
			self.Drxp_Enable: bool = None
			self.Drxp_Prohibit_Timer: enums.ProhibitTimer = None
			self.Mbwp_Enable: bool = None
			self.Mbwp_Prohibit_Timer: enums.ProhibitTimer = None
			self.Mccp_Enable: bool = None
			self.Mccp_Prohibit_Timer: enums.ProhibitTimer = None
			self.Mml_Enable: bool = None
			self.Mml_Prohibit_Timer: enums.ProhibitTimer = None
			self.Msof_Enable: bool = None
			self.Msof_Prohibit_Timer: enums.ProhibitTimer = None
			self.Relp_Enable: bool = None
			self.Relp_Prohibit_Timer: enums.ProhibitTimer = None

	def get_value(self) -> ValueStruct:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio \n
		Snippet: value: ValueStruct = driver.configure.signaling.ueAssistance.nradio.get_value() \n
		Configures UE assistance requests for power saving and handling of overheating. This command combines the other
		configuration commands. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:SIGNaling:UEASsistance:NRADio?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio \n
		Snippet with structure: \n
		structure = driver.configure.signaling.ueAssistance.nradio.ValueStruct() \n
		structure.Dbr_Enable: bool = False \n
		structure.Dbr_Prohibit_Timer: enums.ProhibitTimer = enums.ProhibitTimer.INF \n
		structure.Oass_Enable: bool = False \n
		structure.Oass_Prohibit_Timer: enums.ProhibitTimer = enums.ProhibitTimer.INF \n
		structure.Drxp_Enable: bool = False \n
		structure.Drxp_Prohibit_Timer: enums.ProhibitTimer = enums.ProhibitTimer.INF \n
		structure.Mbwp_Enable: bool = False \n
		structure.Mbwp_Prohibit_Timer: enums.ProhibitTimer = enums.ProhibitTimer.INF \n
		structure.Mccp_Enable: bool = False \n
		structure.Mccp_Prohibit_Timer: enums.ProhibitTimer = enums.ProhibitTimer.INF \n
		structure.Mml_Enable: bool = False \n
		structure.Mml_Prohibit_Timer: enums.ProhibitTimer = enums.ProhibitTimer.INF \n
		structure.Msof_Enable: bool = False \n
		structure.Msof_Prohibit_Timer: enums.ProhibitTimer = enums.ProhibitTimer.INF \n
		structure.Relp_Enable: bool = False \n
		structure.Relp_Prohibit_Timer: enums.ProhibitTimer = enums.ProhibitTimer.INF \n
		driver.configure.signaling.ueAssistance.nradio.set_value(value = structure) \n
		Configures UE assistance requests for power saving and handling of overheating. This command combines the other
		configuration commands. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:SIGNaling:UEASsistance:NRADio', value)

	def clone(self) -> 'NradioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NradioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
