from __future__ import annotations

import re

from momotor.bundles import RecipeBundle, ConfigBundle, BundleFormatError
from momotor.options.doc import annotate_docstring
from momotor.options.option import OptionDefinition, OptionNameDomain
from momotor.options.parser.placeholders import replace_placeholders
from momotor.options.providers import Providers
from momotor.options.task_id import task_number_from_id, StepTaskId
from momotor.options.types import StepTasksType
from ._domain import DOMAIN

TASKS_OPTION_NAME = OptionNameDomain('tasks', DOMAIN)

#: The :momotor:option:`tasks@scheduler` option defines the number of sub-tasks for a step.
TASKS_OPTION = OptionDefinition(
    name=TASKS_OPTION_NAME,
    type='string',
    doc="""\
        Enable multiple tasks for this step. If not provided, a single task is generated for this step.

        This option can directly define the number of tasks, but the actual number of tasks can also be defined
        in the top-level options of the recipe or the options of the configuration bundle.

        The following table describes the various values that are valid for this option:

        ============ ============================
        Tasks option Recipe/config option allowed
        ============ ============================
        ``*``        At least one dimension required (e.g. ``2``, ``2.2`` etc)
        ``*?``       Zero or more dimensions allowed.
        ``?``        A single dimension required (e.g. ``1``, ``2``)
        ``?.?``      Two dimensions required (e.g. ``1.1``, ``2.2``)
        ``?.?.?``    Three dimensions required (e.g. ``1.2.3``, ``2.2.2``)
        ``?.*``      At least two dimensions required (e.g. ``1.2``, ``1.2.3``)
        ``?.??``     One dimension required, two dimensions allowed.
        ``?.??.??``  One dimension required, two or three dimensions allowed.
        ``4.?``      Exactly two dimensions required, and the first must be ``4`` (e.g. ``4.1``, ``4.2``)
        ``4.*``      At least two dimensions required, and the first must be ``4`` (e.g. ``4.1``, ``4.2.3``)
        ``4.4``      A fixed dimension. Config option not required, but if provided, MUST equal ``4.4``
        ``?.*?``     Allowed but identical to ``*``, so not recommended.
        ``?.??.*?``  Allowed but identical to ``?.*``, so not recommended.
        ============ ============================

        There is no limit to the number of dimensions allowed.

        The ``?`` and ``*`` wildcards indicate required dimensions. The ``??`` and ``*?`` wildcards indicate optional
        dimensions. The optional requirements must be the last dimensions in the option, e.g. ``??.?`` is not valid,
        but ``?.??`` is. There can only be one ``*`` or ``*?`` wildcard in the option, and it must be the last one.
    """,
    location=('config', 'recipe', 'step')
)

TASKS_DEF_RE = re.compile(r'^((([1-9]\d*)|[?])\.)*((([1-9]\d*)|[?*])|((\?\?\.)*([*?]\?)))$')


