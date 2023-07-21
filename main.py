import os
import sys

dir = os.getcwd()
rpath = os.path.dirname(os.path.realpath(__file__))
name = input("Name of project: ")
path = f"{dir}/{name}"

print(name)
cmake_pre = """
cmake_minimum_required(VERSION 3.0)
project(${{PROJECT}})

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

message(STATUS "Src dir: ${CMAKE_SOURCE_DIR}")
message(STATUS "Output dir: ${CMAKE_BINARY_DIR}")
file(GLOB SOURCES
    src/*.c
    libs/vec/src/vec.c
)

add_executable(${PROJECT_NAME} ${SOURCES})

target_include_directories(${PROJECT_NAME} PRIVATE
    src/
    libs/vec/src
)


target_link_libraries(${PROJECT_NAME}

)

set_property(TARGET ${PROJECT_NAME} PROPERTY C_STANDARD 11)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_definitions(${PROJECT_NAME} PRIVATE DEBUG)
    target_compile_options(${PROJECT_NAME} PRIVATE -g)
endif()

if(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_definitions(${PROJECT_NAME} PRIVATE NDEBUG)
    target_compile_options(${PROJECT_NAME} PRIVATE -O3)
endif()

if(UNIX AND CMAKE_GENERATOR MATCHES "Makefiles")
    target_compile_options(${PROJECT_NAME} PRIVATE -DBX_CONFIG_DEBUG=1)
endif()
"""

cmake_text = cmake_pre.replace("${{PROJECT}}", name)
print(cmake_text)

main = """
#include <stdio.h>

int main(int argc, char* argv[]) {
    return 0;
}
"""

gitignore = """
bin/
CMakeFiles/
Makefile
"""

cmds = [
    f"mkdir {path}",
    f"mkdir {path}/src",
    f"mkdir {path}/libs",
    f"mkdir {path}/bin",

    f"touch {path}/src/main.c",
    f"echo '{main}' > {path}/src/main.c",

    f"touch {path}/CMakeLists.txt",
    f"echo '{cmake_text}' > {path}/CMakeLists.txt",

    f"touch {path}/.gitignore",
    f"echo '{gitignore}' > {path}/.gitignore",

    f"git init {path}",
    f"cd {path} && git submodule add https://github.com/dssgabriel/vec.git {path}/libs/vec/ && cd {dir}",
]

for cmd in cmds:
    os.system(cmd)
    # print(cmd)
