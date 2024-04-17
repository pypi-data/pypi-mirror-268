set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# copy shader files
# https://stackoverflow.com/a/77075253
set(MY_RESOURCE_FILES 
    shaders/image_vertex.glsl
    shaders/image_fragment.glsl
    shaders/arrows_vertex.glsl
    shaders/arrows_geometry.glsl
    shaders/arrows_fragment.glsl
    resources/SEGOEUI.TTF
)

# DLLs that need to be copied to the EXE file's directory
set(DLLS_TO_COPY "")

set(IMGUI_DIR "${CMAKE_CURRENT_SOURCE_DIR}/vendor/imgui-1.90")

SET(SYFLOW_SOURCE_FILES
        ${MY_RESOURCE_FILES}
        "Log.h" "Pipeline.h" "Pipeline.cpp" "FileImageSource.h"
        "FileImageSource.cpp" "GLRenderer.cpp" "GLRenderer.h"
        "vendor/glad/src/glad.c"
        "vendor/nvof/NvOFCuda.cpp" "vendor/nvof/NvOFCuda.h" "vendor/nvof/NvOF.cpp" "vendor/nvof/NvOF.h" "vendor/nvof/NvOFUtils.cpp" "vendor/nvof/NvOFUtils.h" "vendor/nvof/nvOpticalFlowCommon.h" "vendor/nvof/nvOpticalFlowCuda.h"
        "vendor/glad/src/glad.c"
        "${IMGUI_DIR}/imgui.cpp" "${IMGUI_DIR}/imgui_demo.cpp" "${IMGUI_DIR}/imgui_draw.cpp" "${IMGUI_DIR}/imgui_tables.cpp" "${IMGUI_DIR}/imgui_widgets.cpp"
        "${IMGUI_DIR}/backends/imgui_impl_glfw.cpp" "${IMGUI_DIR}/backends/imgui_impl_opengl3.cpp"
        "Shader.cpp" "Shader.h"
        "ThreadSafeQueue.h" "OpticalFlowUploader.cpp" "OpticalFlowUploader.h"
        OpticalFlowUploader.cpp
        OpticalFlowUploader.h
        OpticalFlowExecutor.cpp
        OpticalFlowExecutor.h
        GLUtils.cpp
        OpticalFlowSaver.cpp
        OpticalFlowSaver.h
        TextureManager.cpp
        TextureManager.h
        DummyImageSink.cpp
        DummyImageSink.h
        CameraAPI.h
        CameraAPI.cpp
        gui/GUIComponent.h
        gui/SourceChooserGUI.cpp
        gui/SourceChooserGUI.h
        gui/DisplayOptionsGUI.cpp
        gui/DisplayOptionsGUI.h
        gui/ControlGUI.cpp
        gui/ControlGUI.h
        gui/StatsGUI.cpp
        gui/StatsGUI.h
        gui/GUIWindow.cpp
        gui/GUIWindow.h
        gui/SaverOptionsGUI.cpp
        gui/SaverOptionsGUI.h
        ConvertToFloat.cu
        ConvertToFloat.h
        SubPixelPostProcess.cu
        SubPixelPostProcess.h
        CudaImage.h
        CPUImageOwned.h
        Point.h
        CPUImageOwned.cpp
        OpticalFlowImage.cpp
        OpticalFlowImage.h
        gui/PostProcessGUI.cpp
        gui/PostProcessGUI.h
        CudaImage.cu
)
set(SYFLOW_INCLUDE_DIRS
        ${OPENGL_INCLUDE_DIR}
        ${CUDAToolkit_INCLUDE_DIRS}
        "${CMAKE_CURRENT_SOURCE_DIR}/vendor/glad/include"
        "${IMGUI_DIR}"
        "${ARAVIS_INCLUDE_DIRS}"
)
set(SYFLOW_LINK_DIRS
        "${ARAVIS_LIBRARY_DIRS}"
)
set(SYFLOW_LINK_LIBS
        ${OPENGL_LIBRARIES}
        glfw
        CUDA::cudart
        CUDA::cuda_driver
        "${ARAVIS_LIBRARIES}"
)

set(OpenGL_GL_PREFERENCE GLVND)
find_package(OpenGL REQUIRED)

find_package(CUDAToolkit)
set(CMAKE_CUDA_ARCHITECTURES 75)
enable_language(CUDA)
set(CMAKE_CUDA_SEPARABLE_COMPILATION ON)
set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -g")  # include debug information
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -G")  # debug build mode
endif()

option(SYFLOW_ENABLE_ARAVIS "Enable Aravis Genicam Video Library" on)
if(SYFLOW_ENABLE_ARAVIS)
    # aravis adfef07d7040a167f68c0d47d5929426cf5d6740
    #find_package(PkgConfig REQUIRED)
    #pkg_check_modules(ARAVIS REQUIRED IMPORTED_TARGET aravis-0.10)
    #find_library(ARAVIS_LIBRARIES aravis-0.10 REQUIRED)
    find_package(aravis)
    list(APPEND SYFLOW_LINK_LIBS aravis::aravis)
    #add_compile_definitions(-DSYFLOW_ENABLE_ARAVIS)
    list(APPEND SYFLOW_SOURCE_FILES 
        AravisSource.cpp
        AravisSource.h)
