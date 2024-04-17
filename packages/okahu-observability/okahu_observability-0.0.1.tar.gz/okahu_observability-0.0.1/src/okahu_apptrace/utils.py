import logging
import os
from opentelemetry.trace import Tracer, Span

logger = logging.getLogger(__name__)

def _with_tracer_wrapper(func):
    """Helper for providing tracer for wrapper functions."""

    def _with_tracer(tracer, to_wrap):
        def wrapper(wrapped, instance, args, kwargs):
            return func(tracer, to_wrap, wrapped, instance, args, kwargs)

        return wrapper

    return _with_tracer

@_with_tracer_wrapper
def task_wrapper(tracer: Tracer, to_wrap, wrapped, instance, args, kwargs):
    """Instruments and calls every function defined in TO_WRAP."""

    # Some Langchain objects are wrapped elsewhere, so we ignore them here
    if instance.__class__.__name__ in ("AgentExecutor"):
        return wrapped(*args, **kwargs)

    if hasattr(instance, "name") and instance.name:
        name = f"{to_wrap.get('span_name')}.{instance.name.lower()}"
    elif to_wrap.get("span_name"):
        name = to_wrap.get("span_name")
    else:
        name = f"langchain.task.{instance.__class__.__name__}"
    kind = to_wrap.get("kind")
    with tracer.start_as_current_span(name) as span:
        return_value = wrapped(*args, **kwargs)
        if is_root_span(span):
            workflow_name = span.resource.attributes.get("service.name")
            span.set_attribute("workflow_name",workflow_name)

    return return_value

@_with_tracer_wrapper
async def atask_wrapper(tracer, to_wrap, wrapped, instance, args, kwargs):
    """Instruments and calls every function defined in TO_WRAP."""

    # Some Langchain objects are wrapped elsewhere, so we ignore them here
    if instance.__class__.__name__ in ("AgentExecutor"):
        return wrapped(*args, **kwargs)

    if hasattr(instance, "name") and instance.name:
        name = f"{to_wrap.get('span_name')}.{instance.name.lower()}"
    elif to_wrap.get("span_name"):
        name = to_wrap.get("span_name")
    else:
        name = f"langchain.task.{instance.__class__.__name__}"
    kind = to_wrap.get("kind")
    with tracer.start_as_current_span(name) as span:
        return_value = await wrapped(*args, **kwargs)

    return return_value

@_with_tracer_wrapper
async def allm_wrapper(tracer, to_wrap, wrapped, instance, args, kwargs):
    # Some Langchain objects are wrapped elsewhere, so we ignore them here
    if instance.__class__.__name__ in ("AgentExecutor"):
        return wrapped(*args, **kwargs)

    if hasattr(instance, "name") and instance.name:
        name = f"{to_wrap.get('span_name')}.{instance.name.lower()}"
    elif to_wrap.get("span_name"):
        name = to_wrap.get("span_name")
    else:
        name = f"langchain.task.{instance.__class__.__name__}"
    kind = to_wrap.get("kind")
    with tracer.start_as_current_span(name) as span:
        update_llm_endpoint(curr_span= span, instance=instance)
        

        return_value = await wrapped(*args, **kwargs)

    return return_value

@_with_tracer_wrapper
def llm_wrapper(tracer: Tracer, to_wrap, wrapped, instance, args, kwargs):
    
    # Some Langchain objects are wrapped elsewhere, so we ignore them here
    if instance.__class__.__name__ in ("AgentExecutor"):
        return wrapped(*args, **kwargs)

    if hasattr(instance, "name") and instance.name:
        name = f"{to_wrap.get('span_name')}.{instance.name.lower()}"
    elif to_wrap.get("span_name"):
        name = to_wrap.get("span_name")
    else:
        name = f"langchain.task.{instance.__class__.__name__}"
    kind = to_wrap.get("kind")
    with tracer.start_as_current_span(name) as span:
        update_llm_endpoint(curr_span= span, instance=instance)
        

        return_value = wrapped(*args, **kwargs)

    return return_value

def update_llm_endpoint(curr_span: Span, instance):
    triton_llm_endpoint = os.environ.get("TRITON_LLM_ENDPOINT")
    if triton_llm_endpoint is not None and len(triton_llm_endpoint) > 0:
        curr_span.set_attribute("server_url", triton_llm_endpoint)

    if 'model_name' in instance.__dict__:
        model_name = instance.__dict__.get("model_name")
        curr_span.set_attribute("openai_model_name", model_name)

def is_root_span(curr_span: Span) -> bool:
    return curr_span.parent == None

def get_input_from_args(chain_args):
    if len(chain_args) > 0 and type(chain_args[0]) == str:
        return chain_args[0]
    return ""
