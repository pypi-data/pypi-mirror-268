#pragma once

class GUIComponent {
public:
    // Render a sub-window using ImGui, which (for example) could display stats or allow controlling something
    virtual void drawImGui() {};
    // Use OpenGL directly to render something to the window
    virtual void drawOpenGL(int width, int height) {};
};