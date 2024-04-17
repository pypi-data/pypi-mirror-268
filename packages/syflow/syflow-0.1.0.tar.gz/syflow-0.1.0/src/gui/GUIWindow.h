#pragma once

#include <glad/glad.h>
#include <vector>
#include "GUIComponent.h"
#include "GLFW/glfw3.h"
#include <memory>

class GUIWindow {
private:
    GLFWwindow *window;
    void CleanupGui();
public:
    std::vector<std::shared_ptr<GUIComponent>> components;
    void Show(int width, int height);
    void RunRenderLoop();
};
