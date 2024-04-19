from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrMmwMeasCls:
	"""NrMmwMeas commands group definition. 3 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrMmwMeas", core, parent)

	@property
	def network(self):
		"""network commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_network'):
			from .Network import NetworkCls
			self._network = NetworkCls(self._core, self._cmd_group)
		return self._network

	def clone(self) -> 'NrMmwMeasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NrMmwMeasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
