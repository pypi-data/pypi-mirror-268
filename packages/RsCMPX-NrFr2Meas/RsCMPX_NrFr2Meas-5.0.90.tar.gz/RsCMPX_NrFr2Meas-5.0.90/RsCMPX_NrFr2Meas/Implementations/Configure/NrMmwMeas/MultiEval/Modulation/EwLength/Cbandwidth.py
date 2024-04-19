from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbandwidthCls:
	"""Cbandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands
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

	def set(self, length_cp_norm_60: int, length_cp_norm_120: int, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth<bw> \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.ewLength.cbandwidth.set(length_cp_norm_60 = 1, length_cp_norm_120 = 1, channelBw = repcap.ChannelBw.Default) \n
		Specifies the EVM window length in samples for a selected channel bandwidth, depending on the SC spacing. \n
			:param length_cp_norm_60: Samples for normal CP, 60-kHz SC spacing
			:param length_cp_norm_120: Samples for normal CP, 120-kHz SC spacing
			:param channelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'Cbandwidth')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('length_cp_norm_60', length_cp_norm_60, DataType.Integer), ArgSingle('length_cp_norm_120', length_cp_norm_120, DataType.Integer))
		channelBw_cmd_val = self._cmd_group.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth{channelBw_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class CbandwidthStruct(StructBase):
		"""Response structure. Fields: \n
			- Length_Cp_Norm_60: int: Samples for normal CP, 60-kHz SC spacing
			- Length_Cp_Norm_120: int: Samples for normal CP, 120-kHz SC spacing"""
		__meta_args_list = [
			ArgStruct.scalar_int('Length_Cp_Norm_60'),
			ArgStruct.scalar_int('Length_Cp_Norm_120')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length_Cp_Norm_60: int = None
			self.Length_Cp_Norm_120: int = None

	def get(self, channelBw=repcap.ChannelBw.Default) -> CbandwidthStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth<bw> \n
		Snippet: value: CbandwidthStruct = driver.configure.nrMmwMeas.multiEval.modulation.ewLength.cbandwidth.get(channelBw = repcap.ChannelBw.Default) \n
		Specifies the EVM window length in samples for a selected channel bandwidth, depending on the SC spacing. \n
			:param channelBw: optional repeated capability selector. Default value: Bw50 (settable in the interface 'Cbandwidth')
			:return: structure: for return value, see the help for CbandwidthStruct structure arguments."""
		channelBw_cmd_val = self._cmd_group.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth{channelBw_cmd_val}?', self.__class__.CbandwidthStruct())

	def clone(self) -> 'CbandwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CbandwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
