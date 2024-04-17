import argparse
import os

import uvicorn

from r2r.main import E2EPipelineFactory, R2RConfig

current_file_path = os.path.dirname(__file__)
configs_path = os.path.join(current_file_path, "..", "configs")

OPTIONS = {
    "default": None,
    "local_ollama": os.path.join(configs_path, "local_ollama.json"),
    "local_llama_cpp": os.path.join(configs_path, "local_llama_cpp.json"),
    "local_embedding_qdrant": os.path.join(configs_path, "local_embedding_qdrant.json"),
}


def create_app(config_name: str = "default"):
    config_name = os.getenv("CONFIG_OPTION") or config_name
    config_path = OPTIONS[config_name]

    app = E2EPipelineFactory.create_pipeline(
        config=R2RConfig.load_config(config_path)
    )
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="R2R Pipeline")
    parser.add_argument(
        "--config",
        type=str,
        default="default",
        choices=OPTIONS.keys(),
        help="Configuration option for the pipeline",
    )
    args, _ = parser.parse_known_args()

    app = create_app(args.config)

    uvicorn.run(app, host="0.0.0.0", port=8000)
