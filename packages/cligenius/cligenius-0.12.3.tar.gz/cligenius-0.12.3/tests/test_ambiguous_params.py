import pytest
import cligenius
from cligenius.testing import CliRunner
from cligenius.utils import (
    AnnotatedParamWithDefaultValueError,
    DefaultFactoryAndDefaultValueError,
    MixedAnnotatedAndDefaultStyleError,
    MultipleCligeniusAnnotationsError,
    _split_annotation_from_cligenius_annotations,
)
from typing_extensions import Annotated

runner = CliRunner()


def test_split_annotations_from_cligenius_annotations_simple():
    # Simple sanity check that this utility works. If this isn't working on a given
    # python version, then no other tests for Annotated will work.
    given = Annotated[str, cligenius.Argument()]
    base, cligenius_annotations = _split_annotation_from_cligenius_annotations(given)
    assert base is str
    # No equality check on the param types. Checking the length is sufficient.
    assert len(cligenius_annotations) == 1


def test_forbid_default_value_in_annotated_argument():
    app = cligenius.Cligenius()

    # This test case only works with `cligenius.Argument`. `cligenius.Option` uses positionals
    # for param_decls too.
    @app.command()
    def cmd(my_param: Annotated[str, cligenius.Argument("foo")]):
        ...  # pragma: no cover

    with pytest.raises(AnnotatedParamWithDefaultValueError) as excinfo:
        runner.invoke(app)

    assert vars(excinfo.value) == {
        "param_type": cligenius.models.ArgumentInfo,
        "argument_name": "my_param",
    }


def test_allow_options_to_have_names():
    app = cligenius.Cligenius()

    @app.command()
    def cmd(my_param: Annotated[str, cligenius.Option("--some-opt")]):
        print(my_param)

    result = runner.invoke(app, ["--some-opt", "hello"])
    assert result.exit_code == 0, result.output
    assert "hello" in result.output


@pytest.mark.parametrize(
    ["param", "param_info_type"],
    [
        (cligenius.Argument, cligenius.models.ArgumentInfo),
        (cligenius.Option, cligenius.models.OptionInfo),
    ],
)
def test_forbid_annotated_param_and_default_param(param, param_info_type):
    app = cligenius.Cligenius()

    @app.command()
    def cmd(my_param: Annotated[str, param()] = param("foo")):
        ...  # pragma: no cover

    with pytest.raises(MixedAnnotatedAndDefaultStyleError) as excinfo:
        runner.invoke(app)

    assert vars(excinfo.value) == {
        "argument_name": "my_param",
        "annotated_param_type": param_info_type,
        "default_param_type": param_info_type,
    }


def test_forbid_multiple_cligenius_params_in_annotated():
    app = cligenius.Cligenius()

    @app.command()
    def cmd(
        my_param: Annotated[str, cligenius.Argument(), cligenius.Argument()],
    ):
        ...  # pragma: no cover

    with pytest.raises(MultipleCligeniusAnnotationsError) as excinfo:
        runner.invoke(app)

    assert vars(excinfo.value) == {"argument_name": "my_param"}


def test_allow_multiple_non_cligenius_params_in_annotated():
    app = cligenius.Cligenius()

    @app.command()
    def cmd(my_param: Annotated[str, "someval", cligenius.Argument(), 4] = "hello"):
        print(my_param)

    result = runner.invoke(app)
    # Should behave like normal
    assert result.exit_code == 0, result.output
    assert "hello" in result.output


@pytest.mark.parametrize(
    ["param", "param_info_type"],
    [
        (cligenius.Argument, cligenius.models.ArgumentInfo),
        (cligenius.Option, cligenius.models.OptionInfo),
    ],
)
def test_forbid_default_factory_and_default_value_in_annotated(param, param_info_type):
    def make_string():
        return "foo"  # pragma: no cover

    app = cligenius.Cligenius()

    @app.command()
    def cmd(
        my_param: Annotated[str, param(default_factory=make_string)] = "hello",
    ):
        ...  # pragma: no cover

    with pytest.raises(DefaultFactoryAndDefaultValueError) as excinfo:
        runner.invoke(app)

    assert vars(excinfo.value) == {
        "argument_name": "my_param",
        "param_type": param_info_type,
    }


@pytest.mark.parametrize(
    "param",
    [
        cligenius.Argument,
        cligenius.Option,
    ],
)
def test_allow_default_factory_with_default_param(param):
    def make_string():
        return "foo"

    app = cligenius.Cligenius()

    @app.command()
    def cmd(my_param: str = param(default_factory=make_string)):
        print(my_param)

    result = runner.invoke(app)
    assert result.exit_code == 0, result.output
    assert "foo" in result.output


@pytest.mark.parametrize(
    ["param", "param_info_type"],
    [
        (cligenius.Argument, cligenius.models.ArgumentInfo),
        (cligenius.Option, cligenius.models.OptionInfo),
    ],
)
def test_forbid_default_and_default_factory_with_default_param(param, param_info_type):
    def make_string():
        return "foo"  # pragma: no cover

    app = cligenius.Cligenius()

    @app.command()
    def cmd(
        my_param: str = param("hi", default_factory=make_string),
    ):
        ...  # pragma: no cover

    with pytest.raises(DefaultFactoryAndDefaultValueError) as excinfo:
        runner.invoke(app)

    assert vars(excinfo.value) == {
        "argument_name": "my_param",
        "param_type": param_info_type,
    }


@pytest.mark.parametrize(
    ["error", "message"],
    [
        (
            AnnotatedParamWithDefaultValueError(
                argument_name="my_argument",
                param_type=cligenius.models.ArgumentInfo,
            ),
            "`Argument` default value cannot be set in `Annotated` for 'my_argument'. Set the default value with `=` instead.",
        ),
        (
            MixedAnnotatedAndDefaultStyleError(
                argument_name="my_argument",
                annotated_param_type=cligenius.models.OptionInfo,
                default_param_type=cligenius.models.ArgumentInfo,
            ),
            "Cannot specify `Option` in `Annotated` and `Argument` as a default value together for 'my_argument'",
        ),
        (
            MixedAnnotatedAndDefaultStyleError(
                argument_name="my_argument",
                annotated_param_type=cligenius.models.OptionInfo,
                default_param_type=cligenius.models.OptionInfo,
            ),
            "Cannot specify `Option` in `Annotated` and default value together for 'my_argument'",
        ),
        (
            MixedAnnotatedAndDefaultStyleError(
                argument_name="my_argument",
                annotated_param_type=cligenius.models.ArgumentInfo,
                default_param_type=cligenius.models.ArgumentInfo,
            ),
            "Cannot specify `Argument` in `Annotated` and default value together for 'my_argument'",
        ),
        (
            MultipleCligeniusAnnotationsError(
                argument_name="my_argument",
            ),
            "Cannot specify multiple `Annotated` Cligenius arguments for 'my_argument'",
        ),
        (
            DefaultFactoryAndDefaultValueError(
                argument_name="my_argument",
                param_type=cligenius.models.OptionInfo,
            ),
            "Cannot specify `default_factory` and a default value together for `Option`",
        ),
    ],
)
def test_error_rendering(error, message):
    assert str(error) == message
