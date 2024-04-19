import json
from collections import OrderedDict
from pathlib import Path

import typer
from cookiecutter import exceptions as exc
from cookiecutter.main import cookiecutter

from cookieplone.exceptions import GeneratorException
from cookieplone.utils import console, files


def _remove_internal_keys(context: OrderedDict) -> dict:
    """Remove internal and computed keys."""
    new_context = {
        key: value for key, value in context.items() if not key.startswith("_")
    }
    return new_context


def generate(
    repository,
    tag,
    no_input,
    extra_context,
    replay,
    overwrite_if_exists,
    output_dir,
    config_file,
    default_config,
    passwd,
    template,
    skip_if_file_exists,
    keep_project_on_failure,
) -> Path:
    try:
        result = cookiecutter(
            repository,
            tag,
            no_input,
            extra_context=extra_context,
            replay=replay,
            overwrite_if_exists=overwrite_if_exists,
            output_dir=output_dir,
            config_file=config_file,
            default_config=default_config,
            password=passwd,
            directory=template,
            skip_if_file_exists=skip_if_file_exists,
            accept_hooks=True,
            keep_project_on_failure=keep_project_on_failure,
        )
    except (
        exc.ContextDecodingException,
        exc.OutputDirExistsException,
        exc.InvalidModeException,
        exc.FailedHookException,
        exc.UnknownExtension,
        exc.InvalidZipRepository,
        exc.RepositoryNotFound,
        exc.RepositoryCloneFailed,
    ) as e:
        raise GeneratorException(message=str(e), original=e)  # noQA:B904
    except exc.UndefinedVariableInTemplate as undefined_err:
        context_str = json.dumps(undefined_err.context, indent=2, sort_keys=True)
        msg = f"""{undefined_err.message}
        Error message: {undefined_err.error.message}
        Context: {context_str}
        """
        raise GeneratorException(message=msg, original=undefined_err)  # noQA:B904
    else:
        return Path(result)


def generate_subtemplate(
    template: str, output_dir: Path, folder_name: str, context: OrderedDict
) -> Path:
    # Extract path to repository
    repository = context.get("_checkout") or context.get("_template")

    if not repository or not (Path(repository) / template).exists():
        # TODO: Error message
        raise typer.Exit(code=1)
    # Cleanup context
    extra_context = _remove_internal_keys(context)
    ## Add folder name again
    extra_context["__folder_name"] = folder_name
    ## Disable GHA for subcomponent
    extra_context["__gha_enable"] = False
    # Enable quiet mode
    console.enable_quiet_mode()
    # Call generate
    try:
        result = generate(
            repository,
            None,  # We should have the tag already locally
            True,  # No input
            extra_context,
            False,  # Not running a replay
            True,  # overwrite_if_exists
            output_dir,
            None,  # config_file
            None,  # default_config,
            None,  # password
            template,
            False,  # skip_if_file_exists,
            False,  # keep_project_on_failure
        )
    except GeneratorException as exc:
        console.disable_quiet_mode()
        raise exc
    else:
        console.disable_quiet_mode()
        path = Path(result)
        # Remove GHA folder
        files.remove_gha(path)
        # Return path
        return path
