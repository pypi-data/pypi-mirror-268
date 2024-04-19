from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OccCls:
	"""Occ commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("occ", core, parent)

	def set(self, length: int, index: int, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:OCC \n
		Snippet: driver.configure.nrMmwMeas.cc.allocation.pucch.occ.set(length = 1, index = 1, carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies the OCC length and index for PUCCH format F4, for carrier <no>, allocation <a>. \n
			:param length: OCC length
			:param index: OCC index
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('length', length, DataType.Integer), ArgSingle('index', index, DataType.Integer))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUCCh:OCC {param}'.rstrip())

	# noinspection PyTypeChecker
	class OccStruct(StructBase):
		"""Response structure. Fields: \n
			- Length: int: OCC length
			- Index: int: OCC index"""
		__meta_args_list = [
			ArgStruct.scalar_int('Length'),
			ArgStruct.scalar_int('Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length: int = None
			self.Index: int = None

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> OccStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:OCC \n
		Snippet: value: OccStruct = driver.configure.nrMmwMeas.cc.allocation.pucch.occ.get(carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies the OCC length and index for PUCCH format F4, for carrier <no>, allocation <a>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for OccStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUCCh:OCC?', self.__class__.OccStruct())
