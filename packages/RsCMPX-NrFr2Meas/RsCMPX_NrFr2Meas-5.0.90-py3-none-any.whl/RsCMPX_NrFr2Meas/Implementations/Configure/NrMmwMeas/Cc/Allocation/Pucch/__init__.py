from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PucchCls:
	"""Pucch commands group definition. 12 total commands, 8 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def isfHopping(self):
		"""isfHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isfHopping'):
			from .IsfHopping import IsfHoppingCls
			self._isfHopping = IsfHoppingCls(self._core, self._cmd_group)
		return self._isfHopping

	@property
	def shPrb(self):
		"""shPrb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shPrb'):
			from .ShPrb import ShPrbCls
			self._shPrb = ShPrbCls(self._core, self._cmd_group)
		return self._shPrb

	@property
	def ghopping(self):
		"""ghopping commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ghopping'):
			from .Ghopping import GhoppingCls
			self._ghopping = GhoppingCls(self._core, self._cmd_group)
		return self._ghopping

	@property
	def icShift(self):
		"""icShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icShift'):
			from .IcShift import IcShiftCls
			self._icShift = IcShiftCls(self._core, self._cmd_group)
		return self._icShift

	@property
	def tdoIndex(self):
		"""tdoIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdoIndex'):
			from .TdoIndex import TdoIndexCls
			self._tdoIndex = TdoIndexCls(self._core, self._cmd_group)
		return self._tdoIndex

	@property
	def dmrs(self):
		"""dmrs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Dmrs import DmrsCls
			self._dmrs = DmrsCls(self._core, self._cmd_group)
		return self._dmrs

	@property
	def occ(self):
		"""occ commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_occ'):
			from .Occ import OccCls
			self._occ = OccCls(self._core, self._cmd_group)
		return self._occ

	def set(self, pucch_format: enums.PucchFormat, no_symbols: int, start_symbol: int, no_rbs: int, start_rb: int, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh \n
		Snippet: driver.configure.nrMmwMeas.cc.allocation.pucch.set(pucch_format = enums.PucchFormat.F0, no_symbols = 1, start_symbol = 1, no_rbs = 1, start_rb = 1, carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies settings related to the PUCCH allocation, for carrier <no>, allocation <a>.
			INTRO_CMD_HELP: For Signal Path = Network, use: \n
			- [CONFigure:]SIGNaling:NRADio:CELL:PUCCh:FORMat
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:PUCCh:FORMat
			- [CONFigure:]SIGNaling:NRADio:CELL:PUCCh:SPRB
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:PUCCh:SPRB  \n
			:param pucch_format: PUCCH format
			:param no_symbols: Number of allocated OFDM symbols in each uplink slot.
			:param start_symbol: Index of the first allocated symbol in each uplink slot.
			:param no_rbs: Number of allocated UL RBs.
			:param start_rb: Index of the first allocated RB.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('pucch_format', pucch_format, DataType.Enum, enums.PucchFormat), ArgSingle('no_symbols', no_symbols, DataType.Integer), ArgSingle('start_symbol', start_symbol, DataType.Integer), ArgSingle('no_rbs', no_rbs, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUCCh {param}'.rstrip())

	# noinspection PyTypeChecker
	class PucchStruct(StructBase):
		"""Response structure. Fields: \n
			- Pucch_Format: enums.PucchFormat: PUCCH format
			- No_Symbols: int: Number of allocated OFDM symbols in each uplink slot.
			- Start_Symbol: int: Index of the first allocated symbol in each uplink slot.
			- No_Rbs: int: Number of allocated UL RBs.
			- Start_Rb: int: Index of the first allocated RB."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Pucch_Format', enums.PucchFormat),
			ArgStruct.scalar_int('No_Symbols'),
			ArgStruct.scalar_int('Start_Symbol'),
			ArgStruct.scalar_int('No_Rbs'),
			ArgStruct.scalar_int('Start_Rb')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pucch_Format: enums.PucchFormat = None
			self.No_Symbols: int = None
			self.Start_Symbol: int = None
			self.No_Rbs: int = None
			self.Start_Rb: int = None

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> PucchStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh \n
		Snippet: value: PucchStruct = driver.configure.nrMmwMeas.cc.allocation.pucch.get(carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies settings related to the PUCCH allocation, for carrier <no>, allocation <a>.
			INTRO_CMD_HELP: For Signal Path = Network, use: \n
			- [CONFigure:]SIGNaling:NRADio:CELL:PUCCh:FORMat
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:PUCCh:FORMat
			- [CONFigure:]SIGNaling:NRADio:CELL:PUCCh:SPRB
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:PUCCh:SPRB  \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for PucchStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUCCh?', self.__class__.PucchStruct())

	def clone(self) -> 'PucchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PucchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
