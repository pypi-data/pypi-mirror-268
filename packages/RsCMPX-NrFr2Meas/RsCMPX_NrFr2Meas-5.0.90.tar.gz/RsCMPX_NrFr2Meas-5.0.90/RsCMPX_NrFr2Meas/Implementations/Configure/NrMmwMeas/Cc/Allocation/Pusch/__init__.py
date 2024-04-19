from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PuschCls:
	"""Pusch commands group definition. 5 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def additional(self):
		"""additional commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_additional'):
			from .Additional import AdditionalCls
			self._additional = AdditionalCls(self._core, self._cmd_group)
		return self._additional

	@property
	def sgeneration(self):
		"""sgeneration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgeneration'):
			from .Sgeneration import SgenerationCls
			self._sgeneration = SgenerationCls(self._core, self._cmd_group)
		return self._sgeneration

	@property
	def nlayers(self):
		"""nlayers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nlayers'):
			from .Nlayers import NlayersCls
			self._nlayers = NlayersCls(self._core, self._cmd_group)
		return self._nlayers

	# noinspection PyTypeChecker
	class PuschStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Mapping_Type: enums.MappingType: PUSCH mapping type
			- No_Symbols: int: Number of allocated OFDM symbols in each uplink slot. For mapping type A, the minimum value is 4 symbols.
			- Start_Symbol: int: Index of the first allocated symbol in each uplink slot. For mapping type A, only 0 is allowed.
			- No_Rbs: int: Number of allocated UL RBs.
			- Start_Rb: int: Index of the first allocated RB.
			- Mod_Scheme: enums.ModScheme: Modulation scheme π/2-BPSK, QPSK, 16QAM, 64QAM, 256QAM"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mapping_Type', enums.MappingType),
			ArgStruct.scalar_int('No_Symbols'),
			ArgStruct.scalar_int('Start_Symbol'),
			ArgStruct.scalar_int('No_Rbs'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_enum('Mod_Scheme', enums.ModScheme)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mapping_Type: enums.MappingType = None
			self.No_Symbols: int = None
			self.Start_Symbol: int = None
			self.No_Rbs: int = None
			self.Start_Rb: int = None
			self.Mod_Scheme: enums.ModScheme = None

	def set(self, structure: PuschStruct, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh \n
		Snippet with structure: \n
		structure = driver.configure.nrMmwMeas.cc.allocation.pusch.PuschStruct() \n
		structure.Mapping_Type: enums.MappingType = enums.MappingType.A \n
		structure.No_Symbols: int = 1 \n
		structure.Start_Symbol: int = 1 \n
		structure.No_Rbs: int = 1 \n
		structure.Start_Rb: int = 1 \n
		structure.Mod_Scheme: enums.ModScheme = enums.ModScheme.BPSK \n
		driver.configure.nrMmwMeas.cc.allocation.pusch.set(structure, carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies settings related to the PUSCH allocation, for carrier <no>, allocation <a>. The ranges for the allocated RBs
		have dependencies, see 'PUSCH RB allocation'.
			INTRO_CMD_HELP: For Signal Path = Network, use: \n
			- [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:CHMapping
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:UESCheduling:UDEFined:SASSignment:UL:TDOMain:CHMapping
			- [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:SYMBol
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:UESCheduling:UDEFined:SASSignment:UL:TDOMain:SYMBol
			- [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:RB
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:UESCheduling:UDEFined:SASSignment:UL:RB
			- [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:MCS
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:UESCheduling:UDEFined:SASSignment:UL:MCS  \n
			:param structure: for set value, see the help for PuschStruct structure arguments.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUSCh', structure)

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> PuschStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh \n
		Snippet: value: PuschStruct = driver.configure.nrMmwMeas.cc.allocation.pusch.get(carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies settings related to the PUSCH allocation, for carrier <no>, allocation <a>. The ranges for the allocated RBs
		have dependencies, see 'PUSCH RB allocation'.
			INTRO_CMD_HELP: For Signal Path = Network, use: \n
			- [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:CHMapping
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:UESCheduling:UDEFined:SASSignment:UL:TDOMain:CHMapping
			- [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:SYMBol
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:UESCheduling:UDEFined:SASSignment:UL:TDOMain:SYMBol
			- [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:RB
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:UESCheduling:UDEFined:SASSignment:UL:RB
			- [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:MCS
			- [CONFigure:]SIGNaling:NRADio:CELL:BWP<bb>:UESCheduling:UDEFined:SASSignment:UL:MCS  \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for PuschStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUSCh?', self.__class__.PuschStruct())

	def clone(self) -> 'PuschCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PuschCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
