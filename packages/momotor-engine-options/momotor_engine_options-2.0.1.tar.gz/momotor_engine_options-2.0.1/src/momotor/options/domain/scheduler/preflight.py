from __future__ import annotations

import collections
import json
import logging
import typing
import warnings

from typing_extensions import TypeAlias  # Py 3.10+

from momotor.bundles import ResultsBundle
from momotor.bundles.elements.properties import Property
from momotor.bundles.elements.result import Result, Outcome
from momotor.options.doc import annotate_docstring
from momotor.options.option import OptionDefinition, OptionNameDomain
from momotor.options.parser.modifier import parse_mod
from momotor.options.parser.placeholders import replace_placeholders
from momotor.options.parser.selector import match_by_selector, parse_selector
from momotor.options.parser.tasks import replace_task_placeholder
from momotor.options.providers import Providers
from ._domain import DOMAIN

logger = logging.getLogger(__package__)


SCHEDULER_PREFLIGHT_OPTION_NAME = OptionNameDomain('preflight', DOMAIN)

ACTION_SEPARATOR = '=>'

DEFAULT_PREFLIGHT_SELECTOR = '%any error'
DEFAULT_PREFLIGHT_ACTION = 'skip-error'
DEFAULT_PREFLIGHT_OPTION = f'{DEFAULT_PREFLIGHT_SELECTOR} {ACTION_SEPARATOR} {DEFAULT_PREFLIGHT_ACTION}'

#: The :momotor:option:`preflight@scheduler` option allows recipes to indicate situations in which the
#: checklet does not have to be executed.
PREFLIGHT_OPTION = OptionDefinition(
    name=SCHEDULER_PREFLIGHT_OPTION_NAME,
    type='string',
    doc=f"""\
        A preflight check handled by the scheduler. This allows recipes to indicate situations in which the
        checklet does not have to be executed.
        
        The expected format for the option value is: 
        
        .. productionlist:: preflight-option
           preflight_option: [ `~selector:selector` ] "{ACTION_SEPARATOR}" [ `preflight_status` | `preflight_props` ]
           preflight_status: text status message
           preflight_props: "{{" `prop` ":" `value` ( "," `prop` ":" `value` )* "}}"
           action: "run" | "pass" | "pass-secret" | "pass-hidden" 
                 : | "fail" | "fail-secret" | "fail-hidden" | "skip" 
                 : | "error" | "skip-error"
        
        If a :ref:`selector <selector>` matches or is empty, a results bundle based on the action and status message 
        is created (unless the action is :token:`run <preflight-option:action>`). 
        If no selectors match, or a selector matches with action :token:`run <preflight-option:action>`, 
        no result is created and the step should execute as normal.
                         
        Possible values for :token:`~preflight-option:action` are:
        
        * :token:`run <preflight-option:action>`: runs the checklet. When a :token:`run <preflight-option:action>` 
          action is encountered, no further preflight options are processed.
        * :token:`pass <preflight-option:action>`, :token:`pass-secret <preflight-option:action>`, and 
          :token:`pass-hidden <preflight-option:action>`: will return a `pass` outcome without running the checklet.
        * :token:`fail <preflight-option:action>`, :token:`fail-secret <preflight-option:action>`, and 
          :token:`fail-hidden <preflight-option:action>`: will return a `fail` outcome without running the checklet.
        * :token:`skip <preflight-option:action>` and :token:`skip-error <preflight-option:action>`: will return a 
          `skip` outcome without running the checklet.
        * :token:`error <preflight-option:action>`: will return an `error` outcome without running the checklet.
        
        If a result is created, the properties will contain a `preflight-trigger` property with the selector
        that triggered the action, a `source` property with the name of this module. If `status` is provided
        and does not start with a ``{{``, a `status` property with the status message is added. If `status` starts
        with a ``{{``, it is parsed as a (json style) dictionary of properties and added to the result properties.
        
        Some of the actions will add additional properties to the result:
        
        * :token:`pass-secret <preflight-option:action>` and :token:`fail-secret <preflight-option:action>` will 
          also add a `secret` property with value ``True``.
        * :token:`pass-hidden <preflight-option:action>` and :token:`fail-hidden <preflight-option:action>` will
          add `secret` and `hidden` properties with value ``True``.
        * :token:`skip <preflight-option:action>` and :token:`skip-error <preflight-option:action>` adds a `skipped`
          property with value ``True``.
        * :token:`skip-error <preflight-option:action>` additionally adds a `deps-error` property with value ``True``.
        
        The default preflight check is:
        
        .. code-block:: text
        
            {DEFAULT_PREFLIGHT_OPTION}
        
        This check is always executed before any other preflight checks provided in the options. 
        To disable the default action and run the checklet even if one of the dependencies had an error, add  
        at least one :token:`error <preflight-option:action>` preflight action, e.g. ``error {ACTION_SEPARATOR} run`` 
    """,
    multiple=True,
    all=True,
    location=('config', 'recipe', 'step')
)

LABEL_OPTION = OptionDefinition(
    name=OptionNameDomain('label'),
    type='string',
    location=('config', 'recipe', 'step')
)

# Properties for 'pass-secret' and 'fail-secret' actions
SECRET_PROPERTIES = {
    'secret': True,
}

# Properties for 'pass-hidden' and 'fail-hidden' actions
HIDDEN_PROPERTIES = {
    **SECRET_PROPERTIES,
    'hidden': True,
}

# Properties for 'skip' action
SKIP_PROPERTIES = {
    'skipped': True,
}

