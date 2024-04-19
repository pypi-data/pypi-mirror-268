from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	@property
	def scIndex(self):
		"""scIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scIndex'):
			from .ScIndex import ScIndexCls
			self._scIndex = ScIndexCls(self._core, self._cmd_group)
		return self._scIndex

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Seg_Reliability: int: Reliability indicator for the segment
			- Statist_Expired: int: Reached statistical length in slots
			- Out_Of_Tolerance: int: Percentage of measured subframes with failed limit check
			- Ripple_1: float: Max (range 1) - min (range 1)
			- Ripple_2: float: Max (range 2) - min (range 2)
			- Max_R_1_Min_R_2: float: Max (range 1) - min (range 2)
			- Max_R_2_Min_R_1: float: Max (range 2) - min (range 1)
			- Min_R_1: float: Min (range 1)
			- Max_R_1: float: Max (range 1)
			- Min_R_2: float: Min (range 2)
			- Max_R_2: float: Max (range 2)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Ripple_1'),
			ArgStruct.scalar_float('Ripple_2'),
			ArgStruct.scalar_float('Max_R_1_Min_R_2'),
			ArgStruct.scalar_float('Max_R_2_Min_R_1'),
			ArgStruct.scalar_float('Min_R_1'),
			ArgStruct.scalar_float('Max_R_1'),
			ArgStruct.scalar_float('Min_R_2'),
			ArgStruct.scalar_float('Max_R_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
			self.Out_Of_Tolerance: int = None
			self.Ripple_1: float = None
			self.Ripple_2: float = None
			self.Max_R_1_Min_R_2: float = None
			self.Max_R_2_Min_R_1: float = None
			self.Min_R_1: float = None
			self.Max_R_1: float = None
			self.Min_R_2: float = None
			self.Max_R_2: float = None

	def fetch(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> FetchStruct:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:CC<carrier>]:ESFLatness:CURRent \n
		Snippet: value: FetchStruct = driver.nrMmwMeas.multiEval.listPy.segment.cc.esFlatness.current.fetch(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return equalizer spectrum flatness single value results for segment <no>, for carrier <c>. \n
		Suppressed linked return values: reliability \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:ESFLatness:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment
			- Statist_Expired: int: Reached statistical length in slots
			- Out_Of_Tolerance: int: Percentage of measured subframes with failed limit check
			- Ripple_1: float or bool: Limit check result for max (range 1) - min (range 1) .
			- Ripple_2: float or bool: Limit check result for max (range 2) - min (range 2) .
			- Max_R_1_Min_R_2: float or bool: Limit check result for max (range 1) - min (range 2) .
			- Max_R_2_Min_R_1: float or bool: Limit check result for max (range 2) - min (range 1) ."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float_ext('Ripple_1'),
			ArgStruct.scalar_float_ext('Ripple_2'),
			ArgStruct.scalar_float_ext('Max_R_1_Min_R_2'),
			ArgStruct.scalar_float_ext('Max_R_2_Min_R_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
			self.Out_Of_Tolerance: int = None
			self.Ripple_1: float or bool = None
			self.Ripple_2: float or bool = None
			self.Max_R_1_Min_R_2: float or bool = None
			self.Max_R_2_Min_R_1: float or bool = None

	def calculate(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> CalculateStruct:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:CC<carrier>]:ESFLatness:CURRent \n
		Snippet: value: CalculateStruct = driver.nrMmwMeas.multiEval.listPy.segment.cc.esFlatness.current.calculate(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return equalizer spectrum flatness single value results for segment <no>, for carrier <c>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		return self._core.io.query_struct(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:ESFLatness:CURRent?', self.__class__.CalculateStruct())

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
