from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DchTypeCls:
	"""DchType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dchType", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: int: No parameter help available
			- Channel_Type: enums.ChannelTypeA: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_enum('Channel_Type', enums.ChannelTypeA)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Channel_Type: enums.ChannelTypeA = None

	def fetch(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> FetchStruct:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:CC<carrier>]:MODulation:DCHType \n
		Snippet: value: FetchStruct = driver.nrMmwMeas.multiEval.listPy.segment.cc.modulation.dchType.fetch(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		No command help available \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:MODulation:DCHType?', self.__class__.FetchStruct())
