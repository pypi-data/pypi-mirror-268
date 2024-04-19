from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InitCls:
	"""Init commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("init", core, parent)

	def set(self, initialization: enums.GhopingInit, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:GHOPping:INIT \n
		Snippet: driver.configure.nrMmwMeas.cc.allocation.pucch.ghopping.init.set(initialization = enums.GhopingInit.CID, carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies the type of ID used to initialize group hopping and sequence hopping, for carrier <no>, allocation <a>. \n
			:param initialization: Cell ID or hopping ID
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = Conversions.enum_scalar_to_str(initialization, enums.GhopingInit)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUCCh:GHOPping:INIT {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocationMore=repcap.AllocationMore.Default) -> enums.GhopingInit:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:GHOPping:INIT \n
		Snippet: value: enums.GhopingInit = driver.configure.nrMmwMeas.cc.allocation.pucch.ghopping.init.get(carrierComponent = repcap.CarrierComponent.Default, allocationMore = repcap.AllocationMore.Default) \n
		Specifies the type of ID used to initialize group hopping and sequence hopping, for carrier <no>, allocation <a>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocationMore: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: initialization: Cell ID or hopping ID"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocationMore_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationMore, repcap.AllocationMore)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocationMore_cmd_val}:PUCCh:GHOPping:INIT?')
		return Conversions.str_to_scalar_enum(response, enums.GhopingInit)
