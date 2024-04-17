#version 330 core

layout(location = 0) in vec2 displacement_in;

out vec2 displacement;

uniform uint width_vectors;
uniform uint block_size;

void main() {
	uint y_index = uint(gl_VertexID) / width_vectors;
	uint x_index = uint(gl_VertexID) - (width_vectors * y_index);
	// position in pixels
	gl_Position = vec4((x_index + 0.5) * block_size, (y_index + 0.5) * block_size, 0.0, 1.0);
	displacement = displacement_in;
}