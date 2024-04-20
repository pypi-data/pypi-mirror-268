from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NbehaviorCls:
	"""Nbehavior commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nbehavior", core, parent)

	@property
	def rrcReject(self):
		"""rrcReject commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrcReject'):
			from .RrcReject import RrcRejectCls
			self._rrcReject = RrcRejectCls(self._core, self._cmd_group)
		return self._rrcReject

	def get_di_timer(self) -> float or bool:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NBEHavior:DITimer \n
		Snippet: value: float or bool = driver.configure.signaling.fgs.nbehavior.get_di_timer() \n
		Configures the data inactivity timer for 5GS tracking areas. With enabled timer, an RRC connection is released when there
		has been no activity on the connection (no traffic) for the configured time. \n
			:return: timer: (float or boolean) Numeric value: Enables the timer and sets the timer value. ON: Enables the timer, using the configured numeric value. OFF: Disables the timer (no release due to inactivity) .
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NBEHavior:DITimer?')
		return Conversions.str_to_float_or_bool(response)

	def set_di_timer(self, timer: float or bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NBEHavior:DITimer \n
		Snippet: driver.configure.signaling.fgs.nbehavior.set_di_timer(timer = 1.0) \n
		Configures the data inactivity timer for 5GS tracking areas. With enabled timer, an RRC connection is released when there
		has been no activity on the connection (no traffic) for the configured time. \n
			:param timer: (float or boolean) Numeric value: Enables the timer and sets the timer value. ON: Enables the timer, using the configured numeric value. OFF: Disables the timer (no release due to inactivity) .
		"""
		param = Conversions.decimal_or_bool_value_to_str(timer)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NBEHavior:DITimer {param}')

	def get_krrc(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NBEHavior:KRRC \n
		Snippet: value: bool = driver.configure.signaling.fgs.nbehavior.get_krrc() \n
		Selects whether the RRC connection is kept after a registration in a 5GS tracking area. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NBEHavior:KRRC?')
		return Conversions.str_to_bool(response)

	def set_krrc(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NBEHavior:KRRC \n
		Snippet: driver.configure.signaling.fgs.nbehavior.set_krrc(enable = False) \n
		Selects whether the RRC connection is kept after a registration in a 5GS tracking area. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NBEHavior:KRRC {param}')

	def clone(self) -> 'NbehaviorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NbehaviorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
