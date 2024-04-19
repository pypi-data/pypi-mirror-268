from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AtToleranceCls:
	"""AtTolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atTolerance", core, parent)

	def set(self, tol_2330: float, tol_3040: float) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:ACLR:ATTolerance \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.aclr.atTolerance.set(tol_2330 = 1.0, tol_3040 = 1.0) \n
		Defines the test tolerance for relative ACLR limits, depending on the carrier frequency. \n
			:param tol_2330: Test tolerance for carrier frequencies ≥ 23.45 GHz and ≤ 30.3 GHz
			:param tol_3040: Test tolerance for carrier frequencies 30.3 GHz and ≤ 40.8 GHz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tol_2330', tol_2330, DataType.Float), ArgSingle('tol_3040', tol_3040, DataType.Float))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:ACLR:ATTolerance {param}'.rstrip())

	# noinspection PyTypeChecker
	class AtToleranceStruct(StructBase):
		"""Response structure. Fields: \n
			- Tol_2330: float: Test tolerance for carrier frequencies ≥ 23.45 GHz and ≤ 30.3 GHz
			- Tol_3040: float: Test tolerance for carrier frequencies 30.3 GHz and ≤ 40.8 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Tol_2330'),
			ArgStruct.scalar_float('Tol_3040')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tol_2330: float = None
			self.Tol_3040: float = None

	def get(self) -> AtToleranceStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:ACLR:ATTolerance \n
		Snippet: value: AtToleranceStruct = driver.configure.nrMmwMeas.multiEval.limit.aclr.atTolerance.get() \n
		Defines the test tolerance for relative ACLR limits, depending on the carrier frequency. \n
			:return: structure: for return value, see the help for AtToleranceStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:ACLR:ATTolerance?', self.__class__.AtToleranceStruct())