@annotate_docstring(TASKS_OPTION_NAME=TASKS_OPTION_NAME)
def get_scheduler_tasks_option(recipe: RecipeBundle, config: ConfigBundle | None, step_id: str) \
        -> StepTasksType | None:
    """ Get the :momotor:option:`{TASKS_OPTION_NAME}` option for a single step from the step,
    recipe or config.

    A step supporting sub-tasks must define this option in the recipe. It declares the number of sub-tasks
    supported. The format for the definition is as follows:

    ============ ============================
    Tasks option Recipe/config option allowed
    ============ ============================
    ``*``        At least one dimension required (e.g. ``2``, ``2.2`` etc)
    ``*?``       Zero or more dimensions allowed.
    ``?``        A single dimension required (e.g. ``1``, ``2``)
    ``?.?``      Two dimensions required (e.g. ``1.1``, ``2.2``)
    ``?.?.?``    Three dimensions required (e.g. ``1.2.3``, ``2.2.2``)
    ``?.*``      At least two dimensions required (e.g. ``1.2``, ``1.2.3``)
    ``?.??``     One dimension required, two dimensions allowed.
    ``?.??.??``  One dimension required, two or three dimensions allowed.
    ``4.?``      Exactly two dimensions required, and the first must be ``4`` (e.g. ``4.1``, ``4.2``)
    ``4.*``      At least two dimensions required, and the first must be ``4`` (e.g. ``4.1``, ``4.2.3``)
    ``4.4``      A fixed dimension. Config option not required, but if provided, MUST equal ``4.4``
    ``?.*?``     Allowed but identical to ``*``, so not recommended.
    ``?.??.*?``  Allowed but identical to ``?.*``, so not recommended.
    ============ ============================

    There is no limit to the number of dimensions allowed.

    Values in the config take priority over values in the recipe. If the option in the recipe contains dimension
    wildcards ``?``, ``*``, ``??``, or ``*?`` the option in the config must fill in those values.

    The ``?`` and ``*`` wildcards indicate required dimensions. The ``??`` and ``*?`` wildcards indicate optional
    dimensions. The optional requirements must be the last dimensions in the option, e.g. ``??.?`` is not valid,
    but ``?.??`` is. There can only be one ``*`` or ``*?`` wildcard in the option, and it must be the last one.

    :param recipe: the recipe bundle
    :param config: (optional) the config bundle
    :param step_id: the id of the step
    :return: the tasks option, parsed into a tuple of ints
    """
    value_def_providers = Providers(
        recipe=recipe,
        task_id=StepTaskId(step_id, None)
    )
    value_def = TASKS_OPTION.resolve(value_def_providers, False)
    value_def = replace_placeholders(value_def, value_def_providers)
    if value_def is not None:
        value_def = value_def.strip()

    value_providers = Providers(
        recipe=recipe,
        config=config
    )
    value = TASKS_OPTION.resolve(
        value_providers, {
            'recipe': step_id,
            'config': step_id
        }
    )
    value = replace_placeholders(value, value_providers)
    if value is not None:
        value = value.strip()

    if not value_def:
        if value is None:
            return None
        else:
            raise BundleFormatError(f"Step {step_id!r}: {TASKS_OPTION_NAME} option not supported")

    if not TASKS_DEF_RE.match(value_def):
        raise BundleFormatError(f"Step {step_id!r}: invalid {TASKS_OPTION_NAME} option"
                                f" definition {value_def!r}")

    value_def_parts = value_def.split('.')
    if value_def_parts[-1] == '*?':
        wildcard = True
        value_def_parts.pop()
    elif value_def_parts[-1] == '*':
        wildcard = True
        value_def_parts[-1] = '?'
    else:
        wildcard = False

    min_length = 0
    for p in value_def_parts:
        if p == '??':
            break
        min_length += 1

    if not wildcard and '?' not in value_def_parts and '??' not in value_def_parts:
        # Fixed dimension -- value is optional but must be equal to value_def if provided
        if value and value != value_def:
            raise BundleFormatError(f"Step {step_id!r}: {TASKS_OPTION_NAME} option value {value!r} "
                                    f"does not match definition {value_def!r}")

        return task_number_from_id(value_def)

    elif not value:
        if min_length > 0:
            # Missing value option
            raise BundleFormatError(f"Step {step_id!r}: missing required {TASKS_OPTION_NAME} option")

        return None

    else:
        try:
            step_tasks = []
            for pos, part in enumerate(value.split('.')):
                try:
                    part_def = value_def_parts[pos]
                except IndexError:
                    if not wildcard:
                        raise ValueError
                else:
                    if part_def not in {'?', '??', part}:
                        raise ValueError

                step_tasks.append(int(part))

        except ValueError:
            step_tasks = None

        if step_tasks is None or len(step_tasks) < min_length:
            raise BundleFormatError(f"Step {step_id!r}: {TASKS_OPTION_NAME} option value {value!r} "
                                    f"does not match definition {value_def!r}")

        return tuple(step_tasks) if step_tasks else None
