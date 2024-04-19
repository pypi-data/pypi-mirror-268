from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Nr_Neg: float: ACLR for the adjacent NR channel with lower frequency
			- Carrier: float: Power in the allocated NR channel
			- Nr_Pos: float: ACLR for the adjacent NR channel with higher frequency
			- Antenna_1_Carrier: float: Power in the allocated NR channel, at RX antenna 1
			- Antenna_2_Carrier: float: Power in the allocated NR channel, at RX antenna 2"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Nr_Neg'),
			ArgStruct.scalar_float('Carrier'),
			ArgStruct.scalar_float('Nr_Pos'),
			ArgStruct.scalar_float('Antenna_1_Carrier'),
			ArgStruct.scalar_float('Antenna_2_Carrier')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nr_Neg: float = None
			self.Carrier: float = None
			self.Nr_Pos: float = None
			self.Antenna_1_Carrier: float = None
			self.Antenna_2_Carrier: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:MEValuation:ACLR:CURRent \n
		Snippet: value: ResultData = driver.nrMmwMeas.multiEval.aclr.current.read() \n
		Returns the relative ACLR values as displayed in the table below the ACLR diagram. The current and average values can be
		retrieved. See also 'Square Spectrum ACLR'. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NRMMw:MEASurement<Instance>:MEValuation:ACLR:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:ACLR:CURRent \n
		Snippet: value: ResultData = driver.nrMmwMeas.multiEval.aclr.current.fetch() \n
		Returns the relative ACLR values as displayed in the table below the ACLR diagram. The current and average values can be
		retrieved. See also 'Square Spectrum ACLR'. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:ACLR:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Nr_Neg: enums.ResultStatus2: ACLR for the adjacent NR channel with lower frequency
			- Carrier: enums.ResultStatus2: Power in the allocated NR channel
			- Nr_Pos: enums.ResultStatus2: ACLR for the adjacent NR channel with higher frequency
			- Antenna_1_Carrier: enums.ResultStatus2: Power in the allocated NR channel, at RX antenna 1
			- Antenna_2_Carrier: enums.ResultStatus2: Power in the allocated NR channel, at RX antenna 2"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Nr_Neg', enums.ResultStatus2),
			ArgStruct.scalar_enum('Carrier', enums.ResultStatus2),
			ArgStruct.scalar_enum('Nr_Pos', enums.ResultStatus2),
			ArgStruct.scalar_enum('Antenna_1_Carrier', enums.ResultStatus2),
			ArgStruct.scalar_enum('Antenna_2_Carrier', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nr_Neg: enums.ResultStatus2 = None
			self.Carrier: enums.ResultStatus2 = None
			self.Nr_Pos: enums.ResultStatus2 = None
			self.Antenna_1_Carrier: enums.ResultStatus2 = None
			self.Antenna_2_Carrier: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation:ACLR:CURRent \n
		Snippet: value: CalculateStruct = driver.nrMmwMeas.multiEval.aclr.current.calculate() \n
		Returns the relative ACLR values as displayed in the table below the ACLR diagram. The current and average values can be
		retrieved. See also 'Square Spectrum ACLR'. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:ACLR:CURRent?', self.__class__.CalculateStruct())
