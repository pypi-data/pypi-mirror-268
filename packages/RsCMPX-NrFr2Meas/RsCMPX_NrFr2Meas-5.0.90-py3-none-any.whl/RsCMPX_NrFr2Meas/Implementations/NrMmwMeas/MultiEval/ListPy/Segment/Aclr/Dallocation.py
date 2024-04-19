from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DallocationCls:
	"""Dallocation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dallocation", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Seg_Reliability: str: No parameter help available
			- Nr_Res_Blocks: int: No parameter help available
			- Offset_Res_Blocks: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Seg_Reliability'),
			ArgStruct.scalar_int('Nr_Res_Blocks'),
			ArgStruct.scalar_str('Offset_Res_Blocks')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: str = None
			self.Nr_Res_Blocks: int = None
			self.Offset_Res_Blocks: str = None

	def fetch(self, sEGMent=repcap.SEGMent.Default) -> FetchStruct:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:ACLR:DALLocation \n
		Snippet: value: FetchStruct = driver.nrMmwMeas.multiEval.listPy.segment.aclr.dallocation.fetch(sEGMent = repcap.SEGMent.Default) \n
		No command help available \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:ACLR:DALLocation?', self.__class__.FetchStruct())
