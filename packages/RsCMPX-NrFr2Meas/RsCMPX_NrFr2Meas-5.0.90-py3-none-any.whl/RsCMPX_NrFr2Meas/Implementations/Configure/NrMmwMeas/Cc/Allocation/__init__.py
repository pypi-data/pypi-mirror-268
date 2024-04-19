from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllocationCls:
	"""Allocation commands group definition. 20 total commands, 5 Subgroups, 0 group commands
	Repeated Capability: AllocationMore, default value after init: AllocationMore.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("allocation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_allocationMore_get', 'repcap_allocationMore_set', repcap.AllocationMore.Nr1)

	def repcap_allocationMore_set(self, allocationMore: repcap.AllocationMore) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AllocationMore.Default
		Default value after init: AllocationMore.Nr1"""
		self._cmd_group.set_repcap_enum_value(allocationMore)

	def repcap_allocationMore_get(self) -> repcap.AllocationMore:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bwp(self):
		"""bwp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwp'):
			from .Bwp import BwpCls
			self._bwp = BwpCls(self._core, self._cmd_group)
		return self._bwp

	@property
	def ctype(self):
		"""ctype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctype'):
			from .Ctype import CtypeCls
			self._ctype = CtypeCls(self._core, self._cmd_group)
		return self._ctype

	@property
	def pusch(self):
		"""pusch commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def pucch(self):
		"""pucch commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	@property
	def srs(self):
		"""srs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	def clone(self) -> 'AllocationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AllocationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
