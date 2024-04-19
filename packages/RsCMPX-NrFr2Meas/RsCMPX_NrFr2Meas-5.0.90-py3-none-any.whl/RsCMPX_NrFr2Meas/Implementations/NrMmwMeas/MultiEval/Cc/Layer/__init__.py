from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LayerCls:
	"""Layer commands group definition. 83 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: Layer, default value after init: Layer.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("layer", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_layer_get', 'repcap_layer_set', repcap.Layer.Nr1)

	def repcap_layer_set(self, layer: repcap.Layer) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Layer.Default
		Default value after init: Layer.Nr1"""
		self._cmd_group.set_repcap_enum_value(layer)

	def repcap_layer_get(self) -> repcap.Layer:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def trace(self):
		"""trace commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .EvMagnitude import EvMagnitudeCls
			self._evMagnitude = EvMagnitudeCls(self._core, self._cmd_group)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import MerrorCls
			self._merror = MerrorCls(self._core, self._cmd_group)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import PerrorCls
			self._perror = PerrorCls(self._core, self._cmd_group)
		return self._perror

	@property
	def iemission(self):
		"""iemission commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iemission'):
			from .Iemission import IemissionCls
			self._iemission = IemissionCls(self._core, self._cmd_group)
		return self._iemission

	@property
	def esFlatness(self):
		"""esFlatness commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_esFlatness'):
			from .EsFlatness import EsFlatnessCls
			self._esFlatness = EsFlatnessCls(self._core, self._cmd_group)
		return self._esFlatness

	@property
	def modulation(self):
		"""modulation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	def clone(self) -> 'LayerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LayerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
