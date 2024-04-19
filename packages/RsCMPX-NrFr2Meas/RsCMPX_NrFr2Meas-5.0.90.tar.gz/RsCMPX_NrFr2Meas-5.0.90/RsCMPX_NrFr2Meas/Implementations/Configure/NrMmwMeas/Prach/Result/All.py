from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, modulation: bool, power_dynamics: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult[:ALL] \n
		Snippet: driver.configure.nrMmwMeas.prach.result.all.set(modulation = False, power_dynamics = False) \n
		Enables or disables the evaluation of results in the PRACH measurement.
		This command combines all other CONFigure:NRMMw:MEAS<i>:PRACh:RESult... commands. \n
			:param modulation: OFF: Do not evaluate the results. ON: Evaluate the results.
			:param power_dynamics: OFF: Do not evaluate the results. ON: Evaluate the results.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('modulation', modulation, DataType.Boolean), ArgSingle('power_dynamics', power_dynamics, DataType.Boolean))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Modulation: bool: OFF: Do not evaluate the results. ON: Evaluate the results.
			- Power_Dynamics: bool: OFF: Do not evaluate the results. ON: Evaluate the results."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Modulation'),
			ArgStruct.scalar_bool('Power_Dynamics')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Modulation: bool = None
			self.Power_Dynamics: bool = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.nrMmwMeas.prach.result.all.get() \n
		Enables or disables the evaluation of results in the PRACH measurement.
		This command combines all other CONFigure:NRMMw:MEAS<i>:PRACh:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:ALL?', self.__class__.AllStruct())
