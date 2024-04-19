from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 12 total commands, 7 Subgroups, 0 group commands
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
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .Cbandwidth import CbandwidthCls
			self._cbandwidth = CbandwidthCls(self._core, self._cmd_group)
		return self._cbandwidth

	@property
	def plcId(self):
		"""plcId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plcId'):
			from .PlcId import PlcIdCls
			self._plcId = PlcIdCls(self._core, self._cmd_group)
		return self._plcId

	@property
	def taPosition(self):
		"""taPosition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taPosition'):
			from .TaPosition import TaPositionCls
			self._taPosition = TaPositionCls(self._core, self._cmd_group)
		return self._taPosition

	@property
	def bwPart(self):
		"""bwPart commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwPart'):
			from .BwPart import BwPartCls
			self._bwPart = BwPartCls(self._core, self._cmd_group)
		return self._bwPart

	@property
	def nallocations(self):
		"""nallocations commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nallocations'):
			from .Nallocations import NallocationsCls
			self._nallocations = NallocationsCls(self._core, self._cmd_group)
		return self._nallocations

	@property
	def allocation(self):
		"""allocation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_allocation'):
			from .Allocation import AllocationCls
			self._allocation = AllocationCls(self._core, self._cmd_group)
		return self._allocation

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
