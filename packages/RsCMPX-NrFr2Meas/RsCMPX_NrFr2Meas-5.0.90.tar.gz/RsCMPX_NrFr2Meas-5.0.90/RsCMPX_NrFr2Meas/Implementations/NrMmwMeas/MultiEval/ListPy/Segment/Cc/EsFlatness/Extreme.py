from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

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
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:CC<carrier>]:ESFLatness:EXTReme \n
		Snippet: value: FetchStruct = driver.nrMmwMeas.multiEval.listPy.segment.cc.esFlatness.extreme.fetch(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return equalizer spectrum flatness single value results for segment <no>, for carrier <c>. \n
		Suppressed linked return values: reliability \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:ESFLatness:EXTReme?', self.__class__.FetchStruct())

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
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:CC<carrier>]:ESFLatness:EXTReme \n
		Snippet: value: CalculateStruct = driver.nrMmwMeas.multiEval.listPy.segment.cc.esFlatness.extreme.calculate(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return equalizer spectrum flatness single value results for segment <no>, for carrier <c>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		return self._core.io.query_struct(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:ESFLatness:EXTReme?', self.__class__.CalculateStruct())
