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
class SgenerationCls:
	"""Sgeneration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sgeneration", core, parent)

	def set(self, initialization: enums.Initialization, dmrs_id: int, nscid: int, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:SGENeration \n
		Snippet: driver.configure.nrMmwMeas.cc.allocation.pusch.sgeneration.set(initialization = enums.Initialization.CID, dmrs_id = 1, nscid = 1, carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Configures the initialization of the DM-RS sequence generation, for carrier <no>, allocation <a>. \n
			:param initialization: CID: cell ID used DMRSid: DMRS ID used
			:param dmrs_id: ID for Initialization = DMRSid.
			:param nscid: Parameter nSCID.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('initialization', initialization, DataType.Enum, enums.Initialization), ArgSingle('dmrs_id', dmrs_id, DataType.Integer), ArgSingle('nscid', nscid, DataType.Integer))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUSCh:SGENeration {param}'.rstrip())

	# noinspection PyTypeChecker
	class SgenerationStruct(StructBase):
		"""Response structure. Fields: \n
			- Initialization: enums.Initialization: CID: cell ID used DMRSid: DMRS ID used
			- Dmrs_Id: int: ID for Initialization = DMRSid.
			- Nscid: int: Parameter nSCID."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Initialization', enums.Initialization),
			ArgStruct.scalar_int('Dmrs_Id'),
			ArgStruct.scalar_int('Nscid')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Initialization: enums.Initialization = None
			self.Dmrs_Id: int = None
			self.Nscid: int = None

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> SgenerationStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:SGENeration \n
		Snippet: value: SgenerationStruct = driver.configure.nrMmwMeas.cc.allocation.pusch.sgeneration.get(carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Configures the initialization of the DM-RS sequence generation, for carrier <no>, allocation <a>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for SgenerationStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUSCh:SGENeration?', self.__class__.SgenerationStruct())
