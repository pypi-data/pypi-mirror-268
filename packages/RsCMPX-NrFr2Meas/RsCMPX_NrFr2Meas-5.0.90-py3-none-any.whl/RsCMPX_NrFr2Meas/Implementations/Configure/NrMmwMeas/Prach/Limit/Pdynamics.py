from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdynamicsCls:
	"""Pdynamics commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdynamics", core, parent)

	def set(self, enable: bool, on_power_upper: float, on_power_lower: float, off_power_upper: float) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PDYNamics \n
		Snippet: driver.configure.nrMmwMeas.prach.limit.pdynamics.set(enable = False, on_power_upper = 1.0, on_power_lower = 1.0, off_power_upper = 1.0) \n
		No command help available \n
			:param enable: No help available
			:param on_power_upper: No help available
			:param on_power_lower: No help available
			:param off_power_upper: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('on_power_upper', on_power_upper, DataType.Float), ArgSingle('on_power_lower', on_power_lower, DataType.Float), ArgSingle('off_power_upper', off_power_upper, DataType.Float))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PDYNamics {param}'.rstrip())

	# noinspection PyTypeChecker
	class PdynamicsStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: No parameter help available
			- On_Power_Upper: float: No parameter help available
			- On_Power_Lower: float: No parameter help available
			- Off_Power_Upper: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('On_Power_Upper'),
			ArgStruct.scalar_float('On_Power_Lower'),
			ArgStruct.scalar_float('Off_Power_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.On_Power_Upper: float = None
			self.On_Power_Lower: float = None
			self.Off_Power_Upper: float = None

	def get(self) -> PdynamicsStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PDYNamics \n
		Snippet: value: PdynamicsStruct = driver.configure.nrMmwMeas.prach.limit.pdynamics.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PdynamicsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PDYNamics?', self.__class__.PdynamicsStruct())
