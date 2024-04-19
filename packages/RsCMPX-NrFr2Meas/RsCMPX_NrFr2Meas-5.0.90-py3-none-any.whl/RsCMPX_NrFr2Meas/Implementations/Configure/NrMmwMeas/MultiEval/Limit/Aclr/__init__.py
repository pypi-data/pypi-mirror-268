from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AclrCls:
	"""Aclr commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aclr", core, parent)

	@property
	def nr(self):
		"""nr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nr'):
			from .Nr import NrCls
			self._nr = NrCls(self._core, self._cmd_group)
		return self._nr

	@property
	def atTolerance(self):
		"""atTolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atTolerance'):
			from .AtTolerance import AtToleranceCls
			self._atTolerance = AtToleranceCls(self._core, self._cmd_group)
		return self._atTolerance

	def clone(self) -> 'AclrCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AclrCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
