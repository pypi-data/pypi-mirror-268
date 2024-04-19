from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	@property
	def negativ(self):
		"""negativ commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_negativ'):
			from .Negativ import NegativCls
			self._negativ = NegativCls(self._core, self._cmd_group)
		return self._negativ

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def positiv(self):
		"""positiv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_positiv'):
			from .Positiv import PositivCls
			self._positiv = PositivCls(self._core, self._cmd_group)
		return self._positiv

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
