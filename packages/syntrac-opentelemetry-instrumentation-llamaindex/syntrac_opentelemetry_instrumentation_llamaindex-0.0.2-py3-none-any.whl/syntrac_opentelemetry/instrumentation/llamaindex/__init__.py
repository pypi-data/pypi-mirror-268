"""OpenTelemetry LlamaIndex instrumentation"""

import logging
from typing import Collection

from opentelemetry.trace import get_tracer

from opentelemetry.instrumentation.instrumentor import BaseInstrumentor

from syntrac_opentelemetry.instrumentation.llamaindex.base_agent_instrumentor import (
    BaseAgentInstrumentor,
)
from syntrac_opentelemetry.instrumentation.llamaindex.retriever_query_engine_instrumentor import (
    RetrieverQueryEngineInstrumentor,
)
from syntrac_opentelemetry.instrumentation.llamaindex.base_retriever_instrumentor import (
    BaseRetrieverInstrumentor,
)
from syntrac_opentelemetry.instrumentation.llamaindex.base_synthesizer_instrumentor import (
    BaseSynthesizerInstrumentor,
)
from syntrac_opentelemetry.instrumentation.llamaindex.base_tool_instrumentor import (
    BaseToolInstrumentor,
)
from syntrac_opentelemetry.instrumentation.llamaindex.base_embedding_instrumentor import (
    BaseEmbeddingInstrumentor,
)
from syntrac_opentelemetry.instrumentation.llamaindex.custom_llm_instrumentor import (
    CustomLLMInstrumentor,
)
from syntrac_opentelemetry.instrumentation.llamaindex.query_pipeline_instrumentor import (
    QueryPipelineInstrumentor,
)
from syntrac_opentelemetry.instrumentation.llamaindex.version import __version__

logger = logging.getLogger(__name__)

_instruments = ("llama-index >= 0.7.0",)


class LlamaIndexInstrumentor(BaseInstrumentor):
    """An instrumentor for LlamaIndex SDK."""

    def instrumentation_dependencies(self) -> Collection[str]:
        return _instruments

    def _instrument(self, **kwargs):
        tracer_provider = kwargs.get("tracer_provider")
        tracer = get_tracer(__name__, __version__, tracer_provider)

        RetrieverQueryEngineInstrumentor(tracer).instrument()
        BaseRetrieverInstrumentor(tracer).instrument()
        BaseSynthesizerInstrumentor(tracer).instrument()
        BaseEmbeddingInstrumentor(tracer).instrument()
        CustomLLMInstrumentor(tracer).instrument()
        QueryPipelineInstrumentor(tracer).instrument()
        BaseAgentInstrumentor(tracer).instrument()
        BaseToolInstrumentor(tracer).instrument()

    def _uninstrument(self, **kwargs):
        pass
