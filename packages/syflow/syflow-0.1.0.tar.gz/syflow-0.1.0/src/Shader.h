#pragma once

#include <string>
#include <utility>

class ShaderError : std::exception {
public:
	std::string message;
	ShaderError(std::string message) : message(std::move(message)) {}
	virtual const char* what() {
		return this->message.c_str();
	}
};

class Shader {
public:
	Shader();
	void load(const std::string& vertex_name, const std::string& fragment_name);
	void load(const std::string& vertex_name, const std::string& geometry_name, const std::string& fragment_name);
	~Shader();
	unsigned int program_id;
};