from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, sc_spacing: enums.ScSpacing, allocation: List[int or bool], carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:SASSignment:ALL \n
		Snippet: driver.configure.nrMmwMeas.cc.sassignment.all.set(sc_spacing = enums.ScSpacing.S120k, allocation = [1, True, 2, False, 3], carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param sc_spacing: No help available
			:param allocation: (integer or boolean items) No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sc_spacing', sc_spacing, DataType.Enum, enums.ScSpacing), ArgSingle.as_open_list('allocation', allocation, DataType.IntegerExtList, None))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:SASSignment:ALL {param}'.rstrip())

	def get(self, sc_spacing: enums.ScSpacing, carrierComponent=repcap.CarrierComponent.Default) -> List[int or bool]:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:SASSignment:ALL \n
		Snippet: value: List[int or bool] = driver.configure.nrMmwMeas.cc.sassignment.all.get(sc_spacing = enums.ScSpacing.S120k, carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param sc_spacing: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: allocation: (integer or boolean items) No help available"""
		param = Conversions.enum_scalar_to_str(sc_spacing, enums.ScSpacing)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:SASSignment:ALL? {param}')
		return Conversions.str_to_int_or_bool_list(response)