# Properties for the 'skip-error' action
SKIP_ERROR_PROPERTIES = {
    **SKIP_PROPERTIES,
    'deps-error': True,
}

ActionType: TypeAlias = tuple[Outcome, dict]

PREFLIGHT_ACTIONS: dict[str, ActionType | None] = {
    'run': None,
    'pass': (Outcome.PASS, {}),
    'pass-secret': (Outcome.PASS, SECRET_PROPERTIES),
    'pass-hidden': (Outcome.PASS, HIDDEN_PROPERTIES),
    'fail': (Outcome.FAIL, {}),
    'fail-secret': (Outcome.FAIL, SECRET_PROPERTIES),
    'fail-hidden': (Outcome.FAIL, HIDDEN_PROPERTIES),
    'skip': (Outcome.SKIP, SKIP_PROPERTIES),
    'error': (Outcome.ERROR, {}),
    'skip-error': (Outcome.SKIP, SKIP_ERROR_PROPERTIES),
}


def create_preflight_result(
    providers: Providers, trigger: str, action: ActionType, status: str | None
) -> ResultsBundle | None:
    """ Create a :py:class:`~momotor.bundles.ResultsBundle` with a pre-flight result for the given action
    """
    status_props = {}
    if status is not None:
        status = status.strip()

    if status:
        if status.startswith('{'):
            status = replace_placeholders(status, providers, mod='json')
            logger.debug(f'Preflight status: {status}')
            try:
                status_props = json.loads(status)
            except json.JSONDecodeError:
                warnings.warn(f'Invalid json in preflight status: {status!r}')
                status_props['status'] = status
        else:
            status_props['status'] = replace_placeholders(status, providers, mod='joincs')

    outcome, action_props = action
    properties = {
        **status_props,
        **action_props,
        'preflight-trigger': trigger,
        'source': __name__,
    }

    if 'label' not in properties:
        # Emulate LabelOptionMixin's handling of the label option
        label = LABEL_OPTION.resolve(providers, subdomains=True)
        properties['label'] = replace_task_placeholder(label, providers.task_id)

    bundle = ResultsBundle()

    step = providers.step
    if step:
        options = (option.recreate(bundle) for option in step.options)
    else:
        options = None

    bundle.create(
        results=[
            Result(bundle).create(
                step_id=str(providers.task_id),
                outcome=outcome,
                properties=[
                    Property(bundle).create(name=name, value=value)
                    for name, value in properties.items()
                ],
                options=options,
            )
        ]
    )

    return bundle


@annotate_docstring(SCHEDULER_PREFLIGHT_OPTION_NAME=SCHEDULER_PREFLIGHT_OPTION_NAME)
def preflight_check(providers: Providers) -> ResultsBundle | None:
    """ Evaluate a :momotor:option:`{SCHEDULER_PREFLIGHT_OPTION_NAME}` option in the given `providers`
    and return a :py:class:`~momotor.bundles.ResultsBundle` with a result as defined by the preflight option
    for the task with id `task_id` if any pre-flight options activated.

    :param providers: the providers to use for resolving the pre-flight option
    :return: a :py:class:`~momotor.bundles.ResultsBundle` with a result as defined by the preflight option, or
             `None` if no pre-flight action should be taken.
    """
    preflight_options = collections.deque()
    for preflight_option in PREFLIGHT_OPTION.resolve(providers, True):
        # Only replace placeholders in the selector part of the preflight option,
        # placeholders in the action part are replaced in `create_preflight_result` as the replacement depends
        # on the action type
        lhs, sep, rhs = preflight_option.partition(ACTION_SEPARATOR)
        preflight_options.append(
            (replace_placeholders(lhs, providers) + sep + rhs).strip()
        )

    # If there are no 'error' condition checks, add the default check as the first one
    has_error_selector = False
    for preflight_option in preflight_options:
        if not preflight_option.startswith(ACTION_SEPARATOR):
            try:
                mod, selector = parse_mod(preflight_option)
                type_, refs, oper, value, remainder = parse_selector(selector)
            except ValueError:
                pass
            else:
                if type_ == 'error':
                    has_error_selector = True
                    break

    if not has_error_selector:
        preflight_options = [DEFAULT_PREFLIGHT_OPTION, *preflight_options]

    for preflight_option in preflight_options:
        if preflight_option.startswith(ACTION_SEPARATOR):
            match, remaining = True, preflight_option
        else:
            try:
                match, remaining = match_by_selector(preflight_option, providers)
            except ValueError as e:
                msg = f"Invalid {PREFLIGHT_OPTION.name} option {preflight_option!r}: {e}"
                logger.exception(e)
                raise ValueError(msg)

        ws, sep, action_str = remaining.partition(ACTION_SEPARATOR)
        if ws.strip() or not sep:
            msg = f"Invalid {PREFLIGHT_OPTION.name} option format {preflight_option!r}"
            logger.error(msg)
            raise ValueError(msg)

        action_str = action_str.strip()
        if ' ' in action_str:
            action_str, status = action_str.split(' ', 1)
        else:
            status = None

        try:
            action = PREFLIGHT_ACTIONS[action_str]
        except KeyError:
            msg = f"Invalid {PREFLIGHT_OPTION.name} action {action_str!r} in {preflight_option!r}"
            logger.error(msg)
            raise ValueError(msg)

        if match:
            logger.info(f'{PREFLIGHT_OPTION.name} option {preflight_option!r} MATCHED')
            if action:
                return create_preflight_result(providers, preflight_option, action, status)
            else:
                return None

        logger.debug(f'{PREFLIGHT_OPTION.name} option {preflight_option!r} no match')

    return None
