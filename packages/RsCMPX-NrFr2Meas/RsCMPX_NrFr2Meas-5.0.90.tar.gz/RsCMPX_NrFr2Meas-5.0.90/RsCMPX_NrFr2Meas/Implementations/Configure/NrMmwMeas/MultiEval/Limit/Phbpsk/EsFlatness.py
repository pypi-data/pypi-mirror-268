from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsFlatnessCls:
	"""EsFlatness commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("esFlatness", core, parent)

	def set(self, enable: bool, range_1: float, range_2: float, max_1_min_2: float, max_2_min_1: float) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:PHBPsk:ESFLatness \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.phbpsk.esFlatness.set(enable = False, range_1 = 1.0, range_2 = 1.0, max_1_min_2 = 1.0, max_2_min_1 = 1.0) \n
		Defines limits for the equalizer spectrum flatness (π/2-BPSK modulation) . \n
			:param enable: OFF: disables the limit check ON: enables the limit check
			:param range_1: Upper limit for max(range 1) - min(range 1)
			:param range_2: Upper limit for max(range 2) - min(range 2)
			:param max_1_min_2: Upper limit for max(range 1) - min(range 2)
			:param max_2_min_1: Upper limit for max(range 2) - min(range 1)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('range_1', range_1, DataType.Float), ArgSingle('range_2', range_2, DataType.Float), ArgSingle('max_1_min_2', max_1_min_2, DataType.Float), ArgSingle('max_2_min_1', max_2_min_1, DataType.Float))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:PHBPsk:ESFLatness {param}'.rstrip())

	# noinspection PyTypeChecker
	class EsFlatnessStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Range_1: float: Upper limit for max(range 1) - min(range 1)
			- Range_2: float: Upper limit for max(range 2) - min(range 2)
			- Max_1_Min_2: float: Upper limit for max(range 1) - min(range 2)
			- Max_2_Min_1: float: Upper limit for max(range 2) - min(range 1)"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Range_1'),
			ArgStruct.scalar_float('Range_2'),
			ArgStruct.scalar_float('Max_1_Min_2'),
			ArgStruct.scalar_float('Max_2_Min_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Range_1: float = None
			self.Range_2: float = None
			self.Max_1_Min_2: float = None
			self.Max_2_Min_1: float = None

	def get(self) -> EsFlatnessStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:PHBPsk:ESFLatness \n
		Snippet: value: EsFlatnessStruct = driver.configure.nrMmwMeas.multiEval.limit.phbpsk.esFlatness.get() \n
		Defines limits for the equalizer spectrum flatness (π/2-BPSK modulation) . \n
			:return: structure: for return value, see the help for EsFlatnessStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:PHBPsk:ESFLatness?', self.__class__.EsFlatnessStruct())
