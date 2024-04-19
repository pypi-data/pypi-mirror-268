from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbandwidthCls:
	"""Cbandwidth commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: ChannelBw, default value after init: ChannelBw.Bw50"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbandwidth", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channelBw_get', 'repcap_channelBw_set', repcap.ChannelBw.Bw50)

	def repcap_channelBw_set(self, channelBw: repcap.ChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelBw.Default
		Default value after init: ChannelBw.Bw50"""
		self._cmd_group.set_repcap_enum_value(channelBw)

	def repcap_channelBw_get(self) -> repcap.ChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def blimits(self):
		"""blimits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blimits'):
			from .Blimits import BlimitsCls
			self._blimits = BlimitsCls(self._core, self._cmd_group)
		return self._blimits

	def clone(self) -> 'CbandwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CbandwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
