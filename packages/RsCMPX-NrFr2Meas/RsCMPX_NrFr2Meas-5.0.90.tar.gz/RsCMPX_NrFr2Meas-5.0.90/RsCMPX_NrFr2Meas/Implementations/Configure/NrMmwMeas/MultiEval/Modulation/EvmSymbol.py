from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvmSymbolCls:
	"""EvmSymbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evmSymbol", core, parent)

	def set(self, symbol: int, low_high: enums.LowHigh) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EVMSymbol \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.evmSymbol.set(symbol = 1, low_high = enums.LowHigh.HIGH) \n
		Configures the scope of the EVM vs modulation symbol results. \n
			:param symbol: OFDM symbol to be evaluated.
			:param low_high: Low or high EVM window position.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('symbol', symbol, DataType.Integer), ArgSingle('low_high', low_high, DataType.Enum, enums.LowHigh))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EVMSymbol {param}'.rstrip())

	# noinspection PyTypeChecker
	class EvmSymbolStruct(StructBase):
		"""Response structure. Fields: \n
			- Symbol: int: OFDM symbol to be evaluated.
			- Low_High: enums.LowHigh: Low or high EVM window position."""
		__meta_args_list = [
			ArgStruct.scalar_int('Symbol'),
			ArgStruct.scalar_enum('Low_High', enums.LowHigh)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Symbol: int = None
			self.Low_High: enums.LowHigh = None

	def get(self) -> EvmSymbolStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EVMSymbol \n
		Snippet: value: EvmSymbolStruct = driver.configure.nrMmwMeas.multiEval.modulation.evmSymbol.get() \n
		Configures the scope of the EVM vs modulation symbol results. \n
			:return: structure: for return value, see the help for EvmSymbolStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EVMSymbol?', self.__class__.EvmSymbolStruct())
