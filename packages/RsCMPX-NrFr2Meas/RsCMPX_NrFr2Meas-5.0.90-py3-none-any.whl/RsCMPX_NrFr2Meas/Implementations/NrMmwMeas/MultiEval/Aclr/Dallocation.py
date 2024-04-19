from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


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
			- Nr_Res_Blocks: str: No parameter help available
			- Offset_Res_Blocks: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Nr_Res_Blocks'),
			ArgStruct.scalar_str('Offset_Res_Blocks')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nr_Res_Blocks: str = None
			self.Offset_Res_Blocks: str = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:ACLR:DALLocation \n
		Snippet: value: FetchStruct = driver.nrMmwMeas.multiEval.aclr.dallocation.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:ACLR:DALLocation?', self.__class__.FetchStruct())
