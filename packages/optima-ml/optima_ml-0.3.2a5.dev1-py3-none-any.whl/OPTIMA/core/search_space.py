# -*- coding: utf-8 -*-
"""A module that provides general functionality to handle the hyperparameter search space."""
from typing import Union, Optional, Callable, Any

import numpy as np
import dill

from ray import tune

import OPTIMA.core.tools

run_config_search_space_entry_type = Union[int, float, str, list, tuple, dict]

tune_search_space_entry_type = Union[
    tune.search.sample.Float,
    tune.search.sample.Integer,
    tune.search.sample.Categorical,
    list,
    dict,
    str,
    float,
    int,
]
tune_search_space_type = dict[
    str,
    tune_search_space_entry_type,
]

PBT_search_space_type = dict[
    str, Union[tune.search.sample.Float, tune.search.sample.Integer, tune.search.sample.Categorical, list, dict]
]


def _get_range_search_space_properties(hp_name, hp_value, optuna=False):
    """_summary_.

    Parameters
    ----------
    hp_name : _type_
        _description_
    hp_value : _type_
        _description_
    optuna : _type_
        _description_ (Default value = False)

    Returns
    -------
    _type_
        _description_
    """
    assert "bounds" in hp_value.keys(), "Bounds need to be provided for search space entry of type 'range'!"
    bounds = hp_value["bounds"]

    # gather properties of this search space entry and set defaults for vacant entries
    if hp_value.get("value_type") is not None:
        assert hp_value["value_type"] in [
            "int",
            "float",
        ], f"Unsupported value type {hp_value['value_type']} for hyperparameter {hp_name}."
        value_type = hp_value["value_type"]
    else:
        value_type = "float"
    if hp_value.get("sampling") is not None:
        assert hp_value["sampling"] in [
            "uniform",
            "log",
            "normal",
        ], f"Unsupported sampling option {hp_value['sampling']} for hyperparameter {hp_name}."
        sampling = hp_value["sampling"]
    else:
        sampling = "uniform"
    if hp_value.get("step") is not None:
        if value_type == "int" and int(hp_value["step"]) != hp_value["step"]:
            raise ValueError(
                f"A step value of {hp_value['step']} is not possible for integer search space of {hp_name}!"
            )
        if value_type == "int" and sampling == "log" and hp_value.get("step") != 1 and optuna:
            raise ValueError(
                "Optuna does not support integer log sampling with step != 1. Set step to 1 or sampling to 'uniform'."
            )
        step = hp_value["step"]
    else:
        step = None
    if sampling == "normal":
        if value_type == "int":
            raise ValueError(f"Integer normal search space of {hp_name} is not supported by Tune!")
        assert (
            "mean" in hp_value.keys() and "std" in hp_value.keys()
        ), f"'mean' and 'std' must be provided for 'normal' search space of {hp_name}."
        mean = hp_value["mean"]
        std = hp_value["std"]
    else:
        mean, std = None, None

    return bounds, value_type, sampling, step, mean, std


def _build_search_space_properties(hp_name, hp_value, optuna=False):
    """_summary_.

    Parameters
    ----------
    hp_name : _type_
        _description_
    hp_value : _type_
        _description_
    optuna : _type_
        _description_ (Default value = False)

    Returns
    -------
    _type_
        _description_
    """
    # first check if hyperparameter is fixed
    if not isinstance(hp_value, dict):
        search_space_type = "fixed"
        search_space_entry = hp_value
    else:
        # check if it is a range or choice parameter; this can be given via the "type" option or inferred from the
        # presence of the "bounds" or "values" option
        if hp_value.get("type") == "range" or "bounds" in hp_value.keys():
            # get the properties of this search space entry and set default values for vacant entries
            search_space_type = "range"
            bounds, value_type, sampling, step, mean, std = _get_range_search_space_properties(
                hp_name, hp_value, optuna=optuna
            )
            search_space_entry = (bounds, value_type, sampling, step, mean, std)
        elif hp_value.get("type") == "choice" or "values" in hp_value.keys():
            assert "values" in hp_value.keys(), "Values must be provided for choice search space!"
            search_space_type = "choice"
            search_space_entry = hp_value["values"]
        else:
            raise ValueError(f"Unsupported search space type for hyperparameter {hp_name}: {hp_value}")

    return search_space_type, search_space_entry


