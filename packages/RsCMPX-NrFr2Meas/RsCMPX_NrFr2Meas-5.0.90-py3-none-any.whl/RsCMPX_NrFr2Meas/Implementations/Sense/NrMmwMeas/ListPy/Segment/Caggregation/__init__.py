from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaggregationCls:
	"""Caggregation commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caggregation", core, parent)

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .Cbandwidth import CbandwidthCls
			self._cbandwidth = CbandwidthCls(self._core, self._cmd_group)
		return self._cbandwidth

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def ngBandwidth(self):
		"""ngBandwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ngBandwidth'):
			from .NgBandwidth import NgBandwidthCls
			self._ngBandwidth = NgBandwidthCls(self._core, self._cmd_group)
		return self._ngBandwidth

	def clone(self) -> 'CaggregationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CaggregationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
