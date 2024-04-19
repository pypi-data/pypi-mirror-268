from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbIndexCls:
	"""RbIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbIndex", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment
			- Statist_Expired: int: Reached statistical length in slots
			- Out_Of_Tolerance: int: Percentage of measured subframes with failed limit check
			- General: int: Resource block index for the general margin (at non-allocated RBs)
			- Iq_Image: int: Resource block index for the I/Q image margin (at image frequencies of allocated RBs)
			- Carr_Leakage: int: Resource block index for the carrier leakage margin (at carrier frequency)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_int('General'),
			ArgStruct.scalar_int('Iq_Image'),
			ArgStruct.scalar_int('Carr_Leakage')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
			self.Out_Of_Tolerance: int = None
			self.General: int = None
			self.Iq_Image: int = None
			self.Carr_Leakage: int = None

	def fetch(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> FetchStruct:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:CC<carrier>]:IEMission:MARGin:EXTReme:RBINdex \n
		Snippet: value: FetchStruct = driver.nrMmwMeas.multiEval.listPy.segment.cc.iemission.margin.extreme.rbIndex.fetch(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return resource block indices of the in-band emission measurement for segment <no>, for carrier <c>. At these RB indices,
		the CURRent, AVERage and EXTReme margins have been detected. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:IEMission:MARGin:EXTReme:RBINdex?', self.__class__.FetchStruct())
