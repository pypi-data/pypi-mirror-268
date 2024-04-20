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

	def set(self, initialization: enums.Generator, dmrs_id: int, nscid: int, carrierComponent=repcap.CarrierComponent.Nr1, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:SGENeration \n
		Snippet: driver.configure.nrSubMeas.cc.allocation.pusch.sgeneration.set(initialization = enums.Generator.DID, dmrs_id = 1, nscid = 1, carrierComponent = repcap.CarrierComponent.Nr1, allocation = repcap.Allocation.Default) \n
		Configures the initialization of the DM-RS sequence generation, for carrier <no>, allocation <a>. \n
			:param initialization: PHY: physical cell ID used DID: DMRS ID used
			:param dmrs_id: ID for Initialization = DID.
			:param nscid: Parameter nSCID.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('initialization', initialization, DataType.Enum, enums.Generator), ArgSingle('dmrs_id', dmrs_id, DataType.Integer), ArgSingle('nscid', nscid, DataType.Integer))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:SGENeration {param}'.rstrip())

	# noinspection PyTypeChecker
	class SgenerationStruct(StructBase):
		"""Response structure. Fields: \n
			- Initialization: enums.Generator: PHY: physical cell ID used DID: DMRS ID used
			- Dmrs_Id: int: ID for Initialization = DID.
			- Nscid: int: Parameter nSCID."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Initialization', enums.Generator),
			ArgStruct.scalar_int('Dmrs_Id'),
			ArgStruct.scalar_int('Nscid')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Initialization: enums.Generator = None
			self.Dmrs_Id: int = None
			self.Nscid: int = None

	def get(self, carrierComponent=repcap.CarrierComponent.Nr1, allocation=repcap.Allocation.Default) -> SgenerationStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:SGENeration \n
		Snippet: value: SgenerationStruct = driver.configure.nrSubMeas.cc.allocation.pusch.sgeneration.get(carrierComponent = repcap.CarrierComponent.Nr1, allocation = repcap.Allocation.Default) \n
		Configures the initialization of the DM-RS sequence generation, for carrier <no>, allocation <a>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for SgenerationStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:SGENeration?', self.__class__.SgenerationStruct())
