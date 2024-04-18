from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PerrorCls:
	"""Perror commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("perror", core, parent)

	def fetch(self, xvalue: int or bool, trace_select: enums.TraceSelect) -> float:
		"""SCPI: FETCh:LTE:MEASurement<Instance>:MEValuation:REFMarker:PERRor \n
		Snippet: value: float = driver.multiEval.referenceMarker.perror.fetch(xvalue = 1, trace_select = enums.TraceSelect.AVERage) \n
		Uses the reference marker on the bar graphs: EVM RMS, EVM peak, magnitude error and phase error vs SC-FDMA symbol. \n
		Use RsCmwLteMeas.reliability.last_value to read the updated reliability indicator. \n
			:param xvalue: (integer or boolean) integer Absolute X value of the marker position There are two X values per SC-FDMA symbol on the X axis (symbol 0 low, symbol 0 high, ..., symbol 6 low, symbol 6 high) . Range: 0 to 13
			:param trace_select: CURRent | AVERage | MAXimum
			:return: yvalue: float Absolute Y value of the marker position"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xvalue', xvalue, DataType.IntegerExt), ArgSingle('trace_select', trace_select, DataType.Enum, enums.TraceSelect))
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:LTE:MEASurement<Instance>:MEValuation:REFMarker:PERRor? {param}'.rstrip(), suppressed)
		return Conversions.str_to_float(response)
