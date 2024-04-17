#version 330 core

layout(points) in;
layout(triangle_strip, max_vertices = 7) out;

in vec2 displacement[];
out float magnitude;

uniform mat3 pixel_space_to_ndc;
uniform float shaft_width;
uniform float width_pixels;
uniform float height_pixels;
uniform float display_scale;

void main() {
	// translate from origin to the arrow's position in pixel space
	mat3 translate;
	translate[0] = vec3(1.0, 0.0, 0.0);
	translate[1] = vec3(0.0, 1.0, 0.0);
	translate[2] = vec3(gl_in[0].gl_Position.x, gl_in[0].gl_Position.y, 1.0);

	mat3 rotate;
	magnitude = length(displacement[0]);
	float scaled_magnitude = magnitude * display_scale;
	float cos_theta = displacement[0].x / magnitude;
	float sin_theta = displacement[0].y / magnitude;
	rotate[0] = vec3(cos_theta, sin_theta, 0.0);
	rotate[1] = vec3(-sin_theta, cos_theta, 0.0);
	rotate[2] = vec3(0.0, 0.0, 1.0);

	mat3 transform = pixel_space_to_ndc * translate * rotate;

	float shaft_length = max(scaled_magnitude - shaft_width * 10.0, 0.0);

	// arrow pointing right
	// top left corner
	gl_Position = vec4(transform * vec3(0.0, -shaft_width / 2.0, 1.0), 1.0);
	EmitVertex();

	// bottom left corner
	gl_Position = vec4(transform * vec3(0.0, shaft_width / 2.0, 1.0), 1.0);
	EmitVertex();

	// top right corner
	gl_Position = vec4(transform * vec3(shaft_length, -shaft_width / 2.0, 1.0), 1.0);
	EmitVertex();

	// bottom right corner
	gl_Position = vec4(transform * vec3(shaft_length, shaft_width / 2.0, 1.0), 1.0);
	EmitVertex();

	// tip bottom
	gl_Position = vec4(transform * vec3(shaft_length, shaft_width * 2.0, 1.0), 1.0);
	EmitVertex();

	// tip right
	gl_Position = vec4(transform * vec3(scaled_magnitude, 0.0, 1.0), 1.0);
	EmitVertex();

	// tip top
	gl_Position = vec4(transform * vec3(shaft_length, -shaft_width * 2.0, 1.0), 1.0);
	EmitVertex();
}