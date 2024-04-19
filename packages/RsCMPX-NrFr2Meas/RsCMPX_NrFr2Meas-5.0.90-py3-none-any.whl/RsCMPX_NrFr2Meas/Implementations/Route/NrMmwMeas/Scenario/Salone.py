from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SaloneCls:
	"""Salone commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("salone", core, parent)

	def set(self, rx_connector: enums.RxConnector, rf_converter: enums.RfConverter) -> None:
		"""SCPI: ROUTe:NRMMw:MEASurement<Instance>:SCENario:SALone \n
		Snippet: driver.route.nrMmwMeas.scenario.salone.set(rx_connector = enums.RxConnector.I11I, rf_converter = enums.RfConverter.IRX1) \n
		No command help available \n
			:param rx_connector: No help available
			:param rf_converter: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rx_connector', rx_connector, DataType.Enum, enums.RxConnector), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.RfConverter))
		self._core.io.write(f'ROUTe:NRMMw:MEASurement<Instance>:SCENario:SALone {param}'.rstrip())

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Response structure. Fields: \n
			- Rx_Connector: enums.RxConnector: No parameter help available
			- Rf_Converter: enums.RfConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RfConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rf_Converter: enums.RfConverter = None

	def get(self) -> SaloneStruct:
		"""SCPI: ROUTe:NRMMw:MEASurement<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.nrMmwMeas.scenario.salone.get() \n
		No command help available \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments."""
		return self._core.io.query_struct(f'ROUTe:NRMMw:MEASurement<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())
