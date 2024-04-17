#version 330 core

precision mediump float;

out vec4 fragColor;
in vec2 tex_coord;

uniform sampler2D texture1;
uniform uint display_option;
// contains [min, max]
uniform vec2 display_range;

const uint DISPLAY_OPTION_U = 2u;
const uint DISPLAY_OPTION_V = 3u;

// opengl divides our 16-bit float vectors by (2**15 - 1) when we access the values as floats
// see https://www.khronos.org/opengl/wiki/Normalized_Integer#Signed
// additionally, NvOF uses "S10.5" format, which means the last 5 bits are fractional part
// in other words, the values are 2**5 larger than otherwise would be
// thus the result is that we need to scale by (2**15 - 1) / 2**5
//const float VEC_SCALE_FACTOR = 32767 / 32;
const float VEC_SCALE_FACTOR = 1.0;

void main() {
	vec4 texel = texture(texture1, tex_coord);
	float intensity;
	if (display_option == DISPLAY_OPTION_V) {
		intensity = texel.g;
	} else {
		intensity = texel.r;
	}
	if (display_option == DISPLAY_OPTION_U || display_option == DISPLAY_OPTION_V) {
		float scaled_intensity = VEC_SCALE_FACTOR * intensity;
		// remap [display_min, display_max] -> [0, 1]
		intensity = (scaled_intensity - display_range[0]) / (display_range[1] - display_range[0]);
	}
	fragColor = vec4(intensity, intensity, intensity, 1.0);
}