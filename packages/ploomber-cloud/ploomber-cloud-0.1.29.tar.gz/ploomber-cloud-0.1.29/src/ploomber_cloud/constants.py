VALID_PROJECT_TYPES = {
    "voila",
    "streamlit",
    "docker",
    "panel",
    "solara",
    "shiny-r",
    "dash",
}

VALID_DOCKER_PROJECT_TYPES = {
    "flask",
    "fastapi",
    "chainlit",
    "gradio",
    "shiny",
}

FORCE_INIT_MESSAGE = (
    "You may re-initialize a new project by running 'ploomber-cloud init --force'.\n"
    "For re-deploying an existing project, run "
    "'ploomber-cloud init --from-existing --force'\n"
)
