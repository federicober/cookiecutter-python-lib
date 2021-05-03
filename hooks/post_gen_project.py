import os
import shutil


def delete_other_docs_backend(docs_backend: str) -> None:
    temp_docs_dir_name = f"docs/__{docs_backend}"
    if not os.path.isdir(temp_docs_dir_name):
        raise ValueError(f"Invalid docs backend ({docs_backend})")
    for dropped_candidate_backend in os.listdir("docs"):
        if dropped_candidate_backend.endswith(docs_backend):
            continue
        shutil.rmtree(f"docs/{dropped_candidate_backend}")

    os.rename(temp_docs_dir_name, "_docs")
    shutil.rmtree("docs")
    os.rename("_docs", "docs")


if "sphinx" == "mkdocs":
    delete_other_docs_backend("mkdocs")

elif "sphinx" == "sphinx":
    delete_other_docs_backend("sphinx")

else:
    raise ValueError("Unrecognized docs_backend (sphinx)")
