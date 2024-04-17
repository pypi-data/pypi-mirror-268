# version 3.17 required for cuda features
cmake_minimum_required (VERSION 3.17)

# Enable Hot Reload for MSVC compilers if supported.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

# download extract timestamp
if (CMAKE_VERSION VERSION_GREATER_EQUAL "3.24")
  cmake_policy(SET CMP0135 NEW)
endif()

project ("syflow")

# external libraries
include(FetchContent)
set(GLFW_BUILD_EXAMPLES OFF)
set(GLFW_BUILD_TESTS OFF)
set(GLFW_BUILD_DOCS OFF)
FetchContent_Declare(
        glfw
        URL https://github.com/glfw/glfw/releases/download/3.3.9/glfw-3.3.9.zip
        URL_HASH    SHA256=55261410f8c3a9cc47ce8303468a90f40a653cd8f25fb968b12440624fb26d08
)
FetchContent_MakeAvailable(glfw)

if(SYFLOW_PYTHON)
  find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
  FetchContent_Declare(
          pybind11
          URL https://github.com/pybind/pybind11/archive/refs/tags/v2.11.1.tar.gz
          URL_HASH    SHA256=d475978da0cdc2d43b73f30910786759d593a9d8ee05b1b6846d1eb16c6d2e0c
  )
  FetchContent_MakeAvailable(pybind11)
endif()

add_subdirectory ("src")