def serialize_conditions(search_space: dict[str, run_config_search_space_entry_type]):
    """_summary_.

    Parameters
    ----------
    search_space : dict[str, run_config_search_space_entry_type]
        _description_

    Returns
    -------
    _type_
        _description_
    """
    serialized_search_space = search_space.copy()
    for hp_name, hp_value in search_space.items():
        if isinstance(hp_value, dict):
            serialized_hp_value = hp_value.copy()
            if "bounds" in hp_value.keys() and callable(hp_value["bounds"][1]):
                bounds_hps, bounds_callable = hp_value["bounds"]
                serialized_hp_value["bounds"] = (bounds_hps, dill.dumps(bounds_callable))
            if "values" in hp_value.keys() and callable(hp_value["values"][1]):
                values_hps, values_callable = hp_value["values"]
                serialized_hp_value["values"] = (values_hps, dill.dumps(values_callable))
            if "only" in hp_value.keys():
                only_hps, only_callable = hp_value["only"]
                serialized_hp_value["only"] = (only_hps, dill.dumps(only_callable))
            serialized_search_space[hp_name] = serialized_hp_value
    return serialized_search_space


def build_tune_search_space(search_space: dict[str, run_config_search_space_entry_type]) -> tune_search_space_type:
    """Translates the search space format from the run-config to a Tune search space.

    Since Tune does not support conditional search spaces, a ``ValueError`` will be raised if a conditional search space
    is provided.

    Parameters
    ----------
    search_space : dict[str, run_config_search_space_entry_type]
        The search space in the format used in the run-config.

    Returns
    -------
    tune_search_space_type
        The search space to be provided to Tune.
    """
    # verify the search space is not conditional
    for _, hp_value in search_space.items():
        if isinstance(hp_value, dict) and "only" in hp_value.keys():
            raise ValueError("Tune does not support conditional search spaces!")

    # build the tune search space
    tune_search_space = {}
    for hp_name, hp_value in search_space.items():
        # get the search space properties, i.e. a set of options that are needed to specify the search space entry.
        # Vacant options are populated with default values
        search_space_type, search_space_properties = _build_search_space_properties(hp_name, hp_value)

        # choose the correct Tune search space
        if search_space_type == "fixed":
            tune_search_space[hp_name] = search_space_properties
        elif search_space_type == "range":
            bounds, value_type, sampling, step, mean, std = search_space_properties
            if value_type == "float" and sampling == "uniform" and step is None:
                tune_search_space[hp_name] = tune.uniform(bounds[0], bounds[1])
            elif value_type == "float" and sampling == "uniform" and step is not None:
                tune_search_space[hp_name] = tune.quniform(bounds[0], bounds[1], step)
            elif value_type == "float" and sampling == "log" and step is None:
                tune_search_space[hp_name] = tune.loguniform(bounds[0], bounds[1])
            elif value_type == "float" and sampling == "log" and step is not None:
                tune_search_space[hp_name] = tune.qloguniform(bounds[0], bounds[1], step)
            elif sampling == "normal" and step is None:
                tune_search_space[hp_name] = tune.randn(mean, std)
            elif sampling == "normal" and step is not None:
                tune_search_space[hp_name] = tune.qrandn(mean, std, step)
            elif value_type == "int" and sampling == "uniform" and step is None:
                tune_search_space[hp_name] = tune.randint(bounds[0], bounds[1] + 1)  # upper bound is exclusive
            elif value_type == "int" and sampling == "uniform" and step is not None:
                if step != 1:
                    tune_search_space[hp_name] = tune.qrandint(
                        bounds[0], bounds[1], step
                    )  # upper bound is inclusive if step != 1
                else:
                    tune_search_space[hp_name] = tune.randint(bounds[0], bounds[1] + 1)
            elif value_type == "int" and sampling == "log" and step is None:
                tune_search_space[hp_name] = tune.lograndint(bounds[0], bounds[1] + 1)  # upper bound is exclusive
            elif value_type == "int" and sampling == "log" and step is not None:
                if step != 1:
                    tune_search_space[hp_name] = tune.qlograndint(
                        bounds[0], bounds[1], step
                    )  # upper bound is inclusive if step != 1
                else:
                    tune_search_space[hp_name] = tune.lograndint(bounds[0], bounds[1] + 1)
        elif search_space_type == "choice":
            tune_search_space[hp_name] = tune.choice(search_space_properties)
        else:
            raise RuntimeError(f"Unknown search space type {search_space_type}.")

    return tune_search_space


