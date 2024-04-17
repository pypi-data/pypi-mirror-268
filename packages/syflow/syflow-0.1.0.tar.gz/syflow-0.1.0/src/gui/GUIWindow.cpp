#include "GUIWindow.h"

#include "../Log.h"
#include <imgui.h>
#include <backends/imgui_impl_glfw.h>
#include <backends/imgui_impl_opengl3.h>

static const bool glDebug = true;

static void error_callback(int e, const char *d) {
    Log() << "glfw error " << e << ": " << d;
    exit(EXIT_FAILURE);
}

// from https://learnopengl.com/In-Practice/Debugging
static void APIENTRY glDebugOutput(GLenum source,
                                   GLenum type,
                                   unsigned int id,
                                   GLenum severity,
                                   GLsizei length,
                                   const char *message,
                                   const void *userParam)
{
    // ignore non-significant error/warning codes
    if(id == 131169 || id == 131185 || id == 131218 || id == 131204) return;

    Log() << "---------------";
    Log() << "Debug message (" << id << "): " <<  message;

    switch (source) {
        case GL_DEBUG_SOURCE_API:             Log() << "Source: API"; break;
        case GL_DEBUG_SOURCE_WINDOW_SYSTEM:   Log() << "Source: Window System"; break;
        case GL_DEBUG_SOURCE_SHADER_COMPILER: Log() << "Source: Shader Compiler"; break;
        case GL_DEBUG_SOURCE_THIRD_PARTY:     Log() << "Source: Third Party"; break;
        case GL_DEBUG_SOURCE_APPLICATION:     Log() << "Source: Application"; break;
        case GL_DEBUG_SOURCE_OTHER:           Log() << "Source: Other"; break;
        default:                              Log() << "Source: Unknown"; break;
    }

    switch (type)
    {
        case GL_DEBUG_TYPE_ERROR:               Log() << "Type: Error"; break;
        case GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR: Log() << "Type: Deprecated Behaviour"; break;
        case GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR:  Log() << "Type: Undefined Behaviour"; break;
        case GL_DEBUG_TYPE_PORTABILITY:         Log() << "Type: Portability"; break;
        case GL_DEBUG_TYPE_PERFORMANCE:         Log() << "Type: Performance"; break;
        case GL_DEBUG_TYPE_MARKER:              Log() << "Type: Marker"; break;
        case GL_DEBUG_TYPE_PUSH_GROUP:          Log() << "Type: Push Group"; break;
        case GL_DEBUG_TYPE_POP_GROUP:           Log() << "Type: Pop Group"; break;
        case GL_DEBUG_TYPE_OTHER:               Log() << "Type: Other"; break;
        default:                                Log() << "Type: Default"; break;
    }

    switch (severity) {
        case GL_DEBUG_SEVERITY_HIGH:         Log() << "Severity: high"; break;
        case GL_DEBUG_SEVERITY_MEDIUM:       Log() << "Severity: medium"; break;
        case GL_DEBUG_SEVERITY_LOW:          Log() << "Severity: low"; break;
        case GL_DEBUG_SEVERITY_NOTIFICATION: Log() << "Severity: notification"; break;
        default:                             Log() << "Severity: unknown"; break;
    }
}

