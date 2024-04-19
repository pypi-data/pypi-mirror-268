from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PuschCls:
	"""Pusch commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

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

	# noinspection PyTypeChecker
	class PuschStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Mapping_Type: enums.MappingType: PUSCH mapping type
			- No_Symbols: int: Number of allocated OFDM symbols in each uplink slot.
			- Start_Symbol: int: Index of the first allocated OFDM symbol in each uplink slot. For mapping type A, only 0 is allowed.
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

	def set(self, structure: PuschStruct, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<carrier>]:ALLocation<Allocation>:PUSCh \n
		Snippet with structure: \n
		structure = driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.PuschStruct() \n
		structure.Mapping_Type: enums.MappingType = enums.MappingType.A \n
		structure.No_Symbols: int = 1 \n
		structure.Start_Symbol: int = 1 \n
		structure.No_Rbs: int = 1 \n
		structure.Start_Rb: int = 1 \n
		structure.Mod_Scheme: enums.ModScheme = enums.ModScheme.BPSK \n
		driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.set(structure, sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default, allocation = repcap.Allocation.Default) \n
		Specifies settings related to the PUSCH allocation, for carrier <c>, allocation <a> in segment <no>. The ranges for the
		allocated RBs have dependencies, see 'Resource elements, grids and blocks'. \n
			:param structure: for set value, see the help for PuschStruct structure arguments.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh', structure)

	def get(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default, allocation=repcap.Allocation.Default) -> PuschStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<carrier>]:ALLocation<Allocation>:PUSCh \n
		Snippet: value: PuschStruct = driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.get(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default, allocation = repcap.Allocation.Default) \n
		Specifies settings related to the PUSCH allocation, for carrier <c>, allocation <a> in segment <no>. The ranges for the
		allocated RBs have dependencies, see 'Resource elements, grids and blocks'. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for PuschStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh?', self.__class__.PuschStruct())

	def clone(self) -> 'PuschCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PuschCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
