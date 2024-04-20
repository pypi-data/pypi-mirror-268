from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HandoverCls:
	"""Handover commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("handover", core, parent)

	def set(self, target_cell_mcg: str, target_cell_scg: enums.TargetCellScg = None) -> None:
		"""SCPI: PROCedure:SIGNaling:MOBility:HANDover \n
		Snippet: driver.procedure.signaling.mobility.handover.set(target_cell_mcg = 'abc', target_cell_scg = enums.TargetCellScg.RELease) \n
		Triggers a handover for the MCG, from the current PCell to the <TargetCellMcg>. And triggers SCG mobility, from the
		current PSCell to the <TargetCellScg>. \n
			:param target_cell_mcg: Name of the target cell for the MCG. If you want to keep the old PCell, enter KEEP.
			:param target_cell_scg: (enum or string) Configures SCG mobility.
				- string: If you have a PSCell and you want to change it, set the name of the target cell.
				- omit the parameter: If you have no PSCell or you want to keep it, skip the parameter.
				- RELease: If you want to drop the PSCell, set RELease."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('target_cell_mcg', target_cell_mcg, DataType.String), ArgSingle('target_cell_scg', target_cell_scg, DataType.EnumExt, enums.TargetCellScg, is_optional=True))
		self._core.io.write(f'PROCedure:SIGNaling:MOBility:HANDover {param}'.rstrip())
