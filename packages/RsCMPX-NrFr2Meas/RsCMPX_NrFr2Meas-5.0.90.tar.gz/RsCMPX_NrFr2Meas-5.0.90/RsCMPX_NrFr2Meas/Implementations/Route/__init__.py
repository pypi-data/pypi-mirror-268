from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RouteCls:
	"""Route commands group definition. 5 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("route", core, parent)

	@property
	def nrMmwMeas(self):
		"""nrMmwMeas commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrMmwMeas'):
			from .NrMmwMeas import NrMmwMeasCls
			self._nrMmwMeas = NrMmwMeasCls(self._core, self._cmd_group)
		return self._nrMmwMeas

	def clone(self) -> 'RouteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RouteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
