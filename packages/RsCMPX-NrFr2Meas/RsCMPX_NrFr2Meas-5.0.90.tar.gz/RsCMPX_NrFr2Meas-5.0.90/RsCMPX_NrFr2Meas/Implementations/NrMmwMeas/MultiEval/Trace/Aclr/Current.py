from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Nr_Neg: float: Power in the adjacent NR channel with lower frequency
			- Carrier: float: Power in the allocated NR channel
			- Nr_Pos: float: Power in the adjacent NR channel with higher frequency"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Nr_Neg'),
			ArgStruct.scalar_float('Carrier'),
			ArgStruct.scalar_float('Nr_Pos')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nr_Neg: float = None
			self.Carrier: float = None
			self.Nr_Pos: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:MEValuation:TRACe:ACLR:CURRent \n
		Snippet: value: ResultData = driver.nrMmwMeas.multiEval.trace.aclr.current.read() \n
		Returns the absolute powers as displayed in the ACLR diagram. The current and average values can be retrieved. See also
		'Square Spectrum ACLR'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NRMMw:MEASurement<Instance>:MEValuation:TRACe:ACLR:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:TRACe:ACLR:CURRent \n
		Snippet: value: ResultData = driver.nrMmwMeas.multiEval.trace.aclr.current.fetch() \n
		Returns the absolute powers as displayed in the ACLR diagram. The current and average values can be retrieved. See also
		'Square Spectrum ACLR'. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:TRACe:ACLR:CURRent?', self.__class__.ResultData())
