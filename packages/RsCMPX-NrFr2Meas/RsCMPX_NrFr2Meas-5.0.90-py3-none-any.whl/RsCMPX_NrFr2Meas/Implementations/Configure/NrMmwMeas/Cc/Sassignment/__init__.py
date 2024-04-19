from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SassignmentCls:
	"""Sassignment commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sassignment", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def set(self, sc_spacing: enums.ScSpacing, slot_no: float, allocation: int or bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:SASSignment \n
		Snippet: driver.configure.nrMmwMeas.cc.sassignment.set(sc_spacing = enums.ScSpacing.S120k, slot_no = 1.0, allocation = 1, carrierComponent = repcap.CarrierComponent.Default) \n
		Selects the allocation assigned to UL slot <SlotNo>, for carrier <no>, subcarrier spacing <SCSpacing>. \n
			:param sc_spacing: Subcarrier spacing 60 kHz, 120 kHz.
			:param slot_no: No help available
			:param allocation: (integer or boolean) Allocation assigned to the UL slot. For X slots and DL slots, there is no allocation (NAV) . ON | OFF enables or disables the scheduling of the UL slot.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sc_spacing', sc_spacing, DataType.Enum, enums.ScSpacing), ArgSingle('slot_no', slot_no, DataType.Float), ArgSingle('allocation', allocation, DataType.IntegerExt))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:SASSignment {param}'.rstrip())

	def get(self, sc_spacing: enums.ScSpacing, slot_no: float, carrierComponent=repcap.CarrierComponent.Default) -> int or bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:SASSignment \n
		Snippet: value: int or bool = driver.configure.nrMmwMeas.cc.sassignment.get(sc_spacing = enums.ScSpacing.S120k, slot_no = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Selects the allocation assigned to UL slot <SlotNo>, for carrier <no>, subcarrier spacing <SCSpacing>. \n
			:param sc_spacing: Subcarrier spacing 60 kHz, 120 kHz.
			:param slot_no: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: allocation: (integer or boolean) Allocation assigned to the UL slot. For X slots and DL slots, there is no allocation (NAV) . ON | OFF enables or disables the scheduling of the UL slot."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sc_spacing', sc_spacing, DataType.Enum, enums.ScSpacing), ArgSingle('slot_no', slot_no, DataType.Float))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:SASSignment? {param}'.rstrip())
		return Conversions.str_to_int_or_bool(response)

	def clone(self) -> 'SassignmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SassignmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
