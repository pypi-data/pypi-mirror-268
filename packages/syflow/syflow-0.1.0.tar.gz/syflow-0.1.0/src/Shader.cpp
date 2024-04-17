#include "Shader.h"
#include "Log.h"

#include <fstream>
#include <sstream>
#include <glad/glad.h>
#include <filesystem>
#ifdef _WIN32
#include <windows.h>
#else
#include <limits.h>
#include <unistd.h>
#endif

using namespace std;

// get file path of executable
// https://stackoverflow.com/a/55579815
std::filesystem::path getexepath()
{
#ifdef _WIN32
	wchar_t path[MAX_PATH] = { 0 };
	GetModuleFileNameW(NULL, path, MAX_PATH);
	return path;
#else
	char result[PATH_MAX];
	ssize_t count = readlink("/proc/self/exe", result, PATH_MAX);
	return std::string(result, (count > 0) ? count : 0);
#endif
}

static string read_file(const string& file_name) {
	auto exe_path = getexepath();
	auto full_path = exe_path.parent_path() / "shaders" / file_name;

	Log() << "read shader file " << full_path;

	ifstream ifstream;
	ifstream.exceptions(ifstream::failbit | ifstream::badbit);
	ifstream.open(full_path);

	stringstream sstream;
	sstream << ifstream.rdbuf();
	ifstream.close();

	return sstream.str();
}

static void check_shader_errors(unsigned int shader, GLenum type) {
	const size_t infolog_len = 1024;
	
	int success = 0;
	char infolog[infolog_len];

	if (type == GL_COMPILE_STATUS) {
		glGetShaderiv(shader, type, &success);
		if (success != 1) {
			glGetShaderInfoLog(shader, infolog_len, NULL, infolog);
			Log() << "shader compile error " << infolog;
			throw ShaderError(infolog);
		}
	}
	else if (type == GL_LINK_STATUS) {
		glGetProgramiv(shader, type, &success);
		if (success != 1) {
			glGetProgramInfoLog(shader, infolog_len, NULL, infolog);
			Log() << "shader link error " << infolog;
			throw ShaderError(infolog);
		}
	}
}

static unsigned int load_shader(const string &file_name, GLenum type) {
	string code = read_file(file_name);
	const char* code_cstr = code.c_str();
	unsigned int shader = glCreateShader(type);
	glShaderSource(shader, 1, &code_cstr, NULL);
	glCompileShader(shader);
	check_shader_errors(shader, GL_COMPILE_STATUS);
	return shader;
}

Shader::Shader(): program_id(0) {}

void Shader::load(const std::string& vertex_name, const std::string& fragment_name)
{
	this->load(vertex_name, "", fragment_name);
}

void Shader::load(const std::string& vertex_name, const std::string& geometry_name, const std::string& fragment_name)
{
	unsigned int vertex = load_shader(vertex_name, GL_VERTEX_SHADER);
	unsigned int geometry;
	if (!geometry_name.empty()) {
		geometry = load_shader(geometry_name, GL_GEOMETRY_SHADER);
	}
	unsigned int fragment = load_shader(fragment_name, GL_FRAGMENT_SHADER);

	this->program_id = glCreateProgram();
	glAttachShader(this->program_id, vertex);
	if (!geometry_name.empty()) {
		glAttachShader(this->program_id, geometry);
	}
	glAttachShader(this->program_id, fragment);
	glLinkProgram(this->program_id);
	check_shader_errors(this->program_id, GL_LINK_STATUS);

	glDeleteShader(vertex);
	if (!geometry_name.empty()) {
		glDeleteShader(geometry);
	}
	glDeleteShader(fragment);
}

Shader::~Shader() {
	if (this->program_id) glDeleteProgram(this->program_id);
}