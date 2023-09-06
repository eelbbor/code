import re
import os
import enum
import textwrap


class Type(enum.StrEnum):
    LIB = 'lib'
    COMPONENT = 'component'
    SERVICE = 'service'


def scaffold(project_root_dir: str) -> None:
    prompt = '''Select a Project Type (enter the number):
    1: Library (general for usage in the java package)
    2: Component (business logic lies here)
    3: Service (wraps components and constructs a service with endpoint(s) to be hit)
    '''
    user_input = int(input(prompt))

    type: Type
    if user_input == 1:
        type = Type.LIB
    elif user_input == 2:
        type = Type.COMPONENT
    elif user_input == 3:
        type = Type.SERVICE
    else:
        print('Invalid selection, must be consistent with the prompt.')
        return
    directory = f'{type}s'

    project_name = input(f"Scaffolding your project in '{directory}/'."
                         'Enter a project name (must be single word and use pascal case i.e. '
                         'FooBizBaz): ')
    if not re.match(r'^[A-Za-z]+$', project_name):
        print(f"Invalid project name '{project_name}'. Name must be single word and use pascal case i.e. 'FooBizBaz'")
        return

    package_name = project_name.lower()
    root_dir = os.path.join(project_root_dir, 'java', directory, package_name)
    if os.path.exists(root_dir):
        print(f'Project for this name already exists: {os.path.abspath(root_dir)}')
        return
    print(f"Creating project at '{os.path.abspath(root_dir)}/'")

    # Create the root directory and add a README.
    os.makedirs(root_dir)
    _create_readme(directory=root_dir, overview=project_name)
    _create_build_file(directory=root_dir)

    # Create base directories with build files.
    main_root = os.path.join(root_dir, 'src/main')
    _create_main_build(directory=main_root, package=package_name, type=type)

    test_root = os.path.join(root_dir, 'src/test')
    _create_test_build(directory=test_root, package=package_name, type=type)

    # Add sample files.
    relative_package = os.path.join('java', 'com', 'eelbbor', package_name)
    _create_main_file(directory=os.path.join(main_root, relative_package), package=package_name)
    _create_test_file(directory=os.path.join(test_root, relative_package), package=package_name)


def _create_readme(directory: str, overview: str):
    _create_file(directory=directory, file_name='README.md', content=f'# Overview\n{overview}')


def _create_main_build(directory: str, package: str, type: Type):
    content = textwrap.dedent(f'''\
    java_library(
        name = "{package}-{type}",
        srcs = glob(["java/com/eelbbor/{package}/**/*.java"]),
        visibility = ["//visibility:public"],
        deps = [
            # Add library dependencies here.
        ],
    )
    ''')

    if type == Type.SERVICE:
        binary_content = textwrap.dedent(f'''\
        java_binary(
            name = "{package}-bin",
            main_class = "com.eelbbor.{package}.Main",
            visibility = ["//visibility:public"],
            runtime_deps = [":{package}-{type}"],
        )
        ''')
        content = f'{content}\n{binary_content}'
    _create_build_file(directory=directory, content=content)


def _create_main_file(directory: str, package: str):
    content = textwrap.dedent(f'''\
    package com.eelbbor.{package};

    public class Main {{
        public boolean trueMethod() {{
            return true;
        }}

        public static void main(String... args) throws Exception {{
            System.out.println("Hello World!");
        }}
    }}
    ''')
    _create_file(directory=directory, file_name='Main.java', content=content)


def _create_test_build(directory: str, package: str, type: Type):
    content = textwrap.dedent(f'''\
    load("@rules_jvm_external//:defs.bzl", "artifact")
    load("@contrib_rules_jvm//java:defs.bzl", "JUNIT5_DEPS", "java_test_suite")

    java_test_suite(
        name="tests",
        srcs = glob(["java/com/eelbbor/{package}/**/*.java"]),
        runner = "junit5",
        test_suffixes = ["Test.java"],
        runtime_deps = JUNIT5_DEPS,
        size = "small",
        deps = [
            "//java/{type}s/{package}/src/main:{package}-{type}",
            artifact("org.junit.jupiter:junit-jupiter-api"),
            artifact("org.junit.jupiter:junit-jupiter-params"),
        ],
    )
    ''')
    _create_build_file(directory=directory, content=content)


def _create_test_file(directory: str, package: str):
    content = textwrap.dedent(f'''\
    package com.eelbbor.{package};
    
    import org.junit.jupiter.api.Assertions;
    import org.junit.jupiter.api.Test;

    public class MainTest {{
        @Test
        public void testSomeStuff() {{
            Main main = new Main();
            Assertions.assertTrue(main.trueMethod());
        }}
    }}
    ''')
    _create_file(directory=directory, file_name='MainTest.java', content=content)

def _create_build_file(directory: str, content: str = ''):
    _create_file(directory=directory, file_name='BUILD.bazel', content=content)


def _create_file(directory: str, file_name: str, content: str):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, file_name), 'w') as file:
        file.write(content)
