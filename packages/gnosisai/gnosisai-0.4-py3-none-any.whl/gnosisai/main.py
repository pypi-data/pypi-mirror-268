import os
import click
from jinja2 import Environment, FileSystemLoader
import yaml

# 경로 설정
base_path = os.path.dirname(__file__)  # 현재 파일의 디렉토리 경로
TEMPLATE_DIRECTORY = os.path.join(base_path, "template")
TEMPLATE_FILES_DIRECTORY = os.path.join(base_path, "template_files")

def load_variable(variable_file: str):
    """ YAML 파일에서 변수를 로드합니다. """
    base_path = os.path.dirname(__file__)  # 현재 파일의 디렉토리 경로
    variable_path = os.path.join(base_path, variable_file)
    with open(variable_path, "r") as f:
        variables = yaml.load(f, Loader=yaml.SafeLoader)
    return variables

def format_path(correspond_file_paths, name: str):
    """ 파일 경로를 포맷팅합니다. """
    formatted_paths = {k: v.format(name='./') for k, v in correspond_file_paths.items()}
    return formatted_paths

def copy_directory(source_dir: str, target_dir: str):
    """ 디렉토리를 복사합니다. """
    from distutils.dir_util import copy_tree
    copy_tree(source_dir, target_dir)

def build(template_file_name: str, output_file_path: str, variables):
    """ 템플릿을 사용하여 파일을 생성합니다. """
    env = Environment(loader=FileSystemLoader(TEMPLATE_FILES_DIRECTORY, encoding="utf8"))
    template = env.get_template(template_file_name)
    output = template.render(**variables)
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w') as f:
        f.write(output)

@click.command()
@click.option('--name', prompt='Project name', help='Name of the project to create.')
@click.option('--variable_file', default='vars.yaml', help='Path to the variable file (YAML).')
@click.option('--correspond_file_path', default='correspond_file_path.yaml', help='Path to the file defining corresponding file paths.')
def cli(name, variable_file, correspond_file_path):
    """ 프로젝트 생성 명령어를 처리합니다. """
    variables = load_variable(variable_file)
    correspond_file_paths = load_variable(correspond_file_path)
    formatted_paths = format_path(correspond_file_paths, name)
    
    os.makedirs(name, exist_ok=True)
    copy_directory(TEMPLATE_DIRECTORY, name)
    
    for template_file, output_path in formatted_paths.items():
        build(template_file, os.path.join(name, output_path), variables)
    
    print(f"Project {name} created successfully.")

if __name__ == "__main__":
    cli()