void GUIWindow::Show(int width, int height) {
    // initialize glfw
    glfwSetErrorCallback(error_callback);
    if (!glfwInit()) {
        throw std::runtime_error("failed to init glfw");
    }
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 6);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, true);
    glfwWindowHint(GLFW_SCALE_TO_MONITOR, GLFW_TRUE);
    if (glDebug) {
        glfwWindowHint(GLFW_OPENGL_DEBUG_CONTEXT, GLFW_TRUE);
    }
    window = glfwCreateWindow(width, height, "Demo", nullptr, nullptr);
    glfwMakeContextCurrent(window);
    glfwGetWindowSize(window, &width, &height);

    /* OpenGL */
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        Log() << "Failed to initialize GLAD";
        exit(EXIT_FAILURE);
    }

    Log() << "OpenGL Renderer: " << glGetString(GL_RENDERER);

    if (glDebug) {
        glEnable(GL_DEBUG_OUTPUT);
        glEnable(GL_DEBUG_OUTPUT_SYNCHRONOUS);
        glDebugMessageCallback(glDebugOutput, nullptr);
        glDebugMessageControl(GL_DONT_CARE, GL_DONT_CARE, GL_DONT_CARE, 0, nullptr, GL_TRUE);
    }

    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGuiIO& io = ImGui::GetIO();
    io.ConfigFlags |= ImGuiConfigFlags_NavEnableKeyboard;

    // Setup Dear ImGui style
    ImGui::StyleColorsDark();

    // Setup Platform/Renderer backends
    ImGui_ImplGlfw_InitForOpenGL(window, true);
    ImGui_ImplOpenGL3_Init("#version 130");

    float xscale;
    glfwGetWindowContentScale(window, &xscale, nullptr);

    // Load Fonts
    // - If no fonts are loaded, dear imgui will use the default font. You can also load multiple fonts and use ImGui::PushFont()/PopFont() to select them.
    // - AddFontFromFileTTF() will return the ImFont* so you can store it if you need to select the font among multiple.
    // - If the file cannot be loaded, the function will return a nullptr. Please handle those errors in your application (e.g. use an assertion, or display an error and quit).
    // - The fonts will be rasterized at a given size (w/ oversampling) and stored into a texture when calling ImFontAtlas::Build()/GetTexDataAsXXXX(), which ImGui_ImplXXXX_NewFrame below will call.
    // - Use '#define IMGUI_ENABLE_FREETYPE' in your imconfig file to use Freetype for higher quality font rendering.
    // - Read 'docs/FONTS.md' for more instructions and details.
    // - Remember that in C/C++ if you want to include a backslash \ in a string literal you need to write a double backslash \\ !
    // - Our Emscripten build process allows embedding fonts to be accessible at runtime from the "fonts/" folder. See Makefile.emscripten for details.
    //io.Fonts->AddFontDefault();
    //io.Fonts->AddFontFromFileTTF(R"(c:\Windows\Fonts\segoeui.ttf)", 18.0f);
    io.Fonts->AddFontFromFileTTF("resources/SEGOEUI.TTF", 18.0f * xscale);
    //io.Fonts->AddFontFromFileTTF("../../misc/fonts/DroidSans.ttf", 16.0f);
    //io.Fonts->AddFontFromFileTTF("../../misc/fonts/Roboto-Medium.ttf", 16.0f);
    //io.Fonts->AddFontFromFileTTF("../../misc/fonts/Cousine-Regular.ttf", 15.0f);
    //ImFont* font = io.Fonts->AddFontFromFileTTF("c:\\Windows\\Fonts\\ArialUni.ttf", 18.0f, nullptr, io.Fonts->GetGlyphRangesJapanese());
    //IM_ASSERT(font != nullptr);
}


void GUIWindow::RunRenderLoop() {
    while (!glfwWindowShouldClose(window))
    {
        glfwPollEvents();

        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplGlfw_NewFrame();
        ImGui::NewFrame();
        for (auto &component : this->components) {
            component->drawImGui();
        }
        //ImGui::ShowDemoWindow();

        ImGui::Render();
        int display_w, display_h;
        glfwGetFramebufferSize(window, &display_w, &display_h);
        glViewport(0, 0, display_w, display_h);
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        for (auto &component : this->components) {
            component->drawOpenGL(display_w, display_h);
        }

        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        glfwSwapBuffers(window);
    }

    this->CleanupGui();
}

void GUIWindow::CleanupGui() {
    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplGlfw_Shutdown();
    ImGui::DestroyContext();

    glfwDestroyWindow(window);
    glfwTerminate();
}