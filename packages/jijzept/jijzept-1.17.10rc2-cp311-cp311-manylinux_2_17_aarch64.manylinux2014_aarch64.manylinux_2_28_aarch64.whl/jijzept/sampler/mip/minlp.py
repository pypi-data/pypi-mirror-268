from __future__ import annotations

import typing as typ

import jijmodeling as jm

from jijzept.entity.schema import SolverType
from jijzept.response import JijModelingResponse
from jijzept.sampler.base_sampler import (
    JijZeptBaseSampler,
    ParameterSearchParameters,
    sample_instance,
    sample_model,
)
from jijzept.type_annotation import FixedVariables, InstanceData


class JijMINLPSolver(JijZeptBaseSampler):
    """The client for solving MINLP problems using JijModeling."""

    jijmodeling_solver_type = SolverType(
        queue_name="pyomosolver", solver="MINLPSolver"
    )

    def sample_model(
        self,
        model: jm.Problem,
        instance_data: InstanceData,
        *,
        fixed_variables: FixedVariables = {},
        relaxed_variables: typ.List[str] | None = None,
        max_wait_time: int | float | None = None,
        sync: bool = True,
        queue_name: str | None = None,
    ) -> JijModelingResponse:
        """Solve the MINLP problem using JijModeling.
        
        Args:
            model (jm.Problem): The mathematical model of JijModeling.
            instance_data (InstanceData): The actual values to be assined to the placeholders.
            fixed_variables (FixedVariables, optional): The dictionary of variables to be fixed.
            relaxed_variables (List[str], optional): The labels of the variables to be relaxed to continuous.
            max_wait_time (int | float | None, optional): The number of timeout [sec] for post request. If `None`, 600 will be set. Please note that this argument is for the `jijzept` timeout and not for configuring solver settings, such as solving time.
            sync (bool): Synchronous mode. If `True`, the method waits until the solution is returned.
            queue_name (Optional[str]): Queue name.
        
        Returns:
            JijModelingResponse: Stores solution and other information.

        Examples:
            ```python
                import jijmodeling as jm
                import jijzept as jz

                problem = jm.Problem("One-dimensional Bin Packing Problem")

                L = jm.Placeholder("L")
                b = jm.Placeholder("b", ndim=1)
                w = jm.Placeholder("w", ndim=1)
                m = b.len_at(0, latex="m")
                n = w.len_at(0, latex="n")
                x = jm.IntegerVar("x", shape=(m, n), lower_bound=0, upper_bound=10)
                y = jm.BinaryVar("y", shape=(n,))
                i = jm.Element("i", belong_to=(0, m))
                j = jm.Element("j", belong_to=(0, n))

                problem += jm.sum(j, y[j])
                problem += jm.Constraint("const1", jm.sum(j, x[i, j]) >= b[i], forall=i)
                problem += jm.Constraint("const2", jm.sum(i, w[i] * x[i, j]) <= L * y[j], forall=j)

                instance_data = {
                    "L": 250,
                    "w": [187, 119, 74, 90],
                    "b": [1, 2, 2, 1]
                }

                solver = jz.JijMINLPSolver(config="config.toml")
                response = solver.sample_model(problem, instance_data)
                sampleset = response.get_sampleset()
            ```
        """
        para_search_params = ParameterSearchParameters()

        if queue_name is None:
            queue_name = self.jijmodeling_solver_type.queue_name

        sample_set = sample_model(
            self.client,
            self.jijmodeling_solver_type.solver,
            queue_name=queue_name,
            problem=model,
            instance_data=instance_data,
            fixed_variables=fixed_variables,
            parameter_search_parameters=para_search_params,
            max_wait_time=max_wait_time,
            sync=sync,
            **{"relaxed_variables": relaxed_variables},
        )
        return sample_set

    def sample_instance(
        self,
        instance_id: str,
        *,
        fixed_variables: FixedVariables = {},
        relaxed_variables: typ.List[str] | None = None,
        max_wait_time: int | float | None = None,
        sync: bool = True,
        queue_name: str | None = None,
        system_time: jm.SystemTime = jm.SystemTime(),
    ) -> JijModelingResponse:
        """Solve the MINLP problem using JijModeling.
        
        Args:
            instance_id (str): The ID of the uploaded instance.
            fixed_variables (FixedVariables, optional): The dictionary of variables to be fixed.
            relaxed_variables (List[str], optional): The labels of the variables to be relaxed to continuous.
            max_wait_time (int | float | None, optional): The number of timeout [sec] for post request. If `None`, 600 will be set. Please note that this argument is for the `jijzept` timeout and not for configuring solver settings, such as solving time.
            sync (bool): Synchronous mode. If `True`, the method waits until the solution is returned.
            queue_name (Optional[str]): Queue name.
        
        Returns:
            JijModelingResponse: Stores solution and other information.

        Examples:
            ```python
                import jijmodeling as jm
                import jijzept as jz

                problem = jm.Problem("One-dimensional Bin Packing Problem")

                L = jm.Placeholder("L")
                b = jm.Placeholder("b", ndim=1)
                w = jm.Placeholder("w", ndim=1)
                m = b.len_at(0, latex="m")
                n = w.len_at(0, latex="n")
                x = jm.IntegerVar("x", shape=(m, n), lower_bound=0, upper_bound=10)
                y = jm.BinaryVar("y", shape=(n,))
                i = jm.Element("i", belong_to=(0, m))
                j = jm.Element("j", belong_to=(0, n))

                problem += jm.sum(j, y[j])
                problem += jm.Constraint("const1", jm.sum(j, x[i, j]) >= b[i], forall=i)
                problem += jm.Constraint("const2", jm.sum(i, w[i] * x[i, j]) <= L * y[j], forall=j)

                instance_data = {
                    "L": 250,
                    "w": [187, 119, 74, 90],
                    "b": [1, 2, 2, 1]
                }

                solver = jz.JijMINLPSolver(config="config.toml")

                # upload instance
                instance_id = sampler.upload_instance(problem, instance_data)

                # solve
                response = solver.sample_instance(instance_id)
                sampleset = response.get_sampleset()
            ```
        """
        para_search_params = ParameterSearchParameters()

        if queue_name is None:
            queue_name = self.jijmodeling_solver_type.queue_name

        sample_set = sample_instance(
            client=self.client,
            solver=self.jijmodeling_solver_type.solver,
            queue_name=queue_name,
            instance_id=instance_id,
            fixed_variables=fixed_variables,
            parameter_search_parameters=para_search_params,
            max_wait_time=max_wait_time,
            sync=sync,
            system_time=system_time,
            **{"relaxed_variables": relaxed_variables},
        )

        return sample_set
