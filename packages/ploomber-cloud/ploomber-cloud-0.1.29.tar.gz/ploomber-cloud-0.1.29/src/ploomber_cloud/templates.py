"""
Configure a project from a template
"""

from pathlib import Path
from string import Template
from importlib import resources
import secrets

import requests
import click

from ploomber_cloud.assets import vllm as vllm_resources
from ploomber_cloud.config import PloomberCloudConfig
from ploomber_cloud import init, deploy


def validate_model_name(model_name):
    response = requests.get(f"https://huggingface.co/api/models/{model_name}")

    if response.ok:
        return {"exists": True, "gated": False}
    else:
        output = response.json()
        error_message = output.get("error", {})

        if "gated" in error_message:
            return {"exists": True, "gated": True}
        else:
            return {"exists": False, "gated": False}


def has_access_to_model(model_name, hf_token):
    response = requests.get(
        f"https://huggingface.co/api/models/{model_name}",
        headers={"authorization": "Bearer {}".format(hf_token)},
    )
    return response.ok


def prompt_model_name(text):
    model_name = click.prompt(text, default="facebook/opt-125m")
    response = validate_model_name(model_name)

    while not response["exists"]:
        click.secho(f"Model {model_name} not found, please try again.", fg="red")
        model_name = click.prompt(text, default="facebook/opt-125m")
        response = validate_model_name(model_name)

    return model_name, response["gated"]


def prompt_hf_token(model_name):
    hf_token = click.prompt("Enter your HF_TOKEN")

    while not has_access_to_model(model_name, hf_token):
        click.secho(
            f"The HF_TOKEN provided doesn't have access to {model_name}, please "
            "try again.",
            fg="red",
        )
        hf_token = click.prompt("Enter your HF_TOKEN")

    return hf_token


def get_parameters_and_token():
    model_name, gated = prompt_model_name("Model to serve via vLLM")
    hf_token = None

    if gated:
        click.secho(f"Model {model_name} is gated! Provide an HF_TOKEN", fg="yellow")
        hf_token = prompt_hf_token(model_name)

    params = {
        "MODEL_NAME": model_name,
    }

    return params, hf_token


def generate_env(hf_token):
    env_data = {"VLLM_API_KEY": secrets.token_urlsafe()}

    if hf_token:
        env_data["HF_TOKEN"] = hf_token

    click.echo("API KEY saved to .env file")

    env = "\n".join([f"{k}={v}" for k, v in env_data.items()])

    return {"mapping": env_data, "text": env}


def template(name):
    if name != "vllm":
        raise click.ClickException(f"Template {name} not found. Valid options: vllm")

    if any(Path.cwd().iterdir()):
        raise click.ClickException("This command must be run in an empty directory.")

    dockerfile_template = Template(resources.read_text(vllm_resources, "Dockerfile"))
    params, hf_token = get_parameters_and_token()
    dockerfile = dockerfile_template.substitute(**params)
    requirements = resources.read_text(vllm_resources, "requirements.txt")

    # TODO: update docs, show CLI guide, mention that vlLM requires a gpu and
    # that we have a trial
    env = generate_env(hf_token)
    Path(".env").write_text(env["text"])

    api_key = env["mapping"]["VLLM_API_KEY"]
    click.secho(f"Generated API key: {api_key}", fg="green")

    Path("Dockerfile").write_text(dockerfile)
    Path("requirements.txt").write_text(requirements)
    click.echo("Dockerfile and requirements.txt created")

    init.init(from_existing=False, force=False, project_type="docker")

    config = PloomberCloudConfig()
    config.load()
    config["gpu"] = 1

    test_script_template = Template(resources.read_text(vllm_resources, "test-vllm.py"))
    test_script = test_script_template.substitute(
        API_KEY=api_key,
        APP_ID=config.data["id"],
    )

    Path("test-vllm.py").write_text(test_script)

    confirmation = click.confirm("Do you want to deploy now?", default=True)

    click.secho(
        "test-vllm.py created, once vLLM is running, test it with python test-vllm.py",
        fg="green",
    )

    if not confirmation:
        click.secho(
            "Deployment cancelled. You can deploy with: ploomber-cloud deploy",
            fg="yellow",
        )
        return
    else:
        deploy.deploy(watch=False)
        click.secho("Deployment started, should take about 12 minutes.", fg="green")
