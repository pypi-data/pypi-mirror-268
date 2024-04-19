from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 26 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: CarrierComponentExt, default value after init: CarrierComponentExt.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrierComponentExt_get', 'repcap_carrierComponentExt_set', repcap.CarrierComponentExt.Nr1)

	def repcap_carrierComponentExt_set(self, carrierComponentExt: repcap.CarrierComponentExt) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponentExt.Default
		Default value after init: CarrierComponentExt.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrierComponentExt)

	def repcap_carrierComponentExt_get(self) -> repcap.CarrierComponentExt:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def modulation(self):
		"""modulation commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

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

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
