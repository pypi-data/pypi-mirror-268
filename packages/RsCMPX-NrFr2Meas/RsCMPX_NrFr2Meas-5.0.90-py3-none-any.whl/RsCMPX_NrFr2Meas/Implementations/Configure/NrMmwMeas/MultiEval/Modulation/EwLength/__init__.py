from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EwLengthCls:
	"""EwLength commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ewLength", core, parent)

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .Cbandwidth import CbandwidthCls
			self._cbandwidth = CbandwidthCls(self._core, self._cmd_group)
		return self._cbandwidth

	def set(self, length_cp_norm_60: List[int], length_cp_norm_120: List[int]) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.ewLength.set(length_cp_norm_60 = [1, 2, 3], length_cp_norm_120 = [1, 2, 3]) \n
		Specifies the EVM window length in samples for all channel bandwidths, depending on the SC spacing. For ranges and *RST
		values, see Table 'Ranges and *RST values'. \n
			:param length_cp_norm_60: Comma-separated list of 4 values: for 50 MHz, 100 MHz, 200 MHz, 400 MHz Samples for normal CP, 60-kHz SC spacing
			:param length_cp_norm_120: Comma-separated list of 4 values: for 50 MHz, 100 MHz, 200 MHz, 400 MHz Samples for normal CP, 120-kHz SC spacing
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('length_cp_norm_60', length_cp_norm_60, DataType.IntegerList, None, False, False, 4), ArgSingle('length_cp_norm_120', length_cp_norm_120, DataType.IntegerList, None, False, False, 4))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength {param}'.rstrip())

	# noinspection PyTypeChecker
	class EwLengthStruct(StructBase):
		"""Response structure. Fields: \n
			- Length_Cp_Norm_60: List[int]: Comma-separated list of 4 values: for 50 MHz, 100 MHz, 200 MHz, 400 MHz Samples for normal CP, 60-kHz SC spacing
			- Length_Cp_Norm_120: List[int]: Comma-separated list of 4 values: for 50 MHz, 100 MHz, 200 MHz, 400 MHz Samples for normal CP, 120-kHz SC spacing"""
		__meta_args_list = [
			ArgStruct('Length_Cp_Norm_60', DataType.IntegerList, None, False, False, 4),
			ArgStruct('Length_Cp_Norm_120', DataType.IntegerList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length_Cp_Norm_60: List[int] = None
			self.Length_Cp_Norm_120: List[int] = None

	def get(self) -> EwLengthStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength \n
		Snippet: value: EwLengthStruct = driver.configure.nrMmwMeas.multiEval.modulation.ewLength.get() \n
		Specifies the EVM window length in samples for all channel bandwidths, depending on the SC spacing. For ranges and *RST
		values, see Table 'Ranges and *RST values'. \n
			:return: structure: for return value, see the help for EwLengthStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength?', self.__class__.EwLengthStruct())

	def clone(self) -> 'EwLengthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EwLengthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
