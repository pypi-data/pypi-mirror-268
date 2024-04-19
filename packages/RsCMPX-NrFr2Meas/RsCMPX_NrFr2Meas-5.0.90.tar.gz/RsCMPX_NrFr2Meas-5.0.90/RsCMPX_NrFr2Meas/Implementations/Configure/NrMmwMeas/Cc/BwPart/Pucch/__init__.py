from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PucchCls:
	"""Pucch commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	@property
	def adMrs(self):
		"""adMrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adMrs'):
			from .AdMrs import AdMrsCls
			self._adMrs = AdMrsCls(self._core, self._cmd_group)
		return self._adMrs

	@property
	def phbpsk(self):
		"""phbpsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phbpsk'):
			from .Phbpsk import PhbpskCls
			self._phbpsk = PhbpskCls(self._core, self._cmd_group)
		return self._phbpsk

	def clone(self) -> 'PucchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PucchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