endif()

# debugging:
#get_cmake_property(_variableNames VARIABLES)
#foreach (_variableName ${_variableNames})
#    message("${_variableName}=${${_variableName}}")
#endforeach()

option(ENABLE_V4L2 "Enable V4L2 Video Source" "${UNIX}")
if(ENABLE_V4L2)
    add_compile_definitions(-DENABLE_V4L2)
    list(APPEND SYFLOW_SOURCE_FILES
        V4L2Source.cpp
        V4L2Source.h)
endif()

option(SYFLOW_ENABLE_VIMBA "Enable Vimba SDK Video Source.
On Windows, Vimba SDK 6.0 must be installed.
On Linux, this build script will automatically download the SDK.
For the Python library, you will need to manually set LD_LIBRARY_PATH at runtime." OFF)
message("Syflow: Enable Vimba ${SYFLOW_ENABLE_VIMBA}")
if(SYFLOW_ENABLE_VIMBA)
    list(APPEND SYFLOW_SOURCE_FILES
            VimbaSource.cpp
            VimbaSource.h)
    if(UNIX)
        FetchContent_Declare(
                vimba
                URL https://downloads.alliedvision.com/Vimba64_v6.0_Linux.tgz
                URL_HASH    SHA256=48892d6657c07fe410e627f96ea6ea22c2aeab4f08010a1de25a25a1a19e275c
        )
        FetchContent_Populate(vimba)
        set(VIMBA_HOME "${vimba_SOURCE_DIR}")
        list(APPEND SYFLOW_LINK_LIBS 
            "${VIMBA_HOME}/VimbaCPP/DynamicLib/x86_64bit/libVimbaCPP.so")
        list(APPEND DLLS_TO_COPY
                "${VIMBA_HOME}/VimbaCPP/DynamicLib/x86_64bit/libVimbaCPP.so" "${VIMBA_HOME}/VimbaCPP/DynamicLib/x86_64bit/libVimbaC.so")
    elseif(WIN32)
        set(VIMBA_HOME "C:\\Program Files\\Allied Vision\\Vimba_6.0")
        set(VIMBA_DLL )
        list(APPEND SYFLOW_LINK_LIBS "${VIMBA_HOME}\\VimbaCPP\\Lib\\Win64\\VimbaCPP.lib")
        list(APPEND DLLS_TO_COPY "${VIMBA_HOME}\\VimbaCPP\\Bin\\Win64\\VimbaCPP.dll" "${VIMBA_HOME}\\VimbaCPP\\Bin\\Win64\\VimbaC.dll")
    endif()
    list(APPEND SYFLOW_INCLUDE_DIRS "${VIMBA_HOME}")
endif()

if (SYFLOW_PYTHON)
    # only build python library
    set(SYFLOW_TARGET_NAME "_core")
    python_add_library(_core MODULE ${SYFLOW_SOURCE_FILES} PythonModule.cpp WITH_SOABI)
    target_include_directories(_core PUBLIC ${SYFLOW_INCLUDE_DIRS})
    target_link_directories(_core PRIVATE ${SYFLOW_LINK_DIRS})
    target_link_libraries(_core PRIVATE pybind11::headers ${SYFLOW_LINK_LIBS})
    install(TARGETS _core DESTINATION ./src/syflow)
else()
    # gui executable
    set(SYFLOW_TARGET_NAME "syflow")
    add_executable(syflow WIN32 ${SYFLOW_SOURCE_FILES} "Main.cpp")

    target_include_directories(${SYFLOW_TARGET_NAME} PUBLIC ${SYFLOW_INCLUDE_DIRS})
    target_link_directories(${SYFLOW_TARGET_NAME} PRIVATE ${SYFLOW_LINK_DIRS})
    target_link_libraries(${SYFLOW_TARGET_NAME} PRIVATE ${SYFLOW_LINK_LIBS})
endif()

FOREACH(MY_RESOURCE_FILE ${MY_RESOURCE_FILES})
    add_custom_command(
        TARGET ${SYFLOW_TARGET_NAME}
        COMMAND ${CMAKE_COMMAND} -E copy
            ${CMAKE_CURRENT_SOURCE_DIR}/${MY_RESOURCE_FILE}
            $<TARGET_FILE_DIR:${SYFLOW_TARGET_NAME}>/${MY_RESOURCE_FILE}
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${MY_RESOURCE_FILE}
  )
ENDFOREACH()

if (DLLS_TO_COPY)
    message("COPY ${DLLS_TO_COPY}")
    add_custom_command(
        TARGET ${SYFLOW_TARGET_NAME} POST_BUILD
        # we need to copy DLLs to the same directory as the EXE
        COMMAND ${CMAKE_COMMAND} -E copy_if_different ${DLLS_TO_COPY} $<TARGET_FILE_DIR:${SYFLOW_TARGET_NAME}>
        COMMAND_EXPAND_LISTS
    )
    install(FILES ${DLLS_TO_COPY} DESTINATION ./src/syflow)
endif()