def optuna_search_space(search_space: dict[str, run_config_search_space_entry_type], trial):
    """_summary_.

    Parameters
    ----------
    search_space : dict[str, run_config_search_space_entry_type]
        _description_
    trial : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    # split search space entries into conditional and non-conditional entries and extract the search space properties
    conditional_search_space = {}
    non_conditional_search_space = {}
    for hp_name, serialized_hp_value in search_space.items():
        # assign to conditional and non-conditional sub-search space dicts; serialized callables are bytes instances
        # collect a list of hyperparameters that is needed to check if hp is necessary, and a second list of hps that is
        # needed to decide on a value
        only_depends_hps = []
        value_depends_hps = []
        if isinstance(serialized_hp_value, dict):
            if "bounds" in serialized_hp_value.keys() and isinstance(serialized_hp_value["bounds"][1], bytes):
                value_depends_hps += list(serialized_hp_value["bounds"][0])
            if "values" in serialized_hp_value.keys() and isinstance(serialized_hp_value["values"][1], bytes):
                value_depends_hps += list(serialized_hp_value["values"][0])
            if "only" in serialized_hp_value.keys():
                only_depends_hps += list(serialized_hp_value["only"][0])

        # check if there are any dependencies
        if len(only_depends_hps) + len(value_depends_hps) == 0:
            # get the search space properties, i.e. a set of options that are needed to specify the search space entry.
            # Vacant options are populated with default values
            search_space_type, search_space_properties = _build_search_space_properties(
                hp_name, serialized_hp_value, optuna=True
            )
            non_conditional_search_space[hp_name] = (search_space_type, search_space_properties)
        else:
            conditional_search_space[hp_name] = (
                only_depends_hps,
                list(set(value_depends_hps)),
                serialized_hp_value,
            )  # remove duplicate dependencies

    # save all suggested values in case they are needed for the conditions + all fixed values to be returned later
    suggested_hps = {}
    fixed_hps = {}

    # start with non-conditional hyperparameters
    for hp_name, (hp_type, hp_properties) in non_conditional_search_space.items():
        if hp_type == "fixed":
            fixed_hps[hp_name] = hp_properties
        elif hp_type == "range":
            bounds, value_type, sampling, step, mean, std = hp_properties
            if value_type == "int":
                suggested_hps[hp_name] = trial.suggest_int(
                    hp_name, bounds[0], bounds[1], step=1 if step is None else step, log=sampling == "log"
                )
            elif value_type == "float":
                suggested_hps[hp_name] = trial.suggest_float(
                    hp_name, bounds[0], bounds[1], step=step, log=sampling == "log"
                )
        elif hp_type == "choice":
            suggested_hps[hp_name] = trial.suggest_categorical(hp_name, hp_properties)
        else:
            raise RuntimeError(f"Unknown search space type {hp_type}.")

    # try to iteratively build conditional hyperparameters (as some conditional hyperparameters can depend on
    # other conditional hyperparameters
    cond_hps_to_solve = list(conditional_search_space.keys())
    while len(cond_hps_to_solve) > 0:
        # to check at the end of the iteration if we could solve anything, otherwise break and raise an error
        num_left = len(cond_hps_to_solve)

        # Iterate over remaining conditional hyperparameters
        for hp_name in cond_hps_to_solve:
            only_depends_hps, value_depends_hps, serialized_hp_value = conditional_search_space[hp_name]

            # See if we can evaluate if hyperparameter is needed
            if len(only_depends_hps) > 0:
                only_depends_values = {
                    only_depends_hp: suggested_hps[only_depends_hp]
                    if only_depends_hp in suggested_hps.keys()
                    else fixed_hps[only_depends_hp]
                    if only_depends_hp in fixed_hps.keys()
                    else None
                    for only_depends_hp in only_depends_hps
                }
                if not any(only_depends_value is None for only_depends_value in only_depends_values.values()):
                    # evaluate the only condition
                    only_hps, serialized_only_callable = serialized_hp_value["only"]
                    need_hp = dill.loads(serialized_only_callable)(*[only_depends_values[h] for h in only_hps])
            else:
                # no only condition, so we always need this hyperparameter
                need_hp = True

            if need_hp:
                # if this hyperparameter is needed, check if we can decide on its value
                value_depends_values = {
                    value_depends_hp: suggested_hps[value_depends_hp]
                    if value_depends_hp in suggested_hps.keys()
                    else fixed_hps[value_depends_hp]
                    if value_depends_hp in fixed_hps.keys()
                    else None
                    for value_depends_hp in value_depends_hps
                }
                if not any(value_depends_value is None for value_depends_value in value_depends_values.values()):
                    # we can decide on this hyperparameter's value, so remove it from the list of remaining hyperparameters
                    cond_hps_to_solve.remove(hp_name)

                    # deserialize the hyperparameter search space entry
                    hp_value = serialized_hp_value.copy()
                    if "bounds" in serialized_hp_value.keys() and isinstance(serialized_hp_value["bounds"][1], bytes):
                        bounds_hps, serialized_bounds_callable = serialized_hp_value["bounds"]
                        hp_value["bounds"] = dill.loads(serialized_bounds_callable)(
                            *[value_depends_values[h] for h in bounds_hps]
                        )
                    if "values" in serialized_hp_value.keys() and isinstance(serialized_hp_value["values"][1], bytes):
                        values_hps, serialized_values_callable = serialized_hp_value["values"]
                        hp_value["values"] = dill.loads(serialized_values_callable)(
                            *[value_depends_values[h] for h in values_hps]
                        )

                    # calculate the search space properties of the deserialized hyperparameter search space entry
                    search_space_type, search_space_properties = _build_search_space_properties(
                        hp_name, hp_value, optuna=True
                    )

                    # finally suggest hyperparameter value
                    if search_space_type == "fixed":
                        fixed_hps[hp_name] = search_space_properties
                    elif search_space_type == "range":
                        bounds, value_type, sampling, step, mean, std = search_space_properties
                        if value_type == "int":
                            suggested_hps[hp_name] = trial.suggest_int(
                                hp_name, bounds[0], bounds[1], step=1 if step is None else step, log=sampling == "log"
                            )
                        elif value_type == "float":
                            suggested_hps[hp_name] = trial.suggest_float(
                                hp_name, bounds[0], bounds[1], step=step, log=sampling == "log"
                            )
                    elif search_space_type == "choice":
                        suggested_hps[hp_name] = trial.suggest_categorical(hp_name, search_space_properties)
                    else:
                        raise RuntimeError(f"Unknown search space type {hp_type}.")
                else:
                    # condition is False, thus just skip the suggestion
                    continue
            else:
                # we don't need this hyperparameter, so drop it from the list of remaining hyperparameters
                cond_hps_to_solve.remove(hp_name)

            # check if we actually resolved any new hyperparameter
            if len(cond_hps_to_solve) == num_left:
                raise ValueError("Conditional search space contains circular conditions that cannot be resolved.")

    return fixed_hps


def prepare_search_space_for_PBT(
    search_space: dict[str, run_config_search_space_entry_type], best_hp_values_optuna: Optional[dict] = None
) -> tuple[tune_search_space_type, tune_search_space_type]:
    """Builds the search space for the optimization with Population Based Training.

    All hyperparameters that are not marked with 'supports_mutation' are fixed to the best values found during the
    previous optimization step. If no previous optimization was performed, all hyperparameters in the search space need
    to be mutatable, otherwise an error is raised. The resulting search space is then translated to a Tune search space
    by calling ``build_tune_search_space``.

    Since the ``PopulationBasedTraining``-scheduler needs a search space that does not contain fixed values, a second
    dictionary with the fixed hyperparameter values removed is returned.

    Parameters
    ----------
    search_space : dict[str, run_config_search_space_entry_type]
        The search space as defined in the run-config.
    best_hp_values_optuna : Optional[dict]
        A dictionary containing the best hyperparameter values found during a previous optimization step. (Default value = None)

    Returns
    -------
    tuple[tune_search_space_type, tune_search_space_type]
        The Tune search space with non-mutatable hyperparameters fixed to their best value and the pruned Tune search
        space, containing only mutatable hyperparameters, which is to be provided to the
        ``PopulationBasedTraining``-scheduler.
    """
    # extract the hyperparameters that are marked with "supports_mutation"
    mutatable_hps = []
    non_mutatable_hps = []
    for hp_name, hp_value in search_space.items():
        if isinstance(hp_value, dict) and "supports_mutation" in hp_value.keys() and hp_value["supports_mutation"]:
            mutatable_hps.append(hp_name)
        else:
            non_mutatable_hps.append(hp_name)

    if best_hp_values_optuna is not None:
        # create the two variants of the search space, only with only the mutatable hyperparameters and once also with
        # the fixed best values
        search_space_with_fixed = {}
        search_space_mutatable = {}
        for hp_name, hp_value in search_space.items():
            if hp_name in mutatable_hps:
                # add the mutatable hyperparameter to both search spaces
                search_space_mutatable[hp_name] = hp_value
                search_space_with_fixed[hp_name] = hp_value
            elif isinstance(hp_value, dict):
                # the hyperparameter is not mutatable, thus select the best fixed value and only add it to the
                # search_space_with_fixed dictionary
                print(
                    f"Hyperparameter '{hp_name}' is not marked as mutatable. Fixing it to the best value found during "
                    f"the previous optimization step: {best_hp_values_optuna[hp_name]}."
                )
                search_space_with_fixed[hp_name] = best_hp_values_optuna[hp_name]
            else:
                # if the hyperparameter was fixed from the beginning, we can just silently add it again to the search
                # space
                search_space_with_fixed[hp_name] = hp_value

            # convert the search spaces to Tune search spaces
            tune_search_space_with_fixed = build_tune_search_space(search_space_with_fixed)
            tune_search_space_mutatable = build_tune_search_space(search_space_mutatable)
    else:
        # if we don't have best values to fix non-mutatable hyperparameters, all hyperparameters to optimize need to be
        # mutatable
        assert len(non_mutatable_hps) == 0, (
            f"Hyperparameters {non_mutatable_hps} are not marked with 'support_mutation', and no prior optimization has "
            "been performed to choose fixed values from."
        )

        # convert search space to tune search space
        tune_search_space_mutatable = build_tune_search_space(search_space)
        tune_search_space_with_fixed = tune_search_space_mutatable

    return tune_search_space_with_fixed, tune_search_space_mutatable


def add_random_seed_suggestions(seed: Optional[int] = None) -> Callable:
    """Decorator function to add a random seed to the dictionary of suggestions produced by a search algorithm.

    In order to prevent the search algorithms from trying to optimize the seed, this simple wrapper creates a subclass
    of the searcher and appends a random seed to the suggestions while leaving the rest of the searcher untouched. To
    make the added seeds deterministic, a seed needs to be provided to the wrapper that is used to generate the `numpy`
    random state.

    Parameters
    ----------
    seed : Optional[int]
        Seed to set the `numpy` random state. (Default value = None)

    Returns
    -------
    Callable
        Decorator function that uses the random state created in the outer function.
    """

    def _add_seed(cls: type) -> type:
        """Inner decorator function.

        Creates a subclass of the decorated class and overwrites the ``suggest``-function. When called, the
        ``suggest``-function of the super-class is executed and a new random number is added as key ``'seed'`` to the
        dictionary of suggestions returned by the super-class. To generate this number, the random state provided in the
        outer function is used.

        Returns
        -------
        type
            The subclass of the decorated class with the ``suggest``-function overwritten
        """

        class SearcherWithSeed(cls):
            """Subclass of the decorated class with the ``suggest``-function overwritten."""

            def suggest(self, *args: Any, **kwargs: Any) -> dict:
                """Overwrites the ``suggest``-function of the super-class to add the random seed to the suggestions.

                Parameters
                ----------
                *args : Any
                    Positional arguments of the ``suggest``-function of the super-class.
                **kwargs : Any
                    Keyword arguments of the ``suggest``-function of the super-class.

                Returns
                -------
                dict
                    The dictionary of suggestions returned by the ``suggest``-function of the super-class with the
                    random seed added as an additional entry with key ``'seed'``.
                """
                suggestion = super(SearcherWithSeed, self).suggest(*args, **kwargs)
                suggestion["seed"] = rng.randint(*OPTIMA.core.tools.get_max_seeds())
                return suggestion

        return SearcherWithSeed

    rng = np.random.RandomState(seed)
    return _add_seed
