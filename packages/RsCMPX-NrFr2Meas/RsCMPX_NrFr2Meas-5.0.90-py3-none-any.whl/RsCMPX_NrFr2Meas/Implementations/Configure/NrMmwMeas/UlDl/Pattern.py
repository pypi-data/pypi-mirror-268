from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PatternCls:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, sc_spacing: enums.ScSpacing, dl_slots: int, dl_symbols: int, ul_slots: int, ul_symbols: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:ULDL:PATTern \n
		Snippet: driver.configure.nrMmwMeas.ulDl.pattern.set(sc_spacing = enums.ScSpacing.S120k, dl_slots = 1, dl_symbols = 1, ul_slots = 1, ul_symbols = 1) \n
		Configures the UL-DL pattern for the <SCSpacing>. The ranges have dependencies, see 'TDD UL-DL configuration'.
			INTRO_CMD_HELP: For Signal Path = Network, use: \n
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:DL:NSLots
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:DL:FSSYmbol
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:UL:NSLots
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:UL:FSSYmbol  \n
			:param sc_spacing: Subcarrier spacing for which the other settings apply.
			:param dl_slots: Specifies 'nrofDownlinkSlots'.
			:param dl_symbols: Specifies 'nrofDownlinkSymbols'.
			:param ul_slots: Specifies 'nrofUplinkSlots'.
			:param ul_symbols: Specifies 'nrofUplinkSymbols'.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sc_spacing', sc_spacing, DataType.Enum, enums.ScSpacing), ArgSingle('dl_slots', dl_slots, DataType.Integer), ArgSingle('dl_symbols', dl_symbols, DataType.Integer), ArgSingle('ul_slots', ul_slots, DataType.Integer), ArgSingle('ul_symbols', ul_symbols, DataType.Integer))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:ULDL:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Dl_Slots: int: Specifies 'nrofDownlinkSlots'.
			- Dl_Symbols: int: Specifies 'nrofDownlinkSymbols'.
			- Ul_Slots: int: Specifies 'nrofUplinkSlots'.
			- Ul_Symbols: int: Specifies 'nrofUplinkSymbols'."""
		__meta_args_list = [
			ArgStruct.scalar_int('Dl_Slots'),
			ArgStruct.scalar_int('Dl_Symbols'),
			ArgStruct.scalar_int('Ul_Slots'),
			ArgStruct.scalar_int('Ul_Symbols')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dl_Slots: int = None
			self.Dl_Symbols: int = None
			self.Ul_Slots: int = None
			self.Ul_Symbols: int = None

	def get(self, sc_spacing: enums.ScSpacing) -> GetStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:ULDL:PATTern \n
		Snippet: value: GetStruct = driver.configure.nrMmwMeas.ulDl.pattern.get(sc_spacing = enums.ScSpacing.S120k) \n
		Configures the UL-DL pattern for the <SCSpacing>. The ranges have dependencies, see 'TDD UL-DL configuration'.
			INTRO_CMD_HELP: For Signal Path = Network, use: \n
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:DL:NSLots
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:DL:FSSYmbol
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:UL:NSLots
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:UL:FSSYmbol  \n
			:param sc_spacing: Subcarrier spacing for which the other settings apply.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(sc_spacing, enums.ScSpacing)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:ULDL:PATTern? {param}', self.__class__.GetStruct())
