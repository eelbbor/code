import os

from scripts.scaffold_java import scaffold as scaffold_java


def main(project_root_dir: str) -> None:
    prompt = '''Select a Project Language (enter the number):
    1: Java
    [COMING SOON] 2: JS
    '''
    user_input = int(input(prompt))
    if user_input == 1:
        scaffold_java(project_root_dir=project_root_dir)
    else:
        print('Invalid selection, must be consistent with the prompt.')
        return


if __name__ == "__main__":
    project_root_env_var = 'EELBBOR_CODE_PROJECT_ROOT'
    project_root_dir: str | None = None
    if project_root_env_var in os.environ:
        project_root_env_var = 'EELBBOR_CODE_PROJECT_ROOT'
        project_root_dir = os.environ[project_root_env_var]
    else:
        project_root_dir = str(input(
            f"Enter the project root directory (skip this by setting the '{project_root_env_var}' env var): "))

    if project_root_dir.startswith('~/'):
        project_root_dir = os.path.join(os.path.expanduser("~"), project_root_dir[2:])

    if not os.path.exists(project_root_dir):
        invalid_root_msg = f"Invalid project root '{project_root_dir}' does not exist."
        raise ValueError(invalid_root_msg)

    main(project_root_dir=project_root_dir)
