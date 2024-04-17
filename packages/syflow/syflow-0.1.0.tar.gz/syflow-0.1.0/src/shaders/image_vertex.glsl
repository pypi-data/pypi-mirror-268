#version 330 core

layout(location = 0) in vec2 pos;

uniform mat3 screen_transform;

out vec2 tex_coord;

void main() {
	vec3 transformed_pos = screen_transform * vec3(pos, 1.0);
	gl_Position = vec4(transformed_pos.xy, 0.0, 1.0);
	// flip y for texture coord
	tex_coord = vec2(pos.x, 1.0 - pos.y);
